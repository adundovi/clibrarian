import mimetypes
import os
import urllib2

from clibrarian.libs.abstract import Tool, Command
from api import ArxivApi

class Arxiv(Tool):

    def __init__(self):
        Tool.__init__(self)

        self.api = ArxivApi()
        self.name = 'arxiv'
        self.help = 'Arxiv interface'
        self.commands = {
                'show': Show(),
                'get': Get()
                }

class Show(Command):
    
    def __init__(self):
        Command.__init__(self)

        self.name = 'show'
        self.help = 'Show paper summary'
    
    def init_parser(self, command_parsers):
        Command.init_parser(self, command_parsers)
        
        self.command_parser.add_argument('query',
                                 nargs='?',
                                 help='arXiv ID of the paper')
        self.command_parser.add_argument('-f', '--format',
                                 default='cli',
                                 help='format of the output')

    def process(self):
        query = self.args.query

        papers = self.api.get_papers_by_ids(self.args.query)
        for p in papers:
            p.output(format=self.args.format)

class Get(Command):
    
    def __init__(self):
        Command.__init__(self)

        self.name = 'get'
        self.help = 'Download the paper'
    
    def init_parser(self, command_parsers):
        Command.init_parser(self, command_parsers)
        
        self.command_parser.add_argument('query',
                                 nargs='?',
                                 help='arXiv ID of the paper')
        self.command_parser.add_argument('-f', '--format',
                                 default='pdf',
                                 help='format of the file')

    def download(self, url, filename=None):
        paper = urllib2.urlopen(url)
        if filename is None:
            info = paper.info()
            ext = mimetypes.guess_extension(info['Content-Type'])
            filename = os.path.basename(url)+ext
        with open(filename, "wb") as local_file:
            local_file.write(paper.read())

    def process(self):
        papers = self.api.get_papers_by_ids(self.args.query)
        for p in papers:
            self.download(p.pdf)
