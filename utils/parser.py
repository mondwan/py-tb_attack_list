"""
- `File`: parser.py

- `Author`: Me

- `Email`: 0

- `Github`: 0

- `Description`: Define how to parse comamnd line arguments by using argparse
"""

import argparse

def createParser():
    """
    Factory method for creating a parser for parsing input arguments

    Return:

    - `argparse.ArgumentParser`
    """
    parser = argparse.ArgumentParser(
        prog='tblm',
        description=(
            'A list manager which responsible '
            'for manipulating attack list from travian builder'
        ),
        add_help=False
    )

    parser.add_argument(
        '--config',
        help='Specify the path for the configuration file',
        nargs=1,
        required=True
    )

    parser.add_argument(
        '--input',
        help='Specify the path for the Travian builder data file eg: a.attack',
        nargs=1,
        required=True
    )

    parser.add_argument(
        '--output',
        help='Specify the path for the output file',
        nargs=1,
        required=False,
        default=['new.attack']
    )

    parser.add_argument(
        '--help',
        help='This usage',
        required=False,
        action='store_true'
    )

    return parser
