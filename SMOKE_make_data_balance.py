import pandas as pd

df = pd.read_csv('input/100_data.csv')

# print(df.head())

#SMOKE方法生成全部数据

print(df['churn_state_at_the_end_of_month'])


