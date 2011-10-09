#!/usr/bin/python

"""Create an SQL file from the list of Unicode scripts

The script assumes the txt file to be ../UNIDATA/Scripts.txt. The
result will be written into ./scripts.sql"""

import re
import codecs
import sys

mapfile = open('../UNIDATA/PropertyValueAliases.txt', 'r')
sqlfile = codecs.open('scripts.sql', 'w', 'utf-8')
template = u"INSERT INTO scripts (iso, name) VALUES ('%s', '%s');\n"

sqlfile.write("""\
CREATE TABLE scripts
  iso  TEXT(4) Default 'Zzzz' PRIMARY KEY,
  name TEXT(24) DEFAULT 'Unknown',
);

""")

for line in mapfile.readlines():
    if line.startswith('sc ;'):
        fields = map(lambda s: s.strip(), line.split(';'))
        sqlfile.write(template % (fields[1], fields[2]))

mapfile.close()
sqlfile.close()

