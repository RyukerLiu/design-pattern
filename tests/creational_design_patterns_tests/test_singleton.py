import unittest
from creational_design_patterns.singleton import Singleton, FileSingleton, ThreadSafeFileSingleton

class TestSingleton(unittest.TestCase):
    def test_singleton(self):
        s1 = Singleton()
        s2 = Singleton()

        self.assertIs(s1, s2)


class TestFileSingleton(unittest.TestCase):
    def test_singleton(self):
        f1 = FileSingleton('Test File')
        f2 = FileSingleton('TestXX')

        self.assertIs(f1, f2)

        file = f1.get_file()
        self.assertEqual(file, 'Test File')


class TestThreadSafeFileSingleton(unittest.TestCase):
    def test_singleton(self):
        f1 = ThreadSafeFileSingleton('Test File')
        f2 = ThreadSafeFileSingleton('TestXX')

        self.assertIs(f1, f2)

        file = f1.get_file()
        self.assertEqual(file, 'Test File')
