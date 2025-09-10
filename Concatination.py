import pandas as pd

df_customers = pd.DataFrame({
    "customerID":[1,2,3],
    "Name":["itachi","kakashi","sasuke"]
})
df_orders = pd.DataFrame({
    "customerID":[4,5,6],
    "Name":["sakura","obito","madara"]
})

# vertical(row wise)
# horizontal(col wise)
# default axis= 0
# 0 for vertical
df_concat = pd.concat([df_customers,df_orders],axis = 0,ignore_index=True )
print(df_concat)