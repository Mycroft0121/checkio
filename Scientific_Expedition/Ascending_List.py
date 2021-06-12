from typing import Iterable
def is_ascending(items: Iterable[int]) -> bool:
    # your code here
    if not len(items):

        return True

    pre = items[0]
    for i in range(1, len(items)):
        if items[i]<=pre:
            return False
        pre = items[i]

    return True