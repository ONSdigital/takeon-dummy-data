from . import response_factory
import math

class PreviousPeriods(response_factory.ContributorResponse):
    def split_period(self):
        string_period = str(self.period)
        return (string_period[:4], string_period[4:])

    def decriment(self):
        period_mappings = {"M": 1, "Q": 3, "Y": 1}
        period_atoms = self.split_period()
        if self.form["periodicity"] == "Y":
            new_year = int(period_atoms[0]) - period_mappings["Y"]
            return str(new_year) + period_atoms[1]
        else:
            print("period ratio: {}".format(int(period_atoms[1])/12))
            if int(period_atoms[1])/12 != 1:
                year_part = math.floor(int(period_atoms[1])/12)
                print(year_part)
            else:
                year_part = 0
                print(year_part)

            if 12 < int(period_atoms[1]) - period_mappings[self.form["periodicity"]] < 1:
                month_part = str(int(period_atoms[1]) % 12 + 1)
                print("month part: {}".format(month_part))
            else:
                month_part = str(int(period_atoms[1]) - period_mappings[self.form["periodicity"]])

            if len(month_part) < 2:
                month_part = "0" + month_part

            new_year = int(period_atoms[0]) - year_part
            print("new year: {}".format(new_year))
            print("new month: {}".format(month_part))
            new_period = str(new_year) + str(month_part)
            print("new period: {}".format(new_period))

            return new_period
