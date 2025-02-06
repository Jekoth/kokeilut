nimet = set()

while True:
    try:
        nimi = input("Syötä nimi (tai paina Enter ja lopeta): ")
        if nimi == "":#Stop program after empty string
            print(nimet)
            break

        if nimi in nimet: #If the name is already in the set of names, print that it has been added previously
            print(f"Aiemmin syötetty nimi on {nimi}")
        else:#Else if it is not then add to the set of names
            print(f"Uusi nimi on {nimi}")
            nimet.add(nimi)

    except ValueError:
        print("Error")