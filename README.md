# TradeNotes

> 📝 Personal Trading & Quant Notes | 个人投资交易学习笔记

***

## About This Project

**TradeNotes** is a personal collection of trading and investment notes, with a focus on in-depth strategy analysis of derivatives (US stock options, Hong Kong warrants/CBBCs, etc.), the mathematical principles and practical applications of the Kelly Criterion, while also covering Python quantitative trading and AI Agent trading assistance. These notes cover 16 topics, approximately 135 pages in total.

This project is intended for the following users:

- 🎯 Beginners who want to systematically learn trading and investment knowledge
- 📈 Traders who want to deeply understand derivatives
- 🐍 Developers who want to implement quantitative trading strategies using Python
- 🤖 Technologists interested in AI Agent applications in financial trading

***

## Content Structure

| Topic | Overview |
| :--- | :--- |
| Financial Markets & Trading Basics | Global market overview, macro/fundamental/technical analysis, A-share/HK/US market comparison |
| **Derivatives Markets** ⭐ | Options theory & pricing, buyer/seller strategies, advanced combination strategies, volatility trading, HK warrants/CBBCs |
| Python Quantitative Trading | Python basics, data acquisition, backtesting systems, stock selection & timing, derivatives quant, live trading |
| AI Agent Applications | AI trading overview, AI stock selection & timing, AI execution & risk management, strategy evolution, building a personal trading assistant |
| Trading Psychology & Kelly Criterion ⭐ | **In-depth analysis of the Kelly Criterion**, trading psychology, capital management, trading system construction |

### Highlights

- 🔥 **Derivatives markets are the core**: 8 topics, ~60 pages, accounting for 44% of the content
- 🎯 **Kelly Criterion as a dedicated topic**: ~12 pages of systematic analysis, from mathematical derivation to derivatives practice and Python implementation
- 💻 **Theory meets practice**: Each section includes Python code examples and real-world case studies
- 🌏 **Cross-market perspective**: Covers A-share, Hong Kong, and US markets simultaneously

***

## File Structure

```
TradeNotes/
├── .gitignore # Git ignore rules
├── README.md # Project documentation
├── tradenotes/                   # Notes split by topic
│   ├── 01_金融市场与交易基础.md
│   ├── 02_衍生品基础概念.md
│   ├── ...
│   ├── 18_凯利公式速查与Python量化库速查.md
│   ├── 免责声明.md
│   └── 版权与许可证.md
└── code/                         # Standalone Python scripts
    ├── requirements.txt              Dependency list
    ├── 10_quant_basics/              Quantitative Trading Basics & Backtesting
    │   ├── 01_numpy_basics.py            NumPy Sharpe ratio calculation
    │   ├── 02_pandas_basics.py           Pandas data processing & moving averages
    │   ├── 03_matplotlib_basics.py       Matplotlib visualization
    │   ├── 04_data_fetch.py              AKShare/yfinance data acquisition
    │   ├── 05_data_clean_store.py        Data cleaning & storage
    │   ├── 06_simple_backtest.py         Simple backtesting engine
    │   └── 07_performance_metrics.py     Performance evaluation metrics
    ├── 11_quant_strategies/            Quantitative Strategy Practice
    │   ├── 01_pairs_trading.py           Pairs trading (cointegration test)
    │   └── 02_hmm_market_regime.py       HMM market regime detection
    ├── 12_ai_agent/                    AI Agent Trading Applications
    │   └── 01_llm_financial_analysis.py  LLM financial analysis prompt
    ├── 13_ai_assistant/                Building a Personal AI Trading Assistant
    │   ├── 01_rag_knowledge_base.py      RAG knowledge base construction
    │   └── 02_strategy_generation.py     Automated strategy generation
    └── 14_kelly_criterion/             In-depth Analysis of the Kelly Criterion ⭐
        ├── 01_kelly_classic.py           Classic/continuous/fractional Kelly
        ├── 02_kelly_multi_asset.py       Multi-asset Kelly (with constrained optimization)
        ├── 03_kelly_monte_carlo.py       Monte Carlo simulation comparison
        ├── 04_kelly_bayesian.py          Bayesian dynamic Kelly
        ├── 05_kelly_derivatives.py       Derivatives Kelly (tail risk/fat-tailed/robust correction)
        └── 06_kelly_case_studies.py      5 real-world case studies
```

***

## ⚠️ Disclaimer

**All content in this repository is for educational and reference purposes only and does not constitute any form of investment advice or recommendation.**

- Financial markets carry risks; past performance does not guarantee future returns
- Any trading strategy may result in partial or total loss of principal
- Users should fully understand the relevant risks and make independent judgments based on their own financial situation and risk tolerance before engaging in actual trading
- The authors and contributors shall not be held liable for any direct or indirect losses arising from the use of the content in this repository

**Investing involves risks; enter the market with caution.**

***

## 📄 Copyright & License

Copyright (c) 2026 TradeNotes Authors

This project is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/) (CC BY-NC-SA 4.0). See [LICENSE-CC-BY-NC-SA](./LICENSE-CC-BY-NC-SA) for the full license text.

**You are free to:**

- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material

**Under the following terms:**

- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made
- **NonCommercial** — You may not use the material for commercial purposes
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original
