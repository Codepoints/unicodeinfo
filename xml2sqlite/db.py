#!/usr/bin/python

"""Create an SQL file from a Unicode XML database

The script assumes the XML file to be ./ucd.all.flat.xml. The
result will be written into ./unicodeinfo.sql."""

from xml.parsers import expat
import codecs

xmlfile = open('ucd.all.flat.xml', 'r')
sqlfile = codecs.open('unicodeinfo.sql', 'w', 'utf-8')
template = u"INSERT INTO data (%(fields)s) VALUES (%(values)s);\n"

# boolean fields
boolfields = (
    'Bidi_M', 'Bidi_C', 'CE', 'Comp_Ex', 'XO_NFC', 'XO_NFD', 'XO_NFKC',
    'XO_NFKD', 'Join_C', 'Upper', 'Lower', 'OUpper', 'OLower', 'CI', 'Cased',
    'CWCF', 'CWCM', 'CWL', 'CWKCF', 'CWT', 'CWU', 'IDS', 'OIDS', 'XIDS',
    'IDC', 'OIDC', 'XIDC', 'Pat_Syn', 'Pat_WS', 'Dash', 'Hyphen', 'QMark',
    'Term', 'STerm', 'Dia', 'Ext', 'SD', 'Alpha', 'OAlpha', 'Math', 'OMath',
    'Hex', 'AHex', 'DI', 'ODI', 'LOE', 'WSpace', 'Gr_Base', 'Gr_Ext',
    'OGr_Ext', 'Gr_Link', 'Ideo', 'UIdeo', 'IDSB', 'IDST', 'Radical', 'Dep',
    'VS', 'NChar',
)

# single codepoints (INT)
cpfields = (
    'cp', 'bmg', 'suc', 'slc', 'stc', 'scf',
)

# multiple codepoints (need '#' resolution, 'na' is a special case, here)
cppfields = (
    'na', 'dm', 'FC_NFKC', 'uc', 'lc', 'tc', 'cf', 'NFKC_CF',
)

# integer fields
intfields = (
    'ccc',
)

def start_element(element, attrs):
    if element.endswith('char') and 'cp' in attrs:
        cp = int(attrs['cp'], 16)
        fields = [u'cp']
        values = [unicode(cp)]
        for f, v in attrs.iteritems():
            if f == 'cp':
                continue
            fields.append(f)
            if f in boolfields:
                if v == "Y":
                    values.append(u"1")
                elif v == "N":
                    values.append(u"0")
                else:
                    values.append(u"NULL")
            elif f in cpfields:
                if v == "#":
                    values.append(unicode(cp))
                elif v:
                    values.append(unicode(int(v, 16)))
                else:
                    values.append(u"NULL")
            elif f in cppfields:
                values.append(u'"%s"' % v.replace('#', unicode(attrs['cp'])))
            elif f in intfields:
                values.append(unicode(int(v)))
            else:
                values.append(u'"%s"' % v)
        sqlfile.write(template % {
            'fields': u','.join(fields),
            'values': u','.join(values),
        })
        # give us a hint, where we are at the moment
        print cp

# parse the file with expat
p = expat.ParserCreate()
p.StartElementHandler = start_element
p.ParseFile(xmlfile)

xmlfile.close()
sqlfile.close()

