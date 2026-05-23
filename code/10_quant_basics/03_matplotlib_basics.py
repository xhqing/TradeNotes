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

import pandas as pd
import numpy as np
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'code', 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=200)
prices = 100 + np.cumsum(np.random.randn(200) * 0.5)
df = pd.DataFrame({'close': prices}, index=dates)
df['MA20'] = df['close'].rolling(20).mean()

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df.index, df['close'], label='Close')
ax.plot(df.index, df['MA20'], label='MA20')
ax.set_title('Stock Price with MA20')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend()
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'stock_ma20.png'), dpi=100)
print(f"Chart saved to {os.path.join(OUTPUT_DIR, 'stock_ma20.png')}")
