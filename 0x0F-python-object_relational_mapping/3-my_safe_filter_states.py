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

        # Execute the query to retrieve states (safe from SQL injection)
        cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
