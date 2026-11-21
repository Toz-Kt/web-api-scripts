import requests

nombre = input("Introduce el ID de la moneda: ")
moneda = input("Introduce tu moneda base: ")
url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": f"{nombre}",
    "vs_currencies": f"{moneda}",
}

response = requests.get(url, params=params, timeout=5)
print("Status:", response.status_code)
data = response.json()
print(data)