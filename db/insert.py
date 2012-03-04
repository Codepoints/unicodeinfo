#!/usr/bin/python

"""Read a large SQL file and apply it statement by statement

This seems faster than with the CLI sqlite3 client. Apart from that,
we can simply output a counter to tell us the advance."""

import os
import sqlite3
import sys

sqlfile = 'unicodeinfo.sql'
if len(sys.argv) > 1:
    sqlfile = sys.argv[1]
if not os.path.isfile(sqlfile):
    raise IOError("File not found")

conn = sqlite3.connect('ucd.sqlite')
cur = conn.cursor()

sql = open(sqlfile, 'r').read()
inserts = sql.split(";\n")
i = 0

for insert in inserts:
    cur.execute(insert+';')
    i += 1
    if i % 1000 == 0:
        print i

cur.close()
conn.close()

