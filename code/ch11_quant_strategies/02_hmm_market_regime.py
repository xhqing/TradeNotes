# Copyright (c) 2025 TradeNote Authors
# Licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0).
# See LICENSE.txt for the full license text.

import numpy as np
import pandas as pd

try:
    from hmmlearn.hmm import GaussianHMM
    HAS_HMM = True
except ImportError:
    HAS_HMM = False
    print("hmmlearn未安装，请运行: pip install hmmlearn")

if __name__ == '__main__' and HAS_HMM:
    np.random.seed(42)

    bull = np.random.normal(0.0015, 0.010, 300)
    bear = np.random.normal(-0.0010, 0.025, 200)
    flat = np.random.normal(0.0002, 0.006, 300)

    all_returns = np.concatenate([bull, bear, flat])
    np.random.shuffle(all_returns)

    dates = pd.date_range('2020-01-01', periods=len(all_returns))
    returns = pd.Series(all_returns, index=dates)

    model = GaussianHMM(
        n_components=3,
        covariance_type='full',
        n_iter=500,
        tol=1e-6,
        random_state=42,
        params='stmc',
        init_params='stmc'
    )
    model.fit(returns.values.reshape(-1, 1))
    hidden_states = model.predict(returns.values.reshape(-1, 1))

    means = model.means_.flatten()
    idx = np.argsort(means)[::-1]
    labels = ['牛市', '震荡', '熊市']

    print("各状态参数:")
    for rank, i in enumerate(idx):
        std = np.sqrt(model.covars_[i][0][0])
        print(f"  {labels[rank]}: 均值={model.means_[i][0]:.6f}, 标准差={std:.6f}")

    state_counts = pd.Series(hidden_states).value_counts().sort_index()
    print(f"\n状态分布:\n{state_counts}")

    result = pd.DataFrame({'returns': returns.values, 'state': hidden_states}, index=dates)
    print(f"\n最近5天状态:")
    for date, row in result.tail().iterrows():
        mapped = {idx[0]: '牛市', idx[1]: '震荡', idx[2]: '熊市'}
        state_label = mapped.get(row['state'], '未知')
        print(f"  {date.date()}: 收益={row['returns']:.4f}, 状态={state_label}")
