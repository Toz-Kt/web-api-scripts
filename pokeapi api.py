import requests

juego = input("que juego buscas?: ").lower().strip()
url = f"https://store.steampowered.com/api/storesearch/?term={juego}&l=spanish&cc=MX"
respuesta = requests.get(url)

datos = respuesta.json()
print(datos)