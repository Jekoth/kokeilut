import requests

def hae_random_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        vitsi = data.get("value")
        return vitsi
    else:
        return "Vitsien hakeminen epäonnistui."

def main():
    vitsi = hae_random_vitsi()
    print(vitsi)

if __name__ == "__main__":
    main()