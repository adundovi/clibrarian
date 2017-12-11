import re

from clibrarian.libs.abstract import Tool, Command
from api import GoogleBooksApi 

class Book(Tool):

    def __init__(self):
        Tool.__init__(self)

        self.api = GoogleBooksApi()
        self.name = 'book'
        self.help = 'Google Books interface'
        self.commands = {
                'show': Show(),
                'search': Search()
                }

class Show(Command):
    
    def __init__(self):
        Command.__init__(self)

        self.name = 'show'
        self.help = 'show book'
    
    def init_parser(self, command_parsers):
        Command.init_parser(self, command_parsers)
        
        self.command_parser.add_argument('query',
                                 nargs='?',
                                 help='Query')
        self.command_parser.add_argument('-t', '--type',
                                 default='googleId',
                                 help='Options: googleId, ISBN')
        self.command_parser.add_argument('-f', '--format',
                                 default='cli',
                                 help='format of the output')

    def process(self):
        query = self.args.query

        if self.args.type == 'isbn':
            query = 'isbn:'+query
            books = g.search(query)
            query = books[0].googleId

        book = self.api.get_volumes(query)

        book.output(format=self.args.format)

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

        if self.args.type == 'isbn':
            query = 'isbn:'+query
        books = self.api.search(query, True)

        for book in books:
            book.output()
