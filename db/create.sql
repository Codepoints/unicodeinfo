--
-- Codepoints and their properties
--
CREATE TABLE codepoints (
cp       INTEGER PRIMARY KEY NOT NULL,
age      TEXT(12),
na       TEXT(255),
na1      TEXT(255),
gc       TEXT(2),
ccc      INTEGER(3),  -- 0..255
bc       TEXT(3),
Bidi_M   INTEGER(1),  -- bool
-- bmg      INTEGER(7),  -- cp
Bidi_C   INTEGER(1),  -- bool
dt       TEXT(4),
-- dm       TEXT(255),   -- cp*
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
-- FC_NFKC  TEXT(255),   -- cp*
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
-- suc      INTEGER(7),  -- cp
-- slc      INTEGER(7),  -- cp
-- stc      INTEGER(7),  -- cp
-- uc       TEXT(255),   -- cp+
-- lc       TEXT(255),   -- cp+
-- tc       TEXT(255),   -- cp+
-- scf      INTEGER(7),  -- cp
-- cf       TEXT(255),   -- cp+
CI       INTEGER(1),  -- bool
Cased    INTEGER(1),  -- bool
CWCF     INTEGER(1),  -- bool
CWCM     INTEGER(1),  -- bool
CWL      INTEGER(1),  -- bool
CWKCF    INTEGER(1),  -- bool
CWT      INTEGER(1),  -- bool
CWU      INTEGER(1),  -- bool
-- NFKC_CF  TEXT(255),   -- cp*
-- sc       TEXT(4),
isc      TEXT(2047),
hst      TEXT(3),
JSN      TEXT(3),
InSC     TEXT(24),    -- new in U6
InMC     TEXT(24),    -- new in U6
InPC     TEXT(24),    -- new in U8
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
PCM      INTEGER(1),  -- bool, new in U9
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
kJa                   TEXT(6),    -- new in U8
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
kRSTUnicode           TEXT(255), -- new in U9
kSBGY                 TEXT(255),
kSemanticVariant      TEXT(255),
kSimplifiedVariant    TEXT(255),
kSpecializedSemanticVariant TEXT(255),
kTaiwanTelegraph      TEXT(4),
kTang                 TEXT(255),
kTotalStrokes         TEXT(3),
kTraditionalVariant   TEXT(255),
kTGT_MergedSrc        TEXT(255), -- new in U9
kVietnamese           TEXT(255),
kXHC1983              TEXT(255),
kWubi                 TEXT(2047),
kXerox                TEXT(7),
kZVariant             TEXT(255),
blk                   TEXT(255), -- new in U6.1
scx                   TEXT(255), -- new in U6.1
-- bpb                   INTEGER(7),    -- cp, new in U6.3
bpt                   TEXT(1)   -- /[ocn]{1}/, new in U6.3
);
CREATE INDEX codepoints_name ON codepoints ( na );
CREATE INDEX codepoints_blk ON codepoints ( blk );
CREATE INDEX codepoints_scx ON codepoints ( scx );

--
-- cross-references between codepoints
--
CREATE TABLE codepoint_relation (
  cp       INTEGER(7) REFERENCES codepoints,
  other    INTEGER(7) REFERENCES codepoints,
  relation TEXT(255),
  `order`  INTEGER(3) DEFAULT 0,
  UNIQUE ( cp, other, relation, `order` )
);
CREATE INDEX codepoint_relation_cp ON codepoint_relation ( cp );
CREATE INDEX codepoint_relation_other ON codepoint_relation ( other );

--
-- alias names for a codepoint
--
CREATE TABLE codepoint_alias (
  cp     INTEGER REFERENCES codepoints,
  alias  TEXT(255),
  `type` TEXT(25)
);
CREATE INDEX codepoint_alias_cp ON codepoint_alias ( cp );
CREATE INDEX codepoint_alias_alias ON codepoint_alias ( alias );

--
-- defined Unicode blocks
--
CREATE TABLE blocks (
  name   TEXT(255) PRIMARY KEY,
  first  INTEGER(7),
  last   INTEGER(7)
);
CREATE INDEX blocks_cps ON blocks ( first, last );

--
-- The block a codepoint belongs to
--
CREATE TABLE codepoint_block (
  cp   INTEGER REFERENCES codepoints,
  blk  TEXT(255) REFERENCES blocks,
  UNIQUE ( cp, blk )
);
CREATE INDEX codepoint_block_cp ON codepoint_block ( cp );
CREATE INDEX codepoint_block_blk ON codepoint_block ( blk );

