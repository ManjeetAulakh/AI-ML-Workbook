import pandas as pd

# Customer DataFrame
customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 104],
    "name": ["Alice", "Bob", "Charlie", "Diana"]
})

# Orders DataFrame
orders = pd.DataFrame({
    "order_id": [201, 202, 203, 204, 205],
    "customer_id": [101, 103, 101, 102, 105],
    "order_date": ["2024-05-10", "2024-06-15", "2024-07-01", "2024-07-20", "2024-08-01"],
    "order_amount": [2500, 1800, 3200, 4000, 1500]
})

print("Customers DataFrame:")
print(customers)

print("\nOrders DataFrame:")
print(orders)

# never include non match customer ID
innerMerge = pd.merge(customers, orders, on="customer_id", how="inner")
print("\nInner Merged DataFrame:")
print(innerMerge)

# All include non-match customer ID and fill with nan
outerMerge = pd.merge(customers, orders, on="customer_id", how="outer")
print("\nOuter Merged DataFrame:")
print(outerMerge)

# include all left side value and fill right with null
leftMerge = pd.merge(customers, orders, on="customer_id", how="left")
print("\nLeft Merged DataFrame:")
print(leftMerge)

# include right side all and fill left side with null
rightMerge = pd.merge(customers, orders, on="customer_id", how="right")
print("\nRight Merged DataFrame:")
print(rightMerge)

# return all rows
crossMerge = pd.merge(customers, orders, how="cross")
print("\nCross Merged DataFrame:")
print(crossMerge)