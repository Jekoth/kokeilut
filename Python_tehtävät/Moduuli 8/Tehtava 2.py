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

country_code = input("Enter the country code(FI, USA): ")

#SQL
toimi = yhteys.cursor()
toimi.execute("""
    SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type """, (country_code,))

tulokset = toimi.fetchall()

toimi.close()
yhteys.close()

#Searches for database and prints data
if tulokset:
    print(f"Airports in country {country_code} by type: ")
    for airport_type, count in tulokset:
        print(f"{airport_type}: {count}")
else:
    print("No airports found for the given country code.")
