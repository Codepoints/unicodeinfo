#!/usr/bin/python
"""Fetch Wikipedia abstracts for each codepoint and Unicode block"""


import codecs
import gzip
import json
import logging
import os
import signal
import sys
import urllib
import urllib2
from   cStringIO import StringIO


logger = logging.getLogger('unicodeinfo.wp')


LANG = 'en'


HEADERS = {
    'User-Agent': 'Unicodeinfo, https://github.com/Boldewyn/unicodeinfo',
    'Accept-Language': LANG
}


CACHE_FILE = 'wp.sql.cache'


TARGET = 'wp.sql'


SQL_TPL = u"INSERT INTO codepoint_abstract ( cp, abstract, lang ) VALUES ( %s, '%s', '%s' );\n"


SQL_BLOCK_TPL = u"INSERT INTO block_abstract ( block, abstract, lang ) VALUES ( '%s', '%s', '%s' );\n"


def main():
    letters = fetch_cache()
    c = len(letters)

    if c:
        logger.info("fetched %s letters from cache" % c)
    else:
        logger.info("no letters fetched from cache. Download dump.")
        letters = fetch_single_letter_articles()
        logger.info("Downloading dump complete")
        c = len(letters)

    sqlfile = codecs.open(TARGET, 'a', 'utf-8')

    logger.info("start collecting Wikipedia abstracts")
    done = False
    i = 0
    try:
        while True:
            try:
                letter = letters.pop(0)
            except IndexError:
                break
            else:
                i += 1

            done = False
            ord_letter = ord(letter)
            if 0xE000 <= ord_letter <= 0xF8FF or \
               0xF0000 <= ord_letter <= 0x10FFFF:
                # private use areas. Skip.
                continue

            s = "%10s / %s" % (i, c)
            sys.stdout.write(s)
            sys.stdout.flush()

            extract = fetch_extract(letter)
            if extract:
                sqlfile.write(SQL_TPL % ( ord_letter,
                                          extract.replace(u"'", u"''"),
                                          LANG))
                done = True

            sys.stdout.write(len(s) * '\b')
            sys.stdout.flush()

    except (KeyboardInterrupt, SystemExit):
        if not done and letter:
            letters.insert(0, letter)
        with codecs.open(CACHE_FILE, 'wb', 'utf-8') as cache:
            cache.write('\n'.join([l.encode('UTF-8') for l in letters]))
        raise

    logger.info("start collecting Unicode block abstracts")
    abstracts = fetch_block_abstracts()
    try:
        with codecs.open(TARGET, 'a', 'utf-8') as sqlfile:
            sqlfile.write(abstracts)
    except (KeyboardInterrupt, SystemExit):
        # here we cannot need the interrupt. Cancel it.
        pass
    logger.info("finished.")


def fetch_cache():
    """fetch unprocessed letters from cache"""
    letters = []

    if os.path.isfile(CACHE_FILE):
        with codecs.open(CACHE_FILE, encoding="UTF-8") as cache:
            for line in cache.readlines():
                letters.append(line.decode('UTF-8').rstrip())
        os.unlink(CACHE_FILE)

    return letters


def fetch_single_letter_articles():
    """fetch from wikipedia the list of all single letter articles"""
    req = urllib2.Request('http://dumps.wikimedia.org/enwiki/'+
            'latest/enwiki-latest-all-titles-in-ns0.gz',
            headers=HEADERS)
    zfile = StringIO(urllib2.urlopen(req).read())
    pfile = gzip.GzipFile(mode='rb', fileobj=zfile)
    content = pfile.read()
    letters = [x.decode('UTF-8') for x in content.splitlines() if len(x.decode('UTF-8')) == 1]

    return letters


def fetch_block_abstracts():
    """fetch the abstracts of all Unicode blocks"""
    req = urllib2.Request('http://en.wikipedia.org/w/api.php' +
            '?action=query&list=categorymembers' +
            '&cmtitle=Category:Unicode_blocks' +
            '&format=json&cmlimit=500&cmprop=title&cmtype=page',
            headers=HEADERS)
    data = json.loads(urllib2.urlopen(req).read())

    abstracts = u""

    for article in data.get("query", {}).get("categorymembers", []):
        wp_title = article["title"]
        if wp_title == "Unicode block":
            continue
        uc_title = wp_title.replace(' (Unicode block)', '')

        extract = fetch_extract(wp_title)
        if extract:
            abstracts += SQL_BLOCK_TPL % ( uc_title.replace(u"'", u"''"),
                                           extract.replace(u"'", u"''"),
                                           LANG)

    return abstracts


def fetch_extract(wikipedia_title):
    """fetch HTML extract of a Wikipedia article"""
    logger.debug("Download extract %s" % wikipedia_title)
    req = urllib2.Request('http://en.wikipedia.org/w/api.php'+
            '?action=query&redirects&format=json&prop=extracts'+
            '&exintro&titles=%s' % urllib.quote(wikipedia_title.encode("UTF-8")),
            headers=HEADERS)

    data = json.loads(urllib2.urlopen(req).read())
    extract = None

    if "pages" in data.get("query", {}):
        p = data["query"]["pages"]
        if "extract" not in p[p.keys()[0]]:
            logger.warning('No extract found for %s!' % wikipedia_title)
            return None
        extract = p[p.keys()[0]]["extract"]

    return extract


if __name__ == '__main__':
    def raiser(signal, frame):
        sys.stderr.write('Received signal for shutdown. Cleaning up...')
        raise KeyboardInterrupt
        sys.exit(0)
    signal.signal(signal.SIGINT, raiser)

    _handler = logging.StreamHandler()
    _handler.setFormatter(logging.Formatter(
        "[%(levelname)s] %(message)s"))
    logger.addHandler(_handler)
    logger.setLevel(logging.INFO)

    main()


