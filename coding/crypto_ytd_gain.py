# filename: crypto_ytd_gain.py

import requests
from datetime import datetime
import time
import json

def get_top_10_crypto():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    return response.json()

def get_historical_price(coin_id, date):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/history"
    params = {
        "date": date.strftime("%d-%m-%Y")
    }
    response = requests.get(url, params=params)
    return response.json()

# Get top 10 cryptocurrencies
top_10 = get_top_10_crypto()

print("Debug - Top 10 cryptocurrencies response:")
print(json.dumps(top_10, indent=2))
print("-" * 30)

# Get current date and January 1st, 2024
today = datetime.now()
jan_1_2024 = datetime(2024, 1, 1)

print(f"Top 10 cryptocurrencies by market cap as of {today.strftime('%Y-%m-%d')}:")

if isinstance(top_10, list):
    for coin in top_10:
        if isinstance(coin, dict) and 'id' in coin and 'name' in coin and 'current_price' in coin:
            coin_id = coin['id']
            coin_name = coin['name']
            current_price = coin['current_price']
            
            print(f"\nProcessing {coin_name}:")
            print(f"Current price: ${current_price}")
            
            # Get historical price for January 1st, 2024
            historical_data = get_historical_price(coin_id, jan_1_2024)
            
            print("Debug - Historical data response:")
            print(json.dumps(historical_data, indent=2))
            print("-" * 30)
            
            # Sleep to avoid hitting API rate limits
            time.sleep(1)
        else:
            print(f"\nUnexpected coin data structure: {coin}")
else:
    print("Unexpected top 10 cryptocurrencies response structure")

print("\nNote: This is a debug output to understand the API response structure.")