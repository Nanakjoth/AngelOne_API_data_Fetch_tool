# Script to fetch historical data for all stocks in the portfolio

import pandas as pd
from utils import authenticate_api, get_portfolio_historical_data, save_to_csv
from config import DEFAULT_FROM_DATE, DEFAULT_TO_DATE

def main():
    # Authenticate with API
    smartApi, feed_token = authenticate_api()
    if not smartApi or not feed_token:
        print("Authentication failed. Exiting.")
        return
    
    # Fetch portfolio historical data
    all_data = get_portfolio_historical_data(
        smartApi, 
        DEFAULT_FROM_DATE, 
        DEFAULT_TO_DATE
    )
    
    if all_data:
        # Save data to CSV
        columns = ['Stock', 'DateTime', 'Open', 'High', 'Low', 'Close', 'Volume']
        df = save_to_csv(all_data, columns, "portfolio_stocks_jan_to_mar.csv")
        
        # Display sample data
        print("\nPortfolio Data Sample:")
        print(df.sample(5) if len(df) > 5 else df)
    else:
        print("No portfolio data retrieved. Exiting.")

if __name__ == "__main__":
    main()