#!/usr/bin/env python
# The arxivcli executable script.

import argparse
import clibrarian.tools

def main(args=None):
    """Regular entry point
    """
    main_parser = argparse.ArgumentParser(
        description='Access different library tools through a command-line interface.')
    tool_parsers = main_parser.add_subparsers(
        title='tool',
        help='Choose the tool',
        dest='tool')

    modules = {}
    for tool in clibrarian.tools.__all__:
        inst_tool = getattr(clibrarian.tools, tool)()
        inst_tool.init_parser(tool_parsers)
        modules[tool] = inst_tool

    args = main_parser.parse_args()

    if args.tool:
        tool = modules[args.tool.title()]
        if args.command:
            command = tool.commands[args.command]
            command.args = args
            command.invoke()

if __name__ == "__main__":
    main()

