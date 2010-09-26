#!/usr/bin/python
"""Command line client to explore the Unicode standard"""

__version__ = "0.9"


def _get_geometry():
    """Get the screen geometry"""
    import os
    rows, columns = os.popen('stty size', 'r').read().split()
    return (int(rows), int(columns))


def _paginate(string, threshold=4, force=None):
    """Display a string with a pager

    'threshold' is used to determine, how many columns
    of the screen are preoccupied.
    'force' can be either 'cat' to not paginate
    or 'more' to force pagination.
    """
    import os
    import sys
    from tempfile import NamedTemporaryFile
    geometry = _get_geometry()
    if force == 'more' or (force is None and
       (len(string.splitlines()) > geometry[0] - threshold)):
        tf = NamedTemporaryFile()
        tf.write(string.encode('utf-8'))
        tf.flush()
        os.system("less %s" % tf.name)
        tf.close()
    else:
        sys.stdout.write(str(string.encode('utf-8')))
        sys.stdout.flush()


def main():
    from argparse import ArgumentParser
    from unicodeinfo import codepoint
    from unicodeinfo import info
    from unicodeinfo import notation
    from unicodeinfo import representation

    _ = lambda s: s
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", dest="verbose",
        default=False, help=_("show additional information"))
    parser.add_argument("-l", "--legend", action="store_true", dest="legend",
        default=False, help=_("show a legend of Unicode abbreviations"))
    parser.add_argument("-x", "--hex",
        action="store_const", const=16, dest="base", default=16,
        help=_("the provided range is hexadecimal (the default)"))
    parser.add_argument("-d", "--dec",
        action="store_const", const=10, dest="base",
        help=_("the provided range is decimal"))
    parser.add_argument("-o", "--oct",
        action="store_const", const=8, dest="base",
        help=_("the provided range is octal"))
    parser.add_argument("-n", "--no-pager", action="store_const",
        const='cat', dest="pager", default=None,
        help=_("don't show paginated output"))
    parser.add_argument("-b", "--block",
        action="store_true", dest="block", default=False,
        help=_("show characters in block CP"))
    parser.add_argument("-r", "--range",
        dest="range", default=False, action="store_true",
        help=_("evaluate the given codepoints as range (default are "
               "independent points)"))
    parser.add_argument("codepoints", metavar="CP", nargs="+",
        help=_("codepoints to evaluate"))
    args = parser.parse_args()

    if args.block:
        lower = upper = None
        for b in info.blocks + info.special_blocks:
            if b[2].lower() == args.codepoints[0].lower():
                lower = b[0]
                upper = b[1]
                break
        if lower is None or upper is None:
            parser.error("Couldn't find block %s." % args.codepoints[0])
        else:
            rng = list(range(lower, upper+1))
    else:
        if args.range:
            args.codepoints = '..'.join(args.codepoints)
        rng = notation.parse_range(args.codepoints)

    s = u""
    if len(rng) == 1:
        cp = codepoint.Codepoint(rng[0])
        for p in codepoint.Codepoint.properties:
            s += u"%s: \t %s\n" % (p, getattr(cp, p))
    else:
        current_block = ""
        for cp in rng:
            cp = codepoint.Codepoint(cp)
            if cp.block is not None and cp.block != current_block:
                s += u" %s \n=%s=\n" % (cp.block, len(cp.block)*"=")
                current_block = cp.block
            s += u"%s\t%s\t%s (%s)\n" % (cp.notation, cp.printable_char, cp.name, cp.category)
    if args.legend:
        s += "\nL E G E N D :\n=============\n%s\n" % representation.get_legend()
    _paginate(s, force=args.pager)


if __name__ == '__main__':
    main()

