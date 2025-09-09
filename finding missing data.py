import pandas as pd
data = {
    "Name":['Roohullah',None,'Luthfullah','Malik','Owais','Sudais'],
    "Age":[59,46,25,23,19,15],
    "Salary":[300000,40000,100000,10000,5000,3000],
    "performance score":[97,97,80,None,80,70]
}
df = pd.DataFrame(data)
print(df)

# false and 0 means nothing is missing.
print(df.isnull())
print(df.isnull().sum())