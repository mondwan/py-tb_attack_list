"""
- `File`: type_position_filter.py

- `Author`: Me

- `Email`: 0

- `Github`: 0

- `Description`: Yet another filter for filtering target with same position
                and same troop type
"""

from base_filter import BaseFilter, FilterException

class TypePositionFilter(BaseFilter):
    """
    Filtering targets with same position and same troop type
    """
    def _filter(self, commands):
        """
        Actual implementation for filtering target with same position and same
        troop mask

        Parameters:

        - `commands`: Array of command objects

        Return:

        - `array of commands`
        """

        ret = []

        memory = {}

        try:
            for command in commands:
                # Get command position
                targetX = int(command['target_x'])
                targetY = int(command['target_y'])
                position = (targetX, targetY)

                # Get a binary mask from the troops distribution
                troops = command['troops']
                tmp = ['0' if t == 0 else '1' for t in troops]
                mask = int(''.join(tmp), 2)

                # Check whether the given command match filtering conditions
                # or not
                if position in memory:
                    masks = memory[position]
                    if mask in masks:
                        # Filter this command out
                        continue
                    else:
                        masks.append(mask)
                else:
                    memory[position] = [mask]

                ret.append(command)

        except ValueError, e:
            raise FilterException(
                'TroopTypeFilter.troopType is not a binary string'
            )

        return ret
