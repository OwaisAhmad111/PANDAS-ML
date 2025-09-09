import pandas as pd
employee = {
    "Names": ["owais","dayan","musa","ahrar","luthf","ahmad","noman"],
    "salary":[900000,800000,30000,20000,50000,45000,25000],
    "age":[19,22,34,23,30,27,32]
}
# Data Frame
df = pd.DataFrame(employee)
print("Data Frame")
print(df)
print("*****************")

# higher salary, single condition
higher_salary = df[df["salary"] > 40000]
print("higher salary > 40000")
print(higher_salary)

print("*****************")
# Double condition, And
filter = df[(df["age"] < 30) & (df['salary'] > 40000)]
print("Filtered rows, age < 30 & sal > 40000, And condition")
print(filter)

print("*****************")
# OR condition
filtered_or = df[(df["age"] > 30) | (df["salary"] > 50000)]
print("Age > 30 | salary > 50000, Or condition")
print(filter)