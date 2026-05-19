# Copyright (c) 2026 TradeNote Authors
# Licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0).
# See LICENSE.txt for the full license text.

import pandas as pd
import numpy as np


class SimpleBacktest:
    def __init__(self, data, strategy, initial_capital=100000):
        self.data = data
        self.strategy = strategy
        self.capital = initial_capital
        self.position = 0
        self.trades = []

    def run(self):
        for i, row in self.data.iterrows():
            signal = self.strategy(row, self.position)
            if signal == 'BUY' and self.position == 0:
                shares = int(self.capital * 0.95 / row['close'])
                if shares > 0:
                    self.position = shares
                    self.capital -= shares * row['close']
                    self.trades.append(('BUY', i, row['close'], shares))
            elif signal == 'SELL' and self.position > 0:
                self.capital += self.position * row['close']
                self.trades.append(('SELL', i, row['close'], self.position))
                self.position = 0
        final_value = self.capital + self.position * self.data.iloc[-1]['close']
        return final_value


def ma_crossover_strategy(row, position):
    if pd.notna(row.get('MA20')) and pd.notna(row.get('MA60')):
        if row['MA20'] > row['MA60'] and position == 0:
            return 'BUY'
        elif row['MA20'] < row['MA60'] and position > 0:
            return 'SELL'
    return 'HOLD'


if __name__ == '__main__':
    np.random.seed(42)
    dates = pd.date_range('2022-01-01', periods=500)
    prices = 100 + np.cumsum(np.random.randn(500) * 0.8)
    df = pd.DataFrame({'close': prices}, index=dates)
    df['MA20'] = df['close'].rolling(20).mean()
    df['MA60'] = df['close'].rolling(60).mean()

    bt = SimpleBacktest(df, ma_crossover_strategy, initial_capital=100000)
    final = bt.run()
    print(f"初始资金: 100,000")
    print(f"最终价值: {final:,.2f}")
    print(f"收益率: {(final - 100000) / 100000:.2%}")
    print(f"交易次数: {len(bt.trades)}")
