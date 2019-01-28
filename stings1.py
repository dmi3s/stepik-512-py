def task(s, a, b):
    count_ = 0
    while count_ < 1000:
        if a not in s:
            return count_
        s = s.replace(a, b)
        count_ += 1
    return None


def main():
    s, a, b = input(), input(), input()
    answer = task(s, a, b)
    if answer is not None:
        print(answer)
    else:
        print("Impossible")


main()


def test_task():
    tasks = [
        ("abab", "ab", "ba", 2),
        ("ababa", "a", "b", 1),
        ("ababa", "b", "a", 1),
        ("ababa", "c", "c", 0),
        ("ababac", "c", "c", None)
    ]
    for s, a, b, answer in tasks:
        assert task(s, a, b) == answer
