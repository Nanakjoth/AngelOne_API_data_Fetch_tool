# Main entry point for the Angel One API Trading application

import sys

def print_menu():
    print("\n===== Angel One API Trading Application =====\n")
    print("1. Fetch historical data for a specific stock")
    print("2. Fetch historical data for all stocks in portfolio")
    print("3. Fetch full history of all stocks in portfolio")
    print("4. Fetch minute-level data for a specific stock")
    print("0. Exit")
    print("\n==========================================")

def main():
    while True:
        print_menu()
        choice = input("\nEnter your choice (0-4): ")
        
        if choice == '0':
            print("Exiting application. Goodbye!")
            sys.exit(0)
        elif choice == '1':
            print("\nFetching historical data for a specific stock...")
            from fetch_historical_data import main as fetch_historical
            fetch_historical()
        elif choice == '2':
            print("\nFetching historical data for all stocks in portfolio...")
            from fetch_portfolio_data import main as fetch_portfolio
            fetch_portfolio()
        elif choice == '3':
            print("\nFetching full history of all stocks in portfolio...")
            from fetch_portfolio_full_history import main as fetch_full_history
            fetch_full_history()
        elif choice == '4':
            print("\nFetching minute-level data for a specific stock...")
            from fetch_minute_data import main as fetch_minute
            fetch_minute()
        else:
            print("Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()