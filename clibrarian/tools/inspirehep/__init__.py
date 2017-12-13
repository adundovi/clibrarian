import re

from clibrarian.libs.abstract import Tool, Command
from api import InspireHEPApi 

class Inspire(Tool):

    def __init__(self):
        Tool.__init__(self)

        self.api = InspireHEPApi()
        self.name = 'inspire'
        self.help = 'INSPIREHEP interface'
        self.commands = {
                'show': Show(),
                'search': Search()
                }

class Show(Command):
    
    def __init__(self):
        Command.__init__(self)

        self.name = 'show'
        self.help = 'show record'
    
    def init_parser(self, command_parsers):
        Command.init_parser(self, command_parsers)
        
        self.command_parser.add_argument('query',
                                 nargs='?',
                                 help='Query')
        self.command_parser.add_argument('-f', '--format',
                                 default='cli',
                                 help='format of the output')

    def process(self):
        query = self.args.query

        result = self.api.get_record(query)

        result.output(format=self.args.format)

class Search(Command):
    
    def __init__(self):
        Command.__init__(self)

        self.name = 'search'
        self.help = 'Search for the book'
    
    def init_parser(self, command_parsers):
        Command.init_parser(self, command_parsers)
        
        self.command_parser.add_argument('query',
                                 nargs='?',
                                 help='Search query')
        self.command_parser.add_argument('-t', '--type',
                                 default='all',
                                 help='Options: all, ISBN')

    def process(self):
        query = self.args.query

        query = re.sub(r"\s+", '+', query)

        results = self.api.search(query)

        for r in results:
            print(r)
