#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
3 arguments: mysql username, mysql password and database name.
Should connect to a MySQL server running on localhost at port 3306.
Sorted in ascending order by cities.id
"""
import MySQLdb
import sys


def list_states(username, password, db_name, state_name):
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
    st_name = state_name
    query = "SELECT cities.name FROM cities "\
            "INNER JOIN states ON cities.state_id = states.id "\
            "WHERE states.name = %s ORDER BY cities.id"
    cur.execute(query, (state_name,))

    results = cur.fetchall()
    cities = ', '.join([row[0] for row in results])
    print(cities)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:  # Ensuring there are four arguments
        list_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
