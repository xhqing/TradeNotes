# Copyright (c) 2026 TradeNotes Authors
# Licensed under CC BY-NC-SA 4.0: https://creativecommons.org/licenses/by-nc-sa/4.0/

import numpy as np

returns = np.array([0.02, -0.01, 0.03, -0.02, 0.01])
sharpe = returns.mean() / returns.std() * np.sqrt(252)
print(f"年化夏普比率: {sharpe:.4f}")
