nimet = set()

while True:
    try:
        nimi = input("Syötä nimi (tai paina Enter ja lopeta)")
        if nimet == "":
            break

    except ValueError:
        print("Error")