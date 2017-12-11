from lxml import etree, objectify
import httplib
import urllib2
import arxivcli.libs.paper

class APSJounralsApi(object):
    """API for APS Journals, e.g. Rev. Mod. Phys
       http://journals.aps.org/rmp/abstract/10.1103/RevModPhys.72.689
    """

    def __init__(self):
        self.url = "http://export.arxiv.org/api/"
        self.method = 'query'
        self.max_results = 10
        self.parameters = ''

    def build_url(self, method=None, parameters=None):
        """Build URL for API access"""
        if method is not None:
            self.method = method
        if parameters is not None:
            self.parameters = parameters

        return "{url}{method}?{parameters}".format(
            url=self.url,
            method=self.method,
            parameters=self.parameters)

    def get_data(self, params, debug=False):
        """Obtain search results"""
        url = self.build_url(parameters=params)

        if debug:
            httplib.HTTPConnection.debuglevel = 1

        req = urllib2.Request(
            url, 
            data=None, 
        )
        return urllib2.urlopen(req).read()

    def get_xml(self, params):
        """Convert XML to python object"""
        return objectify.fromstring(self.get_data(params))

    def search_query(self, string):
        params = "{}&{}&{}"
        return get_xml(params)

    def get_papers_by_ids(self,id_list):
        params = "id_list={}".format(id_list)
        root = self.get_xml(params)
        papers = []
        for e in root.entry:
            papers.append(arxivcli.libs.paper.ArXivPaper(e))

        return papers

