#!/usr/bin/python3
# description of code
"""list states"""
import MySQLdb
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: script.py <username> <password> <database>")
        sys.exit(1)
    username, password, database = sys.argv[1:]
    conn = MySQLdb.connect(
        host="localhost", user=username, password=password, db=database
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states \
            ORDER BY id ASC")
    items = cur.fetchall()
    for item in items:
        print(item)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main(
)
