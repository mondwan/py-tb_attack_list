"""
- `File`: error_filter.py

- `Author`: Me

- `Email`: 0

- `Github`: 0

- `Description`: Filter comamnd with error contents
"""

from base_filter import BaseFilter


class ErrorFilter(BaseFilter):
    """
    Actual implementation for filtering commands with error contents
    """
    def _filter(self, commands):
        """
        Codes for filtering commands with error contents

        Parameters:

        - `commands`: Array of command objects

        Return:

        - `array of commands`
        """
        ret = []

        for command in commands:
            error = command['error']
            if error == '':
                ret.append(command)

        return ret

