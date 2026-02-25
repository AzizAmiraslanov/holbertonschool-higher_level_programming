#!/usr/bin/python3
"""
Lists all states starting with N from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Komut satırından parametrləri alırıq
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # MySQL serverinə qoşuluruq
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="root",
        db=database
    )

    cursor = db.cursor()

    # SQL sorğusu: adı N ilə başlayan ştatlar
    query = "SELECT * FROM states "
         "WHERE BINARY name LIKE 'N%' "
         "ORDER BY id ASC;"
    cursor.execute(query)

    # Nəticələri yazdırırıq
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Bağlantını bağlayırıq
    cursor.close()
    db.close()
