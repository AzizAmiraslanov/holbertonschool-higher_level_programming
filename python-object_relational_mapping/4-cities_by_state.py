#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
Results are sorted by cities.id in ascending order
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

    # SQL sorğusu: cities ilə states join
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
