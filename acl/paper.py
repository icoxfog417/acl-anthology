import re
import calendar
import arxiv
import requests
from bs4 import BeautifulSoup


class Paper():

    def __init__(self,
                 anthology_id="",
                 title="", authors=(),
                 venue="", year="", month="",
                 acl_url="", arxiv_url="",
                 abstract=""):
        self.anthology_id = anthology_id
        self.title = title
        self.authors = authors
        self.venue = venue
        self.year = year
        self.month = month
        self.acl_url = acl_url
        self.arxiv_url = arxiv_url
        self.abstract = abstract

    @classmethod
    def create_from_page(cls, page, with_arxiv=False):
        _page = page
        if isinstance(page, str):
            # The page is directed by URL.
            r = requests.get(page)
            _page = BeautifulSoup(r.content, "html.parser")
            if not r.ok:
                return None

        title_el = _page.find("h2", {"id": "title"}).find("a")
        title = title_el.get_text().strip()

        authors_el = title_el.find_next("p", {"class": "lead"})
        authors = ()
        if authors_el:
            authors = authors_el.find_all("a")
            authors = tuple(a.get_text().strip() for a in authors
                            if a.get("href").startswith("/anthology/people/"))

        area = _page.find("div", {"class": "acl-paper-details"})
        abstract_el = area.find("div", {"class": "acl-abstract"})
        abstract = ""
        if abstract_el:
            abstract_el.find("h5").decompose()
            abstract = abstract_el.get_text().strip()

        attributes = area.find("dl")
        paper = {
            "Anthology ID": "",
            "Venue": "",
            "Year": "",
            "Month": "",
            "URL": ""
        }
        month_dict = dict((v, k) for k, v in
                          enumerate(calendar.month_name))

        for item in attributes.find_all("dt"):
            value = item.find_next("dd")
            if value is None:
                continue
            attr = item.get_text().strip().replace(":", "")
            value = value.get_text().strip()
            if attr == "Anthology ID":
                paper[attr] = value
            elif attr == "Month":
                value = value.split("-")[0]
                value = month_dict[value]
                paper[attr] = str(value)
            elif attr == "Year":
                paper[attr] = value
            elif attr == "Venue":
                paper[attr] = value
            elif attr == "URL":
                paper[attr] = value

        instance = cls(
            paper["Anthology ID"], title, authors,
            paper["Venue"], paper["Year"], paper["Month"],
            paper["URL"]
        )
        instance.abstract = abstract

        if with_arxiv:
            abstract, url = cls.get_arxiv(title)
            instance.arxiv_url = url
            instance.abstract = abstract

        return instance

    @classmethod
    def get_arxiv(cls, title):
        results = arxiv.query(query=title, max_results=1)
        if len(results) > 0:
            paper = results[0]
            abstract = paper.summary.replace("\n", " ")
            url = paper.arxiv_url.replace("http://", "https://")
            url = re.sub("v\\d+$", "", url)
            return abstract, url
        else:
            return "", ""

    def to_json(self, with_arxiv=False):
        obj = {
            "anthology_id": self.anthology_id,
            "title": self.title,
            "authors": ",".join(self.authors),
            "venue": self.venue,
            "year": self.year,
            "month": self.month,
            "acl_url": self.acl_url,
            "abstract": self.abstract
        }

        if with_arxiv:
            obj["arxiv_url"] = self.arxiv_url

        return obj
