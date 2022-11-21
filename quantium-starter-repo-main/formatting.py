import pandas as pd 
def get_pink_morse(df_1):
    df_1=df_1[df_1['product'].str.contains('pink morse')]
    price=df_1['price'].str.split('$',n=1,expand=True)
    print(df_1)
    df_1['sales']=price[1].astype(float)*df_1['quantity']
    del df_1['price']
    del df_1['quantity']
    df_1=df_1[['sales','date','region']]
    return df_1

files=[pd.read_csv('data/daily_sales_data_0.csv'),pd.read_csv('data/daily_sales_data_1.csv'),pd.read_csv('data/daily_sales_data_2.csv')]
for i in files:
    dataframe=get_pink_morse(i)
    dataframe.to_csv('result.csv',mode='a',index='False',header="False")