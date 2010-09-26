"""Methods for representing Unicode data."""


try:
    from PIL import Image
except ImportError:
    Image = None
try:
    from io import BytesIO
except ImportError:
    from cStringIO import StringIO as BytesIO
try:
    from urllib.request import urlopen
    from urllib.error import URLError, HTTPError
except ImportError:
    from urllib2 import urlopen, URLError, HTTPError
import random
import re
from bisect import bisect
from . import info


def render(cp):
    '''Show an ascii art representation of a codepoint

    Based on ASCII Art maker from Steven Kay. Uses
    images from http://unicode.org.
    '''
    if Image is None:
        return '(cannot generate, PIL missing)'
    # greyscale.. the following strings represent
    # 7 tonal ranges, from lighter to darker.
    # for a given pixel tonal level, choose a character
    # at random from that range.
    greyscale = [
                " ",
                " ",
                ".,-",
                "_ivc=!/|\\~",
                "gjez2]/(YL)t[+T7Vf",
                "mdK4ZGbNDXY5P*Q",
                "W8KMA",
                "#%$"
                ]

    # using the bisect class to put luminosity values
    # in various ranges.
    # these are the luminosity cut-off points for each
    # of the 7 tonal levels. At the moment, these are 7 bands
    # of even width, but they could be changed to boost
    # contrast or change gamma, for example.
    zonebounds=[36,72,108,144,180,216,252]

    # open image and resize
    # experiment with aspect ratios according to font
    # baseurl = 'http://decodeunicode.org/data/glyph/26x26/%s.gif'
    baseurl = 'http://www.unicode.org/cgi-bin/refglyph?24-%s'
    if cp < 0x10000:
        url = baseurl % ('%04X' % cp)
    elif cp < 0x100000:
        url = baseurl % ('%05X' % cp)
    else:
        url = baseurl % ('%06X' % cp)
    try:
        src = BytesIO(urlopen(url).read())
    except URLError:
        return "Cannot load representation from %s" % url
    except HTTPError:
        return "Representation does not exist: %s" % url
    else:
        im = Image.open(src)
        im = im.convert("L") # convert to mono

        str = []
        for y in range(0,im.size[1]):
            line = ""
            for x in range(0,im.size[0]):
                lum = 255-im.getpixel((x,y))
                row = bisect(zonebounds,lum)
                possibles = greyscale[row]
                line = line + possibles[random.randint(0,len(possibles)-1)]
            if len(line.replace(" ", "")) or len(str):
                str.append(line)
        while not str[-1].replace(" ", ""):
            str = str[:-1]
        str.append("Source: %s" % url)
        return '\n'.join(str)


def get_legend():
    """Create a sufficiently formated legend string from the list info.legend"""
    lgnd = u""
    for c in info.legend:
        lgnd += c[0] + u':\n'
        ilen = max([ len(x) for x in dict(c[1]).keys() ]) + 2
        for item in c[1]:
            lgnd += u'- ' + u'\t'.join(item) + u'\n'
        lgnd += u'\n'
    return lgnd


