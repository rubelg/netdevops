import re

class FilterModule(object):
    @staticmethod
    def filters():
      filters = {
              "parse_isis_neighbors": FilterModule.parse_isis_neighbors
              }
      return filters
    @staticmethod
    def parse_isis_neighbors(text):
        pattern = r"""
          (?P<Interface>\S+)\s+
          (?P<Neighbor>\S+)\s+
          (?P<Level>\d+)\s+
          (?P<State>\S+)\s+
#          (?P<Hold>(\d+)\s+
#          (?P<SNPA>\(\S+|\s+)
          """

        regex = re.compile(pattern, re.VERBOSE)
        isis_neighbors = []

        for line in text.split("\n"):
          match = regex.search(line)
          if match:
             gdict = match.groupdict()
             isis_neighbors.append(gdict)
        return isis_neighbors
