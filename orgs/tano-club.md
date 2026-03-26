---
orgs_id: "1"
title: "Tano 跨世界同好会"
description: "致力于研究跨维度交互技术与幻想乡生态保护的非营利性技术组织。"
founded: "2024-01-01"
joined_at: "2026-03-26"
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

---
title: Nuxt Content 全功能测试
description: 测试图片、组件、代码和标准语法
layout: default
---

# 1. 标准语法测试

这是一段普通的文本，包含 **加粗**、*斜体* 以及 ~~删除线~~。

* 列表项 A
* 列表项 B
  * 子列表

> 这是一个引用块，用于强调某些核心观点。

---

# 2. 图片引入测试

Nuxt Content 处理 `public/` 目录下的静态资源非常简单。

**方式 A：标准 Markdown 语法**
![测试图片](/orgs/test.jpg)

**方式 B：带属性的 MDC 语法**
![测试图片](/orgs/test.jpg){.w-full .rounded-xl .shadow-lg}

---

# 3. 代码高亮测试

```typescript [app.vue]
export default defineComponent({
  setup() {
    const msg = 'Hello Nuxt Content!'
    console.log(msg)
  }
})