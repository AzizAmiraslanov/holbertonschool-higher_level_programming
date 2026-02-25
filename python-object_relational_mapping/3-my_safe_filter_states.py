#!/usr/bin/python3
"""
Lists all states with a name matching the argument from the database.
Safe from MySQL injection.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="root",
        db=database
    )

    cursor = db.cursor()

    # SQL query using placeholders to prevent SQL injection
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC;"
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
