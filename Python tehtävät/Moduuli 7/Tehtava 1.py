vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")


while True:
    try:
        kuukaudennumero = int(input("Anna kuukauden järjestysnumero (1-12): "))

        if 1 <= kuukaudennumero <= 12:
                vuodenaika = vuodenajat[kuukaudennumero-1]
                print (f"Kuukausi {kuukaudennumero} on {vuodenaika}.")
                break
        else:
            print("Virheellinen numero! Anna luku 1-12")
    except ValueError:
        print("VIRHE! Syötä numero 1-12")