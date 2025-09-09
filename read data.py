import pandas as pd

# read data from csv,excel,json file into dataframe

df = pd.read_json("sample_Data.json",encoding="utf-8")
df = pd.read_csv("sales_data_sample.csv")
df = pd.read_excel("sampleSuperstore.xlsx")
print(df)
