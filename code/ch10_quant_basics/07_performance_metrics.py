import numpy as np
import pandas as pd


def evaluate(equity_curve):
    returns = equity_curve.pct_change().dropna()
    annual_return = (1 + returns).prod() ** (252 / len(returns)) - 1
    sharpe = returns.mean() / returns.std() * np.sqrt(252)
    sortino = returns.mean() / returns[returns < 0].std() * np.sqrt(252)
    max_drawdown = (equity_curve / equity_curve.cummax() - 1).min()
    calmar = annual_return / abs(max_drawdown)
    win_rate = (returns > 0).sum() / len(returns)
    profit_loss_ratio = returns[returns > 0].mean() / abs(returns[returns < 0].mean())
    return {
        '年化收益': f'{annual_return:.2%}',
        '夏普比率': f'{sharpe:.2f}',
        '索提诺比率': f'{sortino:.2f}',
        '最大回撤': f'{max_drawdown:.2%}',
        '卡玛比率': f'{calmar:.2f}',
        '胜率': f'{win_rate:.2%}',
        '盈亏比': f'{profit_loss_ratio:.2f}'
    }


if __name__ == '__main__':
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', periods=252)
    daily_returns = np.random.randn(252) * 0.01 + 0.0003
    equity = pd.Series(100000 * np.cumprod(1 + daily_returns), index=dates)

    metrics = evaluate(equity)
    for k, v in metrics.items():
        print(f"{k}: {v}")
