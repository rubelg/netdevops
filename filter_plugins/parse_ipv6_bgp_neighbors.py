import re

class FilterModule(object):
    @staticmethod
    def filters():
      filters = {
              "parse_ipv6_bgp_neighbors": FilterModule.parse_ipv6_bgp_neighbors
              }
      return filters
    @staticmethod
    def parse_ipv6_bgp_neighbors(text):
        pattern = r"""
          (?P<Peer>\S+\:\w+)\s+
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
        ipv6_bgp_neighbors = []

        for line in text.split("\n"):
          match = regex.search(line)
          if match:
             gdict = match.groupdict()
             ipv6_bgp_neighbors.append(gdict)
        return ipv6_bgp_neighbors
