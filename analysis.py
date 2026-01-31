import pandas as pd

# -----------------------------
# Step 1: Load final dataset
# -----------------------------
final_df = pd.read_csv("final_food_delivery_dataset.csv")

# -----------------------------
# Step 2: Clean columns and types
# -----------------------------
# Remove spaces in column names
final_df.columns = final_df.columns.str.strip()

# Rename user column for clarity
if 'order_user_id' in final_df.columns:
    final_df.rename(columns={'order_user_id':'user_id'}, inplace=True)

# Convert total_amount to numeric
final_df['total_amount'] = pd.to_numeric(final_df['total_amount'], errors='coerce')

# Convert order_date to datetime
final_df['order_date'] = pd.to_datetime(final_df['order_date'], dayfirst=True)

# -----------------------------
# Step 3: Analysis Questions
# -----------------------------

# 1️⃣ City with highest total revenue from Gold members
gold_orders = final_df[final_df['membership'] == 'Gold']
city_revenue = gold_orders.groupby('city')['total_amount'].sum().sort_values(ascending=False)
print("1️⃣ City with highest revenue from Gold members:", city_revenue.head(1).index[0])

# 2️⃣ Cuisine with highest average order value
avg_order_cuisine = final_df.groupby('cuisine')['total_amount'].mean().sort_values(ascending=False)
print("2️⃣ Cuisine with highest average order value:", avg_order_cuisine.head(1).index[0])

# 3️⃣ Distinct users with total orders > 1000
user_total = final_df.groupby('user_id')['total_amount'].sum()
distinct_users = user_total[user_total > 1000].count()
print("3️⃣ Distinct users with orders > ₹1000:", distinct_users)

# 4️⃣ Restaurant rating range with highest revenue
bins = [0, 3.5, 4.0, 4.5, 5.0]
labels = ['3.0-3.5','3.6-4.0','4.1-4.5','4.6-5.0']
final_df['rating_range'] = pd.cut(final_df['rating'], bins=bins, labels=labels)
rating_revenue = final_df.groupby('rating_range')['total_amount'].sum().sort_values(ascending=False)
print("4️⃣ Rating range with highest revenue:", rating_revenue.head(1).index[0])

# 5️⃣ Among Gold members, city with highest average order value
gold_city_avg = gold_orders.groupby('city')['total_amount'].mean().sort_values(ascending=False)
print("5️⃣ City with highest average order value among Gold members:", gold_city_avg.head(1).index[0])

# 6️⃣ Cuisine with lowest distinct restaurants but significant revenue
rest_count = final_df.groupby('cuisine')['name'].nunique()
revenue_by_cuisine = final_df.groupby('cuisine')['total_amount'].sum()
combo_df = pd.DataFrame({'num_restaurants': rest_count, 'revenue': revenue_by_cuisine})
combo_result = combo_df.sort_values(by=['num_restaurants','revenue'], ascending=[True, False])
print("6️⃣ Cuisine with few restaurants but high revenue:", combo_result.head(1).index[0])

# 7️⃣ Percentage of total orders placed by Gold members
gold_order_pct = round(len(gold_orders)/len(final_df) * 100)
print("7️⃣ Percentage of orders by Gold members:", f"{gold_order_pct}%")

# 8️⃣ Restaurant with highest average order value but < 20 total orders
rest_stats = final_df.groupby('name').agg(
    avg_order=('total_amount','mean'),
    total_orders=('order_id','count')
)
top_rest = rest_stats[rest_stats['total_orders'] < 20].sort_values('avg_order', ascending=False)
print("8️⃣ Restaurant with highest avg order (<20 orders):", top_rest.head(1).index[0])

# 9️⃣ Combination with highest revenue (membership + cuisine)
combo = final_df.groupby(['membership','cuisine'])['total_amount'].sum().sort_values(ascending=False)
top_combo = combo.head(1)
print("9️⃣ Membership + Cuisine combination with highest revenue:", top_combo.index[0])

# 🔟 Quarter with highest revenue
final_df['quarter'] = final_df['order_date'].dt.quarter
quarter_revenue = final_df.groupby('quarter')['total_amount'].sum().sort_values(ascending=False)
quarter_map = {1:'Q1 (Jan–Mar)', 2:'Q2 (Apr–Jun)', 3:'Q3 (Jul–Sep)', 4:'Q4 (Oct–Dec)'}
print("🔟 Quarter with highest revenue:", quarter_map[quarter_revenue.head(1).index[0]])
import pandas as pd

# -----------------------------
# Load dataset
# -----------------------------
final_df = pd.read_csv("final_food_delivery_dataset.csv")

# Clean column names
final_df.columns = final_df.columns.str.strip()

# Rename user column
if 'order_user_id' in final_df.columns:
    final_df.rename(columns={'order_user_id':'user_id'}, inplace=True)

# Convert total_amount to numeric
final_df['total_amount'] = pd.to_numeric(final_df['total_amount'], errors='coerce')

# Convert order_date to datetime
final_df['order_date'] = pd.to_datetime(final_df['order_date'], dayfirst=True)

# -----------------------------
# Question Calculations
# -----------------------------

# 1️⃣ Total orders by Gold members
gold_orders = final_df[final_df['membership'] == 'Gold']
total_gold_orders = len(gold_orders)
print(" Total orders placed by Gold members:", total_gold_orders)

# 2️⃣ Total revenue from Hyderabad (rounded)
hyderabad_orders = final_df[final_df['city'].str.lower() == 'hyderabad']
total_revenue_hyderabad = round(hyderabad_orders['total_amount'].sum())
print(" Total revenue from Hyderabad:", total_revenue_hyderabad)

# 3️⃣ Number of distinct users with at least one order
distinct_users = final_df['user_id'].nunique()
print("Distinct users with at least one order:", distinct_users)

# 4️⃣ Average order value for Gold members (2 decimals)
avg_order_gold = round(gold_orders['total_amount'].mean(), 2)
print("Average order value for Gold members:", avg_order_gold)

# 5️⃣ Number of orders for restaurants with rating ≥ 4.5
high_rating_orders = len(final_df[final_df['rating'] >= 4.5])
print("Orders for restaurants with rating ≥ 4.5:", high_rating_orders)

# 6️⃣ Orders in the top revenue city among Gold members
top_gold_city = gold_orders.groupby('city')['total_amount'].sum().idxmax()
orders_top_gold_city = len(gold_orders[gold_orders['city'] == top_gold_city])
print(f"Orders in the top revenue Gold city ({top_gold_city}):", orders_top_gold_city)
print(f"{len(final_df)}")
