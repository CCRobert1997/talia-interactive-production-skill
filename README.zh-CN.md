# Talia 互动影游制作 Skill

[English README](README.md)

一套与模型无关的 Talia 图片/视频互动影游制作 Skill，覆盖分支剧本、媒体生成工单、图片和视频质检、互动配置以及通过验证的 Talia 草稿项目。

选择一个语言版本，将整个目录复制到 Agent harness 支持的 Skill 目录：

- English：`skills/en/talia-interactive-production/`
- 简体中文：`skills/zh-CN/talia-interactive-production/`

两个版本具有相同流程、安全边界、验证脚本和 Skill 名称。同一个 Skill 根目录只安装一个语言版本。

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

需要 Python 3；媒体检查需要 `ffprobe`。Talia CLI、生图、视频和浏览器能力由宿主环境按需提供。

## 许可证

Apache-2.0。
