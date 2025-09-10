import pandas as pd

df_customers = pd.DataFrame({
    "customerID":[1,2,3],
    "Name":["itachi","kakashi","sasuke"]
})
df_orders = pd.DataFrame({
    "customerID":[1,2,4],
    "orders":[230,453,234]
})
# # inner join
df_merged = pd.merge(df_customers,df_orders,on="customerID",how="inner")
print("inner join")
print(df_merged)

# # outer join
df_merged = pd.merge(df_customers,df_orders,on="customerID",how="outer")
print("outer join")
print(df_merged)

# # left join
df_merged = pd.merge(df_customers,df_orders,on="customerID",how = "left")
print("Left join")
print(df_merged)

# #right join
df_merged = pd.merge(df_customers,df_orders,on="customerID", how="right")
print("Right join")
print(df_merged)

df_merged = pd.merge(df_customers,df_orders, how="cross")
print("cross join")
print(df_merged)
