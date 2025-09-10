import pandas as pd
data = {
    "Name":['Roohullah','Noman','Luthfullah','Malik','Owais','Sudais'],
    "Age":[59,46,25,23,46,59],
    "Salary":[300000,40000,100000,10000,5000,3000],
    "performance score":[65,97,80,78,80,70]
}
print("Data set")
df = pd.DataFrame(data)
print(df)

# Grouping in a single column
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)

#More than two column Grouping.
grouped = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)