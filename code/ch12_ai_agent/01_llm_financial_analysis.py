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

financial_data_prompt = """
分析以下公司财报数据，提取关键指标并评估：
- 营收增速和毛利率变化趋势
- 自由现金流是否为正
- 资产负债率是否在合理范围
- 与同行业对比的竞争优势

财报数据：{financial_data}
"""

print("=== LLM财务报告分析Prompt模板 ===")
print(financial_data_prompt)

print("\n=== 使用示例 ===")
sample_data = """
公司: ABC科技
营收: 100亿 (同比+25%)
毛利率: 45% (同比+3pp)
自由现金流: 15亿
资产负债率: 35%
行业平均毛利率: 38%
"""

filled_prompt = financial_data_prompt.format(financial_data=sample_data)
print(filled_prompt)
