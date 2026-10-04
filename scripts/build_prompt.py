#!/usr/bin/env python3
"""Validate an already analyzed design brief and compile an image-editing prompt.

No image reading, network, model invocation, or automatic photo analysis.
Uses the Python standard library. Refuses to overwrite an existing output.
"""
import argparse
import json
import math
from pathlib import Path
import sys


TEXT_FIELDS = (
    'photo', 'person', 'hair', 'outfit', 'accessories', 'pose', 'expression',
    'proportion', 'face', 'line_art', 'color', 'placement', 'grounding',
    'perspective', 'occlusion', 'shadow', 'style_consistency', 'constraints',
)
MODES = {'Mirror', 'Complementary', 'Interactive'}
PRESETS = {'Street Fashion', 'Travel Photography', 'Indoor Lifestyle',
           'Walking Shot', 'Sitting Shot', 'Pose Photography'}
RANGES = {'standing_relative': (0.50, 0.80), 'seated_relative': (0.50, 1.00),
          'frame_relative': (0.05, 0.50)}


def nonempty(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{label} must be a nonempty descriptive string')
    return value.strip()


def string_list(value, label, required=False):
    if not isinstance(value, list):
        raise ValueError(f'{label} must be an array of strings')
    if required and not value:
        raise ValueError(f'{label} must contain at least one visible identity anchor')
    return [nonempty(item, f'{label}[{i}]') for i, item in enumerate(value)]


def fraction(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f'{label} must be a finite normalized number')
    if not 0 <= value <= 1:
        raise ValueError(f'{label} must be between 0 and 1, not source pixel coordinates')
    return value


def calculate_layout(brief):
    """Derive a single resolution-independent character box from measured frame fractions."""
    c = brief.get('composition')
    if not isinstance(c, dict):
        raise ValueError('composition is required for concise generation; measure normalized frame coordinates first')
    c = {key: fraction(c.get(key), f'composition.{key}') for key in
         ('subject_top', 'subject_bottom', 'character_bottom', 'character_center_x', 'character_width')}
    if c['subject_bottom'] <= c['subject_top']:
        raise ValueError('subject_bottom must be below subject_top')
    scale = brief['scale']
    if scale['basis'] in ('standing_relative', 'seated_relative'):
        height = (c['subject_bottom'] - c['subject_top']) * scale['ratio']
    elif scale['basis'] == 'frame_relative':
        height = scale['ratio']
    else:
        height = fraction(brief['composition'].get('character_height'), 'composition.character_height')
    top = c['character_bottom'] - height
    left = c['character_center_x'] - c['character_width'] / 2
    right = c['character_center_x'] + c['character_width'] / 2
    if height <= 0 or c['character_width'] <= 0 or top < 0 or left < 0 or right > 1:
        raise ValueError('Computed character box is empty or extends outside the original frame')
    return dict(top=top, bottom=c['character_bottom'], height=height,
                left=left, right=right, center_x=c['character_center_x'], width=c['character_width'])


def compile_prompt(brief, prompt_format='full'):
    if prompt_format not in ('full', 'concise'):
        raise ValueError('prompt_format must be full or concise')
    if not isinstance(brief, dict):
        raise ValueError('The brief must be a JSON object')
    values = {key: nonempty(brief.get(key), key) for key in TEXT_FIELDS}
    for key in ('level1', 'level2', 'level3', 'unknowns'):
        items = string_list(brief.get(key), key, required=(key == 'level1'))
        values[key] = '; '.join(items) if items else 'none recorded'
    mode = brief.get('pose_mode')
    if not isinstance(mode, str) or mode not in MODES:
        raise ValueError('pose_mode must be Mirror, Complementary or Interactive')
    preset = brief.get('preset')
    if not isinstance(preset, str) or preset not in PRESETS:
        raise ValueError('preset must match one of the six named scene presets')
    values.update(pose_mode=mode, preset=preset)
    if brief.get('support_visible') is not True:
        raise ValueError('No confirmed visible support surface: resolve the design before compiling')

    scale = brief.get('scale')
    if not isinstance(scale, dict):
        raise ValueError('scale must be an object with basis and ratio')
    basis, ratio = scale.get('basis'), scale.get('ratio')
    if not isinstance(basis, str) or basis not in {*RANGES, 'custom'}:
        raise ValueError('scale.basis must be standing_relative, seated_relative, frame_relative or custom')
    if isinstance(ratio, bool) or not isinstance(ratio, (int, float)) or not math.isfinite(ratio) or ratio <= 0:
        raise ValueError('scale.ratio must be a finite positive number, not a boolean')
    explanation = nonempty(scale.get('explanation'), 'scale.explanation')
    if basis == 'custom':
        comparison = nonempty(scale.get('comparison'), 'scale.comparison')
        nonempty(scale.get('reason'), 'scale.reason')
        sentence = f'Approximately {ratio:.0%} of {comparison}. Explicit exception: {scale["reason"]}. '
    else:
        low, high = RANGES[basis]
        if not low <= ratio <= high:
            raise ValueError(f'scale.ratio for {basis} should be {low}–{high}; '
                             'use custom with comparison and reason for a justified exception')
        comparison = {
            'standing_relative': "the real person's visible head-to-lowest-shoe image height, excluding raised props",
            'seated_relative': "the real person's seated head-to-lowest-shoe image height, excluding the chair",
            'frame_relative': 'the original frame height; this is not a human height ratio',
        }[basis]
        sentence = f'Approximately {ratio:.0%} of {comparison}. '
    values['scale_basis'] = basis
    values['scale_description'] = sentence + explanation
    if 'composition' in brief or prompt_format == 'concise':
        box = calculate_layout(brief)
        values['size_control'] = (
            f'Use percentages of the FINAL original-aspect frame, regardless of output resolution. '
            f'The entire illustrated figure including hair and shoes occupies about {box["height"]:.1%} of frame height. '
            f'Its head/hair TOP is at {box["top"]:.1%} of frame height and lowest sole/bottom at {box["bottom"]:.1%}. '
            f'Horizontal center is at {box["center_x"]:.1%} of frame width; '
            f'its silhouette fits approximately within {box["left"]:.1%}–{box["right"]:.1%} of frame width. '
            'The frame fractions above control placement; they are not source-pixel coordinates. '
            'Do not enlarge the body to show small details. Preserve the identifying silhouette and simplify details instead.'
        )
    else:
        values['size_control'] = 'Archive-only brief: normalized composition not supplied; calculate it before actual generation.'
    refs = Path(__file__).resolve().parent.parent / 'references'
    values['negative_prompt'] = (refs / 'negative-prompt.txt').read_text(encoding='utf-8').strip()
    filename = 'prompt-concise.txt' if prompt_format == 'concise' else 'prompt-template.txt'
    template = (refs / filename).read_text(encoding='utf-8')
    return template.format_map(values)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('brief', type=Path)
    parser.add_argument('--format', choices=('concise', 'full'), default='concise',
                        help='Concise prioritized prompt for actual editing (default); full 21-block archive')
    parser.add_argument('--out', type=Path, help='New UTF-8 file; existing files are never overwritten')
    args = parser.parse_args()
    try:
        brief = json.loads(args.brief.read_text(encoding='utf-8'))
        prompt = compile_prompt(brief, args.format)
        if args.out:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            with args.out.open('x', encoding='utf-8') as output:
                output.write(prompt)
            print(f'Saved prompt: {args.out}')
        else:
            sys.stdout.write(prompt)
    except (OSError, ValueError, KeyError) as error:
        print(f'Prompt not compiled: {error}', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
