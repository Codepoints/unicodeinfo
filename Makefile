

DB = xml2sqlite/ucd.sqlite

.PHONY: clean dist-clean

all: db

db: $(DB)

$(DB): xml2sqlite/ucd.all.flat.xml
	cat xml2sqlite/create.sql | sqlite3 "$(DB)"
	(cd xml2sqlite; python db.py; python insert.py)
	rm -f xml2sqlite/unicodeinfo.sql
	cat xml2sqlite/digraphs.sql | sqlite3 "$(DB)"
	cat xml2sqlite/htmlentity.sql | sqlite3 "$(DB)"
	cat xml2sqlite/blocks.sql | sqlite3 "$(DB)"

xml2sqlite/ucd.all.flat.xml:
	wget -O xml2sqlite/ucd.all.flat.zip http://www.unicode.org/Public/5.2.0/ucdxml/ucd.all.flat.zip
	(cd xml2sqlite; unzip ucd.all.flat.zip)
	rm -f xml2sqlite/ucd.all.flat.zip

dist-clean: clean
	-rm -f "$(DB)"
	-rm -f xml2sqlite/ucd.all.flat.*

clean:
	-rm -f xml2sqlite/unicodeinfo.sql

