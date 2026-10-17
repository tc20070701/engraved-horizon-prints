# 离线安装提示词（自包含版）

仓库地址：https://github.com/tc20070701/engraved-horizon-prints

**如果对方的 AI 能联网，用 README 里的三条一键命令就够了**，不必用这份文件。这份是**离线兜底方案**——把 skill 两个文件的全文嵌进提示词，对方不需要下载任何东西。

下面 `--- 复制开始 ---` 到 `--- 复制结束 ---` 之间的内容，整段复制粘给对方的 AI 助手（WorkBuddy / CodeBuddy / Claude Code 等支持 skill 的客户端），它的 AI 会自动建目录、写文件、装好 skill。对方不需要懂任何技术，也不需要下载文件。

> 转发时只发这一段提示词即可，本说明文字不必一起发。

--- 复制开始 ---

帮我安装一个生图技能，名字叫 `engraved-horizon-prints`。请按下面的步骤操作：

1. 确定本机的用户级 skill 目录：Windows 是 `C:\Users\<用户名>\.workbuddy\skills\`，macOS/Linux 是 `~/.workbuddy/skills/`。如果不确定，问我一句。
2. 在该目录下创建两级文件夹：`engraved-horizon-prints\references\`。
3. 在 `engraved-horizon-prints\` 下新建 `SKILL.md`，内容**原样写入**下面第一个代码块里的全部文字（包括开头的 `---` 和结尾的 `---`）。
4. 在 `engraved-horizon-prints\references\` 下新建 `style-guide.md`，内容原样写入下面第二个代码块里的全部文字。
5. 写完后用 Read 工具读一遍两个文件，确认内容完整、没有截断，然后告诉我装好了。

不要修改、不要总结、不要省略文件内容，原样写入即可。

第一个文件 SKILL.md：

````markdown
---
name: engraved-horizon-prints
description: 把用户提供的照片/场景重绘为「蓝白木刻版画·苍茫地平线」风格的艺术图。风格特征：靛蓝+米白为主的双色调木刻/麻胶版画质感，密集手工排线（hatching），竖幅长卷构图，宏大山川天空下点缀极小的人、马、飞鸟剪影。当用户说"把这张照片做成木刻版画/蓝白版画/雕刻风格"、"生成同风格艺术图"、"engraving/linocut 风格化照片"时使用本 skill。典型触发：上传照片后要求风格转换、或按文字描述生成同风格新作。
agent_created: true
---

# Engraved Horizon Prints —— 蓝白木刻版画风格生图

## 用途

把任意照片或文字场景描述，转换为「蓝白木刻版画·苍茫地平线」风格的艺术图，风格基准来自用户提供的 4 张样图（山川湖泊、雪山倒影、群鸟草原、孤马河谷）。

## 工作流

1. **获取画面内容**：
   - 用户上传了照片且当前环境支持图生图 → 直接以照片作为 `image1` 参考图调用生图工具，提示词描述"保留照片的构图与主体"。
   - 当前模型无法读图 → 请用户用一两句话口头描述画面主体与构图（例如"湖边一座山、山脚下一个人"），把描述填进提示词模板的【场景】槽位。
2. **组装提示词**：从 `references/style-guide.md` 复制「风格固定段」，与场景段拼接。风格固定段**一字不改**地附加，场景段描述主体、构图分层、点缀元素。
3. **选择色版**：默认用「蓝+绿+赭三色版」；用户要求"纯蓝白/单色"时换用「纯蓝白单色版」。两种色版的色值与措辞见 references。
4. **调用生图工具**：ImageGen 或等价工具，竖幅比例（9:19~9:20 近似竖长卷轴，工具不支持精确比例时选最高的竖幅档位）。生成后把成品图展示给用户。
5. **验收对照**：用 references 里的「风格自检清单」逐项核对；明显跑偏（出现彩色写实、照片感、缺少排线纹理）时，强化风格段中的排线/版画关键词重新生成一次。

## 关键规则

- 排线（hatching/engraved line work）是风格灵魂，提示词中必须出现，且要求"线条随形走"（contour-following hatching）。
- 画面必须有**极小尺度的生命点缀**（一匹马、一个人、一群飞鸟），与宏大风景形成尺度对比——这是样图最显著的构图签名。
- 禁止照片写实、渐变平滑的数码上色、过多颜色。色数 ≤ 4（含纸底色）。
- 竖幅长构图，主体分层：天空排线区 / 中景山川 / 前景水面或草原。

详细风格 DNA、色值、提示词模板与自检清单见 `references/style-guide.md`。
````

第二个文件 references/style-guide.md：

````markdown
# 风格参考：蓝白木刻版画·苍茫地平线

> 基准：用户 4 张样图（山湖孤马 / 雪山倒影 / 群鸟草原 / 孤马河谷）。本文档是提示词组装的唯一事实来源。

## 风格 DNA（六要素）

1. **版种**：手工木刻 / 麻胶版画（woodcut / linocut print），带老书插图与 WPA 年代海报的复古感。
2. **排线**：整幅画由密集手工刻线构成，无平滑渐变。线条**随形体走向**排布——天空用水平长线，山体用沿坡面的斜线，水面用水平波纹线，草地用短促的戳点与短线。
3. **色彩**：限色印刷（limited color palette, letterpress/risograph feel），≤ 4 色含纸底。
4. **构图**：竖幅长卷（约 9:19），三段分层——大面积天空排线区 / 中景山川 / 前景水面或草原。地平线常压在下三分之一处。
5. **尺度签名**：宏大风景中置一个**极小**的生命元素（一匹马、一个人、一群飞鸟），剪影化处理，营造苍茫感。
6. **质感**：纸张纹理、油墨不均、印刷颗粒、细边框线（部分样图有）、轻微做旧。

## 色版

### 三色版（默认，对应样图 3/4）
- 靛蓝 `#2B4C7E`（主色，天空/山体/线条）
- 米白纸底 `#F2EDDF`
- 鼠尾草绿 `#8A9B6E`（草原/田野）
- 赭黄 `#C9A84C`（点缀，田野高光）

