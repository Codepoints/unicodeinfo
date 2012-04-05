#!/usr/bin/python

"""Create an SQL file for named character sequences

See <http://unicode.org/reports/tr34/> for details.
The result will be written into ./namedsequences.sql"""

import codecs

sqlfile = codecs.open('namedsequences.sql', 'w', 'utf-8')
template = u"INSERT INTO namedsequences (cp, name, `order`) VALUES (%s, '%s', %s);\n"

mapfile = open('../data/unicode/NamedSequences.txt', 'r')
for line in mapfile.readlines():
    if len(line) > 1 and not line.startswith('#'):
        fields = map(lambda s: s.strip(), line.split(';'))
        for order, xcp in enumerate(fields[1].split(' ')):
            sqlfile.write(template % (int(xcp, 16), fields[0], order))
mapfile.close()

sqlfile.close()

