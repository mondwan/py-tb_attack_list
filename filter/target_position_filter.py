"""
- `File`: target_position_filter.py

- `Author`: Me

- `Email`: 0

- `Github`: 0

- `Description`: Delete command objects with duplicated position
"""

from base_filter import BaseFilter


class TargetPositionFilter(BaseFilter):
    """
    Algorithm for filtering targets with duplcated position
    """
    def _filter(self, commands):
        """
        Filter duplicated targets

        Parameters:

        - `commands`: Array of command objects

        Return:

        - `array of commands`
        """
        ret = []

        positions = []

        for command in commands:
            # Cast string to int
            targetX = int(command['target_x'])
            targetY = int(command['target_y'])

            # An identifier formed by x, y
            position = (targetX, targetY)

            # Skip this command
            if position in positions:
                continue

            # Cached this new position
            positions.append(position)

            ret.append(command)

        return ret

