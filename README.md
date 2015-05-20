# About

This is a project for manipulating attack list from tb (travian builder).

At first, repository [py-sort_attack_list][1] covers sorting feature I need.
However, after several days, I found that I need more than sorting.

In order to keep and organize my codes better, here is another repository
which stores codes for manipulating the attack list from tb

## Features

### Sorting

Sort the attack list based on distance between the target and the position we
input

### Filtering

There are several algorithms for filtering targets.

* By target position

Duplicated targets, identified by position, with same position will be deleted

* By troop's type

Targets with same type of troops will be deleted. This one is good for deleting
targets which attacked by certain type of troops

NOTE1: Each of the combination of troops is treated as one special type

* By error contents

Targets with errors like getting locked will be deleted

Above algorithms can be work alone or working together which give you more
powers on filtering.

@author: Mond Wan

[1]: https://github.com/mondwan/py-sort_attack_list
