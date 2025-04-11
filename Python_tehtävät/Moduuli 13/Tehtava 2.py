from flask import Flask, Response
import pymysql
import json

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        port=3306,
        database='flight_game1',
        user='root',
        password='password',
        autocommit=True,
    )

#Päätepiste ICAO-koodilla
@app.route('/kenttä/<icao_code>', methods=['GET'])
def hae_kentta(icao_code):
    connection = None
    try:
        #Yhdistää tietokantaan
        connection = get_db_connection()
        cursor = connection.cursor()

        #Hakee kentän tiedot ICAO-koodilla SQL tiedostosta
        query = "SELECT name, municipality FROM airport WHERE ident = %s"
        cursor.execute(query, (icao_code,))
        result = cursor.fetchone()

        if result:
            #Jos kenttä löytyy, palautetaan JSON-vastaus sanakirjaston
            kentta_nimi, kaupunki = result
            vastaus = {
                "ICAO": icao_code,
                "Name": kentta_nimi,
                "Municipality": kaupunki
            }

            return Response(response=json.dumps(vastaus), status=200, mimetype="application/json")
        else:
            #Jos kenttää ei löydy, palautetaan virhekoodi 404
            virhe_vastaus = {
                "error": "Kenttää ei löytynyt"
            }
            return Response(response=json.dumps(virhe_vastaus), status=404, mimetype="application/json")

    except Exception:
        # Kaikki muut virheet
        virhe_vastaus = {
            "error": "Tapahtui virhe"
        }
        return Response(response=json.dumps(virhe_vastaus), status=500, mimetype="application/json")

    finally:
        #sulke tietokanta, jos on avattu vaikka jos virhe
        if connection:
            connection.close()

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)