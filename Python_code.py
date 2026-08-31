
import pandas as pd
data={
    'Year': ['2008/09', '2012/13','2016/17', '2020/21', '2024/25'],
    'Individuals': [195146, 275822, 424545, 487011, 729811],
    'Companies': [165539, 159259, 204432, 202123, 318739],
    'VAT': [154343, 215023, 289167, 331197, 457789],
    'Total_Revenue': [625100, 813826, 1144081, 1249711, 1855270]
}
df = pd.DataFrame(data)
print(df)

import matplotlib.pyplot as plt
df.to_csv('sars_table_15_clean.csv', index= False)
plt.figure()
plt.plot(df['Year'], df['Total_Revenue'], marker='o')
plt.title('SARS Total Tax Revenue Growth 2008-2024')
plt.ylabel('R million')
plt.xticks(rotation=45)
plt.show()

df.plot(x='Year', y=['Individuals', 'Companies', 'VAT'], kind='bar')
plt.title('Main Sources of Tax Revenue')
plt.ylabel('R million')
plt.show()

growth=((1855270-1249711)/1249711*100)
print(f"Total revenue grew {growth:.1f}% from 2020/21 (COVID) to 2024/25")
