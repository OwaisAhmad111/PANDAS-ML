import pandas as pd
data = {
    "Salary":[300000,40000,100000,10000,None,3000],
    "performance score":[40,50,None,70,80,90]
}
df = pd.DataFrame(data)
print("Before interpolation")
print(df)

# it will show an estimated value.
df["performance score"].interpolate(method="linear",axis=0,inplace=True)
df["Salary"].interpolate(method="linear",axis=0,inplace=True)
print("After interpolation")
print(df)