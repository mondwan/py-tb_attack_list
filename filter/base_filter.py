"""
- `File`: base_filter.py

- `Author`: Me

- `Email`: 0

- `Github`: 0

- `Description`: Define interfaces for a filter
"""

class FilterException(Exception):
    """
    Raise if there are any exception from filter operation
    """
    pass


class BaseFilter(object):
    """
    A base filter do nothing but defines interfaces for filter object
    """
    def __init__(self, filters, cfg):
        """
        Constructor

        Parameters:

        - `filters`: Array of instances of filter

        - `cfg`: ConfigParser.RawConfigParser
        """
        self._filters = filters
        self._cfg = cfg

    def _filter(self, commands):
        """
        Subclass specific algorithm for filtering commands

        Parameters:

        - `commands`: Array of command object
        """
        # Simply return input commands in the base class
        return commands
    
    def addFilter(self, f):
        """
        Add a post filter for this filter

        Parameters:

        - `f`: Instance of a filter object
        """
        self._filter.append(f)

    def filter(self, commands):
        """
        Standard API filters given commands

        Parameters:

        - `commands`: Array of command object

            .. code-block:: py

                {
                    "arriveDate":"2015-05-09T00:37:54",
                    "attackTimes":1,
                    "attackTimes_Limit":0,
                    "attack_interval_max":4,
                    "attack_interval_min":1,
                    "bContinuous":false,
                    "bPause":false,
                    "bWithHero":false,
                    "backDate":"2015-05-09T02:16:51",
                    "decrease":0.0,
                    "decrease_max":0.0,
                    "error":"",
                    "rand":2,
                    "send_number":0,
                    "startTime":"2015-05-08T22:58:57",
                    "state":5,
                    "target":"OMG",
                    "target_x":76,
                    "target_y":77,
                    "troops":[ 0, 5, 0, 0, 0, 0, 0, 0, 0, 0 ],
                    "troops_max":[ 0, 5, 0, 0, 0, 0, 0, 0, 0, 0 ],
                    "type":3 
                }

        Return

        - `array of command object`
        """

        commands = self._filter(commands)

        # Ask following filters to work if any before returning commands
        for f in self._filters:
            commands = f.filter(commands)

        return commands
