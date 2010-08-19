#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('ucd.sqlite')
cur = conn.cursor()


for cp in range(0xE000, 0xF900):
    sp = str(cp)
    cur.execute('INSERT INTO data
("cp", "age", "na", "JSN", "gc", "ccc", "dt", "dm", "nt", "nv", "bc",
 "Bidi_M", "bmg", "suc", "slc", "stc", "uc", "lc", "tc", "scf", "cf", "jt",
 "jg", "ea", "lb", "sc", "Dash", "WSpace", "Hyphen", "QMark", "Radical",
 "Ideo", "UIdeo", "IDSB", "IDST", "hst", "DI", "ODI", "Alpha", "OAlpha",
 "Upper", "OUpper", "Lower", "OLower", "Math", "OMath", "Hex", "AHex",
 "NChar", "VS", "Bidi_C", "Join_C", "Gr_Base", "Gr_Ext", "OGr_Ext",
 "Gr_Link", "STerm", "Ext", "Term", "Dia", "Dep", "IDS", "OIDS", "XIDS",
 "IDC", "OIDC", "XIDC", "SD", "LOE", "Pat_WS", "Pat_Syn", "GCB", "WB", "SB",
 "CE", "Comp_Ex", "NFC_QC", "NFD_QC", "NFKC_QC", "NFKD_QC", "XO_NFC",
 "XO_NFD", "XO_NFKC", "XO_NFKD", "FC_NFKC", "CI", "Cased", "CWCF", "CWCM",
 "CWKCF", "CWL", "CWT", "CWU", "NFKC_CF", "isc", "na1"
)
VALUES
(
 '+sp+', "1.1", "", "", "Co", "0", "none", '+sp+', "None", "", "L", 0, "",
 '+sp+', '+sp+', '+sp+', '+sp+', '+sp+', '+sp+', '+sp+', '+sp+', "U",
 "No_Joining_Group", "A", "XX", "Zzzz", 0, 0, 0, 0, 0, 0, 0, 0, 0, "NA", 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, "XX", "XX", "XX", 0, 0, 1, 1, 1, 1, 0, 0, 0, 0,
 "", 0, 0, 0, 0, 0, 0, 0, 0, '+sp+', "", ""
)
;')


cur.close()
conn.close()

#<char first-cp="E000" last-cp="F8FF" age="1.1" na="" JSN="" gc="Co" ccc="0" dt="none" dm="#" nt="None" nv="" bc="L" Bidi_M="N" bmg="" suc="#" slc="#" stc="#" uc="#" lc="#" tc="#" scf="#" cf="#" jt="U" jg="No_Joining_Group" ea="A" lb="XX" sc="Zzzz" Dash="N" WSpace="N" Hyphen="N" QMark="N" Radical="N" Ideo="N" UIdeo="N" IDSB="N" IDST="N" hst="NA" DI="N" ODI="N" Alpha="N" OAlpha="N" Upper="N" OUpper="N" Lower="N" OLower="N" Math="N" OMath="N" Hex="N" AHex="N" NChar="N" VS="N" Bidi_C="N" Join_C="N" Gr_Base="N" Gr_Ext="N" OGr_Ext="N" Gr_Link="N" STerm="N" Ext="N" Term="N" Dia="N" Dep="N" IDS="N" OIDS="N" XIDS="N" IDC="N" OIDC="N" XIDC="N" SD="N" LOE="N" Pat_WS="N" Pat_Syn="N" GCB="XX" WB="XX" SB="XX" CE="N" Comp_Ex="N" NFC_QC="Y" NFD_QC="Y" NFKC_QC="Y" NFKD_QC="Y" XO_NFC="N" XO_NFD="N" XO_NFKC="N" XO_NFKD="N" FC_NFKC="" CI="N" Cased="N" CWCF="N" CWCM="N" CWKCF="N" CWL="N" CWT="N" CWU="N" NFKC_CF="#" isc="" na1=""/>
#<char first-cp="F0000" last-cp="FFFFD" age="2.0" na="" JSN="" gc="Co" ccc="0" dt="none" dm="#" nt="None" nv="" bc="L" Bidi_M="N" bmg="" suc="#" slc="#" stc="#" uc="#" lc="#" tc="#" scf="#" cf="#" jt="U" jg="No_Joining_Group" ea="A" lb="XX" sc="Zzzz" Dash="N" WSpace="N" Hyphen="N" QMark="N" Radical="N" Ideo="N" UIdeo="N" IDSB="N" IDST="N" hst="NA" DI="N" ODI="N" Alpha="N" OAlpha="N" Upper="N" OUpper="N" Lower="N" OLower="N" Math="N" OMath="N" Hex="N" AHex="N" NChar="N" VS="N" Bidi_C="N" Join_C="N" Gr_Base="N" Gr_Ext="N" OGr_Ext="N" Gr_Link="N" STerm="N" Ext="N" Term="N" Dia="N" Dep="N" IDS="N" OIDS="N" XIDS="N" IDC="N" OIDC="N" XIDC="N" SD="N" LOE="N" Pat_WS="N" Pat_Syn="N" GCB="XX" WB="XX" SB="XX" CE="N" Comp_Ex="N" NFC_QC="Y" NFD_QC="Y" NFKC_QC="Y" NFKD_QC="Y" XO_NFC="N" XO_NFD="N" XO_NFKC="N" XO_NFKD="N" FC_NFKC="" CI="N" Cased="N" CWCF="N" CWCM="N" CWKCF="N" CWL="N" CWT="N" CWU="N" NFKC_CF="#" isc="" na1=""/>
#<char first-cp="100000" last-cp="10FFFD" age="2.0" na="" JSN="" gc="Co" ccc="0" dt="none" dm="#" nt="None" nv="" bc="L" Bidi_M="N" bmg="" suc="#" slc="#" stc="#" uc="#" lc="#" tc="#" scf="#" cf="#" jt="U" jg="No_Joining_Group" ea="A" lb="XX" sc="Zzzz" Dash="N" WSpace="N" Hyphen="N" QMark="N" Radical="N" Ideo="N" UIdeo="N" IDSB="N" IDST="N" hst="NA" DI="N" ODI="N" Alpha="N" OAlpha="N" Upper="N" OUpper="N" Lower="N" OLower="N" Math="N" OMath="N" Hex="N" AHex="N" NChar="N" VS="N" Bidi_C="N" Join_C="N" Gr_Base="N" Gr_Ext="N" OGr_Ext="N" Gr_Link="N" STerm="N" Ext="N" Term="N" Dia="N" Dep="N" IDS="N" OIDS="N" XIDS="N" IDC="N" OIDC="N" XIDC="N" SD="N" LOE="N" Pat_WS="N" Pat_Syn="N" GCB="XX" WB="XX" SB="XX" CE="N" Comp_Ex="N" NFC_QC="Y" NFD_QC="Y" NFKC_QC="Y" NFKD_QC="Y" XO_NFC="N" XO_NFD="N" XO_NFKC="N" XO_NFKD="N" FC_NFKC="" CI="N" Cased="N" CWCF="N" CWCM="N" CWKCF="N" CWL="N" CWT="N" CWU="N" NFKC_CF="#" isc="" na1=""/>
