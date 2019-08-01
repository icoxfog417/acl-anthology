import requests
import time
from bs4 import BeautifulSoup, Comment
from tqdm import tqdm
from acl.paper import Paper
from acl.result_set import ResultSet


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

    def retrieve(self, anthology="", interval=0.5,
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
            print("Download {}.".format(t))
            paper_count = self.anthologies[t].count
            pbar = tqdm(total=paper_count)

            papers[t] = []
            area = page.find("div", {"id": t.lower()})
            _papers = area.find_all("p")
            for p in _papers:
                href = p.find("strong").find("a").get("href")
                url = "https://www.aclweb.org" + href
                p = Paper.create_from_page(url, with_arxiv)
                if p is not None:
                    papers[t].append(p)
                    pbar.update(1)
                    if len(papers) == paper_count:
                        break

                time.sleep(interval)
            pbar.close()

        r = ResultSet(papers, with_arxiv)
        return r

    def set_anthology(self, element):
        contents = element.find("ul", {"class": "list-pl-responsive"})
        for c in contents.find_all("li"):
            title = c.find("a")
            name = title.get_text().strip()
            anthology_id = title.get("href").replace("#", "").upper()
            count_element = title.find_next("span")
            count = int(count_element.get_text().split()[0])
            a = Anthology(name, count)
            self.anthologies[anthology_id] = a

        return self


class Anthology():

    def __init__(self, name, count):
        self.name = name
        self.count = count
