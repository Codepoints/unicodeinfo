#!/usr/bin/python

"""Create an SQL file from the list of HTML entities

The result will be written into ./htmlentities.sql"""

import json

sqlfile = open('htmlentities.sql', 'w')
with open('../data/htmlentities.json') as _json:
    source = json.load(_json)
template = u"INSERT INTO codepoint_alias (cp, alias, `type`) VALUES (%s, '%s', 'html');\n"

for k, v in source.iteritems():
    if len(v['codepoints']) == 1 and k[-1] == ';':
        sqlfile.write(template % (v['codepoints'][0], k[1:-1]))

sqlfile.close()
