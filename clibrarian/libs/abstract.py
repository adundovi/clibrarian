import clibrarian.libs.api

class AbstractCommand(object):
    pass

class Tool(AbstractCommand):
    """Meta-class for every tool
    """
    def __init__(self):
        self.args = []
        self.commands = {}
        self.help = None
        self.name = None
        self.tool_parser = None
        self.command_parsers = None
        self.api = None

    def init_parser(self, tool_parsers):
        self.tool_parser = tool_parsers.add_parser(self.name, help=self.help)
    
        self.command_parsers = self.tool_parser.add_subparsers(
            title='command',
            help='Choose the command',
            dest='command')
        
        for name, inst in self.commands.iteritems():
            inst.init_parser(self.command_parsers)
            inst.api = self.api

class Command(AbstractCommand):

    def __init__(self):
        self.args = []
        self.api = None
        self.help = None
        self.name = None
        self.command_parser = None

    def init_parser(self, command_parsers):
        self.command_parser = command_parsers.add_parser(self.name, help=self.help)

    def invoke(self):
        if self.args.query:
            self.process()
        else:
            self.command_parser.print_help()

    def process(self):
        pass
