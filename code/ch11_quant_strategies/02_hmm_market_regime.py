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
    dates = pd.date_range('2020-01-01', periods=1000)
    returns = pd.Series(np.random.randn(1000) * 0.01, index=dates)

    model = GaussianHMM(n_components=3, covariance_type='full', n_iter=100)
    model.fit(returns.values.reshape(-1, 1))
    hidden_states = model.predict(returns.values.reshape(-1, 1))

    print("各状态均值:")
    for i in range(model.n_components):
        print(f"  状态{i}: 均值={model.means_[i][0]:.6f}, 方差={model.covars_[i][0][0]:.6f}")

    state_counts = pd.Series(hidden_states).value_counts().sort_index()
    print(f"\n状态分布:\n{state_counts}")

    result = pd.DataFrame({'returns': returns, 'state': hidden_states}, index=dates)
    print(f"\n最近5天状态:\n{result.tail()}")
