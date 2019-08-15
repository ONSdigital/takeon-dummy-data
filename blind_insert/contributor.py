import random
import datetime
from insert import InsertData
from get_metadata import Metadata
from construct_class import ClassBuild
from sqlalchemy.ext.declarative import declarative_base

class Contributor():
    def __init__(self,Period="",Survey="", start=0, end=10):
        self.Reference = start
        # self.start = start
        self.end = end
        self.Period = Period
        self.Survey = Survey

    def randomise(self):
        self.FormID = random.randint(1,10)
        self.Status = random.choice(['No Response','Validation Failed','Saved not Validated','Overridden','Dead'])
        self.ReceiptDate = None

        if random.randint(0,10) == 1:
            self.LockedBy = 'Alan'
            self.LockedDate = datetime.datetime.now()
        else:
            self.LockedBy = ''
            self.LockedDate = None

        self.FormType = random.choice(['0001','0002','0003','0004'])
        self.Checkletter = random.choice(['A','E','I','X'])
        self.FrozenSicOutdated = '56423'
        self.RuSicOutdated = '56424'
        self.FrozenSic = '56426'
        self.RuSic = '56424'
        self.FrozenEmployees = random.randint(0,500000)
        self.Employees = random.randint(0,500000)
        self.FrozenEmployment = random.randint(0,500000)
        self.Employment = random.randint(0,500000)
        self.FrozenFteEmployment = round(random.uniform(0,500000),2)
        self.FteEmployment = round(random.uniform(0,500000),2)
        self.FrozenTurnover = random.randint(0,1000000)
        self.Turnover = random.randint(0,1000000)
        self.EnterpriseReference = 9900000000 + random.randint(1,1000000)
        self.WowEnterpriseReference = random.randint(0,999999999)
        self.CellNumber = random.randint(0,1000)
        self.Currency = random.choice(['E','S'])
        self.VatReference = '123456789012'
        self.PayeReference = '3210987654321'
        self.CompanyRegistrationNumber = '123456'
        self.NumberLiveLocalUnits = random.randint(1,10000)
        self.NumberLiveVat = random.randint(1,10000)
        self.NumberLivePaye = random.randint(1,10000)
        self.LegalStatus = random.randint(1,9)
        self.ReportingUnitMarker = 'A'
        self.Region = 'AA'
        self.BirthDate = ''
        self.EnterpriseName = 'An enterprise name'
        self.ReferenceName = 'A reference name'
        self.ReferenceAddress = 'A random reference address'
        self.ReferencePostcode = random.choice(['AA9A 9AA','A9A 9AA','A99 9AA','A9 9AA','AA9 9AA','AA99 9AA'])
        self.TradingStyle = 'A random trading style'
        self.Contact = 'Mr contact person'
        self.Telephone = '01234 567 890'
        self.Fax = '+0044 1234 567 891'
        self.SelectionType = 'G'
        self.InclusionExclusion = 'X'
        self.CreatedBy = 'Frank'
        self.CreatedDate = datetime.datetime.now()
        return self
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.Reference < self.end:
            self.Reference += 1
            return self.randomise()
        else:
            raise StopIteration

    def __len__(self):
        return self.end - self.Reference

x = Contributor("202012", "066", 499000000, 49900002)
table_metadata = Metadata(test_env=True, table_name="contributor", db_name="takeon_test")
table_metadata.make_engine()
table = table_metadata.get_table_data()
base = declarative_base()
constructed_class = ClassBuild("contributor", table, base).build_class()
persist_data = InsertData("takeon_test", "contributor", x, constructed_class, test_env=True)
persist_data.build_mapped_class()

# print(len(x))
# for i in x:
#     print(i.__dict__)
