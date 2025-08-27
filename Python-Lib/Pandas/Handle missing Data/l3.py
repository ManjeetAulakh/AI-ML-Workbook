import pandas as pd;

data = {
    "name": ["ajdkm", None, "simran", "kabir", "ananya", "manav", "nina"],
    "age": [5, 10, 15, 20, None, 30, 35],
}

df = pd.DataFrame(data)

print()
print(df)
print()

# fill with estimated value using interpolate, only for numbers   means when data is time seris. numeric
df["age"] = df["age"].interpolate(method="linear", axis=0)
print(df)




