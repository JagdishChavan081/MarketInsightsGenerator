# importing all necessary lib
from bs4 import BeautifulSoup
from datetime import datetime


# Defining function to scrape Data
def scrape_google_finnace(symbol):
    url = "https://www.google.com/finance/quote/{symbol}:NSE"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    price = soup.find("div", class_="YMlKec fxKbKc").get_text()
    return price


# List of stock symbols
stocks = ["STOCK1", "STOCK2", "STOCK3"]

while True:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {"datetime": [current_time]}

    for stock_symbol in stocks:
        price = scrape_google_finance(stock_symbol)
        data[stock_symbol.lower()] = [price]

    df = pd.DataFrame(data)
    df.to_sql("share_data", conn, if_exists="append", index=False)
    time.sleep(60)
