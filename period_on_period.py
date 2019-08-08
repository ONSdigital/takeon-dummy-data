from . import response_factory

class PeriodOnPeriod(response_factory.ContributorResponse):

    def b_search(self, match: int, search: list, start=0, end=len(search):
             midpoint = math.floor(len(search)/2)
             if search[midpoint]["reference"] == match:
                 return search[midpoint]
             elif search[midpoint]["reference"] > match:
                 return b_search(search, match, start=midpoint+1, end)
             else:
                 return b_search(search, match, start, midpoint-1)


