import unittest
from bs4 import BeautifulSoup
from acl.conference import Conference


class TestConference(unittest.TestCase):

    def test_set_anthology(self):
        element = BeautifulSoup(PAGE.strip(), "html.parser")
        c = Conference("http://dummy")
        c.set_anthology(element)

        self.assertEqual(len(c.anthologies), 4)

        for i, k in enumerate(c.anthologies):
            a = c.anthologies[k]
            if i == 0:
                self.assertEqual(k, "J00-1")
                self.assertEqual(a.name, "Computational Linguistics, Volume 26, Number 1, March 2000")
                self.assertEqual(a.count, 7)
            elif i == 1:
                self.assertEqual(k, "J00-2")
                self.assertEqual(a.name, "Computational Linguistics, Volume 26, Number 2, June 2000")
                self.assertEqual(a.count, 18)
            elif i == 2:
                self.assertEqual(k, "J00-3")
                self.assertEqual(a.name, "Computational Linguistics, Volume 26, Number 3, September 2000")
                self.assertEqual(a.count, 12)
            elif i == 3:
                self.assertEqual(k, "J00-4")
                self.assertEqual(a.name, "Computational Linguistics, Volume 26, Number 4, December 2000")
                self.assertEqual(a.count, 14)

    def test_retrieve_from_element(self):
        element = BeautifulSoup(PAGE.strip(), "html.parser")
        c = Conference("http://dummy")
        result = c.retrieve_from_element(element, "J00-1")
        papers = result.papers
        self.assertEqual(len(papers), 1)
        for k in result.papers:
            self.assertEqual(k, "J00-1")
            self.assertEqual(len(papers[k]), 7)
            self.assertEqual(papers[k][0].title, "Introduction to the Special Issue on Finite-State Methods in NLP")
            self.assertEqual(papers[k][-1].title, "Advertisements")

    def test_retrieve_from_url(self):
        c = Conference.ACL(2018)
        result = c.retrieve("P18-5")
        self.assertEqual(len(result.papers), 1)
        papers = result.papers
        for k in papers:
            self.assertEqual(k, "P18-5")
            self.assertEqual(len(papers[k]), 9)
            self.assertEqual(papers[k][0].title, "Proceedings of ACL 2018, Tutorial Abstracts")
            self.assertEqual(papers[k][-1].title, "Multi-lingual Entity Discovery and Linking")


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
      CL (2000)
       - 
      ACL Anthology
    </title>
    <link href="https://aclanthology.coli.uni-saarland.de/catalog/opensearch.xml" title="ACL Anthology" type="application/opensearchdescription+xml" rel="search">
    <link href="/assets/aclicon-4b361d20024e07166116ed729b9dc696.ico" rel="shortcut icon" type="image/vnd.microsoft.icon">
    <link href="/assets/application-df3251187e128df55318b4136dccc705.css" media="screen" rel="stylesheet">
    <script src="/assets/application-61ecc8e8991d256e6abe6abf56a78a80.js"></script>
    <meta content="authenticity_token" name="csrf-param">
