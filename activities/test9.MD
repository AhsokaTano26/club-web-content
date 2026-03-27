---
title: 图片样式测试合集
date: 2026-04-10
description: 测试 Tailwind + MDC 在图片上的表现
tags: ['Image', 'UI']
author: Tano
---

# 基础图片

![基础](/orgs/test.jpg)

---

# 圆角 + 阴影

![圆角阴影](/orgs/test.jpg){.rounded-xl .shadow-2xl}

---

# 居中 + 限宽

![居中](/orgs/test.jpg){.block .mx-auto .max-w-2xl .rounded-xl}

---

# 玻璃卡片风

![玻璃](/orgs/test.jpg){.p-2 .bg-white/20 .backdrop-blur-md .rounded-xl .shadow-xl}

---

# 悬浮动画（🔥重点）

![hover](/orgs/test.jpg){.rounded-xl .shadow-xl .transition-all .duration-500 hover:scale-[1.03] hover:shadow-2xl}

---

# 多图排列

![1](/orgs/test.jpg){.w-1/3 .inline-block}
![2](/orgs/test.jpg){.w-1/3 .inline-block}
![3](/orgs/test.jpg){.w-1/3 .inline-block}

---

# 超大图（测试溢出）

![超大](/orgs/test.jpg){.w-[1800px]}

---

# 头像样式

![头像](/orgs/test.jpg){.w-32 .h-32 .rounded-full .mx-auto}