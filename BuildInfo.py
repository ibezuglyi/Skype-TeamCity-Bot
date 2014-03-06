__author__ = 'dit'


class BuildInfo():
    def __init__(self, src):
        self.src = src
        self.properties = [u'status', u'webUrl', u'id']

    def _get_build_string(self):
        dict_str = [p.items() for p in self.src]
        r = [v for v in dict_str][0]
        return '\n'.join("{0:s} : {1:s}".format(k, p) for (k, p) in r if k in self.properties)

    def __repr__(self):
        return self._get_build_string()
