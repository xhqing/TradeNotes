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


class BayesianKelly:
    def __init__(self, prior_alpha=10, prior_beta=10):
        self.alpha = prior_alpha
        self.beta = prior_beta

    def update(self, win):
        if win:
            self.alpha += 1
        else:
            self.beta += 1

    @property
    def win_rate(self):
        return self.alpha / (self.alpha + self.beta)

    def kelly(self, b):
        p = self.win_rate
        f = (b * p - (1 - p)) / b
        return max(f, 0)

    @property
    def confidence(self):
        total = self.alpha + self.beta
        return min(total / 50, 1.0)


class DynamicKelly:
    def __init__(self, prior_alpha=10, prior_beta=10):
        self.alpha = prior_alpha
        self.beta = prior_beta

    def update(self, win):
        self.alpha += int(win)
        self.beta += int(not win)

    def get_f(self, b):
        p = self.alpha / (self.alpha + self.beta)
        return max((b * p - (1 - p)) / b, 0)


if __name__ == '__main__':
    print("=== 贝叶斯动态凯利 ===")
    bk = BayesianKelly(prior_alpha=10, prior_beta=10)
    print(f"初始: 胜率={bk.win_rate:.2f}, 凯利={bk.kelly(1.5):.2%}")

    trades = [1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1]
    for i, result in enumerate(trades):
        bk.update(result)
        print(f"第{i+1}笔: 结果={'赢' if result else '输'}, "
              f"胜率={bk.win_rate:.2f}, 凯利={bk.kelly(1.5):.2%}")

    print("\n=== DynamicKelly (书中版本) ===")
    dk = DynamicKelly()
    for result in [1, 1, 0, 1, 0, 1, 1, 0, 1, 1]:
        dk.update(result)
        print(f"胜率估计: {dk.alpha/(dk.alpha+dk.beta):.2f}, "
              f"凯利: {dk.get_f(1.5):.2%}")

    print("\n=== 不同先验的影响 ===")
    for prior_a, prior_b in [(1, 1), (10, 10), (50, 50)]:
        bk2 = BayesianKelly(prior_alpha=prior_a, prior_beta=prior_b)
        for r in [1, 1, 0, 1, 0, 1, 1, 0, 1, 1]:
            bk2.update(r)
        print(f"先验({prior_a},{prior_b}) → 胜率={bk2.win_rate:.2f}, 凯利={bk2.kelly(1.5):.2%}")
