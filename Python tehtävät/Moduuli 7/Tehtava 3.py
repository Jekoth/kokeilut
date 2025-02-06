lentoasemat = {"EFHK": "Helsinki-Vantaa", "EDDF": "Frankfurt"}

while True:
    try:

        print("\n1: Syötä uusi lentoasema")
        print("2: Hae lentoasema ICAO-koodilla")
        print("3: Lopeta")

        valinta = input("Valitse numero 1-3: ")

        if valinta == "1":#Lisää lentoasema sanakirjaan
            icao_koodi = input(f"Syötä ICAO-koodi: ")
            lentoasema = input(f"Syötä lentoaseman nimi: ")
            lentoasemat[icao_koodi] = lentoasema
            print("Lentoasema lisätty")
        elif valinta == "2":#Etsii onko lentoasema sanakirjassa
            icao_koodi = input("Syötä ICAO-koodi haettavalle lentoasemalle: ")
            if icao_koodi in lentoasemat:
                print(f"Lentoaseman nimi: {lentoasemat[icao_koodi]}")
            else:
                print("Lentoasemaa ei löydy.")
        elif valinta == "3":#Lopettaa ohjelman
            print("Ohjelma on lopetettu")
            break
        else:
            print("Valitse numero 1-3")

    except ValueError:
        print("Error!")