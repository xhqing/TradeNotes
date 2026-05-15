# TradeNote

> 📖 投资交易知识与量化实践手册 | A Comprehensive Handbook on Trading & Quantitative Finance

---

## 关于本书

**TradeNote** 是一本精炼的投资交易知识手册，重点覆盖衍生品（美股期权、港股轮证、期货等）的深度策略分析、凯利公式的数学原理与实战应用，兼顾 Python 量化交易与 AI Agent 交易辅助。全书分为五卷共 16 章，预计成书约 135 页。

本书面向以下读者群体：

- 🎯 希望系统学习投资交易知识的初学者
- 📈 想要深入理解衍生品（期权、轮证、期货）的交易者
- 🐍 希望通过 Python 实现量化交易策略的开发者
- 🤖 关注 AI Agent 在金融交易领域应用的技术人员

---

## 书籍结构

| 卷 | 名称 | 章节 | 页数 | 内容概要 |
|:---:|:---|:---:|:---:|:---|
| 一 | 投资交易基础速览 | 第 1 章 | ~10 页 | 全市场概览、宏观/财务/技术分析、A股/港股/美股制度对比 |
| 二 | **衍生品市场** ⭐ | 第 2~9 章 | ~60 页 | 期权理论与定价、买方/卖方策略、高级组合策略、波动率交易、港股轮证、期货 |
| 三 | Python 量化交易 | 第 10~11 章 | ~18 页 | Python入门、数据获取、回测系统、选股择时、衍生品量化、实盘交易 |
| 四 | AI Agent 应用 | 第 12~13 章 | ~18 页 | AI交易概览、AI选股择时、AI执行风控、策略进化、个人交易助手构建 |
| 五 | 交易心态与凯利公式 ⭐ | 第 14~16 章 | ~26 页 | **凯利公式深度解析**、交易心理学、资金管理、交易系统构建 |

> 📋 完整大纲详见 [TradeNote_Outline.md](./TradeNote_Outline.md)

### 本书亮点

- 🔥 **衍生品市场是核心**：8 章、约 60 页，占全书 44%
- 🎯 **凯利公式独立成章**：约 12 页系统性拆解，从数学推导到衍生品实战再到 Python 实现
- 💻 **理论与实践结合**：每部分都有 Python 代码示例和实战案例
- 🌏 **跨市场视角**：同时覆盖 A 股、港股、美股三大市场

---

## 项目状态

📝 **初稿完成** —— 全书 16 章正文已撰写完毕，18 个 Python 脚本均已通过运行测试。

---

## 文件说明

```
TradeNote/
├── .gitignore                    # Git 忽略规则（排除 tmp/ 等生成文件目录）
├── README.md                     # 项目说明文档
├── TradeNote.md                  # 全书正文（完整16章 + 附录）
├── TradeNote_Outline.md          # 书籍完整大纲与目录
└── code/                         # 可独立运行的 Python 脚本
    ├── requirements.txt              依赖清单
    ├── ch10_quant_basics/            第10章 量化交易基础与回测
    │   ├── 01_numpy_basics.py            NumPy 计算夏普比率
    │   ├── 02_pandas_basics.py           Pandas 数据处理与均线
    │   ├── 03_matplotlib_basics.py       Matplotlib 可视化
    │   ├── 04_data_fetch.py              AKShare/yfinance 数据获取
    │   ├── 05_data_clean_store.py        数据清洗与存储
    │   ├── 06_simple_backtest.py         简易回测引擎
    │   └── 07_performance_metrics.py     绩效评估指标
    ├── ch11_quant_strategies/        第11章 量化策略实战
    │   ├── 01_pairs_trading.py           配对交易（协整检验）
    │   └── 02_hmm_market_regime.py       HMM 市场状态识别
    ├── ch12_ai_agent/                第12章 AI Agent 交易应用
    │   └── 01_llm_financial_analysis.py  LLM 财务分析 Prompt
    ├── ch13_ai_assistant/            第13章 构建个人 AI 交易助手
    │   ├── 01_rag_knowledge_base.py      RAG 知识库搭建
    │   └── 02_strategy_generation.py     策略自动生成
    └── ch14_kelly_criterion/         第14章 凯利公式深度解析 ⭐
        ├── 01_kelly_classic.py           经典/连续/分数凯利
        ├── 02_kelly_multi_asset.py       多元凯利（含约束优化）
        ├── 03_kelly_monte_carlo.py       蒙特卡洛模拟对比
        ├── 04_kelly_bayesian.py          贝叶斯动态凯利
        ├── 05_kelly_derivatives.py       衍生品凯利（尾部/厚尾/稳健修正）
        └── 06_kelly_case_studies.py      5 个实战案例
```

---

## 贡献指南

欢迎通过以下方式参与贡献：

- 🔍 发现大纲中的遗漏或错误，提交 Issue 或 Pull Request
- 💡 对某一章节有独到见解，欢迎分享你的经验与案例
- 🐛 发现代码示例中的 bug，欢迎指正

### 贡献流程

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-idea`)
3. 提交更改 (`git commit -m '添加了某个章节的内容'`)
4. 推送到分支 (`git push origin feature/amazing-idea`)
5. 创建 Pull Request

---

## 许可证

本项目基于 [MIT 许可证](./LICENSE) 开源。

Copyright © 2026 TradeNote Authors.

---

## ⚠️ 免责声明

**本书及本仓库中的所有内容仅供教育和学习参考，不构成任何形式的投资建议或推荐。**

- 金融市场存在风险，过往表现不代表未来收益
- 任何交易策略都可能导致本金的部分或全部损失
- 读者在进行实际交易前，应充分了解相关风险，并根据自身财务状况和风险承受能力做出独立判断
- 作者及贡献者对因使用本书内容而产生的任何直接或间接损失不承担任何责任

**投资有风险，入市需谨慎。**
