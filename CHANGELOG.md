# 更新日志

本文件记录 TradeNotes 项目的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/)，
版本号遵循[语义化版本](https://semver.org/lang/zh-CN/)。

## [1.1.2](https://github.com/xhqing/TradeNotes/compare/v1.1.1...v1.1.2) - 2026-05-28

### 变更

- 移除交易笔记文档（01~18）的 H1 标题行
- 移除用户使用说明文档（21~25）的 H1 标题行
- 更新版本号压缩包文件名改为 tradenotes-v1.1.2.zip

## [1.1.1](https://github.com/xhqing/TradeNotes/compare/v1.1.0...v1.1.1) - 2026-05-28

### 变更

- 更新 Notion 用户使用说明，压缩包文件名改为 tradenotes-v1.1.1.zip

## [1.1.0](https://github.com/xhqing/TradeNotes/compare/v1.0.0...v1.1.0) - 2026-05-28

### 新增

- 免责声明文档（19\_免责声明.md）
- 版权与许可证文档（20\_版权与许可证.md）
- 飞书用户使用说明（21\_飞书用户使用说明.md）
- Lark 用户使用说明（22\_Lark用户使用说明.md）
- Typora 用户使用说明（23\_Typora用户使用说明.md）
- Obsidian 用户使用说明（24\_Obsidian用户使用说明.md）
- Notion 用户使用说明（25\_Notion用户使用说明.md）

### 变更

- 重构项目结构，文档目录统一为 tradenotes/
- 更新版权与许可证，统一为 CC BY-NC-SA 4.0 许可
- 增加项目维护者商业授权及再授权条款
- LICENSE 文件重命名为标准命名

### 修复

- 更新 .gitignore，允许提交 Obsidian 配置文件
- 修复 Obsidian 主题配置问题

## [1.0.0](https://github.com/xhqing/TradeNotes/releases/tag/v1.0.0) - 2026-05-24

### 新增

- 初始发布版本
- 18 篇交易学习笔记文档，涵盖金融市场基础、衍生品、期权策略、波动率交易、港股轮证、期货、量化交易、AI Agent、凯利公式、交易心理与系统构建等主题
- 配套 Python 代码脚本，包含 NumPy/Pandas/Matplotlib 基础、数据获取与清洗、回测引擎、绩效指标、配对交易、HMM 市场状态识别、LLM 财务分析、RAG 知识库、策略自动生成、凯利公式系列等模块
- Obsidian 双向链接与深色主题配置
- 中英文 README
- 贡献指南（CONTRIBUTING.md / CONTRIBUTING\_cn.md）

