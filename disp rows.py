import pandas as pd
df = pd.read_csv("sales_data_sample.csv")

print("Print first 10 rows")
print(df.head(1)) # in case no input value it will show 5 by default.

print("Print last 10 rows")
print(df.tail(1))