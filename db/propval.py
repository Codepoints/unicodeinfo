#!/usr/bin/python

"""Create an SQL file from the list of Unicode scripts

The script assumes the txt file to be ../UNIDATA/Scripts.txt. The
result will be written into ./scripts.sql"""

import codecs

mapfile = open('../UNIDATA/PropertyValueAliases.txt', 'r')
sqlfile = codecs.open('propval.sql', 'w', 'utf-8')
template = u"INSERT INTO propval (prop, abbr, name) VALUES ('%s', '%s', '%s');\n"

sqlfile.write("""\
CREATE TABLE propval (
  prop TEXT(12),
  abbr TEXT(255),
  name TEXT(255)
);

""")

for line in mapfile.readlines():
    if len(line) > 1 and not line.startswith('#'):
        fields = map(lambda s: s.strip(), line.split(';'))
        for name in fields[2:]:
            abbr = fields[1]
            if abbr == "n/a":
                abbr = name
            sqlfile.write(template % (fields[0], abbr, name))

mapfile.close()
sqlfile.close()

