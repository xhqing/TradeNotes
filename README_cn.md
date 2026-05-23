# TradeNote

> 📝 个人投资交易学习笔记 | Personal Trading & Quant Notes

***

## 关于本笔记

**TradeNote** 是一份个人投资交易学习笔记，重点记录衍生品（美股期权、港股轮证等）的策略分析、凯利公式的数学原理与实战应用，同时涵盖 Python 量化交易与 AI Agent 交易辅助。笔记共 16 个主题，约 135 页。

本笔记面向以下读者：

- 🎯 希望系统学习投资交易知识的初学者
- 📈 想要深入理解衍生品的交易者
- 🐍 希望通过 Python 实现量化交易策略的开发者
- 🤖 关注 AI Agent 在金融交易领域应用的技术人员

***

## 内容结构

| 主题 | 内容概要 |
| :--- | :--- |
| 金融市场与交易基础 | 全市场概览、宏观/财务/技术分析、A股/港股/美股制度对比 |
| **衍生品市场** ⭐ | 期权理论与定价、买方/卖方策略、高级组合策略、波动率交易、港股轮证 |
| Python 量化交易 | Python入门、数据获取、回测系统、选股择时、衍生品量化、实盘交易 |
| AI Agent 应用 | AI交易概览、AI选股择时、AI执行风控、策略进化、个人交易助手构建 |
| 交易心态与凯利公式 ⭐ | **凯利公式深度解析**、交易心理学、资金管理、交易系统构建 |

### 亮点

- 🔥 **衍生品市场是核心**：8 个主题、约 60 页，占总内容 44%
- 🎯 **凯利公式专题**：约 12 页系统性拆解，从数学推导到衍生品实战再到 Python 实现
- 💻 **理论与实践结合**：每部分都有 Python 代码示例和实战案例
- 🌏 **跨市场视角**：同时覆盖 A 股、港股、美股三大市场

***

## 文件说明

```
TradeNote/
├── .gitignore                    # Git 忽略规则
├── README.md                     # 项目说明
├── docs/                         # 按主题拆分的笔记文档
│   ├── 01_金融市场与交易基础.md
│   ├── 02_衍生品基础概念.md
│   ├── ...
│   ├── 18_凯利公式速查与Python量化库速查.md
│   ├── 免责声明.md
│   └── 版权与许可证.md
└── code/                         # 可独立运行的 Python 脚本
    ├── requirements.txt              依赖清单
    ├── 10_quant_basics/              量化交易基础与回测
    │   ├── 01_numpy_basics.py            NumPy 计算夏普比率
    │   ├── 02_pandas_basics.py           Pandas 数据处理与均线
    │   ├── 03_matplotlib_basics.py       Matplotlib 可视化
    │   ├── 04_data_fetch.py              AKShare/yfinance 数据获取
    │   ├── 05_data_clean_store.py        数据清洗与存储
    │   ├── 06_simple_backtest.py         简易回测引擎
    │   └── 07_performance_metrics.py     绩效评估指标
    ├── 11_quant_strategies/            量化策略实战
    │   ├── 01_pairs_trading.py           配对交易（协整检验）
    │   └── 02_hmm_market_regime.py       HMM 市场状态识别
    ├── 12_ai_agent/                    AI Agent 交易应用
    │   └── 01_llm_financial_analysis.py  LLM 财务分析 Prompt
    ├── 13_ai_assistant/                构建个人 AI 交易助手
    │   ├── 01_rag_knowledge_base.py      RAG 知识库搭建
    │   └── 02_strategy_generation.py     策略自动生成
    └── 14_kelly_criterion/             凯利公式深度解析 ⭐
        ├── 01_kelly_classic.py           经典/连续/分数凯利
        ├── 02_kelly_multi_asset.py       多元凯利（含约束优化）
        ├── 03_kelly_monte_carlo.py       蒙特卡洛模拟对比
        ├── 04_kelly_bayesian.py          贝叶斯动态凯利
        ├── 05_kelly_derivatives.py       衍生品凯利（尾部/厚尾/稳健修正）
        └── 06_kelly_case_studies.py      5 个实战案例
```

***

## ⚠️ 免责声明

**本笔记及本仓库中的所有内容仅供教育和学习参考，不构成任何形式的投资建议或推荐。**

- 金融市场存在风险，过往表现不代表未来收益
- 任何交易策略都可能导致本金的部分或全部损失
- 使用者在进行实际交易前，应充分了解相关风险，并根据自身财务状况和风险承受能力做出独立判断
- 作者及贡献者对因使用本笔记内容而产生的任何直接或间接损失不承担任何责任

**投资有风险，入市需谨慎。**

***

## 📄 版权与许可证

版权所有 (c) 2026 TradeNote 作者

本项目采用双许可证模式：

| 适用范围 | 许可证 | 许可证文件 |
| :--- | :--- | :--- |
| 代码（`code/` 目录下的所有文件） | [GNU Affero 通用公共许可证 v3.0](https://www.gnu.org/licenses/agpl-3.0.html)（AGPL-3.0） | [LICENSE-AGPL](./LICENSE-AGPL) |
| 文档（其他所有内容，包括 `docs/`） | [知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans)（CC BY-NC-SA 4.0） | [LICENSE-CC-BY-NC-SA](./LICENSE-CC-BY-NC-SA) |

### 代码 — AGPL-3.0

- 您可以在 AGPL-3.0 条款下使用、修改和分发代码
- **Copyleft（传染性）**：任何修改版本必须同样以 AGPL-3.0 许可
- **网络交互即分发**：如果您在服务器上运行修改版本并与他人交互，您必须公开源代码

### 文档 — CC BY-NC-SA 4.0

**您可以自由地：**

- **共享** — 在任何媒介以任何形式复制、发行本作品
- **演绎** — 修改、转换或以本作品为基础进行创作

**惟须遵守下列条件：**

- **署名** — 您必须给出适当的署名，提供指向本许可协议的链接，同时标明是否对原始作品作了修改
- **非商业性使用** — 您不得将本作品用于商业目的
- **相同方式共享** — 如果您再混合、转换或者基于本作品进行创作，您必须基于与原先许可协议相同的许可协议分发您贡献的作品
