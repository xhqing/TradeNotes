# Copyright (c) 2026 TradeNotes Authors
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


def kelly_classic(p, b):
    q = 1 - p
    f = (b * p - q) / b
    return max(f, 0)


def fixed_fraction_position(equity, risk_pct, stop_distance_pct):
    return (equity * risk_pct) / stop_distance_pct


def risk_parity_weight(volatilities):
    inv_vol = 1.0 / np.array(volatilities)
    return inv_vol / inv_vol.sum()


if __name__ == '__main__':
    print("=" * 60)
    print("案例一：卖出SPY OTM Put的仓位计算")
    print("=" * 60)
    spy_price = 450
    strike = 440
    delta = -0.15
    premium = 1.50

    p_put = 1 - abs(delta)
    typical_loss = 300
    b_put = (premium * 100) / typical_loss
    f_put = kelly_classic(p_put, b_put)
    print(f"SPY价格: {spy_price}, 行权价: {strike}, Delta: {delta}")
    print(f"胜率 p ≈ {p_put:.2%}")
    print(f"典型亏损: ${typical_loss}, 权利金收入: ${premium*100:.0f}")
    print(f"赔率 b = {b_put:.3f}")
    print(f"凯利比例: {f_put:.2%}")
    print(f"半凯利: {f_put*0.5:.2%}")
    print(f"建议: 考虑尾部风险，单标的不超过净值10-15%")

    print("\n" + "=" * 60)
    print("案例二：轮子策略头寸加码")
    print("=" * 60)
    wheel_p = 0.70
    wheel_avg_win = 200
    wheel_avg_loss = 500
    wheel_b = wheel_avg_win / wheel_avg_loss
    wheel_f = kelly_classic(wheel_p, wheel_b)
    print(f"轮子策略胜率: {wheel_p:.0%}")
    print(f"平均赢: ${wheel_avg_win}, 平均亏: ${wheel_avg_loss}")
    print(f"盈亏比: {wheel_b:.2f}")
    print(f"经典凯利: {wheel_f:.2%}")
    print(f"注意: 卖方策略盈亏比<1, 经典凯利可能为负")
    print(f"建议: 用连续凯利+尾部修正, 单标的仓位10-15%")

    print("\n" + "=" * 60)
    print("案例三：牛熊证高杠杆凯利")
    print("=" * 60)
    p_cbbc = 0.70
    gain_cbbc = 0.05
    loss_cbbc = 0.90
    b_cbbc = gain_cbbc / loss_cbbc
    f_cbbc = kelly_classic(p_cbbc, b_cbbc)
    print(f"胜率: {p_cbbc:.0%}, 收益: {gain_cbbc:.0%}, 亏损: {loss_cbbc:.0%}")
    print(f"赔率: {b_cbbc:.3f}")
    print(f"凯利: {f_cbbc:.2f}")
    print("凯利为负值! 高杠杆牛熊证期望收益为负，凯利公式揭示风险")

    print("\n" + "=" * 60)
    print("案例四：多品种组合多元凯利")
    print("=" * 60)
    mu = np.array([0.12, 0.08, 0.15])
    sigma = np.array([
        [0.04, 0.01, 0.02],
        [0.01, 0.03, 0.005],
        [0.02, 0.005, 0.06]
    ])
    f = np.linalg.solve(sigma, mu)
    labels = ['股票', '债券', '期权策略']
    print("凯利配置:")
    for i, label in enumerate(labels):
        print(f"  {label}: {f[i]:.1%}")
    print("\n半凯利配置:")
    for i, label in enumerate(labels):
        print(f"  {label}: {f[i]*0.5:.1%}")

    print("\n" + "=" * 60)
    print("案例五：理论到实盘的修正")
    print("=" * 60)
    f_theory = kelly_classic(0.6, 1.0)
    discounts = {
        '参数不确定性': 0.75,
        '厚尾修正': 0.85,
        '流动性约束': 0.90,
        '心理承受力': 0.50,
        '相关性不确定性': 0.85,
    }
    f_practical = f_theory
    print(f"理论凯利: {f_theory:.2%}")
    for name, discount in discounts.items():
        f_practical *= discount
        print(f"  × {name}({discount}) → {f_practical:.2%}")
    print(f"\n最终实盘仓位: {f_practical:.2%}")
    print(f"修正系数: {f_practical/f_theory:.2f} (约{f_practical/f_theory*100:.0f}%)")
