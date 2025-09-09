import pandas as pd
data = {
    "Name":['Roohullah','Noman','Luthfullah','Malik','Owais','Sudais'],
    "Age":[59,46,25,23,19,15],
    "Salary":[300000,40000,100000,10000,5000,3000],
    "performance score":[97,97,80,78,80,70]
}
df = pd.DataFrame(data)
print("Data frame")
print(df)
print("********************")

# selecting single column
name = df['Name']
print(name)
print("********************")

# selecting multiple columns, Name & salary
subset = df[["Name","Salary"]]
print(subset)

