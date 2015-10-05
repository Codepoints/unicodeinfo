---
title: Unicodeinfo: Tools to squeeze knowledge out of the Unicode standard
layout: post
---

# Unicodeinfo

## Tools to squeeze knowledge out of the Unicode standard


## SQLite Database:

The directory db contains tools to create an Sqlite3 database
from Unicode’s data. Run `make` to create the database db/ucd.sqlite.

The database itself contains every field as defined in [“Unicode
Character Database in XML”](http://www.unicode.org/reports/tr42/).
Boolean fields (in the original represented by literal "Y" and "N"
values) are converted to INTEGER(1) fields, referenced codepoints are
put in a separate table. The “#” notation mentioned in TR42 is resolved.

Every codepoint in the BMP has a graphical representation (PNG, 16x16px)
attached. This is provided by the GNU Unifont project (see license
below).

The db also contains tables of all blocks, planes, scripts and named
character sequences as well as usual aliases for codepoints (including
HTML entities and digraph names).

For building the database you need:

*   Python 2.5 or newer
*   GNU make or compatible
*   wget for file retreaval
*   basic tools like Perl, sed, cat. Should be there on any *NIX (incl.
    Mac and Cygwin)
*   for the images:
    * ImageMagick's convert
    * pngcrush

All in all it should be straight forward to get from downloading to the
database.


## Python Tools:

The folder python/unicodeinfo contains a python package for handling the
information of the SQLite database. It's not fully finished yet
unfortunately. Use at your own risk.



----

*here be dragons.*


## The Small Print:

The database tools are provided in the public domain, as long as this
doesn’t collide with the
[Terms of Usage of the Unicode Consortium](http://www.unicode.org/copyright.html).
The name “unicodeinfo” of this
project does not imply any kind of affiliation of the author with
Unicode Inc. The graphical representations retrieved via db/unifont.sh
are subject to the UNIFONT LICENSE below.

The applicable license, where public domain dedication is not possible,
is the Creative Commons Zero License:

    <http://creativecommons.org/publicdomain/zero/1.0/>


# Unifont License:

If you want to use the images provided by db/unifont.sh you are bound to
the following usage terms re GNU Unifont:

Roman Czyborra released his work (Perl scripts and font .hex files)
under the following terms:

     All of my works you find here are freeware. You may
     freely copy, use, quote, modify or redistribute them
     as long as you properly attribute my contribution and
     have given a quick thought about whether Roman might
     perhaps be interested to read what you did with his
     stuff. Horizontal rules don't apply.

David Starner released what in this package is named "hex2bdf-split"
under the same license as Roman Czyborra's work.

License for all of Paul Hardy's work (except "johab2ucs2" and
"blanks.hex", mentioned separately), Makefile and debian/ mods
by Anthony Fok, and modified software from Luis Gonzalez Miranda
(with permission granted to Paul Hardy):

     These are released under the terms of the GNU General Public
     License version 2, or (at your option) a later version.

License for Fonts:

     Any fonts using glyphs from the "wqy-cjk.hex" file (including
     the default TrueType font) are bound by the terms of the Wen
     Quan Yi font license.  Those fonts are released under the terms
     of the GNU General Public License (GPL) versionn 2, with the
     exception that embedding the font in a document does not by
     itself bind that document to the terms of the GNU GPL.

     Any fonts that do not use glyphs from the "wqy-cjk.hex" file
     fall under the above "License for all of Roman Czyborra's work".

     The fonts in "./font/precompiled" do use wqy-cjk.hex, and so
     are licensed under the GNU GPL version 2, with the exception
     that embedding the font in a document does not in itself bind
     that document to the terms of the GNU GPL.  The following
     paragraphs explaining the exception is taken from the Wen
     Quan Yi font distribution:

          ** GPL v2.0 license with font embedding exception:

          As a special exception, if you create a document which
          uses this font, and embed this font or unaltered portions
          of this font into the document, this font does not by
          itself cause the resulting document to be covered by
          the GNU General Public License. This exception does not
          however invalidate any other reasons why the document
          might be covered by the GNU General Public License.
          If you modify this font, you may extend this exception
          to your version of the font, but you are not obligated
          to do so. If you do not wish to do so, delete this
          exception statement from your version.

License for "blanks.hex":

     There is one exception to the above rules: Paul Hardy earlier
     released the "blanks.hex" file into the public domain.
