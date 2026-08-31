# sars_revenue_analysis
SARS Tax Revenue Analysis — Table 1.5 (2008/09 – 2024/25)

Tools: Python, pandas, matplotlib  
Source: SARS Tax Statistics 2024, Chapter 1, Table 1.5 Nominal Tax Collections

Objective
Analyze long-term tax revenue trends to understand COVID-19 impact and post-pandemic recovery 

Dataset
Cleaned from official SARS Excel (merged headers). Sample:
- 2008/09: R625bn total (PIT: R195bn, CIT: R165bn, VAT: R154bn)
- 2024/25: R1.855tn total (PIT: R729bn, CIT: R318bn, VAT: R457bn)

Key Insights
1. COVID-19 Dip: Growth slowed to only R1.249tn in 2020/21 (lowest growth in 16 years).
2. Strong Recovery: 48.4% growth from 2020/21 to 2024/25 — total now R1.85tn.
3. Composition Shift:Individuals (PIT) now 39% of revenue (R729bn), dominant source. VAT 25% (R457bn), Companies 17% (R318bn).
4. CIT Volatility: Companies dropped from R165bn (2008) to R159bn (2012) then recovered to R318bn — shows economic cycles.

Charts
- `total_growth.png` — Overall revenue growth 2008-2024
- `composition.png` — PIT vs CIT vs VAT

How to Run python
import pandas as pd
df = pd.read_csv('sars_table_15_clean.csv')
df.plot(x='Year', y=['Individuals','Companies','VAT'], kind='bar')
