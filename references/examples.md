# 两个完整使用示例

以下都是假设的新照片与设计 brief，不把参考图当待改原图，也不声称已经生成或验收。示例 JSON 保留全部字段，默认编译简短执行 Prompt，使用 --format full 编译完整 21 区块与 Negative Prompt。composition 中的数值是明确假设输入的构图，不来自原参考图测量。

## EXAMPLE 01｜街头穿搭：同穿搭、动作变奏

假设原图：真人在画面中右侧，左侧有完整人行道空位。长深棕卷发、绿棒球帽、黑墨镜、黑短袖 T 恤、蓝宽腿工装裤、腰间红围巾、黑斜挎包、银项链、橙饮料、蓝运动鞋。中性酷感，一手持饮料、一手插口袋。

Character Design Brief：

- L1：长卷发＋绿帽、黑墨镜、黑 T / 蓝工装裤、红腰巾。
- L2：黑包、项链、饮料、蓝鞋。饮料在该图占据明显动作关系，可按实际图片升为 L1。
- L3：帽上文字、牛仔颗粒、围巾微纹、缝线、小褶。
- 大形：约 3.5 头身、大头、宽裤；Round Ink 深炭线；核心色块继承穿搭。
- 动作：Complementary；维持持杯 / 插袋意图，腿部放松前后站，不要求逐关节复制。
- 表情：小平嘴、轻头倾，墨镜遮眼，不画生气脸。
- 位置：左侧同地砖深度，约真人可见全身高度 70%，给穿搭留缝。
- 空间：一只鞋稳踏地面，另一脚跟轻抬但前掌有支撑；无真人脸 / 衣着重遮挡，只可选极轻足底暗形。

完整可机读输入：[example-street.json](example-street.json)。运行：

```text
python3 scripts/build_prompt.py references/example-street.json --out /your/output/example-street-prompt.txt
```

最终 Prompt 的关键决策不是“加一个可爱女孩”，而是“保留这组身份锚点，选择动作变奏，放在明确的人行道面片并保持摄影层”。实际执行 Prompt 由 concise 模板编译，完整回查版本使用 --format full；两者都保留保真、身份与空间约束。

## EXAMPLE 02｜室内坐姿：同步手势、真实座位支撑

假设原图：真人坐画面左侧，右侧同深度存在一把真实空椅，桌椅位置清楚。短黑波波头、小刘海、浅蓝条纹衬衫卷袖、浅色短裤、白袜白鞋、一手平板，另一手握笔比 V，轻松微笑。

Character Design Brief：

- L1：短波波头 / 刘海、浅蓝条纹卷袖衬衫、平板与握笔 V 手势。
- L2：短裤、白袜白鞋；未见包，禁止新增。
- L3：缝线、平板反光、小褶与无法辨识的首饰细节。
- 大形：先以约 3.5 头身构造，再弯成坐姿；Loose Pen 深棕细线，少量简眼白。
- 动作：Mirror；手势和持物同义，腿部适当变化。表情轻微闭口笑，不夸大。
- 位置：右侧真实空椅。以座高与景深决定尺度，75% 坐姿外接高度仅是辅助目标。
- 空间：臀部在椅垫上，前扶手在局部衣袖 / 腿前，靠背在后；腿可稍垂，不能为脚触地伸长身体。
- 阴影：不加写实投影，必要时只加浅座面接触暗形。

完整可机读输入：[example-indoor.json](example-indoor.json)。运行：

```text
python3 scripts/build_prompt.py references/example-indoor.json --out /your/output/example-indoor-prompt.txt
```

若真实上传图没有空椅，应重新分析可用座面 / 地面，不能照抄此示例凭空加椅。缺乏支撑时生成器应停止，先解决设计。

## JSON 输入约定

必填非空文本：photo、person、hair、outfit、accessories、pose、expression、proportion、face、line_art、color、placement、grounding、perspective、occlusion、shadow、style_consistency、constraints。

必填字符串数组：level1（至少一项可见锚点）、level2、level3、unknowns（后三项可空）。不是要求所有特征都已知，unknowns 保留未见信息。

pose_mode 只能是 Mirror / Complementary / Interactive。preset 使用六个预设的英文名。support_visible 必须为 true；这是 AI 已确认支撑面的声明，不是脚本图像检测结果。

scale 对象：basis、ratio、explanation。ratio 是小数比例，不能把 70% 写成 70。basis：

- standing_relative：角色站姿画面头到最低鞋底高度 ÷ 真人对应高度，常规允许 0.50～0.80。
- seated_relative：角色坐姿外接高度 ÷ 真人坐姿外接高度，常规允许 0.50～1.00，座面深度优先。
- frame_relative：裁切构图的角色可见高度 ÷ 原图高度，常规工作区间 0.05～0.50；这是软件保护范围，不来自参考统计。
- custom：明确例外，例如用户指定同高或前景透视需要。另填 comparison（比较对象）与 reason（例外原因），仍必须有真实支撑。

常规范围是避免常见错误的校验，不是禁止一切创造性例外。脚本不会分析照片、自动画图或检测真实保真。输出默认拒绝覆盖已有文件。


## v1.1.0 composition 与执行模式

实际生成必填 composition，全部为原图的 0～1 比例：subject_top、subject_bottom（真人可见头到脚 / 坐姿高度）、character_bottom（角色支撑位置）、character_center_x、character_width。生成器算出角色 top / height / left / right，检查框是否越界。相对人体模式用真人高度 × scale.ratio，frame_relative 直接用 scale.ratio，custom 另填 composition.character_height，避免未知比较对象无法换算。

值 0.55 表示画面高度 55%，不是 55 像素。不得自己再写与计算不同的头顶位置 / 总高度；坐姿仍须先由真实座面定 bottom，不能把百分比当支撑检测。

命令默认 concise，适用于工具执行。增加 --format full 保留 21 区块；旧 JSON 缺 composition 时仍能生成 full 回查，concise 会要求先补构图信息，避免静默猜位置。模块 compile_prompt(brief) 保留旧的 full 默认，CLI 默认为 concise。

详见 generation-control.md 的尺寸例子、画法预算、工具保真分流和验收顺序。
