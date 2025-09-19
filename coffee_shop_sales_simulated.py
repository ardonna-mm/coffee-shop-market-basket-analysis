import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("coffee_shop_sales.csv")

# Step 1: Define categories for pairing
# -------------------------------
drinks = df[df['product_category'].str.contains("Coffee|Tea|Latte|Espresso", case=False)]['product_name'].unique()
pastries = df[df['product_category'].str.contains("Bakery|Muffin|Croissant|Brownie", case=False)]['product_name'].unique()


# Step 2: Create a new transaction ID
# -------------------------------
# Randomly group transactions into baskets of size 2–3
np.random.seed(42)
df['new_transaction_id'] = np.random.randint(1, len(df)//2, df.shape[0])

# Step 3: Enrich baskets with second items
# -------------------------------
def add_companion_item(row):
    # If the product is a drink, add a pastry
    if row['product_name'] in drinks and len(pastries) > 0:
        return np.random.choice(pastries)
    # If product is a pastry, add a drink
    elif row['product_name'] in pastries and len(drinks) > 0:
        return np.random.choice(drinks)
    # Otherwise, return None
    return None

# Apply companion logic
df['companion_product'] = df.apply(add_companion_item, axis=1)

# Step 4: Build new simulated dataset
# -------------------------------
# Stack original + companion rows into one DataFrame
companion_rows = df.dropna(subset=['companion_product']).copy()
companion_rows['product_name'] = companion_rows['companion_product']

# Drop the helper column
companion_rows.drop(columns=['companion_product'], inplace=True)
df.drop(columns=['companion_product'], inplace=True)

# Combine original + companion
df_simulated = pd.concat([df, companion_rows], ignore_index=True)

# -------------------------------
# Step 5: Save new dataset
# -------------------------------
df_simulated.to_csv("coffee_shop_sales_simulated.csv", index=False)

print("✅ Simulated dataset created: coffee_shop_sales_simulated.csv")
print("Original rows:", len(df))
print("Simulated rows:", len(df_simulated))
