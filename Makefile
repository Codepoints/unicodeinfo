

UNICODE_VERSION = 6.0.0
DB = xml2sqlite/ucd.sqlite

.PHONY: clean dist-clean sql db all

all: db

db: $(DB)

sql: xml2sqlite/unicodeinfo.full.sql

xml2sqlite/unicodeinfo.full.sql: xml2sqlite/ucd.all.flat.xml
	cat xml2sqlite/create.sql > xml2sqlite/unicodeinfo.full.sql
	(cd xml2sqlite; python db.py; cat unicodeinfo.sql >> unicodeinfo.full.sql)
	rm -f xml2sqlite/unicodeinfo.sql
	cat xml2sqlite/digraphs.sql >> xml2sqlite/unicodeinfo.full.sql
	cat xml2sqlite/htmlentity.sql >> xml2sqlite/unicodeinfo.full.sql
	cat xml2sqlite/blocks.sql >> xml2sqlite/unicodeinfo.full.sql

$(DB): xml2sqlite/ucd.all.flat.xml
	cat xml2sqlite/create.sql | sqlite3 "$(DB)"
	(cd xml2sqlite; python db.py; python insert.py)
	rm -f xml2sqlite/unicodeinfo.sql
	cat xml2sqlite/digraphs.sql | sqlite3 "$(DB)"
	cat xml2sqlite/htmlentity.sql | sqlite3 "$(DB)"
	cat xml2sqlite/blocks.sql | sqlite3 "$(DB)"

xml2sqlite/ucd.all.flat.xml:
	wget -O xml2sqlite/ucd.all.flat.zip http://www.unicode.org/Public/$(UNICODE_VERSION)/ucdxml/ucd.all.flat.zip
	cd xml2sqlite; unzip ucd.all.flat.zip
	rm -f xml2sqlite/ucd.all.flat.zip

UNIDATA:
	mkdir UNIDATA
	wget -O UNIDATA/UCD.zip http://www.unicode.org/Public/$(UNICODE_VERSION)/ucd/UCD.zip
	cd UNIDATA; unzip -o UCD.zip
	rm -f UNIDATA/UCD.zip

dist-clean: clean
	-rm "$(DB)"
	-rm xml2sqlite/ucd.all.flat.*

clean:
	-rm -r UNIDATA
	-rm xml2sqlite/unicodeinfo*.sql

