import exstack as es


def test_sum() -> None:
    s = es.ExtendedStack()
    s.append(2)
    s.append(3)
    s.sum()
    r = s.pop()
    assert r == 5


def test_sub() -> None:
    s = es.ExtendedStack()
    s.append(5)
    s.append(3)
    s.sub()
    r = s.pop()
    assert r == -2


def test_mul() -> None:
    s = es.ExtendedStack()
    s.append(5)
    s.append(3)
    s.mul()
    r = s.pop()
    assert r == 15


def test_div() -> None:
    s = es.ExtendedStack()
    s.append(3)
    s.append(5)
    s.div()
    r = s.pop()
    assert r == 1


def test_complex() -> None:
    ex_stack = es.ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    ex_stack.div()
    assert ex_stack.pop() == 2
    ex_stack.sub()
    assert ex_stack.pop() == 6
    ex_stack.sum()
    assert ex_stack.pop() == 7
    ex_stack.mul()
    assert ex_stack.pop() == 2
    assert len(ex_stack) == 0
