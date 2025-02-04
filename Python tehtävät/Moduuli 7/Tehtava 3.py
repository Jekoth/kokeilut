import os

def clear_screen():
    # Clears the screen based on the OS
    os.system('cls' if os.name == 'nt' else 'clear')

lentoasemat = {"EFHK": "Helsinki-Vantaa", "EDDF": "Frankfurt"}

while True:
    try:
        clear_screen()
        print("1: Syötä uusi lentoasema")
        print("2: Hae lentoasema ICAO-koodilla")
        print("3: Lopeta")

        valinta = input("Valitse numero 1-3: ")

        if valinta == "1":
            print(f"Syötä ICAO-koodi: ")
            print(f"Syötä lentoaseman nimi: ")
        elif valinta == "2":
            print("Syötä ICAO-koodi haettavalle lentoasemalle: ")
        else:
            print("Ohjelma on lopetettu")
            break

    except ValueError:
        print("Error")