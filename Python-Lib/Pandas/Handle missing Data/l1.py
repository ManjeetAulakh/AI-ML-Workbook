import pandas as pd;

data = {
    "name": ["ajdkm", None, "simran", "kabir", "ananya", "manav", "nina"],
    "age": [25, 30, 28, 22, 24, 29, 31],
    "salary": [50000, None, 55000, 48000, 52000, 61000, 58000],
    "score": [88, 92, 85, 90, 87, 93, 89]
}

df = pd.DataFrame(data)

# for string and objects None
# for number NaN

print(df.isnull())
print(df.isnull().sum())

print()
print(df)
print()

# print("After delete missing")
# df.dropna(axis=0, inplace=True)
# print(df)

print()
print("After replace missing value")

df["salary"] = df["salary"].fillna(df["salary"].mean())
# or also df.fillna({"salary": df["salary"].mean()}, inplace=True)

print(df)
