def count_(s, t):
    _count, offset = 0, 0
    while True:
        offset = s.find(t, offset)
        if offset == -1:
            break
        _count += 1
        offset += 1
    return _count


def main():
    s, t = input(), input()
    print(count_(s, t))


main()


def test_count2():
    tests = [
        ("abababa", "aba", 3),
        ("abababa", "abc", 0),
        ("abc", "abc", 1),
        ("aaaaa", "a", 5)
    ]
    for s, t, answer in tests:
        assert count_(s, t) == answer
