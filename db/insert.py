#!/usr/bin/python

"""Read a large SQL file and apply it statement by statement

This seems faster than with the CLI sqlite3 client. Apart from that,
we can simply output a counter to tell us the advance."""

import os
import sqlite3
import sys

if len(sys.argv) != 3:
    raise ValueError("Need exactly two args")
sqlfile = sys.argv[1]
db = sys.argv[2]
if not os.path.isfile(sqlfile):
    raise IOError("SQL file not found")
if not os.path.isfile(db):
    raise IOError("Database not found")

conn = sqlite3.connect(db)
cur = conn.cursor()

sql = open(sqlfile, 'r').read()
inserts = sql.split(";\n")

for i, insert in enumerate(inserts):
    cur.execute(insert+';')
    if i > 0 and i % 1000 == 0:
        print i

cur.close()
conn.close()
