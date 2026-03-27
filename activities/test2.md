---
title: 同好会官网联协映像测试运行
date: 2026-03-30
description: 今天我们成功部署了日历和时间轴组件。
tags: ['开发日志', 'Nuxt']
author: Tano
type: anniversary
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