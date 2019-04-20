import unittest
from bs4 import BeautifulSoup
from acl.paper import Paper


class TestPaper(unittest.TestCase):

    def test_create_from_element(self):
        element = BeautifulSoup(PAGE.strip(), "html.parser")
        instance = Paper.create_from_page(element, with_arxiv=True)
        self._validate(instance)

    def test_create_from_url(self):
        instance = Paper.create_from_page("https://aclweb.org/anthology/papers/D/D18/D18-1003/", with_arxiv=True)
        self._validate(instance)

    def _validate(self, instance):
        self.assertEqual("D18-1003", instance.anthology_id)
        self.assertEqual("DeClarE: Debunking Fake News and False Claims using Evidence-Aware Deep Learning", instance.title)
        self.assertEqual(("Kashyap Popat", "Subhabrata Mukherjee", "Andrew Yates", "Gerhard Weikum"), instance.authors)
        self.assertEqual("EMNLP", instance.venue)
        self.assertEqual("2018", instance.year)
        self.assertEqual("10", instance.month)
        self.assertEqual("https://www.aclweb.org/anthology/D18-1003", instance.acl_url)
        self.assertEqual("https://arxiv.org/abs/1809.06416", instance.arxiv_url)
        self.assertEqual(ABSTRACT.strip(), instance.abstract)


# URL: https://www.aclweb.org/anthology/papers/D/D18/D18-1003/

