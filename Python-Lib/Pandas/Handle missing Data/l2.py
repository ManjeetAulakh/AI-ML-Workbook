import pandas as pd;

data = {
    "name": ["ajdkm", None, "simran", "kabir", "ananya", "manav", "nina"],
    "age": [5, 10, 15, 20, None, 30, 35],
    "salary": [50000, None, 55000, 48000, 52000, 61000, 58000],
    "score": [88, 92, 85, 90, 87, 93, 89]
}

df = pd.DataFrame(data)

print()
print(df)
print()

print("After replace missing value")

df["salary"] = df["salary"].fillna(df["salary"].mean())
# or also df.fillna({"salary": df["salary"].mean()}, inplace=True)
print(df)

# fill with estimated value using interpolate

df.interpolate(method="linear", axis=0, inplace=True)




