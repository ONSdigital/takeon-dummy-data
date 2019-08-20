import response_factory
from numba import jit

class PeriodOnPeriod(response_factory.ContributorResponse):

    def b_search(self, match: int, search: list, start=None, end=None):
              print("start: {}, end: {}".format(start, end))
              midpoint = start + (end - start)//2
              if search[midpoint]["reference"] == match:
                  return (search[midpoint], midpoint)
              elif search[midpoint]["reference"] > match:
                  return self.b_search(match, search, start, midpoint)
              else:
                  return self.b_search(match, search, midpoint, end)
