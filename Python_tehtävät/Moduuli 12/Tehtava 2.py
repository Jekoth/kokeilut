import requests

def get_weather_forecast(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status() #Nostaa virheen

        #JSON-vastaus
        data = response.json()
        print("Säätiedot saatu onnistuneesti.")
        return data

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 429:
            print("Virhe 429: Tilisi on väliaikaisesti estetty ylittävän pyyntörajasi vuoksi.")
            print("Harkitse tilauksen päivittämistä tai odota 10 minuuttia ennen kuin yrität uudelleen.")
        else:
            print(f"HTTP-virhe: {http_err} - {response.text}")
    except Exception as err:
        print(f"Tapahtui virhe: {err}")

    return None

def main():
    api_key = "b312367445622a9c3f3c57e2f809bab9" #API-avain
    city_name = input("Syötä paikkakunnan nimi: ")

    #Hakee säätiedot
    weather_data = get_weather_forecast(city_name, api_key)

    if weather_data:
        #Tulostaa tiedot
        temp = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']
        print(f"Paikkakunta: {city_name}")
        print(f"Lämpötila: {temp}°C")
        print(f"Sää: {weather_description}")

if __name__ == "__main__":
    main()