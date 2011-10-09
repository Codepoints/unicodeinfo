#!/usr/bin/python

"""Insert the codepoints of the private use area into ucd.sqlite"""

import sqlite3

conn = sqlite3.connect('ucd.sqlite')
cur = conn.cursor()

statement = "INSERT INTO data
(
 cp, age, na, JSN, gc, ccc, dt, dm, nt, nv, bc,
 Bidi_M, bmg, suc, slc, stc, uc, lc, tc, scf, cf, jt,
 jg, ea, lb, sc, Dash, WSpace, Hyphen, QMark, Radical,
 Ideo, UIdeo, IDSB, IDST, hst, DI, ODI, Alpha, OAlpha,
 Upper, OUpper, Lower, OLower, Math, OMath, Hex, AHex,
 NChar, VS, Bidi_C, Join_C, Gr_Base, Gr_Ext, OGr_Ext,
 Gr_Link, STerm, Ext, Term, Dia, Dep, IDS, OIDS, XIDS,
 IDC, OIDC, XIDC, SD, LOE, Pat_WS, Pat_Syn, GCB, WB, SB,
 CE, Comp_Ex, NFC_QC, NFD_QC, NFKC_QC, NFKD_QC, XO_NFC,
 XO_NFD, XO_NFKC, XO_NFKD, FC_NFKC, CI, Cased, CWCF, CWCM,
 CWKCF, CWL, CWT, CWU, NFKC_CF, isc, na1
)
VALUES
(
 %(cp)s, '%(age)s', '', '', 'Co', '0', 'none', %(cp)s, 'None', '', 'L', 0, '',
 %(cp)s, %(cp)s, %(cp)s, %(cp)s, %(cp)s, %(cp)s, %(cp)s, %(cp)s, 'U',
 'No_Joining_Group', 'A', 'XX', 'Zzzz', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'NA', 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 'XX', 'XX', 'XX', 0, 0, 1, 1, 1, 1, 0, 0, 0, 0,
 '', 0, 0, 0, 0, 0, 0, 0, 0, %(cp)s, '', ''
)
;"

for cp in range(0xE000, 0xF900):
    cur.execute(statement % { 'cp': str(cp), 'age': '1.1' })

for cp in list(range(0xF0000, 0xFFFFE)) + list(range(0x100000, 0x10FFFE)):
    cur.execute(statement % { 'cp': str(cp), 'age': '2.0' })

cur.close()
conn.close()
