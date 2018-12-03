import requests
import time
from bs4 import BeautifulSoup, Comment
from acl.paper import Paper


class Conference():

    def __init__(self, url):
        self.url = url
        self.anthologies = {}

    @classmethod
    def EMNLP(cls, year):
        return cls._make_conference("emnlp", year)

    @classmethod
    def ACL(cls, year):
        return cls._make_conference("acl", year)

    @classmethod
    def _make_conference(cls, name, year):
        url = "https://aclanthology.info/events/{}-{}".format(name, year)
        return Conference(url)

    def retrieve(self, anthology="", interval=1.0,
                 with_arxiv=False):
        r = requests.get(self.url)
        page = BeautifulSoup(r.content, "html.parser")
        if not r.ok:
            return {}
        else:
            return self.retrieve_from_element(page, anthology,
                                              interval, with_arxiv)

    def retrieve_from_element(self, page, anthology="", interval=1.0,
                              with_arxiv=False):

        self.set_anthology(page)
        if anthology:
            targets = [anthology]
        else:
            targets = list(self.anthologies.keys())

        papers = {}

        for t in targets:
            papers[t] = []
            cursor = page.find("h4", {"id": t})
            cursor = cursor.next_element
            while cursor is not None and cursor.name not in ["h4", "div"]:
                if isinstance(cursor, Comment):
                    cursor = cursor.next_element
                    continue

                if cursor.name != "p":
                    cursor = cursor.next_element
                    continue

                href = cursor.find("strong").find("a").get("href")
                url = "https://aclanthology.info" + href
                p = Paper.create_from_page(url, with_arxiv)
                if p is not None:
                    papers[t].append(p)
                time.sleep(interval)
                cursor = cursor.next_element

        return papers

    def set_anthology(self, element):
        sections = element.find_all("h4")
        content = None
        for s in sections:
            title = s.get_text()
            title = title.lower().replace(" ", "")
            if title == "tableofcontents":
                content = s
                break

        if content is None:
            return self

        header = True
        for row in content.find_next("table").find_all("tr"):
            if header:
                header = False
                continue

            items = row.find_all("td")
            if len(items) >= 2:
                anthology_id = items[0].get_text().strip()
                anthology_name = items[1].get_text().strip()
                self.anthologies[anthology_id] = anthology_name

        return self
