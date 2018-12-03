import unittest
from bs4 import BeautifulSoup
from acl.paper import Paper


class TestPaper(unittest.TestCase):

    def test_create_from_element(self):
        element = BeautifulSoup(PAGE.strip(), "html.parser")
        instance = Paper.create_from_page(element, with_arxiv=True)
        self._validate(instance)

    def test_create_from_url(self):
        instance = Paper.create_from_page("https://aclanthology.info/papers/D18-1003/d18-1003", with_arxiv=True)
        self._validate(instance)

    def _validate(self, instance):
        self.assertEqual("D18-1003", instance.anthology_id)
        self.assertEqual("DeClarE: Debunking Fake News and False Claims using Evidence-Aware Deep Learning", instance.title)
        self.assertEqual(("Kashyap Popat", "Subhabrata Mukherjee", "Andrew Yates", "Gerhard Weikum"), instance.authors)
        self.assertEqual("EMNLP", instance.venue)
        self.assertEqual("2018", instance.year)
        self.assertEqual("10", instance.month)
        self.assertEqual("http://aclweb.org/anthology/D18-1003", instance.acl_url)
        self.assertEqual("https://arxiv.org/abs/1809.06416", instance.arxiv_url)
        self.assertEqual(ABSTRACT.strip(), instance.abstract)


