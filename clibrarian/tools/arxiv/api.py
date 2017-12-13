
from clibrarian.libs.api import AbstractApi
from clibrarian.libs.items import ArXivPaper

class ArxivApi(AbstractApi):
    """API for arXiv
       following http://arxiv.org/help/api/index
    """

    def __init__(self):
        self.baseuri = "http://export.arxiv.org/api/"
        self.method = 'query'
        self.max_results = 10
        self.parameters = ''

    def search_query(self, query):
        url = self.build_url(
                resource='query',
                parameters="")

        return get_xml(url)

    def get_papers_by_ids(self,id_list):
        parameters = "id_list={}".format(id_list)
        url = self.build_url(
                resource='query',
                parameters=parameters)
        
        root = self.get_xml(url)

        papers = []
        for item in root.entry:
            paper = ArXivPaper()
            paper.from_xml(item)
            papers.append(paper)

        return papers

