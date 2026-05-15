# Copyright (c) 2026 TradeNote Authors
# Licensed under the MIT License. See LICENSE file for details.

import numpy as np

returns = np.array([0.02, -0.01, 0.03, -0.02, 0.01])
sharpe = returns.mean() / returns.std() * np.sqrt(252)
print(f"年化夏普比率: {sharpe:.4f}")
