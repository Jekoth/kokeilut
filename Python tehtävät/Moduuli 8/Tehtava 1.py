import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='password',
         autocommit=True,
         collation='utf8mb3_unicode_ci'
         )

ICAO = input("Enter the ICAO code of an airport: ")
