#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
3 arguments: mysql username, mysql password and database name.
Should connect to a MySQL server running on localhost at port 3306.
Sorted in ascending order by cities.id
"""
import MySQLdb
import sys


def list_states(username, password, db_name):
    """
    Connects to a MySQL database and lists all states from the database.
    """
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities "\
            "LEFT JOIN states ON cities.state_id = states.id "\
            "ORDER BY cities.id"
    cur.execute(query)

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:  # Ensuring there are three arguments
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
