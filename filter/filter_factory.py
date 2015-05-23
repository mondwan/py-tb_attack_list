"""
- `File`: filter_factory.py

- `Author`: Me

- `Email`: 0

- `Github`: 0

- `Description`: Define how to instantiate filter object for the caller
"""

def createFilter(cfg):
    """
    Factory method takes configuration for instantiating filter objects

    Parameters:

    - `cfg`: ConfigParser.RawConfigParser

    Return:

    - `Instance of a filter` or None for no such instruction
    """
    filters = [
        {
            'name': 'by_target_position',
            'module': 'target_position_filter',
            'class': 'TargetPositionFilter',
        },
        {
            'name': 'by_troop_type',
            'module': 'troop_type_filter',
            'class': 'TroopTypeFilter',
        },
        {
            'name': 'by_type_position',
            'module': 'type_position_filter',
            'class': 'TypePositionFilter'
        },
        {
            'name': 'by_error',
            'module': 'none'
        },
    ]

    ret = None
    instances = []

    for f in filters:
        isModuleRequired = cfg.getboolean('instruction', f['name'])
        if isModuleRequired:
            module = __import__('filter.%s' % f['module'])
            module = getattr(module, f['module'])
            module = getattr(module, f['class'])
            instances.append(module([], cfg))

    if len(instances) > 0:
        ret = instances[0]
        for instance in instances[1:]:
            ret.addFilter(instance)

    return ret
