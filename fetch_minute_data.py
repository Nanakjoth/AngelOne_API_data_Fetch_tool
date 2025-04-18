# Script to fetch minute-level data for a specific stock

import pandas as pd
import datetime as dt
from utils import authenticate_api, fetch_historical_data_in_chunks, save_to_csv
from config import DEFAULT_STOCK_SYMBOL, DEFAULT_STOCK_TOKEN, BATCH_SIZE_DAYS

def main():
    # Authenticate with API
    smartApi, feed_token = authenticate_api()
    if not smartApi or not feed_token:
        print("Authentication failed. Exiting.")
        return
    
    # Define date range
    start_date = dt.datetime(2025, 1, 1, 9, 15)
    end_date = dt.datetime(2025, 3, 27, 15, 30)
    
    # Fetch minute-level data in chunks
    all_data = fetch_historical_data_in_chunks(
        smartApi,
        DEFAULT_STOCK_TOKEN,
        start_date,
        end_date,
        BATCH_SIZE_DAYS
    )
    
    if all_data:
        # Save data to CSV
        columns = ["DateTime", "Open", "High", "Low", "Close", "Volume"]
        filename = f"{DEFAULT_STOCK_SYMBOL}_minute_data.csv"
        df = save_to_csv(all_data, columns, filename)
        
        # Display sample data
        print("\nMinute-Level Data Sample:")
        print(df.head())
    else:
        print("No minute-level data retrieved. Exiting.")

if __name__ == "__main__":
    main()