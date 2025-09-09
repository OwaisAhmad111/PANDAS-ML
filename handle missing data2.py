import pandas as pd
data = {
    "Name":['Roohullah',None,'Luthfullah','Malik','Owais','Sudais'],
    "Age":[59,46,25,23,19,15],
    "Salary":[300000,40000,100000,10000,None,3000],
    "performance score":[97,97,80,None,80,70]
}
df = pd.DataFrame(data)
print(df)

# the missing values will become 0 bcz of the argument.
df.fillna(0,inplace=True)
print(df)

# in this case we will set the mean value in the none space.
df["Salary"].fillna(df["Salary"].mean(), inplace = True)
df["performance score"].fillna(df["performance score"].mean(),inplace=True)
print(df)