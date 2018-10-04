import unittest
import num


class TestNum(unittest.TestCase):
    #def test_something(self):
    #    self.assertEqual(True, True)
    def test_sqr(self):
        self.assertEqual(num.sqr(2), 1)
        self.assertEqual(num.sqr(3), 1)
        self.assertEqual(num.sqr(4), 2)
        self.assertEqual(num.sqr(5), 2)
        self.assertEqual(num.sqr(6), 2)
        self.assertEqual(num.sqr(9), 3)
        self.assertEqual(num.sqr(10), 3)
        self.assertEqual(num.sqr(100), 10)
        self.assertEqual(num.sqr(120), 10)
        self.assertEqual(num.sqr(121), 11)

    def test_factor(self):
        for arg, res in (
            (2, [2]),
            (3, [3]),
            (4, [2, 2]),
            (100, [2, 2, 5, 5]),
            (102, [2, 3, 17]),
            (108, [2, 2, 3, 3, 3]),
            (127, [127]),
            (743665,  [5, 13, 17, 673] )
        ):
            self.assertEqual(num.factor(arg), res)


    def test_prime(self):
        for arg, res in (
            (2, True),
            (3, True),
            (4, False),
            (7, True),
            (10, False),
            (127, True)
        ):
            self.assertEqual(num.prime(arg), res)

    def test_nod(self):
        self.assertEqual(num.nod(10, 6), 2)
        self.assertEqual(num.nod(35, 12), 1)

    def test_expm(self):
        for x, n, m in ():
            pass


if __name__ == '__main__':
    unittest.main()
