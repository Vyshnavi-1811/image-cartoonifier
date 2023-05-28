import pandas as pd
import numpy as np

df = pd.read_csv('Data - STOCK_US_XNYS_CSV.csv')

df['Date'] = pd.to_datetime(df['Date'])

monthly_avg = df.groupby(pd.Grouper(key='Date', freq='M'))['Close'].mean()

print(monthly_avg)

