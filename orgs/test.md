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

# 🏛️ 样式深度测试报告 (H1)

这是一段普通的文本，用于测试字体和行间距。我们来测试一下 **加粗文本 (Strong)** 是否会自动应用我们设置的 `--theme-primary` 颜色。 

> **引用测试 (Blockquote)**
> 这里是引用区域。根据你的 CSS 配置，左侧的边框颜色应该是动态加载的组织主题色，背景色应该是轻微的透明叠加。

---

## 🎨 交互与组件测试 (H2)

### 1. MDC 组件测试
测试图标渲染（确保已安装 `@nuxt/icon`）：
:icon{name="lucide:shrub" class="w-8 h-8 text-[var(--theme-primary)]"}
:icon{name="lucide:component" class="w-8 h-8 text-gray-400"}

### 2. 原生 HTML 内嵌测试
<div style="padding: 1.5rem; border: 2px dashed var(--theme-primary); border-radius: 8px; margin: 1rem 0; background: color-mix(in srgb, var(--theme-primary), transparent 98%);">
  <h4 style="margin-top: 0; color: var(--theme-primary);">内嵌 HTML 容器</h4>
  <p style="font-size: 0.875rem; margin-bottom: 0;">
    这是一个直接在 Markdown 中编写的 <code>&lt;div&gt;</code>。它应该能正确读取到 <code>app.vue</code> 注入的 CSS 变量。
  </p>
</div>

---

## 📊 数据表现测试 (H2)

### 列表测试
* **核心成员**：测试加粗是否变色
* **建立日期**：测试 `inline code` 样式 `2026-03-26`
* **项目状态**：
    1. 阶段一：初步解密 (Completed)
    2. 阶段二：主题同步 (In Progress)

### 表格测试
| 功能模块 | 状态 | 优先级 |
| :--- | :--- | :--- |
| 主题颜色同步 | ✅ 正常 | 高 |
| 背景图片加载 | ⚠️ 待检查 | 中 |
| 响应式布局 | ✅ 正常 | 高 |

---

## 💻 代码高亮测试 (H3)

```javascript
// 测试代码块渲染
export default defineComponent({
  setup() {
    const theme = useState('themeConfig')
    console.log('Current Primary Color:', theme.value.primaryColor)
    return { theme }
  }
})