# Copyright (c) 2025 TradeNote Authors
# Licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0).
# See LICENSE.txt for the full license text.

import numpy as np


def kelly_multi(mu, sigma):
    return np.linalg.solve(sigma, mu)


def kelly_multi_constrained(mu, sigma, max_leverage=1.0):
    from scipy.optimize import minimize
    n = len(mu)
    def neg_growth(f):
        return -(mu @ f - 0.5 * f @ sigma @ f)
    constraints = [{'type': 'ineq', 'fun': lambda f: max_leverage - np.sum(f)}]
    bounds = [(0, None)] * n
    result = minimize(neg_growth, np.ones(n) / n, bounds=bounds, constraints=constraints)
    return result.x


if __name__ == '__main__':
    print("=== 两资产多元凯利 ===")
    mu = np.array([0.10, 0.08])
    sigma = np.array([[0.04, 0.01], [0.01, 0.03]])
    f = kelly_multi(mu, sigma)
    print(f"凯利配置: 资产1={f[0]:.2%}, 资产2={f[1]:.2%}")
    print(f"总杠杆: {f.sum():.2%}")

    print("\n=== 约束多元凯利 (最大杠杆100%) ===")
    f_c = kelly_multi_constrained(mu, sigma, max_leverage=1.0)
    print(f"凯利配置: 资产1={f_c[0]:.2%}, 资产2={f_c[1]:.2%}")
    print(f"总杠杆: {f_c.sum():.2%}")

    print("\n=== 三资产多元凯利 ===")
    mu3 = np.array([0.12, 0.08, 0.15])
    sigma3 = np.array([
        [0.04, 0.01, 0.02],
        [0.01, 0.03, 0.005],
        [0.02, 0.005, 0.06]
    ])
    f3 = kelly_multi(mu3, sigma3)
    print(f"凯利配置: 股票={f3[0]:.1%}, 债券={f3[1]:.1%}, 期权策略={f3[2]:.1%}")
    half_f3 = f3 * 0.5
    print(f"半凯利:   股票={half_f3[0]:.1%}, 债券={half_f3[1]:.1%}, 期权策略={half_f3[2]:.1%}")
