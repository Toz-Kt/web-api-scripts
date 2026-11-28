import requests
from decimal import Decimal
def formatear_precio(precio):
    dec = Decimal(str(precio))
    if dec < 1:
        return f"{dec.normalize():f}"
    return str(round(float(dec), 2))
opcion = input("1: Check a coin's price | 2: Top 24h losers: ")
if opcion.strip() == "1":
        coin_id = input("Enter coin ID: ").strip().lower()
        vs_currency = input("Enter base currency: ").strip().lower()
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": coin_id,"vs_currencies": vs_currency,}
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            price = data.get(coin_id, {}).get(vs_currency)
            if price is not None:
                print(f"{coin_id} is at: {formatear_precio(price)} {vs_currency.upper()}")
            else:
                print("Coin or currency not found in response.")
        else:
            print(f"Request failed with status code: {response.status_code}")
elif opcion.strip() == "2":
    vs_currency = input("Enter base currency: ").strip().lower()
    url_2 = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": vs_currency, "per_page": 100,}
    response = requests.get(url_2, params=params, timeout=5)
if response.status_code == 200:
        data = response.json()
        filtered_coins = []
        for coin in data:
            change_24h = coin.get("price_change_percentage_24h")
            if change_24h is not None and -99 < change_24h < -0.5:
                filtered_coins.append(coin)
        sorted_coins = sorted(filtered_coins, key=lambda x: x["price_change_percentage_24h"])
        for coin in sorted_coins:
            name = coin.get("name")
            price = coin.get("current_price")
            change_24h = coin.get("price_change_percentage_24h")
            print(f"{name}: {formatear_precio(price)} {vs_currency.upper()} ({change_24h:.2f}%)")
else:
    print(f"Request failed with status code: {response.status_code}")