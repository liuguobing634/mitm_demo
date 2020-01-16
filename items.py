

class VideoInfo(object):

    def __init__(self):
        self._nick = ''
        self._addrs = []
        self._desc = ''

    @property
    def nick(self):
        return self._nick

    @nick.setter
    def nick(self, nick):
        self._nick = nick

    def add_addr(self, addr):
        self._addrs.append(addr)

    @property
    def addrs(self):
        return self._addrs

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, desc):
        self._desc = desc
