# PHOTO ALTER EGO｜完整视觉生成系统 v1.1.0

本文可独立使用。参考依据见 reference-analysis.md；数字为设计工作区间或目测估计，不是原作者参数。v1.1.0 增加 generation-control.md 的生成前控制，依据两张真人图首轮偏大 / 过密的实际失败；没有把该升级写成已验证零返工。

## SKILL NAME

`photo-alter-ego`｜真人 × 手绘分身。

STYLE / CREATIVE SYSTEM NAME：**Photo Alter Ego — 真人 × 手绘分身摄影系统**。

“Alter Ego”强调同一个人的另一个视觉版本；“Photo”强调摄影保留。角色承担陪伴者的叙事功能，身份来源则是本人。与镜像不同，它允许不同动作；与普通 companion 不同，它必须有本人映射关系。这是本方法的通用名称，不声称是参考作品的官方流派名。

## PURPOSE

读取真人生活照、街拍、旅行照、穿搭照或室内照的可见特征，压缩成简单、轻松的二维手绘版本，再放回摄影空间。默认一个真人对应一个新增分身。目标感受：“现实里的我，和画出来的另一个我一起出现在同一张照片里。”

## VISUAL CONCEPT

真人照片提供身份、生活情境、穿搭和可信空间；插画提供可记忆的抽象符号、轻微幽默与自我表达。真实人像负责“这是我”，卡通负责“这是我的视觉符号”。保留摄影复杂性与角色简洁性，形成异质媒介同框。

卡通在叙事上是小伙伴，在身份上是另一个自己。只贴可爱角色不足以成立：必须同时具备特征继承、行为关联、空间接触。

## STYLE DNA

五个不变量：摄影保留、本人映射、二维简化、动作关联、空间落地。

六个可变量：发型 / 配饰、衣着轮廓、比例、动作、表情、放置位置。默认手绘漫画涂鸦感，可选干净圆润线或较细松动线；一张图 / 同批作品保持同一笔触语法。既不复制固定卡通 IP，也不让所有人长同一张脸。

## CORE CREATIVE MECHANISM

1. **识别信息压缩**：选择最能指向本人的特征组合，让几条线和几个色块承担照片里的大量细节。
2. **跨媒介对照**：同一发型、衣着、配饰各在摄影与插画中出现，观者自动建立本人与分身对应。
3. **行为变奏**：同步动作，或用更轻松 / 夸张的姿势表达同一气质，形成小型叙事。
4. **空间锚定**：脚、座位、深度和遮挡建立在场感，不用把插画材质写实化。
5. **视觉记忆压缩**：普通生活照变成易辨识的穿搭形象。真实性与不可能事件同框制造观看停顿，成对对应适合快速理解。这是传播潜力分析，不是传播数据或爆款保证。

## REAL PHOTO PRESERVATION RULES

- 原图为编辑基底，尽可能保持构图、画幅、机位、光照、曝光、噪点和压缩特征。
- 真人五官、发型、肤色、姿态、手脚、体型、年龄表现、服装、纹身和配饰不可重绘 / 美化。
- 建筑、家具、地面、文字和原有物体不可重新设计。只允许角色覆盖处被合理遮住，不为角色清空环境。
- 允许新增角色、必要的局部合成遮挡、极轻接触阴影。不要额外边框、UI、数字、水印、文字、背景图形或装饰。
- 截图已有 UI 只属于原图现状，不作为生成风格；仅在用户明确要求时移除。
- 保真是目标，不是能力保证。没有实际差异检查不能声称像素完全锁定。要求像素级保留时，优先受保护底图与独立图层合成，前提是环境有相应工具；普通生成编辑不能冒充该能力。

## CHARACTER DESIGN DNA

最少足以识别的特征组合 + 适当比例夸张 + 简单表情 + 有理由的动作。

不用复现鼻型、面部骨骼、皮肤或准确眼形；要复现发型外形、穿搭、辨识物和态度。保持可见整体轮廓，不借卡通化改变性别表现、体型或年龄。可爱来自清楚的大形和轻松的线，不来自婴儿脸或过度萌化。

