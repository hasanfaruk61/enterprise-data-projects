import pandas as pd
import numpy as np

def perform_analytics(df):
    try:
        # 1. City basis Revenue Analysis
        city_performance = df.groupby('City')['Total_Price'].agg(['sum', 'mean', 'count']).rename(
            columns={'sum': 'Total_Revenue', 'mean': 'Average_Order_Value', 'count': 'Order_Count'}
        )

        # 2. Product Basis Revenue Analysis
        product_performance = df.groupby('Products')['Total_Price'].sum().sort_values(ascending=False)

        # 3. Performance Score
        sales_array = df['SalesAmount'].values
        min_val = np.min(sales_array)
        max_val = np.max(sales_array)

        df['Performance_Score'] = (sales_array -min_val) / (max_val - min_val)

        # 4. Determining Best City and Best Product
        top_city = city_performance['Total_Revenue'].idxmax()
        top_product = product_performance.idxmax()

        analysis_results = {
            'city_metrics': city_performance,
            'product_metrics': product_performance,
            'top_city': top_city,
            'top_product': top_product,

        }

        return df, analysis_results

    except Exception as e:
        print(f"An Error Occurred: {e}")
        return None, None


if __name__ == "__main__":
    # Read processed_sales_data.csv' to test
    try:
        data = pd.read_csv("processed_sales_data.csv")
        analyzed_df, results = perform_analytics(data)

        if analyzed_df is not None:
            print("\n--- CITY PERFORMANCE (TOP 5) ---")
            print(results['city_metrics'].head())
            print(f"\nTop City: {results['top_city']}")
            print(f"Top Product: {results['top_product']}")

            # Storing Analyzed Data
            analyzed_df.to_csv("analyzed_sales_data.csv", index=False)

    except FileNotFoundError:
        print("Error: 'processed_sales_data.csv' not found. run first preprocessing.py .")