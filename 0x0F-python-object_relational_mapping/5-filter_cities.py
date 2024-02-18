#!/usr/bin/python3
"""lists all cities from the database where state matches the input"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=argv[1], passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT cities.name FROM cities LEFT JOIN states ON \
                   cities.state_id = states.id WHERE states.name = %s \
                   ORDER BY cities.id", (argv[4],))
    print(", ".join(row[0] for row in cursor.fetchall()))
    cursor.close()
    connection.close()
