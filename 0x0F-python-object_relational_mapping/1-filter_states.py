#!/usr/bin/python3
"""lists all states starting with N from the database"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=argv[1], passwd=argv[2], db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                    ORDER BY id")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connection.close()