<meta content="G3T/6PXP/cNdpLCPlORLLautK7kMmPOX1FJLhgrRb8Y=" name="csrf-token">
     

    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
      <script src="/assets/flot/excanvas.min-acb26f3790770ef2451a6af29a42b712.js"></script>
    <![endif]-->

  </head>
  <body class="blacklight-events blacklight-events-show" data-gr-c-s-loaded="true" style="">
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
          <form accept-charset="UTF-8" action="https://aclanthology.coli.uni-saarland.de/catalog" class="search-query-form form-inline clearfix" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="✓"></div>
     

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
                  <div class="row">
  <div class="span12 page-header">
    <h3 style="">Computational Linguistics Journal (2000)</h3>
  </div>

  <div class="span12">
    <h4 style="text-align:center">Table of contents</h4>
    <table class="table table-striped table-bordered">
      <thead>
        <tr>
          <th>Anthology</th>
          <th>Volume</th>
          <th>Papers</th>
        </tr>
      </thead>
      <tbody>
          <tr>
            <td>J00-1</td>
            <td><a href="/events/cl-2000#J00-1">Computational Linguistics, Volume 26, Number 1, March 2000</a></td>
            <td>7</td>
          </tr>
          <tr>
            <td>J00-2</td>
            <td><a href="/events/cl-2000#J00-2">Computational Linguistics, Volume 26, Number 2, June 2000 </a></td>
            <td>18</td>
          </tr>
          <tr>
            <td>J00-3</td>
            <td><a href="/events/cl-2000#J00-3">Computational Linguistics, Volume 26, Number 3, September 2000</a></td>
            <td>12</td>
          </tr>
          <tr>
            <td>J00-4</td>
            <td><a href="/events/cl-2000#J00-4">Computational Linguistics, Volume 26, Number 4, December 2000 </a></td>
            <td>14</td>
          </tr>
      </tbody>
    </table>
    
      <br><br>
      <h4 id="J00-1" class="volume">
        
<!--  :target => "_blank" -->
        <a href="/volumes/computational-linguistics-volume-26-number-1-march-2000.bib"><img alt="Export" height="24" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Computational Linguistics, Volume 26, Number 1, March 2000' to bib format" width="24"></a>
        <a href="https://www.google.com/search?q=Computational Linguistics, Volume 26, Number 1, March 2000"><img alt="Search" height="24" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Computational Linguistics, Volume 26, Number 1, March 2000' on Google" width="24"></a> 
<!-- :target => "_blank"%> -->
        <a href="/volumes/computational-linguistics-volume-26-number-1-march-2000">Computational Linguistics, Volume 26, Number 1, March 2000</a>
      </h4><br>
<!-- @papers = volume.papers.includes(:people) -->
        <p>
    <a href="http://aclweb.org/anthology/J00-1001"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Introduction to the Special Issue on Finite-State Methods in NLP'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-1001/j00-1001.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Introduction to the Special Issue on Finite-State Methods in NLP' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Introduction to the Special Issue on Finite-State Methods in NLP"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Introduction to the Special Issue on Finite-State Methods in NLP' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-1001/j00-1001">Introduction to the Special Issue on Finite-State Methods in NLP</a></strong><br>
  [J00-1001]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/lauri-karttunen">Lauri Karttunen</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/kemal-oflazer">Kemal Oflazer</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-1002"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Incremental Construction of Minimal Acyclic Finite-State Automata'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-1002/j00-1002.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Incremental Construction of Minimal Acyclic Finite-State Automata' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Incremental Construction of Minimal Acyclic Finite-State Automata"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Incremental Construction of Minimal Acyclic Finite-State Automata' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-1002/j00-1002">Incremental Construction of Minimal Acyclic Finite-State Automata</a></strong><br>
  [J00-1002]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/jan-daciuk">Jan Daciuk</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/bruce-w-watson">Bruce W. Watson</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/stoyan-mihov">Stoyan Mihov</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/richard-e-watson">Richard E. Watson</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-1003"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Practical Experiments with Regular Approximation of Context-Free Languages'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-1003/j00-1003.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Practical Experiments with Regular Approximation of Context-Free Languages' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Practical Experiments with Regular Approximation of Context-Free Languages"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Practical Experiments with Regular Approximation of Context-Free Languages' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-1003/j00-1003">Practical Experiments with Regular Approximation of Context-Free Languages</a></strong><br>
  [J00-1003]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/mark-jan-nederhof">Mark-Jan Nederhof</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-1004"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Learning Dependency Translation Models as Collections of Finite-State Head Transducers'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-1004/j00-1004.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Learning Dependency Translation Models as Collections of Finite-State Head Transducers' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Learning Dependency Translation Models as Collections of Finite-State Head Transducers"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Learning Dependency Translation Models as Collections of Finite-State Head Transducers' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-1004/j00-1004">Learning Dependency Translation Models as Collections of Finite-State Head Transducers</a></strong><br>
  [J00-1004]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/hiyan-alshawi">Hiyan Alshawi</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/shona-douglas">Shona Douglas</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/srinivas-bangalore">Srinivas Bangalore</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-1005"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Treatment of Epsilon Moves in Subset Construction'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-1005/j00-1005.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Treatment of Epsilon Moves in Subset Construction' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Treatment of Epsilon Moves in Subset Construction"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Treatment of Epsilon Moves in Subset Construction' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-1005/j00-1005">Treatment of Epsilon Moves in Subset Construction</a></strong><br>
  [J00-1005]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/gertjan-van-noord">Gertjan van Noord</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-1006"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Multitiered Nonlinear Morphology Using Multitape Finite Automata: A Case Study on Syriac and Arabic'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-1006/j00-1006.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Multitiered Nonlinear Morphology Using Multitape Finite Automata: A Case Study on Syriac and Arabic' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Multitiered Nonlinear Morphology Using Multitape Finite Automata: A Case Study on Syriac and Arabic"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Multitiered Nonlinear Morphology Using Multitape Finite Automata: A Case Study on Syriac and Arabic' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-1006/j00-1006">Multitiered Nonlinear Morphology Using Multitape Finite Automata: A Case Study on Syriac and Arabic</a></strong><br>
  [J00-1006]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/george-anton-kiraz">George Anton Kiraz</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-1007"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Advertisements'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-1007/j00-1007.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Advertisements' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Advertisements"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Advertisements' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-1007/j00-1007">Advertisements</a></strong><br>
  [J00-1007]:
