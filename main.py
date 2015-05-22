"""
- `File`: main.py

- `Author`: Me

- `Email`: 0

- `Github`: 0

- `Description`: Main entry for manipulating attack list
"""

import sys
import utils.parser
import utils.auxiliary as auxiliary
import filter.filter_factory as filter_factory
import math
from filter.base_filter import FilterException

class ShowHelpException(Exception):
    """
    Raise if user required dumping usage
    """
    pass

def pump(commands, cfg):
    """
    Process commands with given instruction

    Parameters:

    - `commands`: array of command object

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

    - `cfg`: ConfigParser.RawConfigParser

    Return:

    - `array of command object`
    """

    myFilter = filter_factory.createFilter(cfg)

    # It means we should not do filtering if myFilter is None
    if myFilter is not None:
        commands = myFilter.filter(commands)

    # Sort at last step if required
    isSortRequired = cfg.getboolean('instruction', 'sort')
    if isSortRequired:
        # Cast our position to integer
        myX = int(cfg.get('position', 'x'))
        myY = int(cfg.get('position', 'y'))

        for record in commands:
            # Cast target position to integer
            targetX = int(record['target_x'])
            targetY = int(record['target_y'])
            distance = math.hypot(targetX - myX, targetY - myY)
            distance = round(distance, 2)
            record['distance'] = distance

        commands = sorted(commands, key=lambda command: command['distance'])

    return commands
        

def main(argv):
    """
    Main entry of our list manager

    Parameters:

    - `argv`: array of string

    Return:

    - `int`: 0 is success otherwise failure
    """
    ret = 0
    parser = utils.parser.createParser()

    opt = parser.parse_args(argv)

    try:
        # Stop execution if help flag is on
        if opt.help:
            raise ShowHelpException()

        # Read materials we need for later processing
        cfg = auxiliary.readConfig(opt.config)
        rawJson = auxiliary.readJson(opt.input[0])

        # List we are going to manipulate :)
        commands = rawJson['commands']

        # Pump commands and instruction for filtering, sorting etc
        rawJson['commands'] = pump(commands, cfg)

        # Write final result
        auxiliary.writeJSONFile(rawJson, opt.output[0])

    except ShowHelpException:
        parser.print_help()
        ret = 0
    except FilterException, e:
        ret = 1
        print('ERROR')
        print(e)

    return ret
    

# main()
if __name__ == "__main__":
    # Pass system arguments to main()
    main(sys.argv[1:])
