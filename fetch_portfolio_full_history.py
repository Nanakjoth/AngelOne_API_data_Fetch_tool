# Script to fetch full history of all stocks in the portfolio from purchase date

import pandas as pd
from utils import authenticate_api, get_portfolio_full_history, save_to_csv

def main():
    # Authenticate with API
    smartApi, feed_token = authenticate_api()
    if not smartApi or not feed_token:
        print("Authentication failed. Exiting.")
        return
    
    # Fetch full portfolio history
    all_data = get_portfolio_full_history(smartApi)
    
    if all_data:
        # Save data to CSV
        columns = ['Stock', 'DateTime', 'Open', 'High', 'Low', 'Close', 'Volume']
        df = save_to_csv(all_data, columns, "portfolio_stocks_full_history.csv")
        
        # Display column information
        print("\nDataFrame Columns:", df.columns.tolist())
        print("\nPortfolio Full History Sample:")
        print(df.sample(5) if len(df) > 5 else df)
    else:
        print("No portfolio history data retrieved. Exiting.")

if __name__ == "__main__":
    main()