PAGE = """
<html lang="en-us" class="gr__aclweb_org"><head><meta charset="utf-8"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no"><!--[if IEMobile]><meta http-equiv=cleartype content=on><![endif]--><title>DeClarE: Debunking Fake News and False Claims using Evidence-Aware Deep Learning - ACL Anthology</title><meta name="generator" content="Hugo 0.54.0"><link href="/anthology/aclicon.ico" rel="shortcut icon" type="image/x-icon"><link rel="stylesheet" href="/anthology/css/main.min.ba3d6e9b0848f8f76897d75085eb7071962d72ee7a4a823e9c2a5e729158e8ad.css" media="screen"><link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous"><meta content="DeClarE: Debunking Fake News and False Claims using Evidence-Aware Deep Learning" name="citation_title"><meta content="Kashyap Popat" name="citation_author"><meta content="Subhabrata Mukherjee" name="citation_author"><meta content="Andrew Yates" name="citation_author"><meta content="Gerhard Weikum" name="citation_author"><meta content="Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing" name="citation_conference_title"><meta content="2018" name="citation_publication_date"><meta content="https://www.aclweb.org/anthology/D18-1003" name="citation_pdf_url"><meta content="22" name="citation_firstpage"><meta content="32" name="citation_lastpage"></head><body data-gr-c-s-loaded="true"><nav class="navbar navbar-expand navbar-light bg-gradient-light shadow-sm py-0 mb-3 mb-md-4 mb-xl-5"><div id="navbar-container" class="container"><a class="navbar-brand" href="/anthology/"><img src="/anthology/images/acl-logo.svg" width="56" alt="ACL Logo">
<span class="d-none d-md-inline pl-md-2">ACL Anthology</span></a><form class="form-inline flex-nowrap ml-auto my-1 my-sm-2" action="/anthology/search/?" method="get"><input id="acl-search-box" class="form-control mr-1 mr-sm-2" name="q" type="search" placeholder="Search..." aria-label="Search">
<button class="btn btn-outline-primary" type="submit"><i class="fas fa-search"></i></button></form></div></nav><div class="container"><aside class="alert alert-warning text-center py-1 mt-n3 mt-md-n4 mt-xl-n5" role="alert">You're viewing the latest version of the ACL Anthology.
<a class="btn btn-warning mx-2" href="https://github.com/acl-org/acl-anthology/issues/170">Give feedback</a></aside></div><div id="main-container" class="container"><section id="main"><h2 id="title"><a href="https://www.aclweb.org/anthology/D18-1003">DeClarE: Debunking Fake News and False Claims using Evidence-Aware Deep Learning</a></h2><p class="lead"><a href="/anthology/people/k/kashyap-popat/">Kashyap Popat</a>,
<a href="/anthology/people/s/subhabrata-mukherjee/">Subhabrata Mukherjee</a>,
<a href="/anthology/people/a/andrew-yates/">Andrew Yates</a>,
<a href="/anthology/people/g/gerhard-weikum/">Gerhard Weikum</a></p><hr><div class="row acl-paper-details"><div class="col col-lg-10 order-2"><div class="card bg-light mb-2 mb-lg-3"><div class="card-body acl-abstract"><h5 class="card-title">Abstract</h5>Misinformation such as fake news is one of the big challenges of our society. Research on automated fact-checking has proposed methods based on supervised learning, but these approaches do not consider external evidence apart from labeled training instances. Recent approaches counter this deficit by considering external sources related to a claim. However, these methods require substantial feature modeling and rich lexicons. This paper overcomes these limitations of prior work with an end-to-end model for evidence-aware credibility assessment of arbitrary textual claims, without any human intervention. It presents a neural network model that judiciously aggregates signals from external evidence articles, the language of these articles and the trustworthiness of their sources. It also derives informative features for generating user-comprehensible explanations that makes the neural network predictions transparent to the end-user. Experiments with four datasets and ablation studies show the strength of our method.</div></div><dl><dt>Anthology ID:</dt><dd>D18-1003</dd><dt>Volume:</dt><dd><a href="/anthology/volumes/proceedings-of-the-2018-conference-on-empirical-methods-in-natural-language-processing/">Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing</a></dd><dt>Month:</dt><dd>October-November</dd><dt>Year:</dt><dd>2018</dd><dt>Address:</dt><dd>Brussels, Belgium</dd><dt>Venue:</dt><dd><a href="/anthology/venues/emnlp/">EMNLP</a></dd><dt>SIG:</dt><dd></dd><dt>Publisher:</dt><dd>Association for Computational Linguistics</dd><dt>Pages:</dt><dd>22–32</dd><dt>URL:</dt><dd><a href="https://www.aclweb.org/anthology/D18-1003">https://www.aclweb.org/anthology/D18-1003</a></dd><dt>DOI:</dt><dd></dd><dt class="acl-button-row">Bib Export formats:</dt><dd class="acl-button-row"><a class="btn btn-secondary btn-sm" href="/anthology/papers/D/D18/D18-1003.bib">BibTeX</a>
<a class="btn btn-secondary btn-sm" href="/anthology/papers/D/D18/D18-1003.xml">MODS XML</a>
<a class="btn btn-secondary btn-sm" href="/anthology/papers/D/D18/D18-1003.endf">EndNote</a>
<button type="button" class="btn btn-clipboard btn-secondary btn-sm" data-clipboard-text="@inproceedings{popat-etal-2018-declare,
    title = &quot;DeClarE: Debunking Fake News and False Claims using Evidence-Aware Deep Learning&quot;,
    author = &quot;Popat, Kashyap  and
      Mukherjee, Subhabrata  and
      Yates, Andrew  and
      Weikum, Gerhard&quot;,
    booktitle = &quot;Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing&quot;,
    month = oct # &quot;-&quot; # nov,
    year = &quot;2018&quot;,
    address = &quot;Brussels, Belgium&quot;,
    publisher = &quot;Association for Computational Linguistics&quot;,
    url = &quot;https://www.aclweb.org/anthology/D18-1003&quot;,
    pages = &quot;22--32&quot;,
    abstract = &quot;Misinformation such as fake news is one of the big challenges of our society. Research on automated fact-checking has proposed methods based on supervised learning, but these approaches do not consider external evidence apart from labeled training instances. Recent approaches counter this deficit by considering external sources related to a claim. However, these methods require substantial feature modeling and rich lexicons. This paper overcomes these limitations of prior work with an end-to-end model for evidence-aware credibility assessment of arbitrary textual claims, without any human intervention. It presents a neural network model that judiciously aggregates signals from external evidence articles, the language of these articles and the trustworthiness of their sources. It also derives informative features for generating user-comprehensible explanations that makes the neural network predictions transparent to the end-user. Experiments with four datasets and ablation studies show the strength of our method.&quot;,
}"><i class="far fa-clipboard pr-2"></i>Copy BibTeX to Clipboard</button></dd><dt class="acl-button-row">Video:</dt><dd class="acl-button-row"><a href="https://vimeo.com/305203523" class="btn btn-attachment btn-sm"><i class="fas fa-video"></i>&nbsp;https://vimeo.com/305203523</a></dd></dl></div><div class="acl-paper-link-block"><a class="btn btn-primary" href="https://www.aclweb.org/anthology/D18-1003" title="Open PDF of 'DeClarE: Debunking Fake News and False Claims using Evidence-Aware Deep Learning'"><i class="far fa-file-pdf"></i><span class="pl-2">PDF</span></a>
<a class="btn btn-secondary" href="/anthology/papers/D/D18/D18-1003.bib" title="Export 'DeClarE: Debunking Fake News and False Claims using Evidence-Aware Deep Learning' to bib format"><i class="fas fa-file-export"></i><span class="pl-2 transform-lower-sm">Bib</span><span class="d-none d-sm-inline">TeX</span></a>
<a class="btn btn-secondary" href="https://www.google.com/search?q=DeClarE%3A+Debunking+Fake+News+and+False+Claims+using+Evidence-Aware+Deep+Learning" title="Search for 'DeClarE: Debunking Fake News and False Claims using Evidence-Aware Deep Learning' on Google"><i class="fas fa-search"></i><span class="pl-sm-2 d-none d-sm-inline">Search</span></a>
<a class="btn btn-attachment" href="https://vimeo.com/305203523" title="Open video for 'DeClarE: Debunking Fake News and False Claims using Evidence-Aware Deep Learning'"><i class="fas fa-video"></i><span class="pl-2">Video</span></a></div></div><hr></section></div><footer class="bg-gradient-light py-2 py-xl-3 mt-3 mt-md-4 mt-xl-5"><div class="container"><nav role="navigation" class="nav w-100 justify-content-center"><a class="nav-link" href="/anthology/info/credits/">Credits</a>
<a class="nav-link" href="/anthology/faq/">FAQ</a>
<a class="nav-link" href="/anthology/info/contrib/">For Contributors</a>
<a class="nav-link" href="http://bit.ly/aclAnthologyQ">Ingestion Queue</a>
<a class="nav-link" href="https://github.com/acl-org/acl-anthology/issues/">Issues</a>
<a class="nav-link" href="/anthology/info/corrections/">Request Corrections</a>
<a class="nav-link" href="/anthology/info/volunteer/">Volunteer!</a></nav><hr class="mt-2"></div><div class="container"><p class="text-muted small px-1"><span class="float-right mt-2"><a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png"></a></span>
ACL materials are Copyright ©&nbsp;1963–2019 ACL; other materials are copyrighted by their respective copyright holders. Materials prior to 2016 here are licensed under the <a href="https://creativecommons.org/licenses/by-nc-sa/3.0/">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 International License</a>. Permission is granted to make copies for the purposes of teaching and research. Materials published in or after 2016 are licensed on a <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.</p><p class="text-muted small px-1"><a href="http://mjpost.github.io/">Matt Post</a> (Editor, 2019–) |
<a href="http://www.comp.nus.edu.sg/~kanmy/">Min-Yen Kan</a> (Editor, 2008–2018) |
<a href="http://stevenbird.net/">Steven Bird</a> (Editor, 2001–2007)</p></div></footer><script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script><script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script><script>$(function(){$('[data-toggle="tooltip"]').tooltip()})</script><script src="/anthology/js/clipboard.min.js"></script><script>$(document).ready(function(){if(ClipboardJS.isSupported()){new ClipboardJS(".btn-clipboard");$(".btn-clipboard").removeClass("d-none");}});</script></body><div><div class="gr_-editor gr-iframe-first-load" style="display: none;"><div class="gr_-editor_back"></div><iframe class="gr_-ifr gr-_dialog-content"></iframe></div></div><grammarly-card><div></div></grammarly-card><span class="gr__tooltip"><span class="gr__tooltip-content"></span><i class="gr__tooltip-logo"></i><span class="gr__triangle"></span></span></html>
"""

ABSTRACT = """
Misinformation such as fake news is one of the big challenges of our society. Research on automated fact-checking has proposed methods based on supervised learning, but these approaches do not consider external evidence apart from labeled training instances. Recent approaches counter this deficit by considering external sources related to a claim. However, these methods require substantial feature modeling and rich lexicons. This paper overcomes these limitations of prior work with an end-to-end model for evidence-aware credibility assessment of arbitrary textual claims, without any human intervention. It presents a neural network model that judiciously aggregates signals from external evidence articles, the language of these articles and the trustworthiness of their sources. It also derives informative features for generating user-comprehensible explanations that makes the neural network predictions transparent to the end-user. Experiments with four datasets and ablation studies show the strength of our method.
"""
