#!/usr/bin/python

"""Create an SQL file from the list of Unicode scripts

The script assumes the txt file to be ../UNIDATA/Scripts.txt. The
result will be written into ./scripts.sql"""

import re
import codecs
import sys
import string

sqlfile = codecs.open('alias.sql', 'a', 'utf-8')
template = u"INSERT INTO alias (cp, name, `type`) VALUES (%s, '%s', '%s');\n"

mapfile = open('../UNIDATA/NameAliases.txt', 'r')
for line in mapfile.readlines():
    if ";" in line and line[0] != "#":
        (cp, name) = line.strip().split(";")
        sqlfile.write(template % (int(cp, 16), name.replace("'", "''"), 'unicode'))
mapfile.close()

def handle_buf(buffer, sqlfile, template):
    cp = int(buffer.split("\t")[0], 16)
    for line in buffer.split("\n"):
        if line.startswith("\t= "):
            for alias in line[3:].split(','):
                sqlfile.write(template % (cp, alias.strip().decode("ISO-8859-1").replace("'", "''"), 'alias'))
    return None

mapfile = open('../UNIDATA/NamesList.txt', 'r')
buffer = ""
for line in mapfile.readlines():
    if line[0] in string.hexdigits:
        if buffer != "":
            handle_buf(buffer, sqlfile, template)
        buffer = line
    elif line[0] == "\t" and buffer != "":
        buffer += line
mapfile.close()

sqlfile.close()

