CREATE TABLE data (
cp       INTEGER PRIMARY KEY,
age      TEXT(12),
na       TEXT(255),
na1      TEXT(255),
gc       TEXT(2),
ccc      INTEGER(3),  -- 0..255
bc       TEXT(3),
Bidi_M   INTEGER(1),  -- bool
bmg      INTEGER(7),  -- cp
Bidi_C   INTEGER(1),  -- bool
dt       TEXT(4),
dm       TEXT(255),   -- cp*
CE       INTEGER(1),  -- bool
Comp_Ex  INTEGER(1),  -- bool
NFC_QC   TEXT(1),
NFD_QC   TEXT(1),
NFKC_QC  TEXT(1),
NFKD_QC  TEXT(1),
XO_NFC   INTEGER(1),  -- bool
XO_NFD   INTEGER(1),  -- bool
XO_NFKC  INTEGER(1),  -- bool
XO_NFKD  INTEGER(1),  -- bool
FC_NFKC  TEXT(255),   -- cp*
nt       TEXT(4),
nv       TEXT(255),
jt       TEXT(1),
jg       TEXT(25),
Join_C   INTEGER(1),  -- bool
lb       TEXT(2),
ea       TEXT(2),
Upper    INTEGER(1),  -- bool
Lower    INTEGER(1),  -- bool
OUpper   INTEGER(1),  -- bool
OLower   INTEGER(1),  -- bool
suc      INTEGER(7),  -- cp
slc      INTEGER(7),  -- cp
stc      INTEGER(7),  -- cp
uc       TEXT(255),   -- cp+
lc       TEXT(255),   -- cp+
tc       TEXT(255),   -- cp+
scf      INTEGER(7),  -- cp
cf       TEXT(255),   -- cp+
CI       INTEGER(1),  -- bool
Cased    INTEGER(1),  -- bool
CWCF     INTEGER(1),  -- bool
CWCM     INTEGER(1),  -- bool
CWL      INTEGER(1),  -- bool
CWKCF    INTEGER(1),  -- bool
CWT      INTEGER(1),  -- bool
CWU      INTEGER(1),  -- bool
NFKC_CF  TEXT(255),   -- cp*
sc       TEXT(4),
isc      TEXT(2047),
hst      TEXT(3),
JSN      TEXT(3),
IDS      INTEGER(1),  -- bool
OIDS     INTEGER(1),  -- bool
XIDS     INTEGER(1),  -- bool
IDC      INTEGER(1),  -- bool
OIDC     INTEGER(1),  -- bool
XIDC     INTEGER(1),  -- bool
Pat_Syn  INTEGER(1),  -- bool
Pat_WS   INTEGER(1),  -- bool
Dash     INTEGER(1),  -- bool
Hyphen   INTEGER(1),  -- bool
QMark    INTEGER(1),  -- bool
Term     INTEGER(1),  -- bool
STerm    INTEGER(1),  -- bool
Dia      INTEGER(1),  -- bool
Ext      INTEGER(1),  -- bool
SD       INTEGER(1),  -- bool
Alpha    INTEGER(1),  -- bool
OAlpha   INTEGER(1),  -- bool
Math     INTEGER(1),  -- bool
OMath    INTEGER(1),  -- bool
Hex      INTEGER(1),  -- bool
AHex     INTEGER(1),  -- bool
DI       INTEGER(1),  -- bool
ODI      INTEGER(1),  -- bool
LOE      INTEGER(1),  -- bool
WSpace   INTEGER(1),  -- bool
Gr_Base  INTEGER(1),  -- bool
Gr_Ext   INTEGER(1),  -- bool
OGr_Ext  INTEGER(1),  -- bool
Gr_Link  INTEGER(1),  -- bool
GCB      TEXT(3),
WB       TEXT(6),
SB       TEXT(2),
Ideo     INTEGER(1),  -- bool
UIdeo    INTEGER(1),  -- bool
IDSB     INTEGER(1),  -- bool
IDST     INTEGER(1),  -- bool
Radical  INTEGER(1),  -- bool
Dep      INTEGER(1),  -- bool
VS       INTEGER(1),  -- bool
NChar    INTEGER(1),  -- bool
kAccountingNumeric    TEXT(255),
kAlternateHanYu       TEXT(2047),
kAlternateJEF         TEXT(2047),
kAlternateKangXi      TEXT(2047),
kAlternateMorohashi   TEXT(2047),
kBigFive              TEXT(4),
kCCCII                TEXT(6),
kCNS1986              TEXT(6),
kCNS1992              TEXT(6),
kCangjie              TEXT(255),
kCantonese            TEXT(255),
kCheungBauer          TEXT(2047),
kCheungBauerIndex     TEXT(255),
kCihaiT               TEXT(255),
kCompatibilityVariant TEXT(7),
kCowles               TEXT(255),
kDaeJaweon            TEXT(8),
kDefinition           TEXT(2047),
kEACC                 TEXT(6),
kFenn                 TEXT(255),
kFennIndex            TEXT(255),
kFourCornerCode       TEXT(255),
kFrequency            TEXT(1),
kGB0                  TEXT(4),
kGB1                  TEXT(4),
kGB3                  TEXT(4),
kGB5                  TEXT(4),
kGB7                  TEXT(4),
kGB8                  TEXT(4),
kGradeLevel           TEXT(1),
kGSR                  TEXT(255),
kHangul               TEXT(2047),
kHanYu                TEXT(255),
kHanyuPinlu           TEXT(255),
kHanyuPinyin          TEXT(255),
kHDZRadBreak          TEXT(20),
kHKGlyph              TEXT(255),
kHKSCS                TEXT(4),
kIBMJapan             TEXT(4),
kIICore               TEXT(3),
kIRGDaeJaweon         TEXT(8),
kIRGDaiKanwaZiten     TEXT(6),
kIRGHanyuDaZidian     TEXT(9),
kIRGKangXi            TEXT(8),
kIRG_GSource          TEXT(24),
kIRG_HSource          TEXT(4),
kIRG_JSource          TEXT(10),
kIRG_KPSource         TEXT(7),
kIRG_KSource          TEXT(8),
kIRG_MSource          TEXT(8),
kIRG_TSource          TEXT(255),
kIRG_USource          TEXT(8),
kIRG_VSource          TEXT(6),
kJHJ                  TEXT(2047),
kJIS0213              TEXT(7),
kJapaneseKun          TEXT(255),
kJapaneseOn           TEXT(255),
kJis0                 TEXT(4),
kJis1                 TEXT(4),
kKPS0                 TEXT(4),
kKPS1                 TEXT(4),
kKSC0                 TEXT(4),
kKSC1                 TEXT(4),
kKangXi               TEXT(8),
kKarlgren             TEXT(5),
kKorean               TEXT(255),
kLau                  TEXT(255),
kMainlandTelegraph    TEXT(4),
kMandarin             TEXT(255),
kMatthews             TEXT(6),
kMeyerWempe           TEXT(255),
kMorohashi            TEXT(6),
kNelson               TEXT(255),
kOtherNumeric         TEXT(255),
kPhonetic             TEXT(255),
kPrimaryNumeric       TEXT(255),
kPseudoGB1            TEXT(4),
kRSAdobe_Japan1_6     TEXT(255),
kRSJapanese           TEXT(6),
kRSKanWa              TEXT(6),
kRSKangXi             TEXT(6),
kRSKorean             TEXT(6),
kRSMerged             TEXT(2047),
kRSUnicode            TEXT(255),
kSBGY                 TEXT(255),
kSemanticVariant      TEXT(255),
kSimplifiedVariant    TEXT(255),
kSpecializedSemanticVariant TEXT(255),
kTaiwanTelegraph      TEXT(4),
kTang                 TEXT(255),
kTotalStrokes         TEXT(3),
kTraditionalVariant   TEXT(255),
kVietnamese           TEXT(255),
kXHC1983              TEXT(255),
kWubi                 TEXT(2047),
kXerox                TEXT(7),
kZVariant             TEXT(255),
-- additional (non-standard) info starts here:
digraph               TEXT(7),
htmlentity            TEXT(8)
);
CREATE INDEX name ON data ( na );
CREATE INDEX digraph ON data ( digraph );
