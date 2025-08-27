import pandas as pd

# Read CSV File
# df = pd.read_csv("data.csv")
# print(df)

# Read Excel File
# df = pd.read_excel("superstore.xlsx")
# print(df)

# Custom DataFrame

data = {
    "Name": ["Manjeet","singh","Aulakh"],
    "Age": [10,20,30],
    "City": ["Ratia","Ratia","Ratia"]
}

df = pd.DataFrame(data)
print(df)

# to_json, to_excel
# df.to_csv("output.csv", index=False)

# head and tail for get limited data
print("display first 2 rows")
print(df.head(2))
print(df.tail(3))

print(df.info())