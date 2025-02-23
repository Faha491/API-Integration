import requests
import pandas as pd

# API Endpoint for Cryptocurrency Prices
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",  # Get prices in USD
    "order": "market_cap_desc",
    "per_page": 10,  # Fetch top 10 cryptocurrencies
    "page": 1,
    "sparkline": False
}

# Fetch Data from API
response = requests.get(API_URL, params=PARAMS)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Convert API response to JSON format
    
    # Extract Relevant Data
    crypto_data = []
    for coin in data:
        crypto_data.append({
            "Name": coin["name"],
            "Symbol": coin["symbol"],
            "Price (USD)": coin["current_price"],
            "Market Cap": coin["market_cap"],
            "24h Volume": coin["total_volume"]
        })
    
    # Convert to Pandas DataFrame
    df = pd.DataFrame(crypto_data)

    # Save to CSV
    df.to_csv("crypto_prices.csv", index=False)
    print("Data successfully saved to crypto_prices.csv")
    quit
    
else:
    print(f"API Request Failed! Status Code: {response.status_code}")
