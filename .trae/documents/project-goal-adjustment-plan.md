# TradeNote 项目目标调整计划

## 背景

项目目标从"写书/电子书"变更为"个人笔记整理"，避免被判定为"非法出版物"。主要内容不变，但需全面移除与"书"相关的词汇和意象，重新定位为个人交易笔记与见解。

---

## 修改原则

1. **移除所有"书"相关词汇**：本书 → 本笔记，全书 → 全笔记，成书 → 完成，读者 → 使用者，书籍 → 笔记等
2. **移除封面、前言、版权说明、许可证**（仅限 TradeNote.md 中）
3. **免责声明保留但措辞调整**：将"本书"改为"本笔记"
4. **项目定位统一为**：个人投资交易笔记与见解整理，可在社交平台分享/售卖

---

## 一、TradeNote.md 修改

### 1.1 删除封面区域（第1-28行）
- 删除整个封面 div 块，包括标题、副标题、版本号

### 1.2 删除版权声明（第32-41行）
- 删除第一个"版权声明"section 及 MIT License 全文

### 1.3 删除前言（第44-51行）
- 删除"前言"section 整体

### 1.4 目录区域措辞调整（第54-85行）
- 无需改动，目录本身不含"书"相关词汇

### 1.5 正文中"本书"→"本笔记"替换
- 搜索所有"本书"出现的位置，替换为"本笔记"或"本手册"（根据语境选择最合适的）

### 1.6 删除末尾的版权声明（第1772-1780行）
- 删除第二个"版权声明"section

### 1.7 免责声明措辞调整（第1758-1768行）
- "本书所有内容" → "本笔记所有内容"
- 保留免责声明本身（这是风险提示，与出版物无关）

---

## 二、TradeNote_Outline.md 修改

### 2.1 删除前言相关内容
- 删除"前言 （预计 1 页）"section

### 2.2 替换"书"相关词汇
- "本书是投资交易的系统知识手册" → "本笔记是投资交易的系统知识手册"
- "预计成书约 135 页" → "预计约 135 页"
- "全书分五卷共 16 章" → "全笔记分五卷共 16 章"
- "全书合计" → "合计"
- "全书页数估算汇总" → "页数估算汇总"
- "结论：《TradeNote》预计成书约" → "结论：TradeNote 预计约"
- 删除前言行（页数汇总表中的"前言"行）
- 更新页数占比图中的"前言"行

### 2.3 其他"书"相关词汇
- 逐行检查并替换所有"书"相关表述

---

## 三、README.md（英文版）修改

### 3.1 标题与描述
- "About This Book" → "About This Project"
- "book" → "notes" / "handbook"（根据语境）
- "readers" → "users"

### 3.2 具体替换
- "TradeNote is a concise handbook" → 保持（handbook 可以保留）
- "The book is divided into" → "These notes are divided into"
- "approximately 135 pages in total" → 保持
- "This book is intended for the following readers" → "This project is intended for the following users"
- "Book Structure" → "Content Structure"
- "For the complete outline" → 保持
- "Highlights" → 保持
- "accounting for 44% of the book" → "accounting for 44% of the content"
- "All content in this book and repository" → "All content in this repository"

### 3.3 文件结构说明
- "Full book text" → "Full notes text"
- "Complete book outline" → "Complete content outline"

---

## 四、README_cn.md（中文版）修改

### 4.1 标题与描述
- "关于本书" → "关于本项目"
- "本书" → "本笔记"（全文替换）
- "读者" → "使用者"

### 4.2 具体替换
- "本书面向以下读者群体" → "本笔记面向以下使用者群体"
- "书籍结构" → "内容结构"
- "本书亮点" → "亮点"
- "占全书 44%" → "占总内容 44%"
- "全书 16 章正文已撰写完毕" → "全笔记 16 章正文已撰写完毕"
- "全书正文" → "全笔记正文"
- "书籍完整大纲" → "内容完整大纲"
- "本书及本仓库" → "本笔记及本仓库"

### 4.3 文件说明
- "全书正文（完整16章 + 附录）" → "全笔记正文（完整16章 + 附录）"

---

## 五、不修改的文件

- **LICENSE** — MIT License 文件本身不需要修改，它是代码/项目的许可证，与"出版物"概念无关
- **code/ 目录** — Python 代码不涉及"书"相关词汇，无需修改

---

## 修改检查清单

完成所有修改后，需全局搜索以下关键词确认无遗漏：
- "本书"、"全书"、"成书"、"书籍"、"读者"、"本书是"
- "book"、"ebook"、"readers"、"publication"
- "前言"、"版权声明"、"许可证"（仅在 TradeNote.md 中确认已删除）
