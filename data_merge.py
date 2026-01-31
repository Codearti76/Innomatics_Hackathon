import pandas as pd

orders_df = pd.read_csv("orders.csv")
print(orders_df.head())
users_df = pd.read_json("users.json")
print(users_df.head())
import sqlite3

conn = sqlite3.connect("restaurants.db")

with open("restaurants.sql", "r") as f:
    sql_script = f.read()

conn.executescript("DROP TABLE IF EXISTS restaurants;")
conn.executescript(sql_script)

restaurants_df = pd.read_sql_query(
    "SELECT * FROM restaurants",
    conn
)
merged_df = orders_df.merge(
    users_df,
    on="user_id",
    how="left"
)
final_df = merged_df.merge(
    restaurants_df,
    on="restaurant_id",
    how="left"
)
final_df = final_df.loc[:, ~final_df.columns.duplicated()]
final_df.rename(columns={
    "user_id": "order_user_id"
}, inplace=True)

final_df.to_csv(
    "final_food_delivery_dataset.csv",
    index=False
)
final_df['order_date'] = pd.to_datetime(
    final_df['order_date'],
    dayfirst=True
)


print("✅ Final dataset created successfully!")
