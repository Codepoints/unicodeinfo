#!/usr/bin/python
"""Fetch Wikipedia abstracts for each codepoint

TODO: Fetch abstracts for each Unicode block. Available blocks can be queried
here:

http://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:Unicode_blocks&format=json&cmlimit=500&cmprop=title&cmtype=page
"""


import codecs
import urllib
import urllib2
import json
import gzip
import sys
from StringIO import StringIO


headers = {
    'User-Agent': 'Unicodeinfo, https://github.com/Boldewyn/unicodeinfo'
}


def main():
    req = urllib2.Request('http://dumps.wikimedia.org/enwiki/'+
            'latest/enwiki-latest-all-titles-in-ns0.gz',
            headers=headers)
    zfile = StringIO(urllib2.urlopen(req).read())
    pfile = gzip.GzipFile(mode='rb', fileobj=zfile)
    del zfile
    content = pfile.read()
    del pfile
    letters = [x.decode('UTF-8') for x in content.splitlines() if len(x.decode('UTF-8')) == 1]
    del content

    sqlfile = codecs.open('wp.sql', 'w', 'utf-8')
    sqltpl = u"INSERT INTO codepoint_abstract ( cp, abstract ) VALUES ( %s , '%s' );\n"
    c = len(letters)

    print "start collecting Wikipedia abstracts"
    for i, letter in enumerate(letters):
        s = "%10s / %s" % (i, c)
        sys.stdout.write(s)
        sys.stdout.flush()
        req = urllib2.Request('http://en.wikipedia.org/w/api.php'+
                '?action=query&redirects&format=json&prop=extracts'+
                '&exintro&titles=%s' % urllib.quote(letter.encode("UTF-8")),
                headers=headers)
        req = urllib2.urlopen(req)
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


