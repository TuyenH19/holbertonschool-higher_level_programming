#!/usr/bin/python3
"""
A Python script that lists all states from the database hbtn_0e_0_usa.
This script takes three arguments: mysql username, mysql password, and database name.
The script uses the MySQLdb module to connect to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id.
"""

import MySQLdb
import sys

def connect(username, password, db_name):
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )
    cur = db.cursor()
    return cur
    
def list_states(username, password, db_name):
    """
    Connects to a MySQL database and lists all states from the database.
    """
    cur = connect(username, password, db_name)
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:  # Ensuring there are three arguments
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
