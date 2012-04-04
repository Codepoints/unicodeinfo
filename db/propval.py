#!/usr/bin/python

"""Create an SQL file from the list of Unicode scripts

The script assumes the txt file to be ../data/unicode/Scripts.txt. The
result will be written into ./scripts.sql"""

import codecs

sqlfile = codecs.open('propval.sql', 'w', 'utf-8')
template = u"INSERT INTO propval (prop, abbr, name) VALUES ('%s', '%s', '%s');\n"

mapfile = open('../data/unicode/PropertyValueAliases.txt', 'r')
for line in mapfile.readlines():
    if len(line) > 1 and not line.startswith('#'):
        fields = map(lambda s: s.strip(), line.split(';'))
        for name in fields[2:]:
            abbr = fields[1]
            if abbr == "n/a":
                abbr = name
            sqlfile.write(template % (fields[0], abbr, name))
mapfile.close()

mapfile = open('../data/unicode/PropertyAliases.txt', 'r')
for line in mapfile.readlines():
    if len(line) > 1 and not line.startswith('#'):
        fields = map(lambda s: s.strip(), line.split(';'))
        if len(fields) > 1:
            sqlfile.write(template % ('prop', fields[0], fields[1]))
mapfile.close()

sqlfile.close()

