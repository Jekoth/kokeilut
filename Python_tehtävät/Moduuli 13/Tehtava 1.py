from flask import Flask, Response
import json

app = Flask(__name__)

def onko_alkuluku(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

@app.route('/alkuluku/<luku>')
def tarkista_alkuluku(luku):
    try:
        numero = int(luku)
        vastaus = {
            "Number": numero,
            "isPrime": onko_alkuluku(numero)
        }
        return Response(response=json.dumps(vastaus), status=200, mimetype="application/json")
    except ValueError:
        virhe_vastaus = {
            "status": 400,
            "error": "Virheellinen syöte. Anna kokonaisluku"
        }
        return Response(response=json.dumps(virhe_vastaus), status=400, mimetype="application/json")

@app.errorhandler(404)
def ei_loytynyt(e):
    vastaus = {
        "status": 404,
        "error": "Päätepistettä ei löytynyt"
    }
    return Response(response=json.dumps(vastaus), status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)