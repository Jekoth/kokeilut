import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='password',
    autocommit=True,
    collation='utf8mb3_unicode_ci'
)

#Function that searches for ICAO code from database
def hae_koordinaatit(icao_code):
    cursor = yhteys.cursor()
    cursor.execute("SELECT latitude, longitude FROM airport WHERE ident = %s", (icao_code,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return (result[0], result[1])
    else:
        return None

icao1 = input("Syötä ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Syötä toisen lentokentän ICAO-koodi: ")

#Get airport cordinates
koord1 = hae_koordinaatit(icao1)
koord2 = hae_koordinaatit(icao2)

# Fetch the coordinates of both airports
if koord1 and koord2:
    etaisyys = geodesic(koord1, koord2).kilometers
    print(f"Lentokenttien {icao1} ja {icao2} välinen etäisyys on {etaisyys:.2f} kilometriä.")
else:
    print("Jokin ICAO-koodi on virheellinen tai lentokenttää ei löydy tietokannasta.")

yhteys.close()
