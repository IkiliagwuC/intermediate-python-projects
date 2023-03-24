import requests
import pandas as pd

# Set the API endpoint and parameters
api_endpoint = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "XXX"  # Replace with your API key
}
params = {
    "start": "1",  # Starting position of the listing
    "limit": "500",  # Maximum number of results to return #can also be changed to include low cap and recent coins
    "convert": "USD",  # Currency to convert to
}

# Make the API request
response = requests.get(api_endpoint, headers=headers, params=params)

MIN_CAP = 20000000
MAX_CAP = 500000000
#can also add some index for measuring volatility

# Parse the response
if response.status_code == 200:
    data = response.json()["data"]
    
    # Filter the data by market cap range
    filtered_data = [coin for coin in data 
                     if coin["quote"]["USD"]["market_cap"] >= MIN_CAP and 
                     coin["quote"]["USD"]["market_cap"] <= MAX_CAP]
    
    # Extract the required fields
    results = []
    for coin in filtered_data:
        ticker = coin["symbol"]
        price = coin["quote"]["USD"]["price"]
        market_cap = coin["quote"]["USD"]["market_cap"]
        percent_change_24h = coin["quote"]["USD"]["percent_change_24h"]
        percent_change_60d = coin["quote"]["USD"]["percent_change_60d"]
        volume = coin["quote"]["USD"]["volume_24h"]
#         website = coin["url"]["website"][0]
        
        # Add the results to the list
        results.append({
            "ticker": ticker,
            "price": float(price),
            "market_cap": float(market_cap),
            "percent_change_24h": float(percent_change_24h),
            "percent_change_60d": float(percent_change_60d), 
            "volume": float(volume)})
    #print(results)


data = pd.DataFrame(results)

data['market_cap'] = data['market_cap'].apply(lambda x: '{:,}'.format(x))
data['volume'] = data['volume'].apply(lambda x: '{:,}'.format(x))

pd.options.display.float_format = '{:.2f}'.format


print(data)