Nature of the test data.

3 generic surveys
999A - Monthly
999B - Quarterly
999C - Annual

1 Form definition (Linked to the monthly survey)
This for has multiple questions defined:
    2 numeric
    2 derived
    1 tickbox/checkbox
    1 text




Insert Into dev01.Survey
(
    survey,
    description,
    periodicity,
    CreatedBy,
    CreatedDate
)
Values
( '999A','Generic Monthly Testing Survey','Monthly','fisdba', now() ),
( '999B','Generic Quarterly Testing Survey','Quarterly','fisdba', now() ),
( '999C','Generic Annual Testing Survey','Annual','fisdba', now() )



Insert Into dev01.Form
(
    FormID,
    Survey,
    Description,
    PeriodStart,
    PeriodEnd,
    CreatedBy,
    CreatedDate
)
Values
( 1, '999A', 'Monthly Test Form', '199901', '999912,'fisdba', now() )


Insert Into dev01.Question
(
    Survey,
    QuestionCode,
    CreatedBy,
    CreatedDate
)
Values
( '999A', '1000', 'fisdba', 'now')
( '999A', '1001', 'fisdba', 'now')
( '999A', '2000', 'fisdba', 'now')
( '999A', '3000', 'fisdba', 'now')
( '999A', '4000', 'fisdba', 'now')
( '999A', '4001', 'fisdba', 'now')


Insert Into dev01.FormDefinition
(
    FormID                  serial References dev01.Form(FormID),
    QuestionCode            Varchar(8) Not Null,
    DisplayQuestionNumber   Varchar(16) Not Null,
    DisplayText             Varchar(128) Not Null,
    DisplayOrder            Integer Not Null,
    Type                    Varchar(16) Not Null,
    DerivedFormula          Varchar(128) Not Null,
    CreatedBy               Varchar(16) Not Null,
    CreatedDate             timestamptz Not Null,
    LastUpdatedBy           Varchar(16),
    LastUpdatedDate         timestamptz,


Insert Into dev01.FormDefinition
(
    FormID
    QuestionCode
    DisplayQuestionNumber
    DisplayText
    DisplayOrder
    Type
    DerivedFormula
    CreatedBy
    CreatedDate
    LastUpdatedBy
    LastUpdatedDate
)
Values
( 1, '1000', 'Q1', 'This is a numeric question', 1, 'NUMERIC', '', 'fisdba', now() ),
( 1, '1001', 'Q2', 'This is another numeric question', 1, 'NUMERIC', '', 'fisdba', now() ),
( 1, '2000', 'Q3', 'This is a checkbox question', 1, 'TICKBOX-Yes', '', 'fisdba', now() ),
( 1, '3000', 'Q4', 'This is a text question', 1, 'Text', '', 'fisdba', now() ),
( 1, '4000', 'Q5', 'This is a postive derived question', 1, 'NUMERIC', '1000 + 1001', 'fisdba', now() ),
( 1, '4001', 'Q6', 'This is a subtracted derived question', 1, 'NUMERIC', '1000 - 1001', 'fisdba', now() )


Insert Into dev01.Contributor
(
    Reference                   Varchar(11) Not Null,
    Period                      Char(6) Not Null,
    Survey                      Char(4) References dev01.Survey(Survey),
    FormID                      Integer References dev01.Form(FormID),
    Status                      Varchar(20) Not Null,
    ReceiptDate                 timestamptz,
    FormType                    Char(4) Not Null,
    Checkletter                 Char(1) Not Null,
    FrozenSicOutdated           Char(5) Not Null,
    RuSicOutdated               Char(5) Not Null,
    FrozenSic                   Char(5) Not Null,
    RuSic                       Char(5) Not Null,
    FrozenEmployees             Decimal(13,0) Not Null,
    Employees                   Decimal(13,0) Not Null,
    FrozenEmployment            Decimal(13,0) Not Null,
    Employment                  Decimal(13,0) Not Null,
    FrozenFteEmployment         Decimal(10,3) Not Null,
    FteEmployment               Decimal(10,3) Not Null,
    FrozenTurnover              Decimal(13,0) Not Null,
    Turnover                    Decimal(13,0) Not Null,
    EnterpriseReference         Char(10) Not Null,
    WowEnterpriseReference      Varchar(10) Not Null,
    CellNumber                  SmallInt Not Null,
    Currency                    Char(1) Not Null,
    VatReference                Varchar(12) Not Null,
    PayeReference               Varchar(13) Not Null,
    CompanyRegistrationNumber   Varchar(8) Not Null,
    NumberLiveLocalUnits        Decimal(6,0) Not Null,
    NumberLiveVat               Decimal(6,0) Not Null,
    NumberLivePaye              Decimal(6,0) Not Null,
    LegalStatus                 Char(1) Not Null,
    ReportingUnitMarker         Char(1) Not Null,
    Region                      Char(2) Not Null,
    BirthDate                   Varchar(16) NULL,
    EnterpriseName              Varchar(107) Not Null,
    ReferenceName               Varchar(107) Not Null,
    ReferenceAddress            Varchar(154) Not Null,
    ReferencePostcode           Varchar(8) Not Null,
    TradingStyle                Varchar(107) Not Null,
    Contact                     Varchar(30) Not Null,
    Telephone                   Varchar(20) Not Null,
    Fax                         Varchar(20) Not Null,
    SelectionType               Char(1) Not Null,
    InclusionExclusion          Char(1) Not Null,
    CreatedBy                   Varchar(16) Not Null,
    CreatedDate                 timestamptz Not Null
)
Values
(   '12345678000', '201801', '999B', 1, 'Status', 'now', '', '', '', '', '', '', 0, 0, 0, 0, 0, 0, 0, 0, '', '', 0, 'S', '', '', '', 0, 0, 0, '', '', '', '', '', 'Empty Form', '', '', '', '', '', '', '', '', 'fisdba', now() ),
(   '12345678001', '201801', '999B', 1, 'Status', 'now', '', '', '', '', '', '', 0, 0, 0, 0, 0, 0, 0, 0, '', '', 0, 'S', '', '', '', 0, 0, 0, '', '', '', '', '', 'Value Present (values exist) - 4 Triggered', '', '', '', '', '', '', '', '', 'fisdba', now() ),
(   '12345678002', '201801', '999B', 1, 'Status', 'now', '', '', '', '', '', '', 0, 0, 0, 0, 0, 0, 0, 0, '', '', 0, 'S', '', '', '', 0, 0, 0, '', '', '', '', '', 'Value Present (values all blank) - 0 Triggered', '', '', '', '', '', '', '', '', 'fisdba', now() ),
(   '12345678003', '201801', '999B', 1, 'Status', 'now', '', '', '', '', '', '', 0, 0, 0, 0, 0, 0, 0, 0, '', '', 0, 'S', '', '', '', 0, 0, 0, '', '', '', '', '', 'Value Present (values missing) - 0 Triggered', '', '', '', '', '', '', '', '', 'fisdba', now() ),
(   '12345678010', '201801', '999B', 1, 'Status', 'now', '', '', '', '', '', '', 0, 0, 0, 0, 0, 0, 0, 0, '', '', 0, 'S', '', '', '', 0, 0, 0, '', '', '', '', '', 'PoPM (pervious period is missing)', '', '', '', '', '', '', '', '', 'fisdba', now() )
(   '12345678011', '201801', '999B', 1, 'Status', 'now', '', '', '', '', '', '', 0, 0, 0, 0, 0, 0, 0, 0, '', '', 0, 'S', '', '', '', 0, 0, 0, '', '', '', '', '', 'PoPM (Current period is blank)', '', '', '', '', '', '', '', '', 'fisdba', now() )


Insert Into dev01.response
(
    Reference,
    Period,
    Survey,
    QuestionCode,
    Instance,
    Response,
    CreatedBy,
    CreatedDate
)
Values
(
    ( '12345678001','201801','999B','4001',0,'19',current_user,now()),
    ( '12345678001','201801','999B','4000',0,'21',current_user,now()),
    ( '12345678001','201801','999B','3000',0,'Rhubarb',current_user,now()),
    ( '12345678001','201801','999B','2000',0,'1',current_user,now()),
    ( '12345678001','201801','999B','1000',0,'20',current_user,now()),
    ( '12345678001','201801','999B','1001',0,'1',current_user,now()),

    ( '12345678002','201801','999B','4001',0,'',current_user,now()),
    ( '12345678002','201801','999B','4000',0,'',current_user,now()),
    ( '12345678002','201801','999B','3000',0,'',current_user,now()),
    ( '12345678002','201801','999B','2000',0,'',current_user,now()),
    ( '12345678002','201801','999B','1000',0,'',current_user,now()),
    ( '12345678002','201801','999B','1001',0,'',current_user,now()),
    
    ( '12345678003','201801','999B','4001',0,'0',current_user,now()),
    ( '12345678003','201801','999B','1001',0,'',current_user,now()),


    -- POPM: Missing previous period
    ( '12345678010','201801','999B','1000',0,'20',current_user,now()),
    ( '12345678010','201801','999B','1001',0,'1',current_user,now()),
    
    --( '12345678010','201712','999B','1000',0,'20',current_user,now()),
    --( '12345678010','201712','999B','1001',0,'1',current_user,now()),

    -- POPM: Blank current period
    ( '12345678011','201801','999B','1000',0,'',current_user,now()),
    ( '12345678011','201801','999B','1001',0,'',current_user,now()),

    ( '12345678011','201712','999B','1000',0,'20',current_user,now()),
    ( '12345678011','201712','999B','1001',0,'1',current_user,now()),
)





Create table dev01.ValidationRule
(
    Rule            Varchar(16) Primary Key,
    Name            Varchar(32) Not Null,
    BaseFormula     Varchar(1024) Not Null,
    CreatedBy       Varchar(16) Not Null,
    CreatedDate     timestamptz Not Null,
    LastUpdatedBy   Varchar(16),
    LastUpdatedDate timestamptz
);

Insert Into dev01.ValidationRule
(
    Rule,
    Name,
    BaseFormula,
    CreatedBy,
    CreatedDate
)
Values
( 'VP','Value Present','question != ""',current_user,now()),
( 'POPM','Period on Period Movement','abs(question - comparison_question) > threshold AND question > 0 AND comparison_question > 0',current_user,now()),
( 'POPZC','Period on Period Zero Continuity','question != comparison_question AND ( question = 0 OR comparison_question = 0 ) AND abs(question - comparison_question) > Threshold',current_user,now()),
( 'QvDQ','Question vs Derived Question','question != comparison_question',current_user,now());






Insert Into dev01.ValidationPeriod
(
    Rule,
    PeriodOffset,
    CreatedBy,
    CreatedDate
)
Values
    ('VP',0,current_user,now()),
    ('POPM',0,current_user,now()),
    ('POPM',1,current_user,now()),
    ('POPZC',0,current_user,now()),
    ('POPZC',1,current_user,now()),
    ('QVDQ',0,current_user,now());


Create table dev01.ValidationForm
(
    ValidationID            serial Primary Key,
    FormID                  Int References dev01.Form(FormID),
    Rule                    Varchar(16) References dev01.ValidationRule(Rule),
    PrimaryQuestion         Varchar(4) Not Null,
    DefaultValue            Varchar(8) Not Null,
    Severity                Varchar(16) Not Null,
    CreatedBy               Varchar(16) Not Null,
    CreatedDate             timestamptz Not Null,
    LastUpdatedBy           Varchar(16),
    LastUpdatedDate         timestamptz
);
Create Index idx_validationform_formrule On dev01.ValidationForm(FormID,Rule);
Create Index idx_validationform_question On dev01.ValidationForm(PrimaryQuestion);


Insert Into dev01.ValidationForm
(
    ValidationID,
    FormID,
    Rule,
    QuestionCode,
    DefaultValue,
    Severity,
    CreatedBy,
    CreatedDate
)
Values
    (10,1,'VP','3000','','W',current_user,now()),        # Text
    (11,1,'VP','2000','','E',current_user,now()),        # Checkbox
    (12,1,'VP','1000','','W',current_user,now()),        # Numeric
    (13,1,'VP','4000','','W',current_user,now()),        # Derived Numeric

    (20,1,'POPM','1000','0','W',current_user,now()),     # Numeric
    (21,1,'POPM','1001','0','E',current_user,now()),     # Numeric

    (30,1,'QVDQ','1000','0','W',current_user,now()),     # Numeric
    (31,1,'QVDQ','1001','0','E',current_user,now()),     # Numeric

    (40,1,'POPZC','1000','0','W',current_user,now()),    # Numeric
    (41,1,'POPZC','1001','0','E',current_user,now()),    # Numeric


Insert Into dev01.ValidationParameter
(
    ValidationID,
    AttributeName,
    AttributeValue,
    Parameter,
    Value,
    Source,
    PeriodOffset,
    CreatedBy,
    CreatedDate
)
Values
( 10, 'Default', 'Default', 'question', '3000', 'response', 0, current_user, now() ),
( 11, 'Default', 'Default', 'question', '2000', 'response', 0, current_user, now() ),
( 12, 'Default', 'Default', 'question', '1000', 'response', 0, current_user, now() ),
( 13, 'Default', 'Default', 'question', '4000', 'response', 0, current_user, now() ),

# Q1000 (cp) vs Q1000 (pp) with threshold of 20000
( 20, 'Default', 'Default', 'question', '1000', 'response', 0, current_user, now() ),
( 20, 'Default', 'Default', 'comparison_question', '1000', 'response', 1, current_user, now() ),
( 20, 'Default', 'Default', 'threshold', '20000', '', 0, current_user, now() ),

# Q1001 (cp) vs Q1001 (pp) with threshold of 0
( 21, 'Default', 'Default', 'question', '1001', 'response', 0, current_user, now() ),
( 21, 'Default', 'Default', 'comparison_question', '1001', 'response', 1, current_user, now() ),
( 21, 'Default', 'Default', 'threshold', '0', '', 0, current_user, now() ),

# Q1000 vs DQ4000
( 30, 'Default', 'Default', 'question', '1000', 'response', 0, current_user, now() ),
( 30, 'Default', 'Default', 'comparison_question', '4000', 'response', 0, current_user, now() ),

# Q1001 vs DQ4001
( 31, 'Default', 'Default', 'question', '1001', 'response', 0, current_user, now() ),                
( 31, 'Default', 'Default', 'comparison_question', '4001', 'response', 0, current_user, now() ),

( 40, 'Default', 'Default', 'question', '1000', 'response', 0, current_user, now() ),                # Q1000 (cp) vs Q1000 (pp) with threshold of 30000
( 40, 'Default', 'Default', 'comparison_question', '1000', 'response', 1, current_user, now() ),
( 40, 'Default', 'Default', 'threshold', '30000', '', 0, current_user, now() ),
( 41, 'Default', 'Default', 'question', '1000', 'response', 0, current_user, now() ),                # Q1001 (cp) vs Q1001 (pp) with threshold of 0
( 41, 'Default', 'Default', 'comparison_question', '1000', 'response', 1, current_user, now() ),
( 41, 'Default', 'Default', 'threshold', '0', '', 0, current_user, now() ),










