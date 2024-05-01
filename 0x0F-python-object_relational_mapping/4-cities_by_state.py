#!/usr/bin/python3
import sys
import MySQLdb

def main():
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        conn = MySQLdb.connect(host='localhost', port=3306,
                               user=username, passwd=password, db=db_name)
        cursor = conn.cursor()

        # Execute the query to retrieve cities
        cursor.execute("SELECT cities.id, cities.name, states.name FROM cities "
                       "JOIN states ON cities.state_id = states.id "
                       "ORDER BY cities.id ASC")
        cities = cursor.fetchall()

        # Display the results
        for city in cities:
            print(city)

        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
