#!/usr/bin/python3
"""lists all cities from the database"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=argv[1], passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                   LEFT JOIN states ON cities.state_id = states.id ORDER BY \
                   cities.id")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connection.close()
