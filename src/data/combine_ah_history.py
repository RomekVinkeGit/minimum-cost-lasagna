import json
import pandas as pd
import os
from datetime import datetime

def process_json_file(file_path):
    # Extract date from filename (format: supermarkets_yyyy-mm-dd.json)
    filename = os.path.basename(file_path)
    date_str = filename.split('_')[1].replace('.json', '')  # Get yyyy-mm-dd part
    
    # Read the JSON file
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Create a list to store AH products
    ah_products = []
    
    # Iterate through each supermarket
    for supermarket in data:
        # Only process Albert Heijn data
        if supermarket['c'] == 'AH':
            supermarket_name = supermarket['n']
            
            # Iterate through each product
            for product in supermarket['d']:
                product_data = {
                    'date': date_str,
                    'supermarket': supermarket_name,
                    'supermarket_code': supermarket['c'],
                    'product_name': product['n'],
                    'product_link': product['l'],
                    'price': product['p'],
                    'size': product['s']
                }
                ah_products.append(product_data)
    
    return pd.DataFrame(ah_products)

def main():
    # Get all JSON files from the supermarkets_versions directory
    json_files = [f for f in os.listdir('supermarkets_versions') if f.startswith('supermarkets') and f.endswith('.json')]
    
    if not json_files:
        print("No supermarket JSON files found in the supermarkets_versions directory!")
        return
    
    # Process each file and combine the results
    all_data = []
    for file in json_files:
        print(f"Processing {file}...")
        file_path = os.path.join('supermarkets_versions', file)
        df = process_json_file(file_path)
        all_data.append(df)
    
    # Combine all DataFrames
    combined_df = pd.concat(all_data, ignore_index=True)
    
    # Sort by date and product name
    combined_df = combined_df.sort_values(['date', 'product_name'])
    
    # Save to CSV
    output_file = 'ah_price_history.csv'
    combined_df.to_csv(output_file, index=False)
    print(f"\nCreated {output_file} with {len(combined_df)} products from {len(json_files)} files")
    print(f"Date range: from {combined_df['date'].min()} to {combined_df['date'].max()}")

if __name__ == "__main__":
    main() 