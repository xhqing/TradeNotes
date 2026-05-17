# TradeNote

> A Comprehensive Handbook on Trading & Quantitative Finance | 投资交易知识与量化实践手册

---

## About This Project

**TradeNote** is a concise handbook on trading and investment knowledge, with a focus on in-depth strategy analysis of derivatives (US stock options, Hong Kong warrants/CBBCs, futures, etc.), the mathematical principles and practical applications of the Kelly Criterion, while also covering Python quantitative trading and AI Agent trading assistance. These notes are divided into five volumes with 16 chapters, approximately 135 pages in total.

This project is intended for the following users:

- 🎯 Beginners who want to systematically learn trading and investment knowledge
- 📈 Traders who want to deeply understand derivatives (options, warrants/CBBCs, futures)
- 🐍 Developers who want to implement quantitative trading strategies using Python
- 🤖 Technologists interested in AI Agent applications in financial trading

---

## Content Structure

| Volume | Name | Chapters | Pages | Overview |
|:---:|:---|:---:|:---:|:---|
| I | Trading & Investment Fundamentals | Chapter 1 | ~10 pp | Global market overview, macro/fundamental/technical analysis, A-share/HK/US market comparison |
| II | **Derivatives Markets** ⭐ | Chapters 2–9 | ~60 pp | Options theory & pricing, buyer/seller strategies, advanced combination strategies, volatility trading, HK warrants/CBBCs, futures |
| III | Python Quantitative Trading | Chapters 10–11 | ~18 pp | Python basics, data acquisition, backtesting systems, stock selection & timing, derivatives quant, live trading |
| IV | AI Agent Applications | Chapters 12–13 | ~18 pp | AI trading overview, AI stock selection & timing, AI execution & risk management, strategy evolution, building a personal trading assistant |
| V | Trading Psychology & Kelly Criterion ⭐ | Chapters 14–16 | ~26 pp | **In-depth analysis of the Kelly Criterion**, trading psychology, capital management, trading system construction |

> 📋 For the complete outline, see [TradeNote_Outline.md](./TradeNote_Outline.md)

### Highlights

- 🔥 **Derivatives markets are the core**: 8 chapters, ~60 pages, accounting for 44% of the content
- 🎯 **Kelly Criterion as a standalone chapter**: ~12 pages of systematic analysis, from mathematical derivation to derivatives practice and Python implementation
- 💻 **Theory meets practice**: Each section includes Python code examples and real-world case studies
- 🌏 **Cross-market perspective**: Covers A-share, Hong Kong, and US markets simultaneously

---

## Project Status

📝 **First draft complete** — All 16 chapters have been written, and all 18 Python scripts have been tested and verified.

---

## File Structure

```
TradeNote/
├── .gitignore                    # Git ignore rules (excludes tmp/ and other generated directories)
├── README.md                     # Project documentation
├── TradeNote.md                  # Full notes text (all 16 chapters + appendices)
├── TradeNote_Outline.md          # Complete content outline and table of contents
└── code/                         # Standalone Python scripts
    ├── requirements.txt              Dependency list
    ├── ch10_quant_basics/            Chapter 10: Quantitative Trading Basics & Backtesting
    │   ├── 01_numpy_basics.py            NumPy Sharpe ratio calculation
    │   ├── 02_pandas_basics.py           Pandas data processing & moving averages
    │   ├── 03_matplotlib_basics.py       Matplotlib visualization
    │   ├── 04_data_fetch.py              AKShare/yfinance data acquisition
    │   ├── 05_data_clean_store.py        Data cleaning & storage
    │   ├── 06_simple_backtest.py         Simple backtesting engine
    │   └── 07_performance_metrics.py     Performance evaluation metrics
    ├── ch11_quant_strategies/        Chapter 11: Quantitative Strategy Practice
    │   ├── 01_pairs_trading.py           Pairs trading (cointegration test)
    │   └── 02_hmm_market_regime.py       HMM market regime detection
    ├── ch12_ai_agent/                Chapter 12: AI Agent Trading Applications
    │   └── 01_llm_financial_analysis.py  LLM financial analysis prompt
    ├── ch13_ai_assistant/            Chapter 13: Building a Personal AI Trading Assistant
    │   ├── 01_rag_knowledge_base.py      RAG knowledge base construction
    │   └── 02_strategy_generation.py     Automated strategy generation
    └── ch14_kelly_criterion/         Chapter 14: In-depth Analysis of the Kelly Criterion ⭐
        ├── 01_kelly_classic.py           Classic/continuous/fractional Kelly
        ├── 02_kelly_multi_asset.py       Multi-asset Kelly (with constrained optimization)
        ├── 03_kelly_monte_carlo.py       Monte Carlo simulation comparison
        ├── 04_kelly_bayesian.py          Bayesian dynamic Kelly
        ├── 05_kelly_derivatives.py       Derivatives Kelly (tail risk/fat-tailed/robust correction)
        └── 06_kelly_case_studies.py      5 real-world case studies
```

---

## Contributing

Contributions are welcome in the following ways:

- 🔍 Report omissions or errors in the outline by submitting an Issue or Pull Request
- 💡 Share your unique insights on a particular chapter — your experience and case studies are welcome
- 🐛 Report bugs in code examples

### Contribution Process

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/amazing-idea`)
3. Commit your changes (`git commit -m 'Added content for a chapter'`)
4. Push to the branch (`git push origin feature/amazing-idea`)
5. Create a Pull Request

---

## License

This project is licensed under the [MIT License](./LICENSE).

Copyright © 2026 TradeNote Authors.

---

## ⚠️ Disclaimer

**All content in this repository is for educational and reference purposes only and does not constitute any form of investment advice or recommendation.**

- Financial markets carry risks; past performance does not guarantee future returns
- Any trading strategy may result in partial or total loss of principal
- Users should fully understand the relevant risks and make independent judgments based on their own financial situation and risk tolerance before engaging in actual trading
- The authors and contributors shall not be held liable for any direct or indirect losses arising from the use of the content in this repository

**Investing involves risks; enter the market with caution.**