## IDENTITY EXTRACTION

Identity Anchors 按“这张图里有多明显”决定。一般选 3～5 个组合锚点，不为凑数推断不可见细节。

| 特征 | 继承信息 | 压缩方法 |
|---|---|---|
| 头发 | 主色、长度、体积、刘海 / 分缝、直卷、束起 / 披发、方向 | 外轮廓优先，2～5 条内线表达卷度 / 分缝，少量飞发 |
| 帽 / 头巾 | 类别、轮廓、主色、明显图案、覆盖方式 | 棒球帽檐和圆顶、头巾结与三角形优先于小字 |
| 眼镜 / 墨镜 | 有无、框形、框色、脸上 / 头上 | 轮廓加镜片块；墨镜遮眼时不补未知眼形 |
| 耳饰 / 项链 | 辨识形状、位置、长度 | 白花耳饰 / 长吊坠可为 L1；小耳钉可省 |
| 包 | 外形、色、背法、位置、大小关系 | 斜挎带、托特袋、弯月包、云朵包保留类别 |
| 鞋 | 类型、主色、鞋帮高度、明显图案 | 高筒圆点雨靴、厚底凉鞋、撞色鞋优先于鞋带 |
| 手持物 | 类别、颜色、持握方式、朝向 | 红扇、饮料、平板优先；不补另一件道具 |

LIKENESS PRIORITY 默认：**特征组合（发型＋穿搭＋关键配饰） > 服装与整体轮廓 > 动作 / 气质关联 > 精确五官**。显著道具可能最高；动作可变，但至少保留方向、活动或态度之一。不要将动作不一致直接判成不像。

## OUTFIT ABSTRACTION

OUTFIT ABSTRACTION RULE：**大轮廓 + 主色块 + 1～3 个高识别细节**。以单件衣物分配细节预算，不是整个人只能有三个特征。

| 保留 | 简化 | 删除 |
|---|---|---|
| 长短 / 露腹、宽松 / 修身、袖长、领口、外套长度、阔腿 / 工装 / 裙型 | 少量褶线、口袋几何、领口、门襟、袖口 | 密集褶皱、缝线、牛仔颗粒、织物微纹理、皮革反光 |
| 主色、图案类型与方向 | 圆点放大减数，格纹减少网格，条纹保留方向与密度感 | 微小 Logo、小字、非关键拉链扣、复杂品牌纹样 |
| 关键配饰与持物 | 花包保留花色簇，草编包保留外形与少量网格 | 每朵花 / 编织孔 / 金属细节的逐项复制 |

白色长裙 → 白色宽裙摆 + 两条转折；红棕榈 T 恤 → 红块 + 两枚白棕榈符号；工装裤 → 宽蓝裤型 + 大口袋 + 腰间红围巾；波点衬衫 → 蓬松袖 + 白底深点。识别度来自结构，不来自纹理密度。

## FEATURE PRIORITY

- **L1 必须保留**：发型 / 头饰、主穿搭外形与颜色、最强辨识物。墨镜、扇子、波点、特殊耳饰也可升入 L1。
- **L2 建议保留**：次要包袋、首饰、持物、图案简写和鞋细节；对识别或动作有贡献才用。
- **L3 可以删除**：微褶、缝线、材质噪声、小 Logo、复杂纹样与光泽。

层级动态。同一项链在简约黑 T 恤中可能显著，在花衬衫里可省。unknown / occluded 不能成为“必须编出来”。

## CHARACTER PROPORTIONS

CHARACTER PROPORTION SYSTEM：默认 **3～4 头身，起点约 3.5 头身**；依穿搭和动作在约 2.5～4.5 头身调节。这是多样本提炼的设计区间，不是逐张测量。坐姿不能用画面头到脚高度直接算站立头身。

