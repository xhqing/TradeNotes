# Copyright (c) 2026 TradeNote Authors
# Licensed under the MIT License. See LICENSE file for details.

import numpy as np


def simulate_wealth(f, p, b, n_rounds=1000, n_paths=1000):
    final_wealth = []
    for _ in range(n_paths):
        wealth = 1.0
        for _ in range(n_rounds):
            if np.random.random() < p:
                wealth *= (1 + f * b)
            else:
                wealth *= (1 - f)
            if wealth <= 0:
                wealth = 0
                break
        final_wealth.append(wealth)
    return np.array(final_wealth)


def simulate_wealth_paths(f, p, b, n_rounds=100, n_paths=5):
    paths = []
    for _ in range(n_paths):
        wealth = 1.0
        path = [wealth]
        for _ in range(n_rounds):
            if np.random.random() < p:
                wealth *= (1 + f * b)
            else:
                wealth *= (1 - f)
            path.append(wealth)
        paths.append(path)
    return paths


if __name__ == '__main__':
    np.random.seed(42)
    p, b = 0.6, 1.0
    f_kelly = (b * p - (1 - p)) / b

    print(f"胜率={p}, 赔率={b}")
    print(f"凯利比例 f* = {f_kelly:.2%}")
    print()

    strategies = [
        ('全凯利', f_kelly),
        ('半凯利', f_kelly * 0.5),
        ('1/4凯利', f_kelly * 0.25),
        ('2倍凯利', f_kelly * 2.0),
    ]

    print(f"{'策略':<10} {'f值':<8} {'中位终值':<15} {'均值终值':<15} {'破产率':<10}")
    print("-" * 60)

    for label, f in strategies:
        results = simulate_wealth(f, p, b, n_rounds=500, n_paths=10000)
        median = np.median(results)
        mean = np.mean(results)
        ruin_rate = np.mean(results == 0)
        print(f"{label:<10} {f:<8.3f} {median:<15.4f} {mean:<15.4f} {ruin_rate:<10.2%}")

    print("\n=== 财富路径示例 (100轮) ===")
    for label, f in strategies[:3]:
        paths = simulate_wealth_paths(f, p, b, n_rounds=100, n_paths=3)
        print(f"\n{label} (f={f:.3f}):")
        for i, path in enumerate(paths):
            print(f"  路径{i+1}: 终值={path[-1]:.4f}")
