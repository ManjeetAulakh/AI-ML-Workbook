import pandas as pd;

data = {
    "name": ["ajdkm", "Manej", "simran", "kabir", "ananya", "manav", "nina"],
    "age": [25, 30, 28, 22, 22, 29, 31],
    "salary": [50000, 65000, 55000, 48000, 52000, 61000, 58000],
    "score": [88, 92, 85, 90, 87, 93, 89]
}

df = pd.DataFrame(data)

df.sort_values(by="age", ascending=True,  inplace=True)
print(df)

print()
print("sort mulptile: ")
print()

df.sort_values(by=["age", "score"], ascending=[True, False], inplace=True)
print(df)