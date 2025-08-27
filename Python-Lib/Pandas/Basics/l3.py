import pandas as pd;

data = {
    "name": ["ajdkm", "raj", "simran", "kabir", "ananya", "manav", "nina"],
    "age": [25, 30, 28, 22, 24, 29, 31],
    "salary": [50000, 60000, 55000, 48000, 52000, 61000, 58000],
    "score": [88, 92, 85, 90, 87, 93, 89]
}

df = pd.DataFrame(data)

print("Accssing columns")
subset = df[['name','age']]
print(subset)

print("having salary above 50000")
filterRows = df[df["salary"] > 50000]
print(filterRows)

# adding new colums 
df["bonus"] = df["salary"] * 0.1
print(df)

# by insert insert fucntion we can also pass indice 
df.insert(0, "ID",[10,20,30,40,50,60,70])
print(df)

print()
print("After update: ")
print()

# for update
df.loc[0, "name"] = "Manjeet"
print(df)

print()
print("After update mulpite: ")
print()

df["salary"] = df["salary"] // 100    # floor divison only return interger value
print(df)

#delete single column
df.drop(columns= ["bonus"], inplace=True)   # false return new update df
print(df)