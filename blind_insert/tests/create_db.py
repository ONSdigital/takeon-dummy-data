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

form_stmt = "CREATE TABLE form\
(\
    FormID              int UNIQUE NOT NULL,\
    Survey              varchar(3) NOT NULL,\
    Description         varchar(128) NOT NULL, \
    PeriodStart         varchar(6) NOT NULL,\
    PeriodEnd           varchar(6) NOT NULL,\
    CreatedBy           varchar(16) NOT NULL,\
    CreatedDate         int NOT NULL,\
    LastUpdatedBy       varchar(16) NOT NULL,\
    LastUpdatedDate     int NOT NULL,\
\
    PRIMARY KEY (FormID)\
);"

form_def_stmt = "CREATE TABLE form_definition\
(\
    FormID                  int NOT NULL,           \
    QuestionCode            varchar(4) NOT NULL,           \
    DisplayQuestionNumber   varchar(16) Not Null,       \
    DisplayText             varchar(128) Not Null,      \
    Type                    varchar(16) NOT NULL,       \
    CreatedBy               varchar(16) NOT NULL,       \
    CreatedDate             int NOT NULL, \
    LastUpdatedBy           varchar(16) NOT NULL,       \
    LastUpdatedDate         int NOT NULL, \
\
    PRIMARY KEY (FormID, QuestionCode)\
 );"

survey_stmt = "CREATE TABLE survey\
 (\
     survey              varchar(4) Primary Key,\
     description         varchar(128) Not Null,\
     periodicity         varchar(32) Not Null,\
     CreatedBy           varchar(16) Not Null,\
     CreatedDate         int Not Null,\
     LastUpdatedBy       varchar(16),\
     LastUpdatedDate     int\
);"

question_stmt = "Create table dev01.Question\
(\
    Survey              varchar(4),\
    QuestionCode        varchar(8) Not Null,\
    CreatedBy           varchar(16) Not Null,\
    CreatedDate         int Not Null,\
    LastUpdatedBy       varchar(16),\
    LastUpdatedDate     int,\
\
    Primary Key (Survey, QuestionCode)\
);"

response_stmt = "Create table Response\
(\
    Reference              char(11) Not Null,\
    Period                 char(6) Not Null,\
    Survey                 char(3) References,\
    QuestionCode           char(4) Not Null,\
    Instance               int Not Null,\
    Response               varchar(256) Not Null,\
    CreatedBy              varchar(16) Not Null,\
    CreatedDate            int Not Null,\
    LastUpdatedBy          varchar(16),\
    LastUpdatedDate        int,\
    Primary Key (Reference, Period, Survey, QuestionCode, Instance),\
);"

validation_stmt = "Create table ValidationRule\
(\
    Rule            varchar(16) Primary Key,\
    Name            varchar(32) Not Null,\
    BaseFormula     varchar(1024) Not Null,\
    CreatedBy       varchar(16) Not Null,\
    CreatedDate     int Not Null,\
    LastUpdatedBy   varchar(16),\
    LastUpdatedDate int\
);"

validation_period = "Create table ValidationPeriod\
(\
    Rule            varchar(16),\
    PeriodOffset    int Not Null,\
    CreatedBy       varchar(16) Not Null,\
    CreatedDate     int Not Null,\
    LastUpdatedBy   varchar(16),\
    LastUpdatedDate int,\
    Primary Key (Rule,PeriodOffset)\
);"

validation_form = "Create table ValidationForm\
(\
    ValidationID            INTEGER Primary Key,\
    FormID                  int,\
    Rule                    varchar(16),\
    QuestionCode            varchar(4) Not Null,\
    PreCalculationFormula   Varchar(256) Not Null,\
    Severity                Varchar(16) Not Null,\
    CreatedBy               Varchar(16) Not Null,\
    CreatedDate             int Not Null,\
    LastUpdatedBy           Varchar(16),\
    LastUpdatedDate         int\
);"

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

    def create(self):
        # connect = Connect("takeon_test")
        self.create_db()
        self.create_table(sql_stmt)
        self.create_table(form_stmt)
        self.create_table(form_def_stmt)
        self.create_table(validation_form)

Connect("takeon_test").create()