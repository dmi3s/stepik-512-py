import inheritance


def test_parse_simple_definition():
    name, parents = inheritance.parse_definition(" A ")
    assert name == "A"
    assert not parents


def test_parse_complex_definition():
    name, parents = inheritance.parse_definition("D : A B C ")
    assert name == "D"
    assert parents == ["A", "B", "C"]


def test_parse_request():
    base, derived = inheritance.parse_request("A D")
    assert base == "A"
    assert derived == "D"


def test_inheritance():
    h = inheritance.Hierarchy()
    h.add("A")
    h.add("B", ["A"])
    h.add("C", ["A"])
    h.add("D", ["B", "C"])
    assert h.is_derived_from("B", "A")
    assert h.is_derived_from("C", "A")
    assert h.is_derived_from("D", "A")
    assert not h.is_derived_from("C", "B")


def test_error_in_inheritance():
    h = inheritance.Hierarchy()
    assert not h.is_derived_from("B", "A")


R'''
    A   X
   /|\ / \
  B C Y   Z
   \|  \ /
    D   V
   / \   \
  E   F   W
       \
        G
'''


def test_inheritance(capsys):
    h = inheritance.Hierarchy()
    lst_mro = [
        'G : F',  # сначала отнаследуем от F, потом его объявим, корректный алгоритм все равно правильно обойдёт граф,
        # независимо что было раньше: наследование или объявление
        'A',
        'B : A',
        'C : A',
        'D : B C',
        'E : D',
        'F : D',  # а теперь другая ветка наследования
        'X',
        'Y : X A',  # свяжем две ветки наследования для проверки, обошла ли рекурсия предков Z и предков Y в поисках A
        'Z : X',
        'V : Z Y',
        'W : V',
    ]
    for mro in lst_mro:
        class_name, parents = inheritance.parse_definition(mro)
        h.add(class_name, parents)
    lst_q = [  # список введённых запросов
        ('A G', "Yes"),  # Yes   # A предок G через B/C, D, F
        ('A Z', "No"),  # No    # Y потомок A, но не Y
        ('A W', "Yes"),  # Yes   # A предок W через Y, V
        ('X W', "Yes"),  # Yes   # X предок W через Y, V
        ('X QWE', "No"),  # No    # нет такого класса QWE
        ('A X', "No"),  # No    # классы есть, но они нет родства :)
        ('X X', "Yes"),  # Yes   # родитель он же потомок
        ('1 1', "No")  # No    # несуществующий класс
    ]

    input_values = [str(len(lst_mro))]
    for mro in lst_mro:
        input_values.append(mro)
    input_values.append(str(len(lst_q)))
    for q, __ in lst_q:
        input_values.append(q)

    output = []

    def moc_input(__=""):
        return input_values.pop(0)

    inheritance.input = moc_input
    inheritance.print = lambda s: output.append(s)

    inheritance.main()

    for (__, awaiting), answer in zip(lst_q, output):
        assert awaiting == answer
