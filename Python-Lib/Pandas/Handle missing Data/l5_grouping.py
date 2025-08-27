import pandas as pd;

data = {
    "name": ["Manjeet", "Manjeet", "simran", "Manjeet", "ananya", "Manjeet", "nina"],
    "age": [25, 25, 28, 22, 22, 22, 31],
    "salary": [50000, 65000, 55000, 48000, 52000, 61000, 58000],
    "score": [88, 92, 85, 90, 87, 93, 89]
}

df = pd.DataFrame(data)

print()
print("Single grouping: ")
print()

# means is age vale total itni salary le kar ja rahe hai, it creates groups on age on unique values
grouped = df.groupby("age")["salary"].sum()
print(grouped)

print()
print("Multiple grouping: ")
print()

# means is age vale total itni salary le kar ja rahe hai, it creates groups on age on unique values
grouped1 = df.groupby(["name","age"])["salary"].sum()
print(grouped1)