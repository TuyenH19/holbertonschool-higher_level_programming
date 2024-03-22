#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
Write one that is safe from MySQL injections.
"""
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
    user_input = name_searched
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (user_input,))
    
    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:  # Ensuring there are three arguments
        list_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
