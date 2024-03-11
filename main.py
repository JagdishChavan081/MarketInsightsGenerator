import time
from data_extraction import extract_data
from csv_handling import save_to_csv
from database_handling import insert_into_database


def main():
    stock_symbols = ["AAPL", "GOOGL", "MSFT"]  # Example stock symbols
    while True:
        data = extract_data(stock_symbols)
        save_to_csv(data)
        insert_into_database(data)
        time.sleep(60)  # Wait for 60 seconds before the next iteration


if __name__ == "__main__":
    main()
