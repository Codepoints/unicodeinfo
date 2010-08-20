#!/usr/bin/python

"""Read a large SQL file and apply it statement by statement

This seems faster than with the CLI sqlite3 client. Apart from that,
we can simply output a counter to tell us the advance."""

import sqlite3

conn = sqlite3.connect('ucd.sqlite')
cur = conn.cursor()

sql = open('unicodeinfo.sql', 'r').read()
inserts = sql.split(";\n")
i = 0

for insert in inserts:
    cur.execute(insert+';')
    i += 1
    if i % 1000 == 0:
        print i

cur.close()
conn.close()

