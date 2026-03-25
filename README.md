# 📝 Club Web Content  
这是 同好会官网 (club-web) 的独立内容仓库。本仓库存储所有静态资源、博客文章及时间轴数据，通过 Nuxt Content 远程驱动实时同步至主站。

## 📂 目录结构
```Plaintext
.
├── blog/           # 活动文章 (.md)
├── timeline/       # 时间轴数据 (.md)
├── orgs/           # 组织介绍 (.md)
├── projects/       # 项目文章 (.md)
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

### 3. 组织介绍 (orgs)

存放在 orgs/ 目录下。用于展示组织简介：
```text
---
ID: "2"
title: "Test 组织"
description: "致力于研究跨维度交互技术与幻想乡生态保护的非营利性技术组织。"
founded: "2024-01-01"
leader: "Tano"
members_count: 12
website: "https://example.com"
github: "https://github.com/..."
status: "Verified"
theme:
  logo: "lucide:shrub"
  primaryColor: "#7c3aed"
  bgImage: "/orgs/test.jpg"
  sidebarOpacity: 0.8
  mainOpacity: 0.4
---

这里开始编写正文内容...
```
#### 字段详细说明

|      字段       |   类型   | 必填 | 说明                                                                                                                                                                                                   |        示例         |
|:-------------:|:------:|:--:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------:|
|      ID       | String | 是  | 组织的唯一标识符，建议使用英文或数字。                                                                                                                                                                                  |        "2"        |
|     title     | String | 是  | 组织显示的正式名称。                                                                                                                                                                                           |     "Test 组织"     |
|  description  | String | 是  | 显示在标题下方的斜体描述。                                                                                                                                                                                        | "致力于研究...的非营利组织。" |
|    founded    | String | 是  | 成立日期，建议格式 YYYY-MM-DD。	"2024-01-01"                                                                                                                                                                   |
|    leader     | String | 是  | 现任负责人或创始人名称。	"Tano"                                                                                                                                                                                  |
| members_count | Number | 否  | 核心成员数量。                                                                                                                                                                                              |        12         |
|    website    |  URL   | 否  | 组织的官方网站或主页地址。                                                                                                                                                                                        |    https://...    |
|    github     |  URL   | 否  | 组织的 GitHub 仓库地址。                                                                                                                                                                                     |    https://...    |
|    status     | String | 否  | 验证状态，如 Verified 或 Active。                                                                                                                                                                            |
|     theme     | Object | 否  | 组织的主题配置对象，包含以下子字段：<br> - logo: 图标名称（如 lucide:shrub）<br> - primaryColor: 主题主色（如 #7c3aed）<br> - bgImage: 背景图片路径（如 /orgs/test.jpg）<br> - sidebarOpacity: 侧边栏背景透明度（0-1）<br> - mainOpacity: 主内容背景透明度（0-1） |     see above     |
### 4. 项目文章 (projects)

存放在 projects/ 目录下。用于展示各个组织当前项目：
```text
---
title: "跨世界同好会官网重构"
description: "使用 Nuxt 4 和 Cloudflare D1 进行全站底层重构，提升访问速度与交互体验。"
status: "ongoing"
date: "2026-03-25"
icon: "lucide:layers"
link: "https://github.com/..."
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
