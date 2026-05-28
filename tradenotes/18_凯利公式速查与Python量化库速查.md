

> **关联笔记**：[[14_凯利公式深度解析]] | [[10_量化交易基础与回测]] | [[11_量化策略实战]] | [[15_交易心理与资金管理]]

## 💎 凯利公式速查表

| 场景      | 公式                        | 说明                 |
| :------ | :------------------------ | :----------------- |
| 经典二元赌局  | f\* = (bp-q)/b            | p=胜率, b=净赔率, q=1-p |
| 连续正态分布  | f\* = μ/σ²                | μ=期望超额收益, σ²=方差    |
| 多元凯利    | f\* = Σ⁻¹μ                | Σ=协方差矩阵, μ=期望收益向量  |
| 半凯利     | f = f\*/2                 | 折中方案，降低波动          |
| 稳健凯利    | f = (μ-c·SE)/σ²           | c=保守系数             |
| 贝叶斯动态凯利 | p = α/(α+β), f = (bp-q)/b | α,β随交易更新           |

## 🐍 Python量化库速查

| 库           | 用途       | 安装                      |
| :---------- | :------- | :---------------------- |
| numpy       | 数值计算     | pip install numpy       |
| pandas      | 数据处理     | pip install pandas      |
| matplotlib  | 可视化      | pip install matplotlib  |
| plotly      | 交互可视化    | pip install plotly      |
| akshare     | A股数据     | pip install akshare     |
| yfinance    | 美股数据     | pip install yfinance    |
| backtrader  | 回测框架     | pip install backtrader  |
| vnpy        | 全功能量化    | pip install vnpy        |
| langchain   | AI Agent | pip install langchain   |
| scipy       | 科学计算     | pip install scipy       |
| statsmodels | 统计建模     | pip install statsmodels |
