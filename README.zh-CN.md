# Talia 互动影游制作 Skill

[English README](README.md)

一套与模型无关的 Agent Skill，用于设计和制作 Talia 图片/视频互动影游：分支剧本、媒体生成工单、质检门槛，以及通过 Talia CLI 装配并验证的草稿项目。

适用于任何读取 [Agent Skills](https://agentskills.io) `SKILL.md` 格式的 harness（Claude Code、OpenAI Codex、Cursor、OpenCode 等）；没有 skill 机制的 harness 用一段项目指令指向 `SKILL.md` 即可。

## 安装

一条命令装进多个 harness：

```bash
npx skills@latest add CCRobert1997/talia-interactive-production-skill \
  --agent claude-code --agent codex --agent cursor
```

或手动把 `skills/talia-interactive-production/` 整个目录复制到 harness 的 skill 目录：

| Harness | 路径 |
|---|---|
| Claude Code | `~/.claude/skills/`（用户级）或 `.claude/skills/`（项目级） |
| OpenAI Codex | `~/.codex/skills/`（用户级）或 `.codex/skills/`（项目级） |
| 无 skill 发现机制（自建 DeepSeek harness、Trae、WorkBuddy 等） | 目录留在仓库内，把 [harness-installation.md](skills/talia-interactive-production/references/harness-installation.md) 里的那段指令贴进 `AGENTS.md` / `CLAUDE.md` / 项目规则 / system prompt |

Agent 加载的是英文 `SKILL.md`。给人读的简体中文译本在 `skills/talia-interactive-production/i18n/zh-CN/`，英文为准，译本可能滞后。

## 目录

```
skills/talia-interactive-production/
├── SKILL.md                 # 入口，harness 加载它
├── agents/openai.yaml       # Codex 展示元数据（可选）
├── references/              # SKILL.md 按需引用
├── adapters/                # 每条生图通道一页（codex image_gen / OpenAI Images API / 即梦浏览器 / 仅出工单）
├── templates/               # 复制后填：node_graph.json（直接能过验证器）/ image_order.md / handoff_record.md
├── scripts/                 # Python 3，无第三方依赖（inspect_media 需 ffprobe）
└── i18n/zh-CN/              # SKILL.md + references 的中文译本
```

[PORTABILITY.md](PORTABILITY.md) 记录哪些 harness 跑过可移植性测试，欢迎 PR 填格子。

## 安全边界

Skill 可以装配和验证 Talia 草稿，包括替换已有节点的图片或视频 URL。Skill 不调用 Talia 付费生成、发布、取消发布、删除、账单、积分、订阅、密码或账号管理功能；这些操作由创作者在 Talia 网页端手动完成。

## 模型与 Harness 兼容

工作流根据实际探测到的能力选择路线，不根据模型品牌做假设。生图、识图、视频理解、浏览器上传、Shell 和持久登录通常同时受模型与 harness 影响。无法执行或验证的工作必须标记为 `prepared`（已准备）或 `unverified`（未验证），不能写成已经完成。

## 自带工具

```bash
python3 scripts/capability_probe.py
python3 scripts/validate_node_graph.py path/to/story/node_graph.json
python3 scripts/inspect_media.py path/to/video.mp4
```

需要 Python 3；媒体检查需要 `ffprobe`。Talia CLI 已开源，`npm i -g github:CCRobert1997/talia-cli` 即装（见 [talia-cli.md](skills/talia-interactive-production/references/talia-cli.md)）；生图、视频和浏览器能力由宿主环境按需提供。

## 许可

Apache-2.0。
