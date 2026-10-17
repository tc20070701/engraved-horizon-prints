# engraved-horizon-prints

把任意照片重绘为「**蓝白木刻版画 · 苍茫地平线**」风格艺术图的 AI Skill。

![样图](assets/sample.png)

**风格特征**：手工木刻 / 麻胶版画质感，密集手工排线（hatching），靛蓝 + 米白限色印刷，竖幅长卷构图，宏大风景中点缀极小的人、马、飞鸟剪影。

---

## 一键安装

适用于 WorkBuddy、CodeBuddy、Claude Code 等支持 skill 机制的 AI 客户端。

### macOS / Linux

```bash
git clone https://github.com/tc20070701/engraved-horizon-prints.git ~/.workbuddy/skills/engraved-horizon-prints
```

### Windows（PowerShell）

```powershell
$skills = "$env:USERPROFILE\.workbuddy\skills"
New-Item -ItemType Directory -Force -Path $skills | Out-Null
Invoke-WebRequest https://github.com/tc20070701/engraved-horizon-prints/archive/refs/heads/main.zip -OutFile "$env:TEMP\ehp.zip"
Expand-Archive "$env:TEMP\ehp.zip" -DestinationPath $env:TEMP -Force
Remove-Item "$skills\engraved-horizon-prints" -Recurse -Force -ErrorAction SilentlyContinue
Move-Item "$env:TEMP\engraved-horizon-prints-main" "$skills\engraved-horizon-prints"
```

### 让 AI 帮你装（最省事，无需记命令）

把下面这段整段复制，粘给你的 AI 助手：

```
帮我安装一个生图 skill。请从 https://github.com/tc20070701/engraved-horizon-prints 获取仓库内容（用 WebFetch 读取 raw.githubusercontent.com 上的 SKILL.md 和 references/style-guide.md，或用 git clone 到临时目录），然后在本机的用户级 skill 目录（Windows: C:\Users\<用户名>\.workbuddy\skills\，macOS/Linux: ~/.workbuddy/skills/）下创建 engraved-horizon-prints 文件夹，把 SKILL.md 放在根目录、style-guide.md 放在 references/ 子目录，内容原样写入不要修改。完成后读一遍确认文件完整。
```

> 若你的 AI 无法联网，用仓库里的 [`INSTALL_PROMPT.md`](INSTALL_PROMPT.md) —— 它把两个文件的全文嵌在提示词里，离线也能装。

装完重启一下会话，让客户端重新扫描 skill 列表。

---

## 使用方法

丢一张照片给你的 AI，说一句：

> 做成木刻版画风

就会自动走这个 skill。支持图生图时以原照片为参考保留构图；若模型读不了图，AI 会请你一句话描述画面，再拼提示词生成。

想换色版就直接说：

> 用纯蓝白单色版 / 用三色版

---

## 两种色版

| 色版 | 用色 | 适用 |
|---|---|---|
| **三色版**（默认） | 靛蓝 `#2B4C7E` + 米白纸底 `#F2EDDF` + 鼠尾草绿 `#8A9B6E` + 赭黄 `#C9A84C` | 草原、田野、有植被的场景 |
| **纯蓝白单色版** | 单色靛蓝 `#2B4C7E` + 米白纸底 `#F5F0E1` | 雪山、湖泊、极简场景 |

---

## 目录结构

```
engraved-horizon-prints/
├── SKILL.md                    # 工作流与规则（主控文件）
├── references/
│   └── style-guide.md          # 风格 DNA、色值、提示词模板、自检清单
├── assets/
│   └── sample.png              # 效果样图
├── INSTALL_PROMPT.md           # 自包含安装提示词（离线安装用）
└── README.md
```

---

## 没有生图工具也能用

skill 的核心资产是提示词。若你的环境没有 ImageGen 之类的生图能力，AI 会输出完整提示词，拿去 Midjourney / 即梦 / 其他平台一样能出图。

---

## 自定义

改 `references/style-guide.md` 即可调整风格：换色值、改排线密度描述、调整构图规则、增删场景段。改完 `SKILL.md` 里的工作流不用动。

---

## 注意

生图会消耗额度（单张约 5–10 credits），生成前 AI 会提示。

---

MIT License · 由 杨哥 与 小八 基于 4 张实拍照片的风格分析构建
