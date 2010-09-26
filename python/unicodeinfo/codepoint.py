"""Get information about single Unicode codepoints"""


import unicodedata as ud
from struct import unpack
from . import info
from . import representation


def get_block(cp, default=None):
    """Get the block name of a codepoint"""
    for b in info.blocks:
        if cp >= b[0] and cp <= b[1]:
            return b[2]
    return default


def get_plane(cp, default=None, abbreviation=False):
    """Get the plane name of a codepoint"""
    for p in info.planes:
        if cp >= p[0] and cp <= p[1]:
            return p[2+abbreviation]
    return default


def get_encoding(cp, encoding="utf-8"):
    """Get the representation of a codepoint in a specific encoding"""
    c = str(unichr(cp).encode(encoding))
    return unpack(len(c)*'B', c)


def get_digraph(cp, default=None):
    """Get the RFC 1345 digraph (if any) for a codepoint"""
    if cp < 0xfefd: # that's the highest defined digraph + 1
        return dict(info.digraphs).get(cp, default)
    return default


def get_information(cp, filter=None):
    """Get all (or some) informations about a specific codepoint"""
    i = []
    c = Codepoint(cp)
    if filter is None:
        filter = Codepoint.properties
    for f in filter:
        i.append((f, getattr(c, f)))
    return i


def is_valid_XML(cp):
    """Check, if the codepoint is allowed in XML"""
    c = int(cp) # allow Codepoint, too
    if c == 0x9 or c == 0xA or c == 0xD or\
       (c >=    0x20 and c <=   0xD7FF) or\
       (c >=  0xE000 and c <=   0xFFFD) or\
       (c >= 0x10000 and c <= 0x10FFFF):
        return True
    return False


def lookup(name):
    """Get a codepoint by its Unicode name"""
    try:
        cp = ud.lookup(name)
    except KeyError:
        return None
    else:
        return Codepoint(ord(cp))


# see http://code.activestate.com/recipes/363602/
class LazyProperty(object):
    def __init__(self, calculate_function):
        self._calculate = calculate_function

    def __get__(self, obj, owner=None):
        if obj is None:
            return self
        value = self._calculate(obj)
        setattr(obj, self._calculate.__name__, value)
        return value


class Codepoint(object):
    """A Unicode codepoint"""

    # we need this explicit list, because self.__dict__ is empty
    # at the beginning
    properties = (
        'block', 'digraph', 'utf8', 'char', 'printable_char', 'name',
        'category', 'combining', 'decomposition', 'bidirectional',
        'mirrored', 'decimal', 'digit', 'numeric', 'east_asian_width',
        'representation', 'HTML_entity', 'codepoint', 'plane',
        'title', 'upper', 'lower', 'notation',
    )

    def __init__(self, cp):
        if not isinstance(cp, int):
            raise AttributeError("The given codepoint is not an integer.")
        self.codepoint = cp

    @LazyProperty
    def block(self):
        return get_block(self.codepoint)

    @LazyProperty
    def plane(self):
        return get_plane(self.codepoint)

    @LazyProperty
    def digraph(self):
        return get_digraph(self.codepoint)

    @LazyProperty
    def utf8(self):
        return get_encoding(self.codepoint, 'utf-8')

    @LazyProperty
    def char(self):
        return unichr(self.codepoint)

    @LazyProperty
    def printable_char(self):
        if self.category[0] == "C":
            return ""
        else:
            return self.char

    @LazyProperty
    def name(self):
        return ud.name(self.char, '')

    @LazyProperty
    def category(self):
        return ud.category(self.char)

    @LazyProperty
    def combining(self):
        return ud.combining(self.char)

    @LazyProperty
    def decomposition(self):
        return ud.decomposition(self.char)

    @LazyProperty
    def bidirectional(self):
        return ud.bidirectional(self.char)

    @LazyProperty
    def mirrored(self):
        return ud.mirrored(self.char)

    @LazyProperty
    def decimal(self, default=None):
        return ud.decimal(self.char, default)

    @LazyProperty
    def digit(self, default=None):
        return ud.digit(self.char, default)

    @LazyProperty
    def numeric(self, default=None):
        return ud.numeric(self.char, default)

    @LazyProperty
    def east_asian_width(self):
        return ud.east_asian_width(self.char)

    @LazyProperty
    def representation(self):
        return representation.render(self.codepoint)

    @LazyProperty
    def HTML_entity(self):
        if self.codepoint in dict(info.HTML_entities):
            return '&%s;' % dict(info.HTML_entities)[self.codepoint]
        elif is_valid_XML(self.codepoint):
            return '&#x%X;' % self.codepoint
        return ""

    def has_HTML_entity(self):
        return self.codepoint in dict(info.HTML_entities)

    def normalize(self, form="NFD"):
        return ud.normalize(form, self.char)

    @LazyProperty
    def title(self):
        l = self.char.title()
        if l != self.char:
            return Codepoint(ord(l))
        else:
            return self

    @LazyProperty
    def upper(self):
        l = self.char.upper()
        if l != self.char:
            return Codepoint(ord(l))
        else:
            return self

    @LazyProperty
    def lower(self):
        l = self.char.lower()
        if l != self.char:
            return Codepoint(ord(l))
        else:
            return self

    def __cmp__(self, other):
        return cmp(self.codepoint, other.codepoint)

    @LazyProperty
    def notation(self):
        if self.codepoint < 0x10000:
            return 'U+%04X' % self.codepoint
        else:
            return 'U+%06X' % self.codepoint
    __str__ = lambda self: self.notation

    def __unicode__(self):
        return self.char

    def __int__(self):
        return self.codepoint
    __hash__ = __int__

    def __add__(self, other):
        return self.char + unicode(other)

    def __radd__(self, other):
        return unicode(other) + self.char

    def __mul__(self, other):
        return self.char * int(other)
    __rmul__ = __mul__