PAGE = """
<html lang="en" class="gr__aclanthology_info"><head>
    <meta charset="utf-8">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">

    <!-- Mobile viewport optimization h5bp.com/ad -->
    <meta name="HandheldFriendly" content="True">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">

    <!-- Mobile IE allows us to activate ClearType technology for smoothing fonts for easy reading -->
    <!--[if IEMobile]>
      <meta http-equiv="cleartype" content="on">
    <![endif]-->

    <title>
      DeClarE: Debunking Fake News and False Claims using Evidence-Aware Deep Learning
       - 
      ACL Anthology
    </title>
    <link href="https://aclanthology.coli.uni-saarland.de/catalog/opensearch.xml" title="ACL Anthology" type="application/opensearchdescription+xml" rel="search">
    <link href="/assets/aclicon-4b361d20024e07166116ed729b9dc696.ico" rel="shortcut icon" type="image/vnd.microsoft.icon">
    <link href="/assets/application-df3251187e128df55318b4136dccc705.css" media="screen" rel="stylesheet">
    <script src="/assets/application-61ecc8e8991d256e6abe6abf56a78a80.js"></script>
    <meta content="authenticity_token" name="csrf-param">
<meta content="XRy1OsUAk0KKH9D+uem2XvF8hE4KOhKPQ6hUsaJMEzU=" name="csrf-token">
     

    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
      <script src="/assets/flot/excanvas.min-acb26f3790770ef2451a6af29a42b712.js"></script>
    <![endif]-->

  </head>
  <body class="blacklight-papers blacklight-papers-show">
  <div id="header-navbar-fixed-top" class="navbar navbar-fixed-top">
 <div class="navbar-inner">
  <div class="container">
    <div class="row">
      <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </a>
      <div class="span3">
        <a class="brand" href="/">ACL Anthology</a>
      </div>
      <div class="span6 clearfix" id="searchbar">         
          <form accept-charset="UTF-8" action="https://aclanthology.info/catalog" class="search-query-form form-inline clearfix" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="✓"></div>
    <input name="shortid" type="hidden" value="D18-1003"> 

      <div class="pull-left">
        <label for="search_field" class="hide-text">Search in</label>
        <select class="search_field input-small" id="search_field" name="search_field" title="Targeted search options"><option value="all_fields">All Fields</option>
<option value="title">Title</option>
<option value="author">Author</option>
<option value="publish_date">Year</option>
<option value="venue_name">Venue</option>
<option value="sig_name">SIG</option></select>
        <span class="hide-text">for</span>
      </div>
       <div class="input-append pull-left">
        <label for="q" class="hide-text">Search...</label>
         <input class="search_q q" id="q" name="q" placeholder="Search..." type="text">
        <button type="submit" class="btn btn-primary search-btn" id="search">
          <span class="submit-search-text">Search</span>
          <i class="icon-search icon-white"></i>
        </button>

       </div>

</form>
      </div>

      <div class="span3 nav-collapse">
            <div class="util-links-login">
        <a href="/users/sign_in">Login</a>
    </div>


  <div class="util-links-other">
      <a href="/bookmarks">Bookmarks</a>
    |
    <a href="/search_history">History</a>
  </div>

        <!--% render :partial=>'shared/facets' %>-->

      </div>

    </div>
  </div>
</div>
</div>


  <div id="ajax-modal" class="modal hide fade" tabindex="-1"></div>

<!-- /container -->
  <div id="main-container" class="container">
            <!-- Top bar -->
            <div id="search-found" class="row hidden-phone">
              
            </div>
            <!-- /Top bar -->
            <div id="content" class="row">
                <div class="span12">
                  <div id="main-flashes">
                    <div class="flash_messages">
</div>

                  </div>
                  <!-- Meta tags used by Google Scholar to crawl and index the anthology -->

<!-- Main information for the paper -->
<div class="row">
  <div class="span12 page-header">
    <h2>
        <a href="http://aclweb.org/anthology/D18-1003"><img alt="Pdf" height="24" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'DeClarE: Debunking Fake News and False Claims using Evidence-Aware Deep Learning'" width="24"></a>
<!-- , :target => "_blank" %> -->

      <a href="/papers/D18-1003/d18-1003.bib"><img alt="Export" height="24" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'DeClarE: Debunking Fake News and False Claims using Evidence-Aware Deep Learning' to bib format" width="24"></a>
      <a href="https://www.google.com/search?q=DeClarE: Debunking Fake News and False Claims using Evidence-Aware Deep Learning"><img alt="Search" height="24" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'DeClarE: Debunking Fake News and False Claims using Evidence-Aware Deep Learning' on Google" width="24"></a>
<!-- , :target => "_blank" %> -->
      <a href="http://aclweb.org/anthology/D18-1003">DeClarE: Debunking Fake News and False Claims using Evidence-Aware Deep Learning</a>
<!-- , :target => "_blank" %> -->
    </h2>
  </div>

  <div class="span9">
    <dl class="dl-horizontal">
      <dt><strong>Anthology:</strong></dt>
      <dd>D18-1003&nbsp;</dd>


      <dt>Volume:</dt>
      <dd><a href="/volumes/proceedings-of-the-2018-conference-on-empirical-methods-in-natural-language-processing">Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing</a>&nbsp;</dd>
        <dt><strong>Authors:</strong></dt>
      <dd>
            <a href="/people/kashyap-popat">Kashyap Popat</a>
                    | <a href="/people/subhabrata-mukherjee">Subhabrata Mukherjee</a>
                    | <a href="/people/andrew-yates">Andrew Yates</a>
                    | <a href="/people/gerhard-weikum">Gerhard Weikum</a>
        &nbsp;
      </dd>

      <dt><strong>Month:</strong></dt>
      <dd>October-November&nbsp;</dd>
      <dt><strong>Year:</strong></dt>
      <dd>2018&nbsp;</dd>

        <dt><strong>Venue:</strong></dt>
      <dd>
<!--            <a href="/events/emnlp-2018">EMNLP</a> -->
            <a href="/venues/emnlp">EMNLP</a>
        &nbsp;
      </dd>

      <dt><strong>Address:</strong></dt>
      <dd>Brussels, Belgium&nbsp;</dd>

        <dt><strong>SIG:</strong></dt>
      <dd>
&nbsp;
      </dd>

      <dt><strong>Publisher:</strong></dt>
      <dd>Association for Computational Linguistics&nbsp;</dd>
      <dt><strong>Pages:</strong></dt>
      <dd>22–32&nbsp;</dd>
      <dt><strong>URL:</strong></dt>
      <dd><a href="http://aclweb.org/anthology/D18-1003">http://aclweb.org/anthology/D18-1003</a>&nbsp;</dd>
<!-- , :target => "_blank" if @paper.url  %>&nbsp;</dd> -->
      <dt><strong>DOI:</strong></dt>
      <dd>&nbsp;</dd>
<!-- , :target => "_blank" if @paper.doi %>&nbsp;</dd> -->
      <dt><strong>MRF:</strong></dt>
     <dd>
<!-- 
       < % = link_to "LaTeXML", "http://aclweb.org/anthology/#{@paper.mrf[0]}/#{@paper.mrf[0..2]}/#{@paper.mrf}", title: "Generated by LaTeXML, for publications originating from TeX sources" % >, :target => "_blank" if @paper.mrf %>&nbsp;
--> 
     &nbsp;</dd>
<!--  
        :  &nbsp;
-->
      <dt><strong>Bibtype:</strong></dt>
      <dd>inproceedings&nbsp;</dd>
      <dt><strong>Bibkey:</strong></dt>
      <dd>popat-EtAl:2018:EMNLP&nbsp;</dd>
      <dt><strong>Bib Export formats:</strong></dt>
      <dd>
        <a class="export" href="/papers/D18-1003/d18-1003.bib">BibTeX</a>
        <a class="export" href="/papers/D18-1003/d18-1003.ris">RIS</a>
        <a class="export" href="/papers/D18-1003/d18-1003.endf">Endnote</a>
        <a class="export" href="/papers/D18-1003/d18-1003.xml">MODS XML</a>
        <a class="export" href="/papers/D18-1003/d18-1003.word">MS Word '07</a>
      </dd>
      
    </dl>
  </div>

  <!-- Papers actions -->
  </div>
</div>

                </div>    
            </div> 



<div class="container">
	<hr>
	<div id="footer" class="span12">
		<p>ACL materials are Copyright © 1963-2018 ACL; other materials are copyrighted by their respective copyright holders.  Materials prior to 2016 here are licensed under the <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 International License</a>. Permission is granted to make copies for the purposes of teaching and research.  Materials published in or after 2016 are licensed on a <a href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 License</a>.</p>

		<p style="text-align: center"><a href="/credits">Credits</a> | 
		  <a href="/contributors">Contributors</a> | 
		  <a href="/corrections">Corrections</a> | 
                  <a href="http://bit.ly/aclAnthologyQ">Ingestion Queue</a> | 
                  <a href="https://github.com/WING-NUS/acl/issues">Issues</a> | 
		  <a href="/faq">FAQ</a> 
		</p>
		
		<p><a href="http://www.comp.nus.edu.sg/~kanmy/">Min-Yen Kan</a> (Editor, 2008-) / 
		<a href="http://stevenbird.net/">Steven Bird</a> (Editor, 2001-2007)</p>

<!--		<a href="http://creativecommons.org/licenses/by-nc-sa/4.0/" id="cc_icon" rel="license"><img alt="Creative Commons License" border="0" src="/assets/88x31-42fe130ae66482ef422a8aa0a3896f41.png" /></a> -->
		<a href="http://creativecommons.org/licenses/by/4.0/" id="cc_icon" rel="license"><img alt="Creative Commons License" border="0" src="/assets/cc4by-6c00ea211acf121a2b231d0c31c54b6c.png"></a> 
	</div>
</div>

    

</body></html>
"""

ABSTRACT = """
Misinformation such as fake news is one of the big challenges of our society. Research on automated fact-checking has proposed methods based on supervised learning, but these approaches do not consider external evidence apart from labeled training instances. Recent approaches counter this deficit by considering external sources related to a claim. However, these methods require substantial feature modeling and rich lexicons. This paper overcomes these limitations of prior work with an end-to-end model for evidence-aware credibility assessment of arbitrary textual claims, without any human intervention. It presents a neural network model that judiciously aggregates signals from external evidence articles, the language of these articles and the trustworthiness of their sources. It also derives informative features for generating user-comprehensible explanations that makes the neural network predictions transparent to the end-user. Experiments with four datasets and ablation studies show the strength of our method.
"""
