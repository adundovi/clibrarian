from mako.template import Template
from mako.lookup import TemplateLookup
import os.path

class Item(object):
    id = ''
    title = ''
    authors = ''
    publisher = ''
    publishedDate = ''
    templates = None
    
    def __init__(self):
        
        self.classname = self.__class__.__name__.lower()
        path = os.path.dirname(os.path.realpath(__file__))
        self.templates = TemplateLookup(directories=[path+'/../templates'],
                                        module_directory='/tmp/mako_modules',
                                        input_encoding='utf-8',
                                        output_encoding='utf-8')
    def __repr__(self):
        template = self.templates.get_template(
                "{}_cli.mak".format(self.classname))
        return template.render(item=self)

    def output(self, format='cli'):
        template = self.templates.get_template(
                "{}_{}.mak".format(self.classname, format))
        print(template.render(item=self))
    
    def from_json(json):
        pass


class GoogleBook(Item):
    googleLink = ''
    subtitle = ''
    description = ''
    isbn = ''
    pageCount = 0
    categories = ''
    averageRating = ''
    ratingsCount = ''
   
    def from_json(self, json):

        self.id = json['id']
        self.googleLink = json['selfLink']
        self.title = json['volumeInfo']['title']
        if 'subtitle' in json['volumeInfo']:
            self.subtitle = json['volumeInfo']['subtitle']
        if 'authors' in json['volumeInfo']:
            self.authors = json['volumeInfo']['authors']
        if 'publisher' in json['volumeInfo']:
            self.publisher = json['volumeInfo']['publisher']
        if 'publishedDate' in json['volumeInfo']:
            self.publishedDate = json['volumeInfo']['publishedDate']
        if 'description' in json['volumeInfo']:
            self.description = json['volumeInfo']['description']
        for identifiers in json['volumeInfo']['industryIdentifiers']:
            if identifiers['type'] == "ISBN_13":
                self.isbn = identifiers['identifier']
            elif identifiers['type'] == "ISBN_10":
                self.isbn = identifiers['identifier']
        if 'pageCount' in json['volumeInfo']:
            self.pageCount = json['volumeInfo']['pageCount']
        if 'categories' in json['volumeInfo']:
            self.categories = json['volumeInfo']['categories']
        if 'averageRating' in json['volumeInfo']:
            self.averageRating = json['volumeInfo']['averageRating']
        if 'ratingsCount' in json['volumeInfo']:
            self.ratingsCount = json['volumeInfo']['ratingsCount']

class ArXivPaper(Item):

    def __init__(self, entry):
        Item.__init__(self)

        self.id = entry.id.text
        self.updated = entry.updated.text
        self.publishedDate = entry.published.text
        self.title = entry.title.text.replace('\n', ' ').replace('\r', '')
        self.summary = entry.summary.text.replace('\n', ' ').replace('\r', '')
        self.authors = [author.name.text for author in entry.author]
        self.doi = None
        self.pdf = None #always present
        self.link = None
        self.source = None #equal to pdf if None
        for link in entry.link:
            if 'title' in link.attrib:
                if link.get('title') == 'doi':
                    self.doi = link.get('href')
                if link.get('title') == 'pdf':
                    self.pdf = link.get('href')
            if 'type' in link.attrib:
                if link.get('type') == 'text/html':
                    self.link = link.get('href')
        self.category = entry.category.get('term')
        if '.' in self.category:
            self.category = self.category.split('.')[0]
        
        self.comment = None
        self.primary_category = None
        self.source = self.pdf.replace('/e-print/','/pdf/',1)


class InspireRecord(Item):

    summary = ''
    pagination = ''
    number_of_citations = 0
    number_of_authors = 0
    primary_report_number = []
    doi = []

    def from_json(self, json):
        self.id = json['recid']
        self.title = json['title']['title']
        self.authors = [a['full_name'] for a in json['authors'][:5]]
        if type(json['abstract']) is list:
            self.summary = json['abstract'][0]['summary']
        else:
            self.summary = json['abstract']['summary']
        if 'prepublication' in json:
            if json['prepublication']:
                self.publishedDate = json['prepublication']['date']
        self.pagination = json['physical_description']['pagination']
        self.number_of_citations = json['number_of_citations']
        self.number_of_authors = json['number_of_authors']
        self.primary_report_number = json['primary_report_number']
        self.doi = json['doi']
