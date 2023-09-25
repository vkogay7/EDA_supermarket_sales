import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import calmap

df = pd.read_csv('supermarket_sales.csv')
#print(df.dtypes)

#sns.distplot(df['Rating'])
'''
plt.axvline(x=np.mean(df['Rating']), c='red', ls='--', label='Mean')
plt.axvline(x=np.percentile(df['Rating'], 25), c='green', ls='--', label='25th-75th Percentile')
plt.axvline(x=np.percentile(df['Rating'], 75), c='green', ls='--')
plt.legend()
plt.show()

#df.hist(figsize=(10, 10))

sns.countplot(data=df, x='Branch')
#plt.xlabel('Branch')
plt.ylabel('Count')
plt.title('Count of Customers per Branch')

sns.regplot(data=df, x='Rating',y='gross income',color='darkblue')
plt.title('Relation between Rating and gross income')

sns.boxplot(data=df, x='Branch',y='gross income')

sns.pairplot(data=df)
plt.show()
'''

#na_proportion = df.isna().sum() / len(df)
# Select only numeric columns for correlation calculation
numeric_df = df.select_dtypes(include=[np.number])

# Calculate the correlation matrix
corr_matrix = numeric_df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True)
plt.title('Correlation Matrix Heatmap')
plt.show()