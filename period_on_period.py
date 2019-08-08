from . import response_factory

class PeriodOnPeriod(response_factory.ContributorResponse):

    def b_search(match: int, search: list, start=None, end=None):
              midpoint = start + (end - start)//2
              if search[midpoint]["reference"] == match:
                  return (search[midpoint], midpoint)
              elif search[midpoint]["reference"] > match:
                  return b_search(match, search, start, midpoint)
              else:
                  return b_search(match, search, midpoint, end)


