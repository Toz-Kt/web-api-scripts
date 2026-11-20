import requests

game = input("Which game are you looking for?: ").lower().strip()
url = f"https://store.steampowered.com/api/storesearch/?term={game}&l=spanish&cc=MX"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data["items"]:
        first_game = data["items"][0]
        if "price" in first_game:
            print(f'price: {first_game["price"]["final"] / 100} MXN')
        else:
            print("price: free :D")
    else:
        game = input("That game doesn't exist. Try one more time, which game are you looking for?: ").lower().strip()
        url = f"https://store.steampowered.com/api/storesearch/?term={game}&l=spanish&cc=MX"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data["items"]:
                first_game = data["items"][0]
                if "price" in first_game:
                    print(f'price: {first_game["price"]["final"] / 100} MXN')
                else:
                    print("price: free :D")
else:
    print("Error connecting to the page")