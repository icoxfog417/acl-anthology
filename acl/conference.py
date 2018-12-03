class Conference():

    def __init__(self, url):
        self.url = url

    @classmethod
    def EMNLP(cls, year):
        return cls._make_conference("emnlp", year)

    @classmethod
    def ACL(cls, year):
        return cls._make_conference("acl", year)

    def _make_conference(cls, name, year):
        url = "https://aclanthology.info/events/{}-{}".format(name, year)
        return Conference(url)
