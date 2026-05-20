# Copyright (c) 2026 TradeNote Authors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import numpy as np


def estimate_kelly_params(trades):
    trades = np.array(trades)
    wins = trades[trades > 0]
    losses = trades[trades < 0]
    if len(wins) == 0 or len(losses) == 0:
        return None, None, None
    p = len(wins) / len(trades)
    b = wins.mean() / abs(losses.mean())
    f_star = (b * p - (1 - p)) / b
    return p, b, f_star


def kelly_continuous_adjusted(mu, sigma, tail_multiplier=1.0, kurtosis=0.0):
    f_base = mu / (sigma ** 2)
    f_tail = f_base / (1 + tail_multiplier)
    f_kurt = f_tail - (mu * kurtosis) / (2 * sigma ** 4)
    return max(f_kurt, 0)


def kelly_robust(mu, mu_se, sigma):
    c = 1.5
    return max((mu - c * mu_se) / (sigma ** 2), 0)


if __name__ == '__main__':
    print("=== 从历史交易记录估算凯利参数 ===")
    trades = [200, -150, 300, -200, 150, -100, 250, -180, 100, -120,
              180, -90, 220, -160, 140, -110, 280, -170, 160, -130]
    p, b, f_star = estimate_kelly_params(trades)
    print(f"胜率 p = {p:.2%}")
    print(f"盈亏比 b = {b:.2f}")
    print(f"凯利比例 f* = {f_star:.2%}")
    print(f"半凯利 = {f_star * 0.5:.2%}")

    print("\n=== 期权买方凯利 ===")
    p_buy = 0.30
    b_buy = 3.0
    f_buy = (b_buy * p_buy - (1 - p_buy)) / b_buy
    print(f"胜率={p_buy}, 赔率={b_buy} → 凯利={f_buy:.2%}")

    print("\n=== 尾部风险修正 ===")
    mu, sigma = 0.10, 0.20
    f_base = mu / sigma**2
    print(f"基础凯利: {f_base:.2%}")
    for tm in [1.0, 2.0, 3.0, 5.0]:
        f_adj = kelly_continuous_adjusted(mu, sigma, tail_multiplier=tm)
        print(f"尾部修正(x{tm}): {f_adj:.2%}")

    print("\n=== 厚尾修正 ===")
    for kappa in [0, 3, 6, 10]:
        f_k = kelly_continuous_adjusted(mu, sigma, tail_multiplier=1.0, kurtosis=kappa)
        print(f"超额峰度={kappa}: 凯利={f_k:.2%}")

    print("\n=== 稳健凯利 ===")
    mu_se = 0.03
    print(f"μ={mu}, SE={mu_se}, σ={sigma}")
    for c in [0.5, 1.0, 1.5, 2.0]:
        f_r = kelly_robust(mu, mu_se * c, sigma)
        print(f"保守系数c={c}: 凯利={f_r:.2%}")

    print("\n=== 牛熊证凯利 (收回风险折价) ===")
    p_cbbc = 0.70
    b_cbbc = 0.05 / 0.90
    f_cbbc = (b_cbbc * p_cbbc - (1 - p_cbbc)) / b_cbbc
    print(f"胜率={p_cbbc}, 赔率={b_cbbc:.3f} → 凯利={f_cbbc:.2f}")
    print("凯利为负值，说明高杠杆牛熊证期望收益为负，不建议下注!")