### 纯蓝白单色版（对应样图 1/2）
- 靛蓝 `#2B4C7E` 单色 + 米白纸底 `#F5F0E1`

## 提示词组装

### 模板（英文为主，生图模型对英文更稳）

```
[场景段] + [风格固定段] + [色版段] + [负面约束段]
```

**场景段**（按用户照片/描述填写，务必包含"极小生命点缀"）：
```
A vast {场景主体，如 mountain lake / snow-capped peaks reflected in still water /
rolling grassland valley}, vertical composition, big sky occupying upper half,
a tiny lone {horse / figure / flock of birds} in the {lower third / middle distance},
sense of immense scale and solitude.
```

**风格固定段**（一字不改）：
```
Hand-carved woodcut linocut print style, dense engraved hatching and cross-hatching
line work covering the entire image, contour-following lines (horizontal strokes for
sky and water, diagonal strokes along mountain slopes, short stippled strokes for
grass), vintage book illustration and WPA poster aesthetic, visible paper texture,
ink grain and slight print imperfections, thin border frame, no smooth gradients,
no photographic detail.
```

**色版段（三色版）**：
```
Limited 3-color letterpress palette: indigo blue (#2B4C7E) as dominant color,
cream paper background (#F2EDDF), sage green and ochre accents on the land.
```
**色版段（单色版）**：
```
Monochrome two-tone print: single indigo blue ink (#2B4C7E) on cream paper (#F5F0E1).
```

**负面约束段**：
```
Avoid: photorealism, full-color painting, smooth digital gradients, more than 4 colors,
modern vector-flat style, text or watermark.
```

### 图生图（image-to-image）用法

以用户照片为 `image1` 参考图，提示词开头加：
```
Transform the reference photo into the style below, preserving its composition and
main subjects. 
```
然后拼接：风格固定段 + 色版段 + 负面约束段（场景段可省略或简述主体）。

### 四个样图场景的可复用场景段

1. 山湖孤马：`a majestic mountain range above a calm lake, a tiny white horse grazing on a small patch of shore in the lower middle, turquoise-teal water`
2. 雪山倒影：`snow-capped mountain peaks reflected in still water with concentric ripple rings, grassland strip in the middle, clouds`
3. 群鸟草原：`a flock of birds swirling up from a wide grassland into towering cumulus clouds, a few tiny horses grazing on the plain, distant low mountains`
4. 孤马河谷：`a winding river valley with terraced fields in green and ochre, a lone dark horse standing on a river bend sandbar`

## 风格自检清单（生成后逐项核对）

- [ ] 全图由排线构成，无平滑渐变？
- [ ] 线条方向随形体走（天空水平、山体斜向、水波纹水平）？
- [ ] 色数 ≤ 4，靛蓝为主、米白纸底？
- [ ] 竖幅长构图、三段分层？
- [ ] 有极小尺度的生命点缀（马/人/鸟）？
- [ ] 有纸张纹理/油墨颗粒感，无照片写实感？

任一项不满足 → 在提示词中强化对应关键词重生成。
````

--- 复制结束 ---

## 装好后怎么用

对方重启一下会话（让客户端重新扫描 skill 列表），然后丢一张照片说「做成木刻版画风」即可自动触发。前提是他那边有生图工具（如 ImageGen）；没有的话，skill 会输出完整提示词，他可以拿去别的平台生图。