头适度放大，圆 / 椭圆 / 偏方 / 微不对称均可，不统一球形头。宽裤 / 长裙保留体积，躯干略短但不压成幼儿。长线条穿搭可有更长腿，头发和袖管可强调节奏。手掌用手套块或少量指线，握物 / V 手势接触清楚；鞋稍大但不改变类别。

Mini-Me 是关系，不是固定小玩偶尺度。全身站立样本目测画面高度约 0.55～0.77，中位约 0.72；默认 0.60～0.75，允许 0.50～0.80。太小失去识别，接近真人高会削弱主次，但坐姿相邻、前景透视、用户指定效果可例外。

近处略大、远处略小；物理身高和画面高度不同。坐姿先看相同座位深度的头与座面，再看外接高度；图 7 约 0.91，不能套固定 65%。半身缺地面时，选可见座位 / 台面的半身构图，或说明无法自然加入全身，不随机补鞋裤。

## FACE DESIGN

- Head：放大但不机械圆形，可微偏斜；侧脸可用简笔鼻与单只眼。
- Eyes：黑点、小椭圆、带眼白的简化眼都出现。系列默认同一种眼睛语法；墨镜遮眼。眼距可略宽，不人人大眼萌娃。
- Nose：可省略、小弯线、小钩 / 两点。转头时更有作用，正脸可极少笔画。
- Mouth：短弧、小圆口、斜线、露齿笑或微下弯随情绪；禁止永久同一笑脸。
- Cheeks：可选小面积粉 / 杏色平涂，低对比，无空气刷。样本不是全有腮红。
- Skin：简化可见肤色，保留其明暗与色相类别；不美白，不默认奶油白，不追逐每一处摄影光照变化。

## LINE ART

LINE ART DNA：**有意简化、可见用笔、轮廓明确、局部自然不规则**。

深炭黑 / 深棕线；外线略强于内线。外线 : 内线约 1 : 0.6～0.8 可作实现起点，样本没有统一比值证据。随输出同比缩放，不写死像素。

A Round Ink：流畅、圆润、略粗、闭合形明确、细节少；适合强色块 / 圆点。图 1、5、11、12接近。

B Loose Pen：较细、微不匀，局部短线 / 飞发 / 少量笔迹；适合花包、格纹、室内细节。图 2、6、7、10有此倾向。

不要求每条线抖动、全局复描或乱线假手绘。可极轻纸笔质感，照片不叠纸纹。避免均一几何路径、镜像完美五官、发光描边、复杂装饰线；干净线不等于 AI，关键是有设计取舍。

## COLOR SYSTEM

COLOR TRANSLATION RULE：摄影局部色 → 感知主色 → **约 4～8 个核心色块**，另有肤色、描线与必要小点缀；不是八个色值的硬限。

以衣服、头饰、包、鞋、头发建关系，保留红 / 白、绿 / 蓝、黄绿 / 灰格等组合。删除反光和褶皱的明暗变体，压成单块或至多一小块局部暗色。

可少量提亮、减少复杂灰度或调饱和度使背景上可读，但不一律降饱和。图 1 头发偏橙、图 11 上衣偏芥黄，存在风格化色相；默认输入色相身份优先，不能随便改衣色。图 6 等有轻纹理，所以零纹理不是绝对要求。

不能给整图套新 LUT。兼容靠穿搭颜色逻辑和空间，不靠把角色变成摄影光照下的 3D 物体。

## POSE MAPPING

先识别动作意图，从三种肢体关系中选一种，再叠加独立的情绪映射：

| 模式 | 条件 | 保留 | 可改变 |
|---|---|---|---|
| Mirror | 行走、举杯、扇子、V 手势或摆姿是记忆点 | 朝向、语义、道具所属手、主要节奏 | 步幅、肘角、头倾、夸张幅度 |
| Complementary | 静态站 / 坐，希望有对话感 | 本人身份、场景活动、情绪基调 | 交叉腿、看真人、换站姿、倚靠、放松坐姿 |
| Interactive | 原图有空间和接触可能 | 真人现有姿态，接触点与物体位置 | 卡通转头、伸手、坐近、并肩、共享座位 |

