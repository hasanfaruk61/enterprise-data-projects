import pandas as pd
import numpy as np

def clean_data(df):
    # Cleaning raw data, filling lost values and adding new columns
    try:
        # Dealing NaN values
        # Filling NaN values in amount with average values
        avg_sales = df['SalesAmount'].mean()
        df['SalesAmount'] = df['SalesAmount'].fillna(avg_sales)

        # String Methods (Normalization)
        # Removing spaces for product and city names
        df['Products'] = df['Products'].str.strip().str.title()
        df['City'] = df['City'].str.strip().str.title()

        # Creating New Column (pandas operation)
        # Adding taxes(20%) and creating total price
        df['Tax_Amount'] = df['SalesAmount'] * 0.20
        df['Total_Price'] = df['Tax_Amount'] + df['SalesAmount']

        # Data Type Check
        # Defining CustomerID as String
        df['CustomerID'] = df['CustomerID'].astype(str)

        print('Data cleaning and transforming is successfully completed')
        return df

    except Exception as e:
        print(f"An error occured while cleaning data: {e}")
        return None

if __name__ == '__main__':
    try:
        raw_data = pd.read_csv("raw_sales_data.csv")
        processed_data = clean_data(raw_data)
        if processed_data is not None:
            processed_data.to_csv("processed_sales_data.csv", index=False)
            print("Cleaned Data is stored as 'processed_sales_data.csv' ")
            print(processed_data)
    except FileNotFoundError:
        print("File not found. Please first run 'data_generator.py")