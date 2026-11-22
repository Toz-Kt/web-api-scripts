import requests

coin_id = input("Enter coin ID: ").strip().lower()
vs_currency = input("Enter base currency: ").strip().lower()
url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": coin_id,
    "vs_currencies": vs_currency,
}
response = requests.get(url, params=params, timeout=5)
if response.status_code == 200:
    data = response.json()
    price = data.get(coin_id, {}).get(vs_currency)
    if price is not None:
        print(f"{coin_id} is at: {price} {vs_currency.upper()}")
    else:
        print("Coin or currency not found in response.")
else:
    print(f"Request failed with status code: {response.status_code}")