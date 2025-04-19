# Configuration settings for Angel One API

# API Credentials
API_KEY = ''               # Your Angel One API key
CLIENT_CODE = ''          # Your client code (not email)
MPIN = ''                 # Replace with your actual MPIN
TOTP_SECRET = ''          # Replace with your valid Base32-encoded TOTP secret

# Stock Parameters
DEFAULT_EXCHANGE = "NSE"
DEFAULT_SYMBOL_TOKEN = "99926000"  # Default symbol token
DEFAULT_STOCK_SYMBOL = "SUZLON-EQ"  # Default stock symbol for minute data
DEFAULT_STOCK_TOKEN = "12018"      # Default token for minutes data

# Date Parameters
DEFAULT_FROM_DATE = "2025-01-01 09:15"
DEFAULT_TO_DATE = "2025-03-27 15:30"

# API Parameters
DEFAULT_INTERVAL = "ONE_DAY"
MINUTE_INTERVAL = "ONE_MINUTE"

# Batch Parameters
BATCH_SIZE_DAYS = 7  # For fetching data in batches