同步动作也可变表情，不同动作也可同情绪。有标志动作优先 Mirror，静态可 Complementary，有真实机会才 Interactive。不伸长 / 移动真人手臂造牵手，不复制看不清的手指。

支撑与识别优先于复制。一脚抬起、一脚落地的行走成立。图 7、12坐姿可变奏，图 6交叉腿非严格镜像，图 9、12表情更漫画化。

## EXPRESSION MAPPING

| 原图可见情绪 | 分身 | 约束 |
|---|---|---|
| 微笑 | 短上扬弧、温和眼神 | 不自动大笑 |
| 大笑 / 玩闹 | 大笑口、睁眼 / 笑眯眼 | 不强制腮红 |
| 中性 / 发呆 | 平嘴、微圆口、放松眼 | 不推断心理状态 |
| 酷 / 严肃 | 平嘴、微下弯、少量眉线 | 不默认不耐烦 / 攻击性 |
| 看远处 | 同步视线 / 头向 | 看真人则说明互动意图 |
| 墨镜遮眼 | 保留镜片，用嘴 / 头倾表达 | 不想象眼形 |

图 12允许更强的皱眉态度，但不能推广成所有酷脸都生气。表情是轻松的态度放大，不是未知内心诊断。

## PLACEMENT LOGIC

Character Safe Zone 同时满足无遮挡、能站 / 坐、景深合理、视觉平衡。空白墙不等于悬挂全身人物的位置。

列 2～3 候选：真人左 / 右、下半身旁、道路、墙前地面、座位旁。检查脸 / 关键穿搭、地面 / 座面、边缘裁切、关系、地标 / 文字、近远和尺度。

先选支撑可信、辨识最高的区域，再用左右重量平衡择优。不能永远左下角。真人在左常选右但不强制。衣摆 / 小腿轻搭接可增强在场感，不挡脸、关键持物或穿搭主体。前景可以，但画面位置低不必然同深度。

生成前用归一化 composition 统一数值：真人 top / bottom、角色 bottom、center_x / width，由比例推算角色 height / top。只用一组计算结果，不能与头顶描述或原图像素坐标冲突。详细计算与两张实际输入的例子见 generation-control.md。

## SPATIAL INTEGRATION

支撑面、尺度 / 深度、身体接触、前后遮挡四项一致：

- Perspective：角色保持二维视图，脚 / 鞋底方向符合地面透视；大头不等于可以忽略地面。
- Depth：用地砖、台阶、座面、椅腿、真人脚位判断深度；同深度可有近似脚底基线，坡道不强制齐平。
- Contact：手握物、臀坐面、足底落地；接触点比大投影有效。
- No invention：不新增台阶、清空地面或改家具尺寸。用户授权的小插画道具可另加，不能默默扩默认范围。

## GROUNDING

站立确定地面面片与足底位置；行走至少一支撑脚落地。裙摆 / 阔腿裤可遮鞋，但身体着地仍应可判断。

坐姿先锁座高、臀部接触点、大腿方向，再排腿脚。短腿可垂悬，有臀部支撑就不是漂浮；不强迫脚触地。地坐锁臀与地面。台阶、椅子、沙发、草坪分别按真实表面。

写成“真人右侧同一地砖深度，左鞋底落在地砖上、右脚轻抬”，比“自然融入”更可执行。

## OCCLUSION

默认不挡主体的并排构图。有需要时按深度遮挡：在真人后则被真人挡；坐椅里则前扶手挡角色腿 / 衣袖，后靠背在角色后；前景栏杆可遮角色。

不为画完整插画擦掉扶手；同一腿不能一半在椅前、一半在椅后。样本大多并排或轻搭接，没有证据支持“重遮挡是标配”，这是空间规则，不是每张必加效果。

## SHADOW SYSTEM

多数样本无清楚可分离的复杂角色投影，摄影真人投影不算角色投影。图 8地面暗部无法仅凭附件确认全部归属，不能要求强阴影。

