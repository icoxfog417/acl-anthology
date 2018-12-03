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
            print("Download {}.".format(t))
            paper_count = self.anthologies[t].count
            pbar = tqdm(total=paper_count)

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
                    pbar.update(1)
                    if len(papers) == paper_count:
                        break

                time.sleep(interval)
                cursor = cursor.next_element
            pbar.close()

        r = ResultSet(papers, with_arxiv)
        return r

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
            if len(items) >= 3:
                anthology_id = items[0].get_text().strip()
                name = items[1].get_text().strip()
                count = int(items[2].get_text().strip())
                a = Anthology(name, count)
                self.anthologies[anthology_id] = a

        return self


class Anthology():

    def __init__(self, name, count):
        self.name = name
        self.count = count
