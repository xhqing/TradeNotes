# Copyright (c) 2025 TradeNote Authors
# Licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0).
# See LICENSE.txt for the full license text.

import numpy as np

returns = np.array([0.02, -0.01, 0.03, -0.02, 0.01])
sharpe = returns.mean() / returns.std() * np.sqrt(252)
print(f"年化夏普比率: {sharpe:.4f}")
