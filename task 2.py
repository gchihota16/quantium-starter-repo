import pandas
df0 = pandas.read_csv('data/daily_sales_data_0.csv')
df0['product'] = df0['product'].str.strip().str.lower()

df0= df0[df0['product'] == 'pink morsel']

df0['price'] = df0['price'].str.replace('$','',regex=False).astype(float)

df0['sales'] = df0['quantity'] * df0['price']

df0 = df0[['sales', 'date', 'region']]
print(df0)



df1 = pandas.read_csv('data/daily_sales_data_1.csv')
df1['product'] = df1['product'].str.strip().str.lower()

df1= df1[df1['product'] == 'pink morsel']

df1['price'] = df1['price'].str.replace('$','',regex=False).astype(float)

df1['sales'] = df1['quantity'] * df1['price']

df1 = df1[['sales', 'date', 'region']]
print(df1)



df2 = pandas.read_csv('data/daily_sales_data_2.csv')
df2['product'] = df2['product'].str.strip().str.lower()

df2= df2[df2['product'] == 'pink morsel']

df2['price'] = df2['price'].str.replace('$','',regex=False).astype(float)

df2['sales'] = df2['quantity'] * df2['price']

df2 = df2[['sales', 'date', 'region']]
print(df2)

final_df = pandas.concat([df0, df1, df2], ignore_index=True)

final_df.to_csv('Formattedoutput.csv', index=False)
