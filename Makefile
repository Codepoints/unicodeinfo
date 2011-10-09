

UNICODE_VERSION = 6.0.0
DB = xml2sqlite/ucd.sqlite

.PHONY: clean dist-clean sql db all

all: db

db: $(DB)

sql: xml2sqlite/unicodeinfo.full.sql

xml2sqlite/unicodeinfo.full.sql: xml2sqlite/ucd.all.flat.xml xml2sqlite/blocks.sql xml2sqlite/scripts.sql
	cat xml2sqlite/create.sql > xml2sqlite/unicodeinfo.full.sql
	(cd xml2sqlite; python db.py; cat unicodeinfo.sql >> unicodeinfo.full.sql)
	rm -f xml2sqlite/unicodeinfo.sql
	cat xml2sqlite/alias.sql >> xml2sqlite/unicodeinfo.full.sql
	cat xml2sqlite/blocks.sql >> xml2sqlite/unicodeinfo.full.sql
	cat xml2sqlite/scripts.sql >> xml2sqlite/unicodeinfo.full.sql

$(DB): xml2sqlite/ucd.all.flat.xml xml2sqlite/blocks.sql xml2sqlite/scripts.sql
	-rm -f "$(DB)"
	cat xml2sqlite/create.sql | sqlite3 "$(DB)"
	(cd xml2sqlite; python db.py; python insert.py)
	rm -f xml2sqlite/unicodeinfo.sql
	cat xml2sqlite/alias.sql | sqlite3 "$(DB)"
	cat xml2sqlite/blocks.sql | sqlite3 "$(DB)"
	cat xml2sqlite/scripts.sql | sqlite3 "$(DB)"

xml2sqlite/blocks.sql: UNIDATA/Blocks.txt xml2sqlite/blocks.py
	cd xml2sqlite; python blocks.py

xml2sqlite/scripts.sql: UNIDATA/Scripts.txt UNIDATA/PropertyValueAliases.txt xml2sqlite/scripts.py
	cd xml2sqlite; python scripts.py

xml2sqlite/ucd.all.flat.xml:
	wget -O xml2sqlite/ucd.all.flat.zip http://www.unicode.org/Public/$(UNICODE_VERSION)/ucdxml/ucd.all.flat.zip
	cd xml2sqlite; unzip ucd.all.flat.zip
	rm -f xml2sqlite/ucd.all.flat.zip

UNIDATA/Blocks.txt: UNIDATA/ReadMe.txt
UNIDATA/Scripts.txt: UNIDATA/ReadMe.txt
UNIDATA/PropertyValueAliases.txt: UNIDATA/ReadMe.txt

UNIDATA/ReadMe.txt:
	mkdir UNIDATA
	wget -O UNIDATA/UCD.zip http://www.unicode.org/Public/$(UNICODE_VERSION)/ucd/UCD.zip
	cd UNIDATA; unzip -o UCD.zip
	rm -f UNIDATA/UCD.zip

dist-clean: clean
	-rm -f "$(DB)"
	-rm -f xml2sqlite/ucd.all.flat.*

clean:
	-rm -f -r UNIDATA
	-rm -f xml2sqlite/unicodeinfo*.sql
	-rm -f xml2sqlite/blocks.sql
	-rm -f xml2sqlite/scripts.sql
	-rm -f xml2sqlite/digraphs.sql
	-rm -f xml2sqlite/htmlentities.sql
	-rm -f xml2sqlite/alias.sql

xml2sqlite/digraphs.sql:
	wget -q -O - http://www.rfc-editor.org/rfc/rfc1345.txt | \
	sed -n '/^ [^ ]\{1,6\} \+[0-9A-Fa-f]\{4\}    [^ ].*$$/p' | \
	sed 's/^ \([^ ]\{1,6\}\) \+\([0-9A-Fa-f]\{4\}\)    [^ ].*$$/\1\t\2/' > xml2sqlite/digraphs.tmp
	perl -p -e 's/^([^\t]+)\t([0-9a-f]{4})$$/"INSERT INTO alias (cp, name, `type`) VALUES (".hex("$$2").", '"'"'".join("'"''"'", split("'"'"'", $$1))."'"'"', '"'digraph'"');"/e' xml2sqlite/digraphs.tmp > xml2sqlite/digraphs.sql
	rm xml2sqlite/digraphs.tmp

xml2sqlite/htmlentities.sql:
	cd xml2sqlite; python htmlentities.py

xml2sqlite/alias.sql: xml2sqlite/htmlentities.sql xml2sqlite/digraphs.sql
	true > $@
	cat $^ > $@

