from itertools import product

import numpy as np
import pandas as pd

def generate_raw_data(n=300):
    #Constant Data Lists
    cities = ["New York City", "Los Angeles", "Chicago", "Houston", "Phoenix",
              "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
              "Austin", "Jacksonville", "Fort Worth", "Columbus", "San Francisco",
              "Charlotte", "Indianapolis", "Seattle", "Denver", "Washington D.C."]

    products = ["Smartphone", "Laptop", "Smartwatch", "Tablet", "Desktop Computer",
                "Wireless Earbuds", "Gaming Console", "Digital Camera", "Drone", "External Hard Drive"]

    #1.Data Producing
    customer_ids = np.random.randint(1000,2000, size=n)
    chosen_products = np.random.choice(products, size=n)
    chosen_cities = np.random.choice(cities, size=n)
    months = np.random.randint(1,13, size=n)

    #2. Prices
    sales = np.random.uniform(50, 5000, size=n)

    #3. Outliers (2% percent)
    outlier_count = int(n * 0.02)
    outlier_indices = np.random.choice(n, size=outlier_count, replace=False)
    sales[outlier_indices] = np.random.uniform(20000, 50000, size=outlier_count)

    #4. Adding NaN Values (10% of data)
    nan_count = int(n * 0.1)
    nan_indices = np.random.choice(n, size=nan_count, replace=False)
    sales[nan_indices] = np.nan

    #5. DataFrame
    df = pd.DataFrame({
        'CustomerID': customer_ids,
        'Products': chosen_products,
        'City': chosen_cities,
        'SalesAmount':sales,
        'Month': months
    })

    return df

if __name__ == "__main__":
    raw_df = generate_raw_data(300)
    raw_df.to_csv("raw_sales_data.csv", index=False)
    print("Veri üretildi: 300 satır, uç değerler ve NaN'lar dahil, negatifler hariç.")
    print(raw_df.describe())
