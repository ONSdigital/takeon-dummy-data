from . import response_factory

class PeriodOnPeriod(response_factory.ContributorResponse):

    def b_search(self, match: int, search: list):
             mid_point = math.floor(len(search)/2)
             if search[mid_point]["reference"] == match:
                 return search[mid_point]
             elif search[mid_point]["reference"] > match:
                 return b_search(search[:mid_point], match)
             else:
                 return b_search(search[mid_point:], match)


