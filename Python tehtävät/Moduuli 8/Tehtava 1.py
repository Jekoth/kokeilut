import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='password',
    autocommit=True,
    collation='utf8mb3_unicode_ci'
)

ICAO = input("Enter the ICAO code of an airport: ")

toimi = yhteys.cursor()
toimi.execute("SELECT name, municipality FROM airport WHERE ident = %s", (ICAO,))
tulos = toimi.fetchone()

toimi.close()
yhteys.close()

if tulos:
    print(f"Airport Name: {tulos[0]}, Municipality: {tulos[1]}")
else:
    print("No airport found with the given ICAO code.")
