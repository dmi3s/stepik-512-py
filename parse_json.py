import json
import collections
import string


class Hierarchy(dict):
    def is_derived_from(self, derived: string, base: string) -> bool:
        if derived not in self:
            return False
        if derived == base:
            return True
        for p in self[derived]:
            if p == base or self.is_derived_from(p, base):
                return True
        return False

    def is_base_of(self, base: string, derived: string) -> bool:
        return self.is_derived_from(derived, base)


def count_parents(hierarchy, counters):
    for c in hierarchy:
        for p in hierarchy:
            if hierarchy.is_base_of(c, p):
                counters[c] += 1


def go(jstr):
    lst = json.loads(jstr)
    hierarchy = Hierarchy()
    for d in lst:
        hierarchy[d['name']] = d['parents']
    # print(hierarchy)
    counters = collections.Counter()
    count_parents(hierarchy, counters)
    result = list(counters.items())
    result.sort()
    for name, count in result:
        print(f"{name} : {count}")


test_str = '''[
    {"name": "B", "parents": ["A", "C"]},
    {"name": "C", "parents": ["A"]},
    {"name": "A", "parents": []},
    {"name": "D", "parents":["C", "F"]},
    {"name": "E", "parents":["D"]},
    {"name": "F", "parents":[]}
]'''

one_more_test_str = '''[
    {"name": "G", "parents": ["F"]},
    {"name": "A", "parents": []},
    {"name": "B", "parents": ["A"]},
    {"name": "C", "parents": ["A"]},
    {"name": "D", "parents": ["B", "C"]},
    {"name": "E", "parents": ["D"]},
    {"name": "F", "parents": ["D"]},
    {"name": "X", "parents": []},
    {"name": "Y", "parents": ["X", "A"]},
    {"name": "Z", "parents": ["X"]},
    {"name": "V", "parents": ["Z", "Y"]},
    {"name": "W", "parents": ["V"]}
]'''


# go(input())
go(one_more_test_str)
