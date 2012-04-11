#!/usr/bin/python


import codecs
import urllib
import urllib2
import json
import gzip
import sys
from StringIO import StringIO


def main():
    zfile = StringIO(urllib2.urlopen('http://dumps.wikimedia.org/enwiki/'+
                     'latest/enwiki-latest-all-titles-in-ns0.gz').read())
    pfile = gzip.GzipFile(mode='rb', fileobj=zfile)
    content = pfile.read()
    letters = [x.decode('UTF-8') for x in content.splitlines() if len(x.decode('UTF-8')) == 1]
    sqlfile = codecs.open('wp.sql', 'w', 'utf-8')
    sqltpl = u"INSERT INTO codepoint_abstract ( cp, abstract ) VALUES ( %s , '%s' );\n"
    c = len(letters)
    print "start collecting"
    for i, letter in enumerate(letters):
        s = "%10s / %s" % (i, c)
        sys.stdout.write(s)
        sys.stdout.flush()
        req = urllib2.urlopen('http://en.wikipedia.org/w/api.php'+
                    '?action=query&redirects&format=json&prop=extracts'+
                    '&exintro&titles=%s' % urllib.quote(letter.encode("UTF-8")))
        data = json.loads(req.read())
        if "query" in data:
            if "pages" in data["query"]:
                p = data["query"]["pages"]
                k = p.keys()[0]
                abstract = p[p.keys()[0]]["extract"]
                sqlfile.write(sqltpl % ( ord(letter),
                                         abstract.replace(u"'", u"''") ))
        sys.stdout.write(len(s) * '\b')
        sys.stdout.flush()


if __name__ == '__main__':
    main()


