#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('ucd.sqlite')
cur = conn.cursor()

sql = open('unicodeinfo.sql', 'r').read()
inserts = sql.split(";\n")
i = 0

for insert in inserts:
    cur.execute(insert+';')
    i += 1
    print i

cur.close()
conn.close()

