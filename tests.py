import inheritance
import unittest


class TestInheritanceParsers(unittest.TestCase):
    def test_parse_simple_definition(self):
        name, parents = inheritance.parse_definition(" A ")
        self.assertEqual(name, "A")
        self.assertFalse(parents)

    def test_parse_complex_definition(self):
        name, parents = inheritance.parse_definition("D : A B C ")
        self.assertEqual(name, "D")
        self.assertEqual(parents, ["A", "B", "C"])

    def test_parse_request(self):
        base, derived = inheritance.parse_request("A D")
        self.assertEqual(base, "A")
        self.assertEqual(derived, "D")


class TestInheritance(unittest.TestCase):
    def test_inheritance(self):
        h = inheritance.Hierarchy()
        h.add("A")
        h.add("B", ["A"])
        h.add("C", ["A"])
        h.add("D", ["B", "C"])
        self.assertTrue(h.is_derived_from("B", "A"))
        self.assertTrue(h.is_derived_from("C", "A"))
        self.assertTrue(h.is_derived_from("D", "A"))
        self.assertFalse(h.is_derived_from("C", "B"))

    def test_error_in_inheritance(self):
        h = inheritance.Hierarchy()
        h.is_derived_from("B", "A")

    def test_complex(self):
        h = inheritance.Hierarchy()
        lst_mro = [  # список введённых строк
            'G : F',
            # сначала отнаследуем от F, потом его объявим, корректный алгоритм все равно правильно обойдёт граф, независимо что было раньше: наследование или объявление
            'A',
            'B : A',
            'C : A',
            'D : B C',
            'E : D',
            'F : D',
            # а теперь другая ветка наследования
            'X',
            'Y : X A',
            # свяжем две ветки наследования для проверки, обошла ли рекурсия предков Z и предков Y в поисках A
            'Z : X',
            'V : Z Y',
            'W : V',
        ]
        for mro in lst_mro:
            class_name, parents = inheritance.parse_definition(mro)
            h.add(class_name, parents)
        lst_q = [  # список введённых запросов
            ('A G', True),  # Yes   # A предок G через B/C, D, F
            ('A Z', False),  # No    # Y потомок A, но не Y
            ('A W', True),  # Yes   # A предок W через Y, V
            ('X W', True),  # Yes   # X предок W через Y, V
            ('X QWE', False),  # No    # нет такого класса QWE
            ('A X', False),  # No    # классы есть, но они нет родства :)
            ('X X', True),  # Yes   # родитель он же потомок
            ('1 1', False)  # No    # несуществующий класс
        ]
        for q, awaiting in lst_q:
            b, d = inheritance.parse_request(q)
            answer = h.is_base_of(b, d)
            self.assertEqual(awaiting, answer)


if __name__ == '__main__':
    unittest.main()
