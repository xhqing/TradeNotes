# Copyright (c) 2026 TradeNote Authors
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

import akshare as ak
import yfinance as yf

print("=== A股数据 (AKShare) ===")
try:
    df_a = ak.stock_zh_a_hist(symbol="000001", period="daily",
                              start_date="20240101", end_date="20241231")
    print(df_a.head())
    print(f"A股数据行数: {len(df_a)}")
except Exception as e:
    print(f"AKShare获取失败: {e}")

print("\n=== 美股数据 (yfinance) ===")
try:
    data = yf.download("SPY", start="2024-01-01", end="2024-12-31", progress=False)
    print(data.head())
    print(f"美股数据行数: {len(data)}")
except Exception as e:
    print(f"yfinance获取失败: {e}")
