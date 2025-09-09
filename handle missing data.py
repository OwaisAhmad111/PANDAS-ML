import pandas as pd
data = {
    "Name":['Roohullah',None,'Luthfullah','Malik','Owais','Sudais'],
    "Age":[59,46,25,23,19,15],
    "Salary":[300000,40000,100000,10000,None,3000],
    "performance score":[97,97,80,None,80,70]
}
df = pd.DataFrame(data)
print(df)

print("*****************")
df.dropna(inplace=True) # all the missing data with there other info will be deleated.
print(df)

df.dropna(axis = 0,inplace=True) # 0 is for rows and 1 for columns.
print(df)