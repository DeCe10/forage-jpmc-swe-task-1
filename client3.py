import json
import random
import urllib.request
import time

# Server API URL
QUERY = "http://localhost:8080/query?id={}"

# Number of requests
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    if price_b == 0:
        return
    return price_a / price_b


# Main
if __name__ == "__main__":
    prices = {}  # Store prices of 'ABC' and 'DEF'

    for _ in range(N):

        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        # Print the raw JSON response for debugging


        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print(f"Quoted {stock} at (bid: {bid_price}, ask: {ask_price}, price: {price})")

        if 'ABC' in prices and 'DEF' in prices:
            ratio = getRatio(prices['ABC'], prices['DEF'])
            print(f"Ratio of ABC to DEF: {ratio}")

        # Sleep for a while (e.g., 1 second) to avoid making requests too quickly
        time.sleep(1)
