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

        # Execute the query to retrieve states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
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