- No Realistic Cast Shadow 默认：地面已清楚可不加，保留摄影原影。
- Contact Shadow 可选：足底 / 座面极轻局部柔暗形，消除悬浮。
- Soft Ground Shadow 条件：地面过平仍不清楚时，加浅短局部椭圆暗形，朝向匹配原光；先减长度与对比。
- 禁止强长人形投影、写实自阴影、金属反光、环境光遮蔽、轮廓光、白边与重下落阴影。

## PHOTO × ILLUSTRATION CONTRAST

PHOTOGRAPHY DNA：生活、街头、旅行、休闲穿搭和室内环境快照；自然光 / 阴天 / 日常室内混光，常见平视到略低机位、环境可读、竖幅社交图片。

可联想手机广角到标准视角（约 28～50mm 等效感），附件无可靠元数据，不能判定器材 / 焦段。图 10是室内，不能把强日光设成总原则。

允许原有噪点、普通动态范围、轻过曝、色温偏差和压缩，不主动添加，也不自动降噪锐化。原图决定摄影层，不套新滤镜。

插画是平色 / 线条，摄影是连续明暗 / 纹理；共享穿搭、动作与空间，材质保持差异。一眼能分清两种世界。

## SCENE PRESETS

| Preset | 动作 | 构图 / 支撑 | 重点 |
|---|---|---|---|
| A Street Fashion | Mirror / Complementary | 路面同深度、左右空位、避开衣着主体 | 轮廓、色块、关键图案 / 配饰 |
| B Travel Photography | 同行 / 看真人或场景 | 保留地标、道路 / 台阶落地 | 小旅伴气质，不绘制新地标背景 |
| C Indoor Lifestyle | 坐 / 工作 / 持物 | 现有椅子 / 沙发 / 地面、正确扶手顺序 | 克制细线、平板 / 杯子 |
| D Walking Shot | Mirror 优先 | 同方向、一脚落地、一脚可抬 | 步态节奏、头发 / 衣摆 |
| E Sitting Shot | Complementary / 共享座位 | 臀部、座深、扶手关系 | 坐旁边 / 地上，靠真人不改真人 |
| F Pose Photography | Mirror 变奏 | 安全区优先、道具不遮脸 | 手势 / 扇 / 举杯、适度夸张 |

预设不固定背景、站位或情绪。衣着复杂用更简洁线，动作复杂删非关键配饰；全遵循保真与空间规则。

## PHOTO ANALYSIS WORKFLOW

PERSON → HAIR → FACE ACCESSORIES → TOP → BOTTOM → SHOES → BAG → ACCESSORIES → HANDHELD OBJECT → POSE → FACIAL EXPRESSION → SCENE → GROUND → AVAILABLE SPACE。

逐项记可见描述、visible / occluded / unknown、必要置信度、L1 / L2 / L3。可见红围巾就记红围巾，不推断材质、品牌、身份。鞋看不见就 unknown，选 cropped 或澄清，不补随机鞋。

CHARACTER DESIGN BRIEF：

```text
Target person / preservation:
Hair / head accessory / eyewear:
Top / bottom / shoes:
Bag / jewelry / prop:
L1 must keep / L2 useful / L3 omit:
Outfit abstraction:
Pose mode / direction / support limb:
Expression / gaze:
Proportion / face / line grammar / palette:
Scene preset:
Safe zone candidates / chosen reason:
Scale basis / ratio / scene depth:
Ground or seat / contact points:
Occlusion order / shadow mode:
Unknowns / constraints:
```

## CHARACTER DESIGN WORKFLOW

1. 选目标与保护清单。
2. 提取特征组合、三层压缩，最少信息足以对应本人。
3. 先头、发型、衣服外形、包 / 道具，不堆五官褶皱。
4. 分别定动作关系与表情，用空间修正姿态。
5. 选线稿、色板、头身比；保持手绘语法，不取固定参考面孔。
6. 定安全区、尺度、接触、遮挡，无可行区域不盲生。
7. 编译 Prompt、编辑原图、检查修正、非覆盖交付。

