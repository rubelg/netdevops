import re

class FilterModule(object):
    @staticmethod
    def filters():
      filters = {
              "parse_bgp_neighbors": FilterModule.parse_bgp_neighbors
              }
      return filters
    @staticmethod
    def parse_bgp_neighbors(text):
        pattern = r"""
          (?P<Peer>\d+\.\d+\.\d+\.\d+)\s+
          (?P<AS>\d+)\s+
          (?P<InPkt>\d+)\s+
          (?P<OutPkt>\d+)\s+
          (?P<OutQ>\d+)\s+
          (?P<Flaps>\d+)\s+
          (?P<Last>(\S+|\s+))\s+
#          (?P<LastUpDwn>\S+\s+\S+)\s+
          (?P<UpDwnTime>\S+)\s+
          (?P<State>\S+)
          """

        regex = re.compile(pattern, re.VERBOSE)
        bgp_neighbors = []

        for line in text.split("\n"):
          match = regex.search(line)
          if match:
             gdict = match.groupdict()
             bgp_neighbors.append(gdict)
        return bgp_neighbors
