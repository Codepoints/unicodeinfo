"""Parsing methods related to Unicode

This module provides methods for parsing string representations
of Unicode characters and ranges.
"""


import re
import sys
from unicodedata import lookup
from . import codepoint


def parse_range(a, base=None, encoding=None):
    """Find a range of Unicode codepoints

    Parameter a may be either a list of or a single string. The
    method then searches for ',' in the input, splits at occurences
    and tries to evaluate the results as codepoint ranges.

    Codepoint ranges are assumed to be separated by one of '..', '-'
    or ':'.

    The base and encoding parameters are handed down to parse() to
    decide which base and encoding the notations are evaluated against.

    Examples:
    >>> parse_range('U+AA..U+AF , A5 , b1-b4')
    [165, 170, 171, 172, 173, 174, 175, 177, 178, 179, 180]
    >>> parse_range(('AA', 'AB'))
    [170, 171]
    >>> parse_range(('AA..AC..AB'))
    [170, 171, 172]
    >>> parse_range('LATIN CAPITAL LETTER B..67', 10)
    [66, 67]
    >>> parse_range(u'\u00c4')
    [196]
    """
    rng = []
    if isinstance(a, basestring):
        a = [a]
    for b in a:
        b = b.strip()
        for d in re.split(r'\s*,\s*', b.strip()):
            # try to split on common delimiters:
            f = [ parse(cp, base) for cp in re.split(r'\s*(?:-|\.\.|:)\s*', d) ]
            if len(f) > 1:
                f.sort()
                rng += list(range(f[0], f[-1] + 1))
            else:
                rng += f
    rng = list(set(rng))
    rng.sort()
    return rng


def parse(a, base=None, encoding=None):
    """Find the codepoint of a notation or character

    The 'base' parameter decides against which base the input is evaluated.
    Currently, 'parse' recognizes these notations (case insensitive):

    * U+1234
    * \U1234
    * 0x1234
    * 0o1234
    * &#x1234;
    * &#1234;
    * 1234
    * a single character
    * or a full Unicode name

    The 'encoding' parameter decides, which encoding to use for converting
    str input to unicode. It defaults to sys.stdin.encoding.

    Examples:
    >>> parse('U+AB', 16)
    171
    >>> parse('&#123;')
    123
    >>> parse(14)
    14
    >>> parse('14', 10)
    14
    >>> parse('A')
    10
    >>> parse(u'\u00c4')
    196
    >>> parse('0x0010', 10)
    16
    >>> parse('0o0010', 10)
    8
    >>> parse('LATIN CAPITAL LETTER A')
    65
    """
    if isinstance(a, int) or isinstance(a, codepoint.Codepoint):
        # it already seems to be a codepoint
        return a
    elif isinstance(a, str):
        a = unicode(a, encoding or sys.stdin.encoding)
    else:
        a = unicode(a)
    if base == 16 or base is None:
        n = '[0-9A-F]'
        base = 16
    elif base == 10:
        n = '[0-9]'
    elif base == 8:
        n = '[0-7]'

    if re.match(r'(U\+|\\U)'+n+'+$', a, re.I): # U+0010 / \u0010
        return int(a[2:], base)
    elif re.match(r'U'+n+'+$', a, re.I):       # U0010
        return int(a[1:], base)
    elif re.match(r'0x[0-9A-F]+$', a, re.I):   # 0x000F
        return int(a[2:], 16)
    elif re.match(r'0o[0-7]+$', a, re.I):      # 0o0007
        return int(a[2:], 8)
    elif re.match(r'&#x[0-9A-F]+;$', a, re.I): # &#x000F;
        return int(a[3:-1], 16)
    elif re.match(r'&#[0-9]+;$', a, re.I):     # &#0009;
        return int(a[2:-1], 10)
    elif re.match(n+'+$', a, re.I):            # 10
        return int(a, base)
    elif len(a) == 1:                          # x
        return ord(a)
    else:
        try:
            r = lookup(a)
        except KeyError:
            raise ValueError("Unsupported notation: %s" % a)
        else:                                  # "LATIN CAPITAL LETTER X"
            return ord(r)


