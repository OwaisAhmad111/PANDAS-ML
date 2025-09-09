import pandas as pd
data = {
    "Name":['Roohullah','Noman','Luthfullah','Malik','Owais','Sudais'],
    "Age":[59,46,25,23,19,15],
    "salary":[300000,40000,100000,10000,5000,3000],
    "performance score":[97,97,80,78,80,70]
}

df = pd.DataFrame(data)
print("Data Frame")
print(df)
print("***************************")

print("incriminting salary")
df["salary"] = df["salary"] * 0.1
print(df)