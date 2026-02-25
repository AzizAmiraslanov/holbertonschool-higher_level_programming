#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Safe from SQL injection.
Results are sorted by cities.id in ascending order.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Komut satırından parametrləri alırıq
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # MySQL serverinə qoşuluruq
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="root",
        db=database
    )

    cursor = db.cursor()

    # SQL sorğusu: cities ilə states join, safe from injection
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()

    # Nəticələri istənilən formatda çap edirik
    print(", ".join([row[0] for row in results]))

    cursor.close()
    db.close()