</p>
 
      <br><br>
      <h4 id="J00-2" class="volume">
        
<!--  :target => "_blank" -->
        <a href="/volumes/computational-linguistics-volume-26-number-2-june-2000.bib"><img alt="Export" height="24" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Computational Linguistics, Volume 26, Number 2, June 2000 ' to bib format" width="24"></a>
        <a href="https://www.google.com/search?q=Computational Linguistics, Volume 26, Number 2, June 2000 "><img alt="Search" height="24" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Computational Linguistics, Volume 26, Number 2, June 2000 ' on Google" width="24"></a> 
<!-- :target => "_blank"%> -->
        <a href="/volumes/computational-linguistics-volume-26-number-2-june-2000">Computational Linguistics, Volume 26, Number 2, June 2000 </a>
      </h4><br>
<!-- @papers = volume.papers.includes(:people) -->
        <p>
    <a href="http://aclweb.org/anthology/J00-2001"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Integrating Text Planning and Linguistic Choice Without Abandoning Modularity: The IGEN Generator'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2001/j00-2001.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Integrating Text Planning and Linguistic Choice Without Abandoning Modularity: The IGEN Generator' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Integrating Text Planning and Linguistic Choice Without Abandoning Modularity: The IGEN Generator"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Integrating Text Planning and Linguistic Choice Without Abandoning Modularity: The IGEN Generator' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2001/j00-2001">Integrating Text Planning and Linguistic Choice Without Abandoning Modularity: The IGEN Generator</a></strong><br>
  [J00-2001]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/robert-rubinoff">Robert Rubinoff</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-2002"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'A Model for Multimodal Reference Resolution'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2002/j00-2002.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'A Model for Multimodal Reference Resolution' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=A Model for Multimodal Reference Resolution"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'A Model for Multimodal Reference Resolution' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2002/j00-2002">A Model for Multimodal Reference Resolution</a></strong><br>
  [J00-2002]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/luis-pinedaluis-pineda">Luis PinedaLuis Pineda</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/gabriela-garza">Gabriela Garza</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-2003"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'A Multistrategy Approach to Improving Pronunciation by Analogy'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2003/j00-2003.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'A Multistrategy Approach to Improving Pronunciation by Analogy' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=A Multistrategy Approach to Improving Pronunciation by Analogy"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'A Multistrategy Approach to Improving Pronunciation by Analogy' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2003/j00-2003">A Multistrategy Approach to Improving Pronunciation by Analogy</a></strong><br>
  [J00-2003]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/yannick-marchand">Yannick Marchand</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/robert-i-damper">Robert I. Damper</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-2004"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Models of Translational Equivalence among Words'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2004/j00-2004.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Models of Translational Equivalence among Words' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Models of Translational Equivalence among Words"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Models of Translational Equivalence among Words' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2004/j00-2004">Models of Translational Equivalence among Words</a></strong><br>
  [J00-2004]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/i-dan-melamed">I. Dan Melamed</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-2005"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Squibs and Discussions: Pipelines and Size Constraints'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2005/j00-2005.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Squibs and Discussions: Pipelines and Size Constraints' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Squibs and Discussions: Pipelines and Size Constraints"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Squibs and Discussions: Pipelines and Size Constraints' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2005/j00-2005">Squibs and Discussions: Pipelines and Size Constraints</a></strong><br>
  [J00-2005]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/ehud-reiter">Ehud Reiter</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-2006"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: A Grammar Writer's Cookbook'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2006/j00-2006.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: A Grammar Writer's Cookbook' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: A Grammar Writer's Cookbook"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: A Grammar Writer's Cookbook' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2006/j00-2006">Book Reviews: A Grammar Writer's Cookbook</a></strong><br>
  [J00-2006]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/michael-maxwell">Michael Maxwell</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-2007"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: Local Constraints vs. Economy'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2007/j00-2007.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: Local Constraints vs. Economy' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: Local Constraints vs. Economy"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: Local Constraints vs. Economy' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2007/j00-2007">Book Reviews: Local Constraints vs. Economy</a></strong><br>
  [J00-2007]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/annie-zaenen">Annie Zaenen</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-2008"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: Predicative Forms in Natural Language and in Lexical Knowledge Bases'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2008/j00-2008.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: Predicative Forms in Natural Language and in Lexical Knowledge Bases' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: Predicative Forms in Natural Language and in Lexical Knowledge Bases"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: Predicative Forms in Natural Language and in Lexical Knowledge Bases' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2008/j00-2008">Book Reviews: Predicative Forms in Natural Language and in Lexical Knowledge Bases</a></strong><br>
  [J00-2008]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/manfred-stede">Manfred Stede</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-2009"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: Lexical Semantics and Knowledge Representation in Multilingual Text Generation'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2009/j00-2009.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: Lexical Semantics and Knowledge Representation in Multilingual Text Generation' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: Lexical Semantics and Knowledge Representation in Multilingual Text Generation"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: Lexical Semantics and Knowledge Representation in Multilingual Text Generation' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2009/j00-2009">Book Reviews: Lexical Semantics and Knowledge Representation in Multilingual Text Generation</a></strong><br>
  [J00-2009]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/barbara-di-eugenio-67b13ac8-78e1-4ee4-8d61-8ddfd5be37ea">Barbara Di Eugenio</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-2010"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: The Mathematics of Syntactic Structure: Trees and their Logics '" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2010/j00-2010.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: The Mathematics of Syntactic Structure: Trees and their Logics ' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: The Mathematics of Syntactic Structure: Trees and their Logics "><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: The Mathematics of Syntactic Structure: Trees and their Logics ' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2010/j00-2010">Book Reviews: The Mathematics of Syntactic Structure: Trees and their Logics </a></strong><br>
  [J00-2010]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/gerald-penn">Gerald Penn</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-2011"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: Foundations of Statistical Natural Language Processing'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2011/j00-2011.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: Foundations of Statistical Natural Language Processing' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: Foundations of Statistical Natural Language Processing"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: Foundations of Statistical Natural Language Processing' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2011/j00-2011">Book Reviews: Foundations of Statistical Natural Language Processing</a></strong><br>
  [J00-2011]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/lillian-lee">Lillian Lee</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-2012"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: Advances in Automatic Text Summarization '" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2012/j00-2012.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: Advances in Automatic Text Summarization ' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: Advances in Automatic Text Summarization "><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: Advances in Automatic Text Summarization ' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2012/j00-2012">Book Reviews: Advances in Automatic Text Summarization </a></strong><br>
  [J00-2012]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/mark-sanderson">Mark Sanderson</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-2013"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: Extended Finite State Models of Language '" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2013/j00-2013.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: Extended Finite State Models of Language ' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: Extended Finite State Models of Language "><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: Extended Finite State Models of Language ' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2013/j00-2013">Book Reviews: Extended Finite State Models of Language </a></strong><br>
  [J00-2013]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/ed-kaiser">Ed Kaiser</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-2014"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: Optimality Theory '" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2014/j00-2014.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: Optimality Theory ' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: Optimality Theory "><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: Optimality Theory ' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2014/j00-2014">Book Reviews: Optimality Theory </a></strong><br>
  [J00-2014]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/jason-eisner">Jason Eisner</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-2015"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: Systemic Functional Grammar in Natural Language Generation: Linguistic Description and Computational Representation'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2015/j00-2015.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: Systemic Functional Grammar in Natural Language Generation: Linguistic Description and Computational Representation' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: Systemic Functional Grammar in Natural Language Generation: Linguistic Description and Computational Representation"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: Systemic Functional Grammar in Natural Language Generation: Linguistic Description and Computational Representation' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2015/j00-2015">Book Reviews: Systemic Functional Grammar in Natural Language Generation: Linguistic Description and Computational Representation</a></strong><br>
  [J00-2015]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/graham-wilcock">Graham Wilcock</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-2016"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Briefly Noted'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2016/j00-2016.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Briefly Noted' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Briefly Noted"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Briefly Noted' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2016/j00-2016">Briefly Noted</a></strong><br>
  [J00-2016]:
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-2017"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Publications Received'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2017/j00-2017.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Publications Received' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Publications Received"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Publications Received' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2017/j00-2017">Publications Received</a></strong><br>
  [J00-2017]:
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-2018"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Advertisements'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-2018/j00-2018.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Advertisements' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Advertisements"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Advertisements' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-2018/j00-2018">Advertisements</a></strong><br>
  [J00-2018]:
