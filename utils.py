# Utility functions for Angel One API operations

from SmartApi import SmartConnect
import pyotp
import pandas as pd
import datetime as dt
import time
from config import *

def authenticate_api():
    """Authenticate with Angel One API and return the SmartConnect instance and feed token"""
    # Generate the current TOTP code
    totp = pyotp.TOTP(TOTP_SECRET)
    current_totp = totp.now()
    
    # Initialize SmartConnect
    smartApi = SmartConnect(API_KEY)
    
    try:
        # Log in using client code, MPIN, and TOTP
        session_data = smartApi.generateSession(CLIENT_CODE, MPIN, current_totp)
        if session_data.get('status'):
            print("✅ Login successful using MPIN & TOTP!")
        else:
            print("❌ Login failed:", session_data.get('message'))
            return None, None
        
        # Fetch the feed token
        feed_token = smartApi.getfeedToken()
        print("Feed Token:", feed_token)
        
        return smartApi, feed_token
    except Exception as e:
        print(f"❌ Authentication error: {e}")
        return None, None

def get_historical_data(smartApi, symbol_token, from_date, to_date, interval=DEFAULT_INTERVAL, exchange=DEFAULT_EXCHANGE):
    """Fetch historical candle data for a specific symbol"""
    # Prepare parameters for historical data
    historic_params = {
        "exchange": exchange,
        "symboltoken": symbol_token,
        "interval": interval,
        "fromdate": from_date,
        "todate": to_date
    }
    
    try:
        # Request historical candle data
        response = smartApi.getCandleData(historic_params)
        if response.get('status'):
            return response['data']
        else:
            print(f"Error fetching historical data: {response.get('message', 'No message provided')}")
            return None
    except Exception as e:
        print(f"Error in get_historical_data: {e}")
        return None

def get_portfolio_historical_data(smartApi, from_date, to_date, interval=DEFAULT_INTERVAL):
    """Fetch historical data for all stocks in the portfolio"""
    try:
        # Fetch holdings (stocks in portfolio)
        holdings_data = smartApi.holding()
        if not holdings_data.get('status'):
            print("Error fetching holdings:", holdings_data.get('message'))
            return None
            
        holdings = holdings_data['data']
        print("Fetched Portfolio Holdings")
        
        # Prepare a list to store historical data
        all_data = []
        
        # Fetch historical data for each stock in the portfolio
        for stock in holdings:
            symbol_token = stock.get('symboltoken')
            stock_name = stock.get('tradingsymbol')
            
            # Fetch data
            data = get_historical_data(smartApi, symbol_token, from_date, to_date, interval)
            if data:
                for row in data:
                    row.insert(0, stock_name)  # Add stock name to each row
                    all_data.append(row)
            else:
                print(f"No data retrieved for {stock_name}")
        
        return all_data
    except Exception as e:
        print(f"Error in get_portfolio_historical_data: {e}")
        return None

def get_portfolio_full_history(smartApi):
    """Fetch historical data for all stocks from purchase date to today"""
    try:
        # Fetch holdings
        holdings_data = smartApi.holding()
        if not holdings_data.get('status'):
            print("Error fetching holdings:", holdings_data.get('message'))
            return None
            
        holdings = holdings_data['data']
        print("Fetched Portfolio Holdings")
        
        # Prepare a list to store historical data
        all_data = []
        today_date = dt.datetime.today().strftime('%Y-%m-%d %H:%M')
        
        # Fetch historical data for each stock from purchase date to today
        for stock in holdings:
            symbol_token = stock.get('symboltoken')
            stock_name = stock.get('tradingsymbol')
            purchase_date = stock.get('purchasedate', '2020-01-01 09:15')  # Default to 2020 if missing
            
            # Fetch data
            data = get_historical_data(smartApi, symbol_token, purchase_date, today_date)
            if data:
                for row in data:
                    row.insert(0, stock_name)  # Add stock name to each row
                    all_data.append(row)
            else:
                print(f"No data retrieved for {stock_name}")
        
        return all_data
    except Exception as e:
        print(f"Error in get_portfolio_full_history: {e}")
        return None

def fetch_historical_data_in_chunks(smartApi, symbol_token, start_date, end_date, batch_size_days=BATCH_SIZE_DAYS, interval=MINUTE_INTERVAL):
    """Fetch historical data in chunks to avoid API limits"""
    all_data = []
    current_start = start_date
    
    while current_start < end_date:
        current_end = min(current_start + dt.timedelta(days=batch_size_days), end_date)
        print(f"📊 Fetching data from {current_start} to {current_end}...")
        
        # Prepare parameters
        params = {
            "exchange": DEFAULT_EXCHANGE,
            "symboltoken": symbol_token,
            "interval": interval,
            "fromdate": current_start.strftime("%Y-%m-%d %H:%M"),
            "todate": current_end.strftime("%Y-%m-%d %H:%M")
        }
        
        # Fetch data
        response = smartApi.getCandleData(params)
        if response and response.get("status"):
            all_data.extend(response["data"])
        else:
            print(f"❌ Error: {response.get('message', 'Unknown error')}")
        
        # Move to the next batch
        current_start = current_end + dt.timedelta(minutes=1)
        time.sleep(1)  # Pause to avoid API rate limits
    
    return all_data

def save_to_csv(data, columns, filename):
    """Save data to CSV file"""
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(filename, index=False)
    print(f"✅ Saved data to {filename} successfully!")
    return df