import pandas as pd


class ResultSet():

    def __init__(self, papers, with_arxiv):
        self.papers = papers
        self.with_arxiv = with_arxiv

    def to_dataframe(self):
        data = []
        for anth in self.papers:
            for p in self.papers[anth]:
                o = p.to_json(with_arxiv=self.with_arxiv)
                o["anthology"] = anth
                data.append(o)

        df = pd.DataFrame(data)
        return df
