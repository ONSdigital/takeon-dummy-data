import sqlite3 as sq


sql_stmt = "CREATE TABLE contributor\
(\
    Reference                   varchar(11) NOT NULL,              \
    Period                      varchar(6) NOT NULL,               \
    Survey                      varchar(3) NOT NULL,               \
    FormID                      int NOT NULL,                \
    Status                      varchar(20) NOT NULL,           \
    ReceiptDate                 int,              \
    LockedBy                    varchar(16) NOT NULL,           \
    LockedDate                  int,              \
    FormType                    varchar(4) NOT NULL,               \
    Checkletter                 varchar(1) NOT NULL,               \
    FrozenSicOutdated           varchar(5) NOT NULL,               \
    RuSicOutdated               varchar(5) NOT NULL,               \
    FrozenSic                   varchar(5) NOT NULL,               \
    RuSic                       varchar(5) NOT NULL,              \
    FrozenEmployees             Decimal(13,0) NOT NULL,         \
    Employees                   Decimal(13,0) NOT NULL,         \
    FrozenEmployment            Decimal(13,0) NOT NULL,         \
    Employment                  Decimal(13,0) NOT NULL,         \
    FrozenFteEmployment         Decimal(10,3) NOT NULL,         \
    FteEmployment               Decimal(10,3) NOT NULL,         \
    FrozenTurnover              Decimal(13,0) NOT NULL,         \
    Turnover                    Decimal(13,0) NOT NULL,         \
    EnterpriseReference         varchar(10) NOT NULL,           \
    WowEnterpriseReference      varchar(10) NOT NULL,           \
    CellNumber                  SmallInt NOT NULL,              \
    Currency                    varchar(1) NOT NULL,            \
    VatReference                varchar(12) NOT NULL,           \
    PayeReference               varchar(13) NOT NULL,           \
    CompanyRegistrationNumber   varchar(8) NOT NULL,            \
    NumberLiveLocalUnits        Decimal(6,0) NOT NULL,          \
    NumberLiveVat               Decimal(6,0) NOT NULL,          \
    NumberLivePaye              Decimal(6,0) NOT NULL,          \
    LegalStatus                 varchar(1) NOT NULL,            \
    ReportingUnitMarker         varchar(1) NOT NULL,            \
    Region                      varchar(2) NOT NULL,            \
    BirthDate                   varchar(16) NULL,               \
    EnterpriseName              varchar(107) NOT NULL,          \
    ReferenceName               varchar(107) NOT NULL,          \
    ReferenceAddress            varchar(154) NOT NULL,          \
    ReferencePostcode           varchar(8) NOT NULL,            \
    TradingStyle                varchar(107) NOT NULL,          \
    Contact                     varchar(30) NOT NULL,           \
    Telephone                   varchar(20) NOT NULL,           \
    Fax                         varchar(20) NOT NULL,           \
    SelectionType               varchar(1) NOT NULL,            \
    InclusionExclusion          varchar(1) NOT NULL,            \
    CreatedBy                   varchar(16) NOT NULL,           \
    CreatedDate                 int NOT NULL,     \
    LastUpdatedBy               varchar(16),      \
    LastUpdatedDate             int,              \
    PRIMARY KEY (reference, period, survey));"

class Connect:
    def __init__(self, db_name):
        self.db = None
        self.db_name = db_name

    def create_db(self):
        connect = sq.connect(self.db_name)
        self.db = connect
    
    def create_table(self, sql_stmt):
        cursor = self.db.cursor()
        cursor.execute(sql_stmt)

connect = Connect("takeon_test")
connect.create_db()
connect.create_table(sql_stmt)