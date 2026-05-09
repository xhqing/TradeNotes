import pandas as pd
import numpy as np
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

os.makedirs('tmp', exist_ok=True)

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
plt.savefig('tmp/stock_ma20.png', dpi=100)
print("Chart saved to tmp/stock_ma20.png")
