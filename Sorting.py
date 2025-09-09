import pandas as pd

data = {
    "Name":["owais","sudais","muhammad","talha"],
    "Age":[34,56,22,54],
    "Ps":[50,90,43,70]
}
df = pd.DataFrame(data)
print(df)


# True is for ascending and vice versa, its for single column.
df.sort_values(by = "Age",ascending=True,inplace=True)
print("After ascending Age col")
print(df)

print("*************")
# Targeting more than 1 columns.
df.sort_values(by=["Name","Age","Ps"],ascending=[True,True,True],inplace=True)
print("After ascending Name,Age and ps col")
print(df)

