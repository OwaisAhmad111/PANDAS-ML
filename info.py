import pandas as pd
# df = pd.read_json("sample_Data.json")
# print("show info about the data")
# print(df.info())

data = {
    "name":['owais','sudais','luthfullah'],
    "Age" : [19,15,25],
    "city":['peshawar','peshawar','peshawar']

}

df = pd.DataFrame(data)
print("Displaying the info of data set")
print(df.info())