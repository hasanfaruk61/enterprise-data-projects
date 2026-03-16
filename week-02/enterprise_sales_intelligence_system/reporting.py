import pandas as pd

def generate_report(analyzed_df, analysis_results):
    try:
        # 1. Fetch metrics from previous analysis
        city_metrics = analysis_results['city_metrics']
        total_revenue = analyzed_df['Total_Price'].sum()
        general_avg = analyzed_df['Total_Price'].mean()

        # 2. Risk Assessment (Via Bool and If)
        # cities where the average order is 15% below the general average
        risky_cities = []
        for city, row in city_metrics.iterrows():
            # Boolean logic for performance check
            is_underperforming = bool(row['Average_Order_Value'] < (general_avg * 0.85))

            if is_underperforming:
                risky_cities.append(city)

        # 3. Best and Worst Performers (Using Tuples)
        # Storing as (Name, Value) immutable pairs
        best_city_name = analysis_results['top_city']
        best_city_value = city_metrics.loc[best_city_name, 'Total_Revenue']

        worst_city_name = city_metrics['Total_Revenue'].idxmin()
        worst_city_value = city_metrics['Total_Revenue'].min()

        best_performance = (best_city_name, best_city_value)
        worst_performance = (worst_city_name, worst_city_value)

        # 4. Decision Support Metadata (Using Dictionary)
        decision_metadata = {
            "total_sales": total_revenue,
            "risky_count": len(risky_cities),
            "target_reached": bool(total_revenue > 500000),  # Example target
            "status": "Critical" if len(risky_cities) > 3 else "Stable"
        }

        # 5. Formulating the final readable report
        report_output = f"""
        {"=" * 50}
        ENTERPRISE SALES INTELLIGENCE REPORT
        {"=" * 50}

        FINANCIAL SUMMARY:
        - Total Revenue: ${decision_metadata['total_sales']:,.2f}
        - Sales Target Reached: {decision_metadata['target_reached']}

        GEOGRAPHICAL PERFORMANCE (City, Revenue):
        - BEST: {best_performance[0]} (${best_performance[1]:,.2f})
        - WORST: {worst_performance[0]} (${worst_performance[1]:,.2f})

        PRODUCT INSIGHTS:
        - Most Profitable Product: {analysis_results['top_product'].upper()}

        RISK MANAGEMENT:
        - System Status: {decision_metadata['status']}
        - Action Required in: {", ".join(risky_cities) if risky_cities else "None"}

        {"=" * 50}
        """

        return report_output, decision_metadata

    except Exception as e:
        print(f"Error in reporting module: {e}")
        return None, None

if __name__ == "__main__":
    # Test script for the reporting module
    try:
        df = pd.read_csv("analyzed_sales_data.csv")

        test_results = {
            'top_city': "New York City",
            'top_product': "Laptop",
            'city_metrics': df.groupby('City')['Total_Price'].agg(['sum', 'mean']).rename(
                columns={'sum': 'Total_Revenue', 'mean': 'Average_Order_Value'})
        }

        final_report, meta = generate_report(df, test_results)
        print(final_report)

    except FileNotFoundError:
        print("Required data file not found. Please run analytics.py first.")