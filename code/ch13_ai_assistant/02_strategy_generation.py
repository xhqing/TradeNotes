# Copyright (c) 2025 TradeNote Authors
# Licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0).
# See LICENSE.txt for the full license text.

strategy_generation_prompt = """
根据以下交易想法，生成完整的Python回测策略代码：
- 策略逻辑：当20日均线金叉60日均线时买入，死叉时卖出
- 加入2%的止损规则
- 使用Backtrader框架
"""

print("=== LLM策略生成Prompt模板 ===")
print(strategy_generation_prompt)

print("\n=== 参考实现 (Backtrader MA交叉策略) ===")

backtrader_code = '''
import backtrader as bt

class MACrossStrategy(bt.Strategy):
    params = (('fast', 20), ('slow', 60), ('stop_loss', 0.02))

    def __init__(self):
        self.fast_ma = bt.ind.SMA(self.data.close, period=self.p.fast)
        self.slow_ma = bt.ind.SMA(self.data.close, period=self.p.slow)
        self.crossover = bt.ind.CrossOver(self.fast_ma, self.slow_ma)
        self.entry_price = None

    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()
                self.entry_price = self.data.close[0]
        else:
            if self.entry_price and self.data.close[0] < self.entry_price * (1 - self.p.stop_loss):
                self.close()
            elif self.crossover < 0:
                self.close()
'''
print(backtrader_code)
