#!/usr/bin/python

"""Create an SQL file from the list of Unicode blocks

The script assumes the txt file to be ../data/unicode/Blocks.txt. The
result will be written into ./blocks.sql"""

import re
import codecs
import sys

txtfile = open('../data/unicode/Blocks.txt', 'r')
sqlfile = codecs.open('blocks.sql', 'w', 'utf-8')
template = u"INSERT INTO blocks (name, first, last) VALUES (%(values)s);\n"
pat = re.compile(r'^([0-9A-F]{4,6})\.\.([0-9A-F]{4,6}); (.+)\n$', re.I)

for line in txtfile.readlines():
    if len(line) is 1 or line[0] is '#':
        continue
    m = re.search(pat, line)
    if m is not None:
        values = "'%s', %s, %s" % (
            m.group(3).replace("'", "''"),
            int(m.group(1), 16),
            int(m.group(2), 16),
        )
        sqlfile.write(template % {'values': values})
    else:
        print "Unexpected line: \n%s" % line
        sys.exit()

txtfile.close()
sqlfile.close()
