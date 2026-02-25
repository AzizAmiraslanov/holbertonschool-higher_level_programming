#!/usr/bin/python3
"""
Lists all states with a name matching the argument from the database.
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

    # SQL query using format
    query = (
        "SELECT * FROM states WHERE name = '{}' "
        "ORDER BY id ASC;".format(state_name)
    )
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
