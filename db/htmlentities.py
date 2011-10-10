#!/usr/bin/python

"""Create an SQL file from the list of HTML entities

The result will be written into ./htmlentities.sql"""

from htmlentitydefs import entitydefs
import codecs

sqlfile = codecs.open('htmlentities.sql', 'w', 'utf-8')
template = u"INSERT INTO alias (cp, name, `type`) VALUES (%s, '%s', 'html');\n"

for k, v in entitydefs.iteritems():
    k = unicode(k)
    v = v.decode("ISO-8859-1")
    if v[0:2] == '&#':
        v = int(v[2:-1])
    elif len(v) == 1:
        v = ord(v)
    else:
        raise ValueError(v)
    sqlfile.write(template % (v, k))

sqlfile.close()

