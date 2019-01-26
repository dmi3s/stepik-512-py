import string
from typing import List


class Hierarchy:
    def __init__(self) -> ():
        self.dict = {}

    def add(self, name: string, parents: List = None) -> None:
        self.dict[name] = parents

    def is_derived_from(self, derived: string, base: string) -> bool:
        if derived not in self.dict:
            return False
        if derived == base:
            return True
        for p in self.dict[derived]:
            if p == base or self.is_derived_from(p, base):
                return True
        return False

    def is_base_of(self, base: string, derived: string) -> bool:
        return self.is_derived_from(derived, base)


def parse_definition(definition: string) -> (string, []):
    if ":" not in definition:
        return definition.strip(), []
    name, bases = definition.split(":", 1)
    return name.strip(), bases.strip().split(" ")


def parse_request(req: string) -> (string, string):
    base, derived = req.strip().split(" ", 1)
    return base, derived


def main():
    h = Hierarchy()
    for __ in range(int(input())):
        class_name, parents = parse_definition(input())
        h.add(class_name, parents)
    for __ in range(int(input())):
        b, d = parse_request(input())
        answer = "Yes" if h.is_base_of(b, d) else "No"
        print(answer)


if __name__ == '__main__':
    main()
