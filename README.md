This is a follow-along project by Coursera aimed at familiarizing myself with pandas, matplotlib, and seaborn. It's also an opportunity to showcase my ability to work with pandas and understand the output it provides.<br><br>
<a href='https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales'>Dataset</a>
## Exploring Headers
To view the top row of our dataset:
```python
print(df.head(0))

Columns:
```
['Invoice ID', 'Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Unit price', 'Quantity', 'Tax 5%', 'Total', 'Date', 'Time', 'Payment', 'cogs', 'gross margin percentage', 'gross income', 'Rating']


### Columns Format:
```python
print(df.dtypes)
```

- Invoice ID: object
- Branch: object
- City: object
- Customer type: object
- Gender: object
- Product line: object
- Unit price: float64
- Quantity: int64
- Tax 5%: float64
- Total: float64
- Date: object
- Time: object
- Payment: object
- cogs: float64
- gross margin percentage: float64
- gross income: float64
- Rating: float64

## Drawing Distribution Plot Using Matplotlib
Exploring the 'Rating' column, we can observe a uniform distribution, indicating that no particular number spikes out. Mean, 25th, and 75th percentiles are also included in the plot.
```python
sns.distplot(df['Rating'])
plt.axvline(x=np.mean(df['Rating']), c='red', ls='--', label='Mean')
plt.axvline(x=np.percentile(df['Rating'], 25), c='green', ls='--', label='25th-75th Percentile')
plt.axvline(x=np.percentile(df['Rating'], 75), c='green', ls='--')
plt.legend()
plt.show()
```

![Rating Distribution](https://github.com/vkogay7/EDA_supermarket_sales/assets/73743006/78b07794-e6d6-4536-9ecf-334ab4e36e46)

## Drawing Histograms
To gather more information and track some tendencies based on output:
```python
df.hist(figsize=(10, 10))
plt.show()
```

![Histograms](https://github.com/vkogay7/EDA_supermarket_sales/assets/73743006/3fd62453-31bf-4826-b05f-b1015d333e2b)

## Drawing Countplot
Visualizing the count of customers per branch:
```python
sns.countplot(data=df, x='Branch')
plt.xlabel('Branch')
plt.ylabel('Count')
plt.title('Count of Customers per Branch')
plt.show()
```

![Countplot](https://github.com/vkogay7/EDA_supermarket_sales/assets/73743006/32716b1f-b279-4aae-86b2-e7b6c4837349)

## Regression Plot
To track the relationship between two columns, e.g., Rating and gross income:
```python
sns.regplot(data=df, x='Rating', y='gross income', color='darkblue')
plt.title('Relation between Rating and gross income')
plt.show()
```

We can see that the relationship is relatively neutral.

![Regression Plot](https://github.com/vkogay7/EDA_supermarket_sales/assets/73743006/ea1a959a-5ede-440d-a834-1d69e6926f4d)

## Boxplots
Visualizing boxplots for branches and gross income:
```python
sns.boxplot(data=df, x='Branch', y='gross income')
plt.show()
```

All branches are quite similar, with slight differences in median, 25th quartile, 75th quartile, and a higher maximum in branch C.

![Boxplots](https://github.com/vkogay7/EDA_supermarket_sales/assets/73743006/627add97-e03d-4cf2-910c-3726548a5ebe)

## Pairplots
A comprehensive visualization of various relationships:
```python
sns.pairplot(data=df)
plt.show()
```

![Pairplots](https://github.com/vkogay7/EDA_supermarket_sales/assets/73743006/d0efb63f-38ab-4076-a9c2-a5a57009dc8a)

## Heatmap Correlation Matrix
```python
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True)
plt.title('Correlation Matrix Heatmap')
plt.show()
```

Visible correlations are indicated with the scale bar.

![Correlation Matrix Heatmap](https://github.com/vkogay7/EDA_supermarket_sales/assets/73743006/9c493918-6b49-4b89-b944-00df2a75322e)

Weirdly, it shows values only for the first row, and 'gross margin' has NaN relations to everything, which is why every relation with it is white.
