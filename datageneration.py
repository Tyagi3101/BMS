"""
Data Generation Script for Bakery Management System (BMS)
Generates sample bakery sales data for testing and demonstration
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_bakery_data(num_records=2000, output_file='data/bakery_sales_2000.csv'):
    """
    Generate sample bakery sales data.
    
    Args:
        num_records (int): Number of sales records to generate (default: 2000)
        output_file (str): Output CSV file path (default: 'data/bakery_sales_2000.csv')
    
    Returns:
        pd.DataFrame: Generated sales dataframe
    """
    np.random.seed(42)
    
    # Bakery items and their typical prices
    items = ['Croissant', 'Sourdough', 'Baguette', 'Ciabatta', 'Focaccia', 
             'Brioche', 'Rye Bread', 'Whole Wheat', 'Multigrain', 'Donut']
    prices = [3.50, 4.25, 3.75, 4.00, 3.25, 4.50, 3.90, 3.80, 4.10, 2.50]
    
    # Generate hourly sales data
    dates = pd.date_range(start='2023-01-01', periods=num_records, freq='1H')
    records = []
    
    for date in dates:
        # Random number of sales per hour
        num_sales = np.random.randint(1, 5)
        for _ in range(num_sales):
            item_idx = np.random.randint(0, len(items))
            records.append({
                'sale_date': date,
                'item_name': items[item_idx],
                'item_price': prices[item_idx] + np.random.uniform(-0.25, 0.25)
            })
    
    df = pd.DataFrame(records)
    df.to_csv(output_file, index=False)
    
    return df

if __name__ == '__main__':
    print("Generating bakery sales data...")
    df = generate_bakery_data()
    print(f"✓ Generated {len(df)} sales records")
    print(f"✓ Saved to data/bakery_sales_2000.csv")
    print(f"\nDataset Summary:")
    print(f"  - Date range: {df['sale_date'].min()} to {df['sale_date'].max()}")
    print(f"  - Unique items: {df['item_name'].nunique()}")
    print(f"  - Total revenue: ${df['item_price'].sum():.2f}")
