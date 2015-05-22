"""
- `File`: troop_type_filter.py

- `Author`: Me

- `Email`: 0

- `Github`: 0

- `Description`: Implement a filter for filtering out targets with given
    troop type
"""

from base_filter import BaseFilter, FilterException

class TroopTypeFilter(BaseFilter):
    """
    Algorithm for filtering out targets with given troop type
    """
    def _filter(self, commands):
        """
        Filter targets with given troop's type

        Parameters:

        - `commands`: Array of command objects

        Return:

        - `array of commands`
        """

        ret = []

        troopType = self._cfg.get('TroopTypeFilter', 'troopType')

        # Convert troopTypes (binary string) to integer 
        try:
            mask = int(troopType.replace(' ', ''), 2)

            for command in commands:
                troops = command['troops']
                # Get a binary mask from the troops distribution
                tmp = ['0' if t == 0 else '1' for t in troops]
                troopMask = int(''.join(tmp), 2)

                if troopMask != mask:
                    ret.append(command)
            
        except ValueError, e:
            raise FilterException(
                'TroopTypeFilter.troopType is not a binary string'
            )
        
        return ret
