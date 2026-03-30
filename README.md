# 📝 Club Web Content  
这是 **同好会官网 (club-web)** 的独立内容仓库。本仓库存储所有静态资源、结构化 Markdown 数据，通过 Nuxt Content 引擎远程驱动，实现主站内容的实时同步与解耦管理。

## 📂 目录结构
```Plaintext
.
├── activities/     # 活动数据 (.md)
├── blog/           # 官方博客 (.md)
├── notice/         # 官方公告 (.md)
├── timeline/       # 官方进度 (.md)
├── orgs/           # 组织档案 (.md)
├── projects/       # 联协公招 (.md)
└── archive/        # 联协映像 (.md)
🚀 内容规范 (Frontmatter)
每篇 Markdown 文件必须包含符合规范的 md Frontmatter 字段，以便主站程序正确解析。
```
1. 活动 (Activities)  
存放在 activities/ 目录下。用于展示各类社团活动。

```md
---
title: "活动标题"
description: "简要介绍"
date: "2026-03-30"
status: "online" # 可选: online, in_person, regional
org: "ORG_CODE"  # 所属组织代号
author: "编写人"
type: "official" # 可选: official, anniversary, nexus
---

这里开始编写正文...
```
2. 官方博客 (Blog)  
存放在 blog/ 目录下。

```md
---
title: "博客标题"
date: "2026-03-30"
description: "内容摘要"
author: "编写人"
type: "docu"     # 可选: docu (文件), artic (推文), rese (研究成果)
---

这里开始编写正文...
```
3. 官方公告 (Notice)  
存放在 notice/ 目录下。

```md
---
title: "公告标题"
date: "2026-03-30"
description: "公告核心内容摘要"
author: "发布人"
type: "notice"   # 可选: regula (条例), event (官方活动), notice (公告)
---

这里开始编写正文...
```
4. 官方进度 (Timeline)  
存放在 timeline/ 目录下。用于记录项目或同好会的发展轨迹。

```md
---
title: "进度节点名称"
date: "2026-03-30"
description: "进度详细说明"
author: "记录人"
status: "prog"   # 可选: prog (进度), changes (更改), record (记录)
---

这里开始编写正文...
```
5. 组织档案 (Orgs)  
存放在 orgs/ 目录下。定义组织的基础信息与视觉样式。

```md
---
orgs_id: "tech-01"
title: "组织名称"
description: "组织介绍"
founded: "2024-01-01"
joined_at: "2025-01-01"
members_count: 10
website: "https://..."
github: "[https://github.com/](https://github.com/)..."
status: true     # 是否加入联协体系
leader: "负责人名称"
location: "global" # 可选: regional, global
type: "fc"       # 可选: fc (应援团), dkk (同好会)
tag: "official"  # 可选: branch (分支), official (官方)
theme:
  logo: "lucide:shrub"     # 组件库图标或路径
  primaryColor: "#7c3aed"  # 组织主题色
  bgImage: "/orgs/test.jpg" 
---

这里开始编写正文...
```
6. 联协公招 (Project)  
存放在 projects/ 目录下。

```md
---
title: "项目名称"
description: "项目介绍"
orgs: "所属组织"
date: "2026-03-30"
author: "编写人"
status: "funding" # 可选: funding (众筹中), need_creator (需创作者), finding_resonance (寻共鸣), others
link: "https://..."
---

这里开始编写正文...
```
7. 联协映像 (Archive)  
存放在 archive/ 目录下。  

```md
---
title: "映像名称"
description: "映像介绍"
orgs: "所属组织"
date: "2026-03-30"
author: "编写人"
type: "gallery"  # 可选: gallery (图册), tweet (推文)
---

这里开始编写正文...
```
🛠 维护与同步  
解耦模式：本仓库作为 Content Provider，不包含任何程序逻辑，仅负责存储数据。  
自动触发：推送到 main 分支后，GitHub Action 会触发主站的重新构建或 Hook 刷新。  
格式检查：  
请严格遵守 md 语法（冒号后必须有空格）。  
日期请使用 YYYY-MM-DD 格式。  
图片路径请确保主站 public 目录下存在对应资源。  
⚠️ 注意事项  
字段唯一性：orgs_id 必须唯一，以便在其他板块（如 Activity）中通过该 ID 进行关联。  
状态枚举：请务必使用代码中定义的英文枚举值（如 online），不要直接写中文，否则前端可能无法匹配对应的 UI 组件。  