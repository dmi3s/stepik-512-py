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


def parse_definition(definition: string) -> (string, []):
    if ":" not in definition:
        return definition.strip(), []
    name, bases = definition.split(":", 1)
    return name.strip(), bases.strip().split(" ")


def main():
    h = Hierarchy()
    for _ in range(int(input())):
        name, bases = parse_definition(input())
        h[name] = bases
    prev = []
    for _ in range(int(input())):
        ex = input().strip()
        for p in prev:
            if h.is_derived_from(ex, p):
                print(ex)
                break
        prev.append(ex)


main()


if __name__ == '__main__':
    main()
