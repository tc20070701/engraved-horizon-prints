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
