import pandas as pd

df = pd.read_excel("sampleSuperstore.xlsx")
print(df)
print(f'shape = {df.shape}')
print(f'columns = {df.columns}')