import pandas as pd

data = {
    "name":['owais','sudais','luthfullah'],
    "Age" : [19,15,25],
    "city":['peshawar','peshawar','peshawar']

}
df = pd.DataFrame(data)
print(df)

# save to csv file.
df.to_csv("output.csv",index=False)

# save to xlasx.
df.to_excel("output.xlsx",index=False)

# save to jason.
df.to_json("output.json",index=False)