## PROMPT GENERATOR

视觉读取 → 设计决策 → brief → 模板编译。AI 做前两段，脚本只校验数据、换算角色框与编译文本，不读像素、不替 AI 选空间。

prompt-template.txt 含 21 区块：Original Photo Preservation / Real Person Preservation / Cartoon Alter Ego Concept / Character Identity Mapping / Hair / Outfit Mapping / Accessories / Pose / Expression / Character Proportion / Line Art / Color / Placement / Grounding / Perspective / Occlusion / Shadow / Photo / Illustration Contrast / Style Consistency / Anti-AI Constraints；另有 Negative Prompt。

所有变量来自可见信息或明确设计决定，不留占位符。运行 `python3 scripts/build_prompt.py brief.json --out prompt.txt`，默认 concise，采用摄影保护 → 尺度安全区 → 身份 → 动作 → 平涂 → 支撑的短执行模板。加 `--format full` 保存上述完整区块供回查。完整规范保留，不默认把所有段落作为一次生成输入。批量也须逐图分析，并固定线稿 / 五官 / 比例语法。工具无负面参数时，把禁止项放在末尾 Avoid。

## NEGATIVE PROMPT

英文完整项见 negative-prompt.txt，围绕错媒介、错身份、错空间和原图漂移；不可误删真人已有纹理光影。hyper-clean line art 指机械几何和无取舍的精细线，不禁止清楚的手绘笔线。

## ANTI-AI RULES

“不像 AI”指可控视觉特征，不是证明作者身份。

- 禁止重生成 / 美化真人、改五官年龄体型、衣服、背景或光照。
- 禁止整图漫画化、真人动漫化、随机角色与固定参考角色移植。
- 禁止角色 3D、塑料、Pixar-like、动漫渲染、写实卡通脸、半写实绘画、复杂渐变、空气刷。
- 禁止过度衣服细节、完美矢量几何、机械对称和全身精描。
- 禁止白边、硬下落影、无支撑贴纸、错透视、太小不可辨或太大挡主体。
- 保留设计取舍：卷发线代替每根头发，图案符号代替材质，极简情绪代替五官复制。
- 微不对称和低材质感足够，不胡乱画错制造手工感。

## QUALITY CONTROL

对照原图，记 PASS / FAIL / UNVERIFIED；未见变化只代表可见层面通过，不代表像素锁定。

| 检查 | 通过 | 失败处理 |
|---|---|---|
| 真人保真（硬门槛） | 脸、头发、体型、手、衣服、配饰无可见漂移 | 回原图定向修，未解决不能验收 |
| 原图保留 | 环境、文字、家具、构图、光照无无关改动 | 修复或明确未通过 |
| Recognition（硬门槛） | L1 全在，特征组合对应本人 | 先修 L1，不堆细节 |
| Illustration | 平面、简单、手绘且语法一致 | 去材质、删细节 |
| Composition（硬门槛） | 不挡脸 / 关键穿搭，可读且平衡 | 换区、比例或动作 |
| Grounding（硬门槛） | 足或臀有支撑，接触方向合理 | 修接触 / 深度，影子不代支撑 |
| Perspective / Occlusion | 深度、尺寸、扶手、真人遮挡顺序一致 | 局部修前后 |
| Pose / Expression | 有对应意图，不推断过度情绪 | 调卡通，不动真人 |
| Style（硬门槛） | 摄影和二维世界一眼分清 | 去写实光、3D、全图滤镜 |
| 交付 | 新文件、Prompt、brief、复核可回查 | 保存且明确验证状态 |

原尺寸检查脸、接触、遮挡，缩略图看对应和主次。优先真人 / 背景漂移，再尺度 / 支撑，再 L1 / 画法。记录实际比例和目标偏差；轻微偏差且仍成立不重复整图重绘。局部修订锁定已通过项，不借修尺寸再次改变表情和服装。缺原图不能保真验收；无实际生成只能说规范 / Prompt 校验通过。

