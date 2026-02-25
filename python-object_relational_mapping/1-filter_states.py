#!/usr/bin/python3
"""
Lists all states starting with N from the database provided as argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # SQL query: case-sensitive N
    query = ("SELECT * FROM states "
             "WHERE BINARY name LIKE 'N%' "
             "ORDER BY id ASC;")
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()
    