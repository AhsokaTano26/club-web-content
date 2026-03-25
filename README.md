# 📝 Club Web Content  
这是 同好会官网 (club-web) 的独立内容仓库。本仓库存储所有静态资源、博客文章及时间轴数据，通过 Nuxt Content 远程驱动实时同步至主站。

## 📂 目录结构
```Plaintext
.
├── blog/           # 文章 (.md)
├── timeline/       # 时间轴数据 (.md)
└── assets/         # 存放文章中引用的图片、附件
```
## 🚀 内容规范
### 1. 博客文章 (Blog)

存放在 blog/ 目录下。每篇 Markdown 文件必须包含以下 Frontmatter 字段：
```text
---
title: "文章标题"
date: "2026-03-24"
type: "official" # 可选值: anniversary, exhibition, official
description: "简短的文章摘要"
---

这里开始编写正文内容...
```
### 2. 时间轴 (Timeline)

存放在 timeline/ 目录下。用于展示同好会的发展历程：
```text
---
title: "里程碑事件名称"
date: "2026-01-01"
description: "事件的具体描述"
---

这里开始编写正文内容...
```
## 🛠 维护与同步
本仓库与主站采用 Decoupled (解耦) 模式运行：

直接编辑：你可以直接在 GitHub 网页端或本地克隆本仓库修改 .md 文件。

自动触发：推送到 main 分支后，GitHub Action 会触发 Cloudflare Pages 的 Deploy Hook，自动重新构建主站。

本地预览：在主项目 club-web 中运行 npm run dev，Nuxt 会自动拉取此仓库的最新内容。

## ⚠️ 注意事项
图片资源：请尽量将图片放在 assets/ 文件夹下，并使用相对路径引用。

格式检查：确保 YAML Frontmatter 格式正确（注意冒号后的空格），否则主站可能会解析失败。

分支管理：主站仅拉取 main 分支的内容。
