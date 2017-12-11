from mako.template import Template
from mako.lookup import TemplateLookup
import os.path

class ArXivPaper(object):

    def __init__(self, entry):
        self.id = entry.id.text
        self.updated = entry.updated.text
        self.published = entry.published.text
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

        path = os.path.dirname(os.path.realpath(__file__))
        self.templates = TemplateLookup(directories=[path+'/../templates'],
                                        module_directory='/tmp/mako_modules',
                                        input_encoding='utf-8',
                                        output_encoding='utf-8')

    def output(self, format='cli'):
        template = self.templates.get_template(format+'.mak')
        print(template.render(paper=self)) 
