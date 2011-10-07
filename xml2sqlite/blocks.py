#!/usr/bin/python

"""Create an SQL file from the list of Unicode blocks

The script assumes the txt file to be ../UNIDATA/Blocks.txt. The
result will be written into ./blocks.sql"""

import re
import codecs
import sys

txtfile = open('../UNIDATA/Blocks.txt', 'r')
sqlfile = codecs.open('blocks.sql', 'w', 'utf-8')
template = u"INSERT INTO blocks (name, first, last, `type`) VALUES (%(values)s);\n"
pat = re.compile(r'^([0-9A-F]{4,6})\.\.([0-9A-F]{4,6}); (.+)\n$', re.I)

sqlfile.write("""\
CREATE TABLE blocks (
  name   TEXT(255) PRIMARY KEY,
  first  INTEGER(7),
  last   INTEGER(7),
  `type` TEXT(7)
);
CREATE INDEX cps ON blocks ( first, last );
CREATE INDEX `type` ON blocks ( `type` );

""")

for line in txtfile.readlines():
    if len(line) is 1 or line[0] is '#':
        continue
    m = re.search(pat, line)
    if m is not None:
        values = "'%s', %s, %s, 'block'" % (
            m.group(3).replace("'", "''"),
            int(m.group(1), 16),
            int(m.group(2), 16),
        )
        sqlfile.write(template % {'values': values})
    else:
        print "Unexpected line: \n%s" % line
        sys.exit()

sqlfile.write("""
INSERT INTO blocks (name, first, last, `type`) VALUES ('Basic Multilingual Plane', 0, 65535, 'plane');
INSERT INTO blocks (name, first, last, `type`) VALUES ('Supplementary Multilingual Plane', 65536, 131071, 'plane');
INSERT INTO blocks (name, first, last, `type`) VALUES ('Supplementary Ideographic Plane', 131072, 196607, 'plane');
INSERT INTO blocks (name, first, last, `type`) VALUES ('Tertiary Ideographic Plane', 196608, 262143, 'plane');
INSERT INTO blocks (name, first, last, `type`) VALUES ('Supplementary Special-purpose Plane', 917504, 983039, 'plane');
INSERT INTO blocks (name, first, last, `type`) VALUES ('Supplementary Private Use Area - A', 983040, 1048575, 'plane');
INSERT INTO blocks (name, first, last, `type`) VALUES ('Supplementary Private Use Area - B', 1048576, 1114111, 'plane');

INSERT INTO blocks (name, first, last, `type`) VALUES ('ASCII', 0, 127, 'special');
""")

txtfile.close()
sqlfile.close()

