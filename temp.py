from typing import List


class NonPositiveError(Exception):
    pass


class PositiveList(List):
    def append(self, num):
        if num > 0:
            super(List, self).append(num)
        else:
            raise NonPositiveError(str(num))
