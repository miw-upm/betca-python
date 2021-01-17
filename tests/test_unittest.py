import unittest


class TestLifecycle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('before all tests')

    def setUp(self):
        print('before each test')

    def test_1(self):
        print('test_1')

    def test_2(self):
        print('test_2')

    def tearDown(self):
        print('after each test')

    @classmethod
    def tearDownClass(cls):
        print('after all tests')


class TestAsserts(unittest.TestCase):

    def setUp(self):
        self.__str = 'ten'
        self.__list = [1, 2, 3]
        self.__list_same = self.__list
        self.__list2 = [1, 2, 3]
        self.__list3 = [2, 1, 3]
        self.__none = None
        self.__dict = {"name": "John", "age": 36}
        self.__dict2 = {"age": 36, "name": "John"}

    def test_1(self):
        self.assertEqual(10, 5*2)  # value equality
        self.assertEqual('ten', 't'+'en')
        self.assertEqual(self.__list, self.__list2)
        self.assertEqual(self.__dict, self.__dict2)
        self.assertNotEqual(self.__list, self.__list3)
        self.assertTrue(2 > 0)
        self.assertFalse(2 < 0)
        self.assertIs(self.__list, self.__list_same)  # reference equality
        self.assertIsNot(self.__list, self.__list2)
        self.assertIsNone(self.__none)
        self.assertIsNotNone(self.__str)
        self.assertIn(1, self.__list)
        self.assertNotIn(0, self.__list)

    def test_2(self):
        with self.assertRaises(ZeroDivisionError):
            x = 4/0

    def test_3(self):
        self.assertAlmostEqual(1.001, 1.002, 2)
        self.assertNotAlmostEqual(1.001, 1.002, 3)
        self.assertGreater(3, 2)
        self.assertGreaterEqual(3, 2)
        self.assertLess(2, 3)
        self.assertLessEqual(2, 2)
        self.assertRegex("abbb", r"ab*")
        self.assertNotRegex("bbb", r"ab*")




