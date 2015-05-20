"""
- `File`: auxiliary.py

- `Author`: Me

- `Email`: 0

- `Github`: 0

- `Description`: Provides calls for doing simple but tedious tasks
"""

import json as JSON
import ConfigParser
import io

def readJson(jsonPath, encoding='utf-8'):
    """
    Helper method return a JSON object by reading from a given f

    Parameters:

    - `jsonPath`: Path to the json input

    Return:

    - json
    """
    ret = None
    with open(jsonPath, 'r') as f:
        ret = JSON.load(f, encoding=encoding)

    return ret

def readConfig(configPath):
    """
    Helper method reads configuration from config.ini

    Parameters:

    - `configPath`: Path to the configuration file

    Return:

    - `ConfigParser.RawConfigParser`
    """
    config = ConfigParser.RawConfigParser()
    config.read(configPath)

    return config

def writeJSONFile(jsonContent, outputPath):
    """
    Helper method writes a JSON content which encoded in UTF-8 so that we can
    read chinese characters in the list

    Parameters:

    - `jsonContent`: Python dictionary

    - `outputPath`: Path for output configuration
    """
    with io.open(outputPath, 'w', encoding='utf8') as f:
        data = JSON.dumps(jsonContent, ensure_ascii=False)
        f.write(unicode(data))

