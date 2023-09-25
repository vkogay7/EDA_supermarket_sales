# EDA_supermarket_sales
This is follow-along project by Coursera in order to familiarize with pandas, matplotlib, seaborn

<h3>Exploring headers</h3>
<code>print(df.head(0))</code><br>
Will provide us with the top row of our dataset<br>
<code>Columns: [Invoice ID, Branch, City, Customer type, Gender, Product line, Unit price, Quantity, Tax 5%, Total, Date, Time, Payment, cogs, gross margin percentage, gross income, Rating]
</code><br>
<h2>Columns format: </h2>
<code>print(df.dtypes)</code>
<textbox>
Invoice ID                  object
Branch                      object
City                        object
Customer type               object
Gender                      object
Product line                object
Unit price                 float64
Quantity                     int64
Tax 5%                     float64
Total                      float64
Date                        object
Time                        object
Payment                     object
cogs                       float64
gross margin percentage    float64
gross income               float64
Rating                     float64
  </textbox>
<h3>Drawing distribution plot using matplotlib</h3>
<h2>On example of 'Rating' column we can see uniform distribution, meaning none of particular nubmer spikes out. Mean, 25th and 75th Percentiles are on the plot as well</h2>
<code>sns.distplot(df['Rating'])
plt.axvline(x=np.mean(df['Rating']), c='red', ls='--', label='Mean')
plt.axvline(x=np.percentile(df['Rating'], 25), c='green', ls='--', label='25th-75th Percentile')
plt.axvline(x=np.percentile(df['Rating'], 75), c='green', ls='--')
plt.legend()
plt.show()</code><br>

![image](https://github.com/vkogay7/EDA_supermarket_sales/assets/73743006/78b07794-e6d6-4536-9ecf-334ab4e36e46)

<h3>Drawing histograms</h3>
<code>df.hist(figsize=(10, 10))
plt.show()</code><br>
<h2>We can get more information, track some tendencies based on output</h2>
![image](https://github.com/vkogay7/EDA_supermarket_sales/assets/73743006/3fd62453-31bf-4826-b05f-b1015d333e2b)

<h3>Drawing countplot</h3>
<h2>On this countplot we can see amount of customers per branch</h2>
<code>sns.countplot(data=df, x='Branch')
plt.xlabel('Branch')
plt.ylabel('Count')
plt.title('Count of Customers per Branch')

plt.show()</code><br>
![image](https://github.com/vkogay7/EDA_supermarket_sales/assets/73743006/32716b1f-b279-4aae-86b2-e7b6c4837349)
<h3>Regression plot</h3>
<h2>In order to track relation between to columns, in our case Rating and gross income:</h2>
<code>sns.regplot(data=df, x='Rating',y='gross income',color='darkblue')
plt.title('Relation between Rating and gross income')
plt.show()</code>
<h2>We can see that relation is pretty neutral</h2>
![image](https://github.com/vkogay7/EDA_supermarket_sales/assets/73743006/ea1a959a-5ede-440d-a834-1d69e6926f4d)
<h3>Boxplots</h3>
<code>sns.boxplot(data=df, x='Branch',y='gross income')
plt.show()</code>
<h2>All the branches are pretty equal with slight differences in median, 25th quartile, 75th quartile as well as maximum amount is bigger in branch C</h2>
![image](https://github.com/vkogay7/EDA_supermarket_sales/assets/73743006/627add97-e03d-4cf2-910c-3726548a5ebe)
<h3>Pairplots</h3>
<h2>Huge amount of useful information, where we can track all kinds of relations</h2>
<code>sns.pairplot(data=df)
plt.show()</code>
![image](https://github.com/vkogay7/EDA_supermarket_sales/assets/73743006/d0efb63f-38ab-4076-a9c2-a5a57009dc8a)



