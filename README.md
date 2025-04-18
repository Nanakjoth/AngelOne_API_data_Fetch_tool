# Angel One API Trading Application

This application provides functionality to fetch and analyze stock data from Angel One's trading platform using their SmartAPI.

## Setup

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Configure your API credentials:
   - Open `config.py`
   - Update the following variables with your actual credentials:
     - `API_KEY`: Your Angel One API key
     - `CLIENT_CODE`: Your client code (not email)
     - `MPIN`: Your MPIN
     - `TOTP_SECRET`: Your valid Base32-encoded TOTP secret

## Usage

Run the main application:
```
python main.py
```

This will display a menu with the following options:

1. **Fetch historical data for a specific stock**
   - Fetches daily historical data for a specific stock (configured in `config.py`)
   - Saves data to `historical_data.csv`

2. **Fetch historical data for all stocks in portfolio**
   - Fetches daily historical data for all stocks in your portfolio
   - Saves data to `portfolio_stocks_jan_to_mar.csv`

3. **Fetch full history of all stocks in portfolio**
   - Fetches daily historical data for all stocks in your portfolio from their purchase dates
   - Saves data to `portfolio_stocks_full_history.csv`

4. **Fetch minute-level data for a specific stock**
   - Fetches minute-level data for a specific stock (configured in `config.py`)
   - Fetches data in batches to avoid API limits
   - Saves data to `[STOCK_SYMBOL]_minute_data.csv`

## File Structure

- `main.py`: Main entry point for the application
- `config.py`: Configuration settings and API credentials
- `utils.py`: Utility functions for API operations
- `fetch_historical_data.py`: Script to fetch historical data for a specific stock
- `fetch_portfolio_data.py`: Script to fetch historical data for all stocks in portfolio
- `fetch_portfolio_full_history.py`: Script to fetch full history of all stocks in portfolio
- `fetch_minute_data.py`: Script to fetch minute-level data for a specific stock
- `requirements.txt`: List of required dependencies

## Notes

- Make sure to keep your API credentials secure
- The application uses TOTP (Time-based One-Time Password) for authentication
- Data is fetched in batches to avoid API rate limits