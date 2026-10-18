#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
engraved-horizon-prints 通用安装脚本

把本 skill 装到本机所有「支持 skill 机制」的 AI 客户端目录里，
一次运行，同时覆盖 WorkBuddy / CodeBuddy / Claude Code。

用法：
    python install.py          # 安装到所有已识别的客户端目录
    python install.py --list   # 只列出会安装到哪些目录，不实际写入

原理：skill 就是一份 SKILL.md + references/，放到各客户端的
<用户目录>/.<客户端>/skills/<skill-name>/ 下即可被自动加载。
"""

import os
import shutil
import sys

SKILL_NAME = "engraved-horizon-prints"

# 各客户端技能目录（相对用户主目录）
TARGET_DIRS = [
    ".workbuddy/skills",   # WorkBuddy
    ".codebuddy/skills",   # CodeBuddy Code
    ".claude/skills",      # Claude Code
]

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_ROOT = os.path.join(HERE, "SKILL.md")
SRC_REFS = os.path.join(HERE, "references")


def list_only():
    home = os.path.expanduser("~")
    print("会安装到以下目录（用户主目录 %s 下）：" % home)
    for d in TARGET_DIRS:
        print("  -", os.path.join(home, d, SKILL_NAME))
    print("\n运行 `python install.py` 即可实际写入。")


def main():
    if "--list" in sys.argv:
        list_only()
        return

    if not os.path.isfile(SRC_ROOT):
        print("错误：找不到 SKILL.md，请在本仓库根目录下运行本脚本。")
        sys.exit(1)

    home = os.path.expanduser("~")
    installed = []
    for d in TARGET_DIRS:
        dest = os.path.join(home, d, SKILL_NAME)
        try:
            os.makedirs(dest, exist_ok=True)
            shutil.copy2(SRC_ROOT, os.path.join(dest, "SKILL.md"))
            refs_dest = os.path.join(dest, "references")
            if os.path.isdir(SRC_REFS):
                if os.path.isdir(refs_dest):
                    shutil.rmtree(refs_dest)
                shutil.copytree(SRC_REFS, refs_dest)
            installed.append(dest)
        except OSError as e:
            print("跳过 %s（失败：%s）" % (dest, e))

    if not installed:
        print("未能安装到任何目录。")
        sys.exit(1)

    print("已安装到 %d 个位置：" % len(installed))
    for p in installed:
        print("  ✔", p)
    print("\n装完重启对应客户端会话，让它重新扫描 skill 列表即可生效。")


if __name__ == "__main__":
    main()
