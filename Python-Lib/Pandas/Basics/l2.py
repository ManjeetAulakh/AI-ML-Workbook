# describe function

import pandas as pd;

data = {
    "name": ["ajdkm", "raj", "simran", "kabir", "ananya", "manav", "nina"],
    "age": [25, 30, 28, 22, 24, 29, 31],
    "salary": [50000, 60000, 55000, 48000, 52000, 61000, 58000],
    "score": [88, 92, 85, 90, 87, 93, 89]
}

df = pd.DataFrame(data)
print(df)

print(df.describe())

# for quick find of number of rows and colums
print(f'Rows and columns: {df.shape}')
print(f'columns Names: {df.columns}')
