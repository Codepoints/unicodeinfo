#!/usr/bin/python

"""Create an SQL file from the list of Unicode scripts

The script assumes the txt file to be ../data/unicode/Scripts.txt. The
result will be written into ./scripts.sql"""

import codecs
import string

sqlfile = codecs.open('alias.sql', 'a', 'utf-8')
template = u"INSERT INTO codepoint_alias (cp, alias, `type`) VALUES (%s, '%s', '%s');\n"

mapfile = open('../data/unicode/NameAliases.txt', 'r')
for line in mapfile.readlines():
    if ";" in line and line[0] != "#":
        (cp, name, typ) = line.strip().split(";")
        sqlfile.write(template % (int(cp, 16), name.replace("'", "''"),
                                  typ))
mapfile.close()

def handle_buf(buffer, sqlfile, template):
    cp = int(buffer.split("\t")[0], 16)
    for line in buffer.split("\n"):
        if line.startswith("\t= "):
            buffer = ""
            aliases = []
            for chunk in line[3:].split(','):
                if buffer and ")" in chunk:
                    aliases.append(buffer+","+chunk)
                    buffer = ""
                elif buffer:
                    buffer += ',' + chunk
                elif "(" in chunk and ")" not in chunk:
                    buffer = chunk
                else:
                    aliases.append(chunk)
            if buffer:
                aliases.append(buffer)

            for alias in aliases:
                sqlfile.write(template % (cp, alias.strip().decode("ISO-8859-1").replace("'", "''"), 'alias'))
    return None

mapfile = open('../data/unicode/NamesList.txt', 'r')
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

