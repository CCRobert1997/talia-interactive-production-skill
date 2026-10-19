# Talia CLI 安全用法

## 安装

CLI 开源于 <https://github.com/CCRobert1997/talia-cli>（MIT），仓内直接附带预构建单文件，只需 Node 20+：

```bash
npm i -g github:CCRobert1997/talia-cli
talia login you@example.com     # 与 editor.taliaapp.com 同一个创作者账号
talia whoami
```

工作区里 `talia` 已在 `PATH` 时直接用。在 Talia 编辑器 monorepo 内等价写法是 `npm run cli -- <命令>`。

不设 `SUPABASE_URL` / `SUPABASE_ANON_KEY` 时 CLI 默认连 Talia 生产库；内置 anon key 本就公开，RLS 把每次写入限定到登录者本人。要连其他实例，设这两个变量（或写 `~/.talia/config.json`）覆盖。

## 读机器可解析输出

所有读命令支持 `--json`，输出一行 JSON；写命令加 `--json` 输出 `{"ok":true,"id":"…"}`。优先用 `--json`，不要解析自然语言输出。先执行只读检查：

```bash
talia whoami --json
talia projects --json
talia validate <projectId> --json
```

## 允许操作

Skill 可以创建草稿项目；新增和更新节点；设置标题、图片、视频和自动推进；设置开始节点；新增和更新选项；配置样式、Tap Region 和互动模板；新增变量和成就；上传已经制作好的素材；导入大纲；列出状态；运行验证。

允许替换已有节点的图片或视频 URL。替换前记录节点 ID、旧 URL、新 URL 和已验收本地源文件。替换并不授权删除旧素材。

## 排除操作

不得调用或封装以下命令：通过 Talia 付费生成媒体；发布、更新已发布快照或取消发布；删除项目、选项、素材、变量、成就或远程媒体；修改账单、积分、订阅、密码或账号设置。

已安装 CLI 即使暴露这些命令，也不代表本 Skill 可以使用。

## 修改流程

1. 根据项目记录和只读输出确认项目 ID。
2. 确认每项本地媒体已经通过质检。
3. 记录当前 ID 和旧值。
4. 只执行必要的最小修改。
5. 运行 `talia validate <projectId>`。
6. 记录命令、受影响 ID/URL、验证输出和剩余人工操作。
7. 在网页端预览每条路线；由创作者手动发布。

不要把凭据写入 Shell 历史、项目文件、示例或日志。使用 CLI 凭据存储或环境提供的安全登录流程。
