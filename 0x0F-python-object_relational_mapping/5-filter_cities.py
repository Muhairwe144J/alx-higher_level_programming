#!/usr/bin/python3
import sys
import MySQLdb

def main():
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    try:
        conn = MySQLdb.connect(host='localhost', port=3306,
                               user=username, passwd=password, db=db_name)
        cursor = conn.cursor()

        # Execute the query to retrieve cities of the specified state
        cursor.execute("SELECT cities.id, cities.name FROM cities "
                       "JOIN states ON cities.state_id = states.id "
                       "WHERE states.name = %s "
                       "ORDER BY cities.id ASC", (state_name,))
        cities = cursor.fetchall()

        # Display the results
        city_names = ', '.join(city[1] for city in cities)
        print(city_names)

        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
