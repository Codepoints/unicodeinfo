

UNICODE_VERSION = 6.0.0
DB = db/ucd.sqlite

.PHONY: clean dist-clean sql db all

all: db

db: $(DB)

sql: db/unicodeinfo.full.sql

db/unicodeinfo.full.sql: db/ucd.all.flat.xml db/blocks.sql db/alias.sql db/propval.sql
	cat db/create.sql > db/unicodeinfo.full.sql
	(cd db; python db.py; cat unicodeinfo.sql >> unicodeinfo.full.sql)
	rm -f db/unicodeinfo.sql
	cat db/alias.sql >> db/unicodeinfo.full.sql
	cat db/blocks.sql >> db/unicodeinfo.full.sql
	cat db/propval.sql >> db/unicodeinfo.full.sql

$(DB): db/ucd.all.flat.xml db/blocks.sql db/alias.sql db/propval.sql
	-rm -f "$(DB)"
	cat db/create.sql | sqlite3 "$(DB)"
	(cd db; python db.py; python insert.py)
	rm -f db/unicodeinfo.sql
	cat db/alias.sql | sqlite3 "$(DB)"
	cat db/blocks.sql | sqlite3 "$(DB)"
	cat db/propval.sql | sqlite3 "$(DB)"

db/ucd.all.flat.xml:
	wget -O db/ucd.all.flat.zip http://www.unicode.org/Public/$(UNICODE_VERSION)/ucdxml/ucd.all.flat.zip
	cd db; unzip ucd.all.flat.zip
	rm -f db/ucd.all.flat.zip

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
	-rm -f db/ucd.all.flat.*

clean:
	-rm -f -r UNIDATA
	-rm -f db/unicodeinfo*.sql
	-rm -f db/blocks.sql
	-rm -f db/digraphs.sql
	-rm -f db/htmlentities.sql
	-rm -f db/alias.sql
	-rm -f db/propval.sql

db/blocks.sql: UNIDATA/Blocks.txt db/blocks.py
	cd db; python blocks.py

db/digraphs.sql:
	wget -q -O - http://www.rfc-editor.org/rfc/rfc1345.txt | \
	sed -n '/^ [^ ]\{1,6\} \+[0-9A-Fa-f]\{4\}    [^ ].*$$/p' | \
	sed 's/^ \([^ ]\{1,6\}\) \+\([0-9A-Fa-f]\{4\}\)    [^ ].*$$/\1\t\2/' > db/digraphs.tmp
	perl -p -e 's/^([^\t]+)\t([0-9a-f]{4})$$/"INSERT INTO alias (cp, name, `type`) VALUES (".hex("$$2").", '"'"'".join("'"''"'", split("'"'"'", $$1))."'"'"', '"'digraph'"');"/e' db/digraphs.tmp > db/digraphs.sql
	rm db/digraphs.tmp

db/htmlentities.sql:
	cd db; python htmlentities.py

db/alias.sql: db/htmlentities.sql db/digraphs.sql db/alias.py
	true > $@
	cat db/htmlentities.sql db/digraphs.sql > $@
	cd db; python alias.py

db/propval.sql: db/propval.py
	cd db; python propval.py

