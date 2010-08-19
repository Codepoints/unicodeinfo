

DB = "xml2sqlite/ucd.sqlite"

.PHONY: all

all: db

db: xml2sqlite/ucd.sqlite

xml2sqlite/ucd.sqlite: xml2sqlite/ucd.all.flat.xml
	cat xml2sqlite/create.sql | sqlite3 $(DB)
	(cd xml2sqlite; python db.py; python insert.py)
	rm -f xml2sqlite/unicodeinfo.sql
	cat xml2sqlite/digraph.sql | sqlite3 $(DB)
	cat xml2sqlite/htmlentity.sql | sqlite3 $(DB)



