# Copyright (c) 2026 TradeNote Authors
# Licensed under the MIT License. See LICENSE file for details.

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
