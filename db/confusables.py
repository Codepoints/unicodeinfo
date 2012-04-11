#!/usr/bin/python

"""Create an SQL file from the confusables of TR 39"""

import codecs

sqlfile = codecs.open('confusables.sql', 'w', 'utf-8')
template = u"INSERT INTO codepoint_confusables (id, cp, other, `type`, `order`) VALUES (%s, %s, %s, '%s', %s);\n"

with codecs.open('../data/confusables.txt', 'r', 'utf-8') as mapfile:
    next(mapfile) # skip first line 'cause of BOM
    for count, line in enumerate(mapfile):
        line = line.split("#")[0].strip()
        if len(line):
            fields = map(lambda s: s.strip(), line.split(';'))
            for i, other in enumerate(fields[1].split(' ')):
                sqlfile.write(template % (count, int(fields[0], 16),
                                          int(other, 16), fields[2], i))

sqlfile.close()

