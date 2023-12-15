import re

class FilterModule(object):
    @staticmethod
    def filters():
      filters = {
              "parse_ospf_neighbors": FilterModule.parse_ospf_neighbors
              }
      return filters
    @staticmethod
    def parse_ospf_neighbors(text):
        pattern = r"""
          (?P<Address>\d+\.\d+\.\d+\.\d+)\s+
          (?P<Interface>\S+)\s+
          (?P<State>\S+)\s+
          (?P<ID>\S+)\s+
          (?P<PRI>\S+)\s+
          (?P<Dead>\S+)
          """

        regex = re.compile(pattern, re.VERBOSE)
        ospf_neighbors = []

        for line in text.split("\n"):
          match = regex.search(line)
          if match:
             gdict = match.groupdict()
             ospf_neighbors.append(gdict)
        return ospf_neighbors
