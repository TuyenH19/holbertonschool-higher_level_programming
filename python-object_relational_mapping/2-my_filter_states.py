#!/usr/bin/python3

import MySQLdb
import sys


def list_states(username, password, db_name, name_searched):
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
    sql = "SELECT * FROM states WHERE name LIKE '{0}' ORDER BY id ASC"
    cur.execute(sql.format(name_searched))
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:  # Ensuring there are three arguments
        list_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
