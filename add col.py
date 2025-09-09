import pandas as pd
data = {
    "Name":['Roohullah','Noman','Luthfullah','Malik','Owais','Sudais'],
    "Age":[59,46,25,23,19,15],
    "Salary":[300000,40000,100000,10000,5000,3000],
    "performance score":[97,97,80,78,80,70]
}
df = pd.DataFrame(data)
print(df)

# add column directly but i will be shown in a last column, insert is the best opt.
df["bonus"] =  df["Salary"] * 0.1
print(df)

# Syntax: df.insert(location, "col name", some data)
# add column with your choice location, insert.
df.insert(3,"bonus",df["Salary"] * 0.1)
print(df)

# insert, employee ID
df.insert(0,"employee_ID",[1,2,3,4,5,6])
print(df)