--
-- defined Unicode planes
--
CREATE TABLE planes (
  name   TEXT(255) PRIMARY KEY,
  first  INTEGER(7),
  last   INTEGER(7)
);
CREATE INDEX planes_cps ON planes ( first, last );
INSERT INTO planes (name, first, last) VALUES ('Basic Multilingual Plane', 0, 65535);
INSERT INTO planes (name, first, last) VALUES ('Supplementary Multilingual Plane', 65536, 131071);
INSERT INTO planes (name, first, last) VALUES ('Supplementary Ideographic Plane', 131072, 196607);
INSERT INTO planes (name, first, last) VALUES ('Tertiary Ideographic Plane', 196608, 262143);
INSERT INTO planes (name, first, last) VALUES ('Plane 5 (unassigned)', 262144, 327679);
INSERT INTO planes (name, first, last) VALUES ('Plane 6 (unassigned)', 327680, 393215);
INSERT INTO planes (name, first, last) VALUES ('Plane 7 (unassigned)', 393216, 458751);
INSERT INTO planes (name, first, last) VALUES ('Plane 8 (unassigned)', 458752, 524287);
INSERT INTO planes (name, first, last) VALUES ('Plane 9 (unassigned)', 524288, 589823);
INSERT INTO planes (name, first, last) VALUES ('Plane 10 (unassigned)', 589824, 655359);
INSERT INTO planes (name, first, last) VALUES ('Plane 11 (unassigned)', 655360, 720895);
INSERT INTO planes (name, first, last) VALUES ('Plane 12 (unassigned)', 720896, 786431);
INSERT INTO planes (name, first, last) VALUES ('Plane 13 (unassigned)', 786432, 851967);
INSERT INTO planes (name, first, last) VALUES ('Plane 14 (unassigned)', 851968, 917503);
INSERT INTO planes (name, first, last) VALUES ('Supplementary Special-purpose Plane', 917504, 983039);
INSERT INTO planes (name, first, last) VALUES ('Supplementary Private Use Area - A', 983040, 1048575);
INSERT INTO planes (name, first, last) VALUES ('Supplementary Private Use Area - B', 1048576, 1114111);

--
-- defined properties and their alternate names
--
CREATE TABLE propval (
  prop TEXT(12),
  abbr TEXT(255),
  name TEXT(255)
);
CREATE INDEX propval_prop ON propval ( prop );
CREATE INDEX propval_prop_abbr ON propval ( prop, abbr );

--
-- Scripts defined by their ISO name
--
CREATE TABLE scripts (
  iso  TEXT(4) PRIMARY KEY,
  name TEXT(255)
);

--
-- The script the codepoint belongs to
--
CREATE TABLE codepoint_script (
  cp   INTEGER REFERENCES codepoints,
  sc   TEXT(4) REFERENCES scripts,
  UNIQUE ( cp, sc )
);
CREATE INDEX codepoint_script_cp ON codepoint_script ( cp );
CREATE INDEX codepoint_script_sc ON codepoint_script ( sc );

--
-- graphical representation in PNG format, 16x16px
--
CREATE TABLE codepoint_image (
  cp    INTEGER REFERENCES codepoints,
  image TEXT DEFAULT 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAAAAAA6mKC9AAAAQUlEQVQY022PSQ4AIAgD5/+fxhhbEJEL6bAV4gmc6QBMSC1C9otQ9UOwRntoeqdommsEj8iED+ssae1vbFqfz1Usi/eYaGRQ6NgAAAAASUVORK5CYII=',
  UNIQUE ( cp )
);

--
-- wikipedia abstract about a codepoint
--
CREATE TABLE codepoint_abstract (
  cp       INTEGER REFERENCES codepoints,
  abstract TEXT,
  lang     TEXT DEFAULT 'en',
  UNIQUE ( cp, lang )
);
CREATE INDEX codepoint_abstract_cp ON codepoint_abstract ( cp );
CREATE INDEX codepoint_abstract_cp_lang ON codepoint_abstract ( cp, lang );

--
-- wikipedia abstract about a Unicode block
--
CREATE TABLE block_abstract (
  block    TEXT REFERENCES blocks,
  abstract TEXT,
  lang     TEXT DEFAULT 'en',
  UNIQUE ( block, lang )
);
CREATE INDEX block_abstract_block ON block_abstract ( block );
CREATE INDEX block_abstract_block_lang ON block_abstract ( block, lang );

--
-- other codepoints to be confusable with this
--
CREATE TABLE codepoint_confusables (
  id       INTEGER,
  cp       INTEGER REFERENCES codepoints,
  other    INTEGER REFERENCES codepoints,
  `type`   TEXT,
  `order`  INTEGER
);
CREATE INDEX codepoint_confusables_cp ON codepoint_confusables ( cp );
CREATE INDEX codepoint_confusables_other ON codepoint_confusables ( other );

--
-- named sequences of characters, TR #34
--
CREATE TABLE namedsequences (
  cp      INTEGER(7) REFERENCES codepoints,
  name    TEXT(255),
  `order` INTEGER(3),
  UNIQUE ( cp, name, `order` )
);
CREATE INDEX namedsequences_cp ON namedsequences ( cp );