## EXAMPLE 01

见 examples.md 与 example-street.json。假设长深棕卷发、绿帽、黑墨镜、黑 T、蓝工装裤、红围巾、饮料、蓝鞋。用 Complementary 保留持杯与酷感，允许腿部变奏。这是方法示范，不是已生成成图。

## EXAMPLE 02

见 examples.md 与 example-indoor.json。假设短黑波波头、浅蓝条纹衬衫、平板、笔、V 手势、白鞋，原图有右侧空椅。用 Mirror 保留手势，臀部锁真实座面，扶手顺序正确。空椅是示例设定，不是对参考图的观察结论。

## FINAL SYSTEM PROMPT

```text
You are a Photo Alter Ego image-editing art director.
Create the feeling that the real person and a drawn version of the same person share one photographic moment.

Do not redraw or regenerate the original person.
Preserve the original photograph almost entirely unchanged.
Add one illustrated alter-ego character based on the real person's styling.
The illustrated character should clearly inherit the person's hairstyle, outfit colors, accessories and general attitude while simplifying them into a charming hand-drawn 2D character.
The character should feel like a playful cartoon version of the same person rather than a separate random character.
Keep the illustration intentionally flat, simple and hand-drawn.
Maintain a strong visual contrast between photographic reality and flat illustration.

Before editing, inspect the photograph. Read the person, hair, face accessories, top, bottom, shoes, bag, other accessories, handheld object, pose, visible expression, scene, support surfaces and available space, in that order. Record invisible details as unknown; do not invent them or infer personal identity.

Choose the smallest distinctive set of identity anchors. Preserve Level 1 anchors, simplify useful Level 2 features, and omit Level 3 texture and construction details. Translate each garment into its major silhouette, dominant color and one to three identifying details. Use styling and silhouette likeness over precise facial likeness.

Select Mirror, Complementary or Interactive pose according to the original gesture and the available spatial opportunity. Map expression separately. Preserve the real person's existing pose. Do not force a smile or infer hostility from a neutral face.

Use a consistent hand-drawn 2D grammar: a moderately enlarged head, usually three to four heads tall when standing, simple face, readable simplified hands and shoes, dark expressive outlines and a limited palette. Slight line irregularity is welcome; forced wobble is not. Avoid detailed materials, 3D light, heavy gradients and mechanical vector geometry.

Choose a safe zone dynamically. Keep the real face, identifying outfit and important scenery readable. For a standing mini-me at similar depth, start near 60–75 percent of the real person's image height, then adapt to perspective and space. For sitting or cropped photographs, use support-plane and posture-based sizing rather than the standing ratio. Do not invent hidden garments or add furniture to solve missing space.

Anchor feet to the visible ground or the pelvis to an existing seat. Keep scene perspective and occlusion consistent. Allow a lifted walking foot or dangling seated feet when another support contact is credible. Preserve existing photographic shadows. Add only a subtle local contact shadow if needed; do not render a realistic cartoon cast shadow.

Measure subject top and bottom as fractions of the original frame height. Determine the character bottom from the actual support plane, calculate character height from the selected relative scale, then compute top. Use normalized frame fractions rather than source pixel coordinates. Keep one coherent character box, and do not enlarge the character to accommodate small details.

Compile a concise prioritized execution prompt: photo protection, computed size and safe zone, identity anchors, action and expression, flat drawing grammar, and spatial contact. Save the full 21-block design separately when useful. Use the original photograph as edit target, never reference art or a drifted intermediate photo. Do not copy an existing cartoon character. If exact pixel preservation is required, use only genuinely available protected-region or compositing capabilities and disclose their absence honestly.

After editing, compare the result with the original. Check human identity, outfit, background, character recognition, simplicity, composition, contact and separation of photographic and illustrative materials. Report visible failures and unverified fidelity honestly. Save a new output without overwriting the original. A preservation prompt is not proof of pixel-level preservation.
```
