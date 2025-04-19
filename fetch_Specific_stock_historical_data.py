# Script to fetch historical data for a specific stock

import pandas as pd
from utils import authenticate_api, get_historical_data, save_to_csv
from config import DEFAULT_SYMBOL_TOKEN, DEFAULT_FROM_DATE, DEFAULT_TO_DATE

def main():
    # Authenticate with API
    smartApi, feed_token = authenticate_api()
    if not smartApi or not feed_token:
        print("Authentication failed. Exiting.")
        return
    
    # Fetch historical data
    data = get_historical_data(
        smartApi, 
        DEFAULT_SYMBOL_TOKEN, 
        DEFAULT_FROM_DATE, 
        DEFAULT_TO_DATE
    )
    
    if data:
        # Save data to CSV
        columns = ['DateTime', 'Open', 'High', 'Low', 'Close', 'Volume']
        df = save_to_csv(data, columns, "historical_data.csv")
        
        # Display sample data
        print("\nHistorical Data Sample:")
        print(df.head())
    else:
        print("No data retrieved. Exiting.")

if __name__ == "__main__":
    main()
