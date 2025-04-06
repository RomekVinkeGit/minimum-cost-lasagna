import json
import pandas as pd

# Read the JSON file
with open('supermarkets.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create a list to store all products
all_products = []

# Iterate through each supermarket
for supermarket in data:
    supermarket_name = supermarket['n']
    supermarket_code = supermarket['c']
    
    # Iterate through each product in the supermarket
    for product in supermarket['d']:
        product_data = {
            'supermarket': supermarket_name,
            'supermarket_code': supermarket_code,
            'product_name': product['n'],
            'product_link': product['l'],
            'price': product['p'],
            'size': product['s']
        }
        all_products.append(product_data)

# Create DataFrame
df = pd.DataFrame(all_products)

# Save to CSV
df.to_csv('supermarket_products.csv', index=False)
print(f"Created CSV file with {len(df)} products from {len(data)} supermarkets") 