</p>
 
      <br><br>
      <h4 id="J00-3" class="volume">
        
<!--  :target => "_blank" -->
        <a href="/volumes/computational-linguistics-volume-26-number-3-september-2000.bib"><img alt="Export" height="24" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Computational Linguistics, Volume 26, Number 3, September 2000' to bib format" width="24"></a>
        <a href="https://www.google.com/search?q=Computational Linguistics, Volume 26, Number 3, September 2000"><img alt="Search" height="24" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Computational Linguistics, Volume 26, Number 3, September 2000' on Google" width="24"></a> 
<!-- :target => "_blank"%> -->
        <a href="/volumes/computational-linguistics-volume-26-number-3-september-2000">Computational Linguistics, Volume 26, Number 3, September 2000</a>
      </h4><br>
<!-- @papers = volume.papers.includes(:people) -->
        <p>
    <a href="http://aclweb.org/anthology/J00-3001"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Extracting the Lowest-Frequency Words: Pitfalls and Possibilities'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-3001/j00-3001.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Extracting the Lowest-Frequency Words: Pitfalls and Possibilities' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Extracting the Lowest-Frequency Words: Pitfalls and Possibilities"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Extracting the Lowest-Frequency Words: Pitfalls and Possibilities' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-3001/j00-3001">Extracting the Lowest-Frequency Words: Pitfalls and Possibilities</a></strong><br>
  [J00-3001]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/marc-weeber">Marc Weeber</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/r-harald-baayen">R. Harald Baayen</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/rein-vos">Rein Vos</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-3002"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Incremental Processing and Acceptability'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-3002/j00-3002.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Incremental Processing and Acceptability' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Incremental Processing and Acceptability"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Incremental Processing and Acceptability' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-3002/j00-3002">Incremental Processing and Acceptability</a></strong><br>
  [J00-3002]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/glyn-morrill">Glyn Morrill</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-3003"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-3003/j00-3003.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-3003/j00-3003">Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech</a></strong><br>
  [J00-3003]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/andreas-stolcke">Andreas Stolcke</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/noah-coccaro">Noah Coccaro</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/rebecca-bates">Rebecca Bates</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/paul-taylor">Paul Taylor</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/carol-van-ess-dykema">Carol Van Ess-Dykema</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/klaus-ries">Klaus Ries</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/elizabeth-shriberg">Elizabeth Shriberg</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/daniel-jurafsky-9fa6d96a-bb80-416e-892e-16ade62ae034">Daniel Jurafsky</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/rachel-martin">Rachel Martin</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/marie-meteer">Marie Meteer</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-3004"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'A Compression-based Algorithm for Chinese Word Segmentation'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-3004/j00-3004.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'A Compression-based Algorithm for Chinese Word Segmentation' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=A Compression-based Algorithm for Chinese Word Segmentation"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'A Compression-based Algorithm for Chinese Word Segmentation' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-3004/j00-3004">A Compression-based Algorithm for Chinese Word Segmentation</a></strong><br>
  [J00-3004]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/w-j-teahan">W. J. Teahan</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/rodger-mcnab">Rodger McNab</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/yingying-wen">Yingying Wen</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/ian-h-witten">Ian H. Witten</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-3005"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'The Rhetorical Parsing of Unrestricted Texts: A Surface-based Approach'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-3005/j00-3005.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'The Rhetorical Parsing of Unrestricted Texts: A Surface-based Approach' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=The Rhetorical Parsing of Unrestricted Texts: A Surface-based Approach"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'The Rhetorical Parsing of Unrestricted Texts: A Surface-based Approach' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-3005/j00-3005">The Rhetorical Parsing of Unrestricted Texts: A Surface-based Approach</a></strong><br>
  [J00-3005]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/daniel-marcu">Daniel Marcu</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-3006"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: Foundations of Computational Linguistics: Man-Machine Communication in Natural Language'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-3006/j00-3006.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: Foundations of Computational Linguistics: Man-Machine Communication in Natural Language' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: Foundations of Computational Linguistics: Man-Machine Communication in Natural Language"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: Foundations of Computational Linguistics: Man-Machine Communication in Natural Language' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-3006/j00-3006">Book Reviews: Foundations of Computational Linguistics: Man-Machine Communication in Natural Language</a></strong><br>
  [J00-3006]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/alexander-f-gelbukh">Alexander F. Gelbukh</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-3007"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: Syntactic Wordclass Tagging '" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-3007/j00-3007.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: Syntactic Wordclass Tagging ' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: Syntactic Wordclass Tagging "><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: Syntactic Wordclass Tagging ' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-3007/j00-3007">Book Reviews: Syntactic Wordclass Tagging </a></strong><br>
  [J00-3007]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/adwait-ratnaparkhi">Adwait Ratnaparkhi</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-3008"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: Natural Language Information Retrieval '" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-3008/j00-3008.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: Natural Language Information Retrieval ' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: Natural Language Information Retrieval "><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: Natural Language Information Retrieval ' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-3008/j00-3008">Book Reviews: Natural Language Information Retrieval </a></strong><br>
  [J00-3008]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/simon-corston-oliver">Simon Corston-Oliver</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-3009"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: The MIT Encyclopedia of the Cognitive Sciences'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-3009/j00-3009.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: The MIT Encyclopedia of the Cognitive Sciences' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: The MIT Encyclopedia of the Cognitive Sciences"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: The MIT Encyclopedia of the Cognitive Sciences' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-3009/j00-3009">Book Reviews: The MIT Encyclopedia of the Cognitive Sciences</a></strong><br>
  [J00-3009]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/john-nerbonne">John Nerbonne</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-3010"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Publications Received '" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-3010/j00-3010.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Publications Received ' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Publications Received "><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Publications Received ' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-3010/j00-3010">Publications Received </a></strong><br>
  [J00-3010]:
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-3011"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Erratum'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-3011/j00-3011.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Erratum' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Erratum"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Erratum' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-3011/j00-3011">Erratum</a></strong><br>
  [J00-3011]:
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-3012"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Advertisements'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-3012/j00-3012.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Advertisements' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Advertisements"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Advertisements' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-3012/j00-3012">Advertisements</a></strong><br>
  [J00-3012]:
</p>
 
      <br><br>
      <h4 id="J00-4" class="volume">
        
<!--  :target => "_blank" -->
        <a href="/volumes/computational-linguistics-volume-26-number-4-december-2000.bib"><img alt="Export" height="24" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Computational Linguistics, Volume 26, Number 4, December 2000 ' to bib format" width="24"></a>
        <a href="https://www.google.com/search?q=Computational Linguistics, Volume 26, Number 4, December 2000 "><img alt="Search" height="24" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Computational Linguistics, Volume 26, Number 4, December 2000 ' on Google" width="24"></a> 
<!-- :target => "_blank"%> -->
        <a href="/volumes/computational-linguistics-volume-26-number-4-december-2000">Computational Linguistics, Volume 26, Number 4, December 2000 </a>
      </h4><br>
<!-- @papers = volume.papers.includes(:people) -->
        <p>
    <a href="http://aclweb.org/anthology/J00-4001"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Automatic Text Categorization in Terms of Genre and Author'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-4001/j00-4001.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Automatic Text Categorization in Terms of Genre and Author' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Automatic Text Categorization in Terms of Genre and Author"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Automatic Text Categorization in Terms of Genre and Author' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-4001/j00-4001">Automatic Text Categorization in Terms of Genre and Author</a></strong><br>
  [J00-4001]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/efstathios-stamatatoso">Efstathios Stamatatoso</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/george-kokkinakis">George Kokkinakis</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/nikos-fakotakis">Nikos Fakotakis</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-4002"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Bidirectional Contextual Resolution'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-4002/j00-4002.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Bidirectional Contextual Resolution' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Bidirectional Contextual Resolution"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Bidirectional Contextual Resolution' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-4002/j00-4002">Bidirectional Contextual Resolution</a></strong><br>
  [J00-4002]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/stephen-g-pulman">Stephen G. Pulman</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-4003"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'An Empirically Based System for Processing Definite Descriptions'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-4003/j00-4003.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'An Empirically Based System for Processing Definite Descriptions' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=An Empirically Based System for Processing Definite Descriptions"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'An Empirically Based System for Processing Definite Descriptions' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-4003/j00-4003">An Empirically Based System for Processing Definite Descriptions</a></strong><br>
  [J00-4003]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/renata-vieira">Renata Vieira</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/massimo-poesio">Massimo Poesio</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-4004"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Learning Methods to Combine Linguistic Indicators: Improving Aspectual Classification and Revealing Linguistic Insights'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-4004/j00-4004.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Learning Methods to Combine Linguistic Indicators: Improving Aspectual Classification and Revealing Linguistic Insights' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Learning Methods to Combine Linguistic Indicators: Improving Aspectual Classification and Revealing Linguistic Insights"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Learning Methods to Combine Linguistic Indicators: Improving Aspectual Classification and Revealing Linguistic Insights' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-4004/j00-4004">Learning Methods to Combine Linguistic Indicators: Improving Aspectual Classification and Revealing Linguistic Insights</a></strong><br>
  [J00-4004]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/eric-v-siegel">Eric V. Siegel</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/kathleen-r-mckeown">Kathleen R. McKeown</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-4005"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Squibs and Discussions: On Coreferring: Coreference in MUC and Related Annotation Schemes'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-4005/j00-4005.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Squibs and Discussions: On Coreferring: Coreference in MUC and Related Annotation Schemes' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Squibs and Discussions: On Coreferring: Coreference in MUC and Related Annotation Schemes"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Squibs and Discussions: On Coreferring: Coreference in MUC and Related Annotation Schemes' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-4005/j00-4005">Squibs and Discussions: On Coreferring: Coreference in MUC and Related Annotation Schemes</a></strong><br>
  [J00-4005]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/kees-van-deemter">Kees van Deemter</a>
  <!-- paper.@authors.each do |author| -->
      | <!-- a character for spacing -->
        <a href="/people/rodger-kibble">Rodger Kibble</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-4006"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-4006/j00-4006.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-4006/j00-4006">Book Reviews: Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition</a></strong><br>
  [J00-4006]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/virginia-teller">Virginia Teller</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-4007"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: Artificial Intelligence and Literary Creativity: Inside the Mind of BRUTUS, a Storytelling Machine '" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-4007/j00-4007.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: Artificial Intelligence and Literary Creativity: Inside the Mind of BRUTUS, a Storytelling Machine ' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: Artificial Intelligence and Literary Creativity: Inside the Mind of BRUTUS, a Storytelling Machine "><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: Artificial Intelligence and Literary Creativity: Inside the Mind of BRUTUS, a Storytelling Machine ' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-4007/j00-4007">Book Reviews: Artificial Intelligence and Literary Creativity: Inside the Mind of BRUTUS, a Storytelling Machine </a></strong><br>
  [J00-4007]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/ronald-de-sousa">Ronald de Sousa</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-4008"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: Architectures and Mechanisms for Language Processing '" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-4008/j00-4008.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: Architectures and Mechanisms for Language Processing ' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: Architectures and Mechanisms for Language Processing "><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: Architectures and Mechanisms for Language Processing ' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-4008/j00-4008">Book Reviews: Architectures and Mechanisms for Language Processing </a></strong><br>
  [J00-4008]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/amy-weinberg">Amy Weinberg</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-4009"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Book Reviews: Breadth and Depth of Semantic Lexicons '" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-4009/j00-4009.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Book Reviews: Breadth and Depth of Semantic Lexicons ' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Book Reviews: Breadth and Depth of Semantic Lexicons "><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Book Reviews: Breadth and Depth of Semantic Lexicons ' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-4009/j00-4009">Book Reviews: Breadth and Depth of Semantic Lexicons </a></strong><br>
  [J00-4009]:
  <!-- paper.@authors.each do |author| -->
        <a href="/people/john-s-white">John S. White</a>
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-4010"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Briefly Noted '" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-4010/j00-4010.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Briefly Noted ' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Briefly Noted "><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Briefly Noted ' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-4010/j00-4010">Briefly Noted </a></strong><br>
  [J00-4010]:
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-4011"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Publications Received '" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-4011/j00-4011.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Publications Received ' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Publications Received "><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Publications Received ' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-4011/j00-4011">Publications Received </a></strong><br>
  [J00-4011]:
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-4012"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Author Index: Volume 26'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-4012/j00-4012.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Author Index: Volume 26' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Author Index: Volume 26"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Author Index: Volume 26' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-4012/j00-4012">Author Index: Volume 26</a></strong><br>
  [J00-4012]:
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-4013"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Title Index: Volume 2'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-4013/j00-4013.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Title Index: Volume 2' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Title Index: Volume 2"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Title Index: Volume 2' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-4013/j00-4013">Title Index: Volume 2</a></strong><br>
  [J00-4013]:
</p>
 
        <p>
    <a href="http://aclweb.org/anthology/J00-4014"><img alt="Pdf" height="16" src="/assets/pdf-e4d56a6b7eeaf7d04e84393b8c90d387.png" title="Open PDF of 'Advertisements'" width="16"></a>
<!-- :target => "_blank" %> -->

  <a href="/papers/J00-4014/j00-4014.bib"><img alt="Export" height="16" src="/assets/export-c00225f64d453516e98f003bd9771054.png" title="Export 'Advertisements' to bib format" width="16"></a>
  <a href="https://www.google.com/search?q=Advertisements"><img alt="Search" height="16" src="/assets/search-920350b4d9a5c54fe5102498716a4ff7.png" title="Search for 'Advertisements' on Google" width="16"></a> 
<!-- , :target => "_blank"%> -->


  <strong><a href="/papers/J00-4014/j00-4014">Advertisements</a></strong><br>
  [J00-4014]:
</p>
 
  </div>
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
