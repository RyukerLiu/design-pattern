import unittest
from .singleton import Singleton, FileSingleton, SingletonV2, FileSingletonV2


class TestSingleton(unittest.TestCase):
    def test_singleton(self):
        s1 = Singleton.get_instance()
        s2 = Singleton.get_instance()

        self.assertIs(s1, s2)

    def test_singleton_private_construct(self):
        with self.assertRaises(Exception) as cm:
            s1 = Singleton()

        exc = cm.exception
        self.assertEqual(
            str(exc), 'Singleton should be construct by .get_instance')


class TestFileSingleton(unittest.TestCase):
    def test_singleton(self):
        f1 = FileSingleton.get_instance('Test File')
        f2 = FileSingleton.get_instance('Test File')

        self.assertIs(f1, f2)

        file = f1.get_file()
        self.assertEqual(file, 'Test File')

    def test_singleton_private_construct(self):
        with self.assertRaises(Exception) as cm:
            f1 = FileSingleton('Test File')

        exc = cm.exception
        self.assertEqual(
            str(exc), 'Singleton should be construct by .get_instance')


class TestSingletonV2(unittest.TestCase):
    def test_singleton(self):
        s1 = SingletonV2()
        s2 = SingletonV2()

        self.assertIs(s1, s2)


class TestFileSingletonV2(unittest.TestCase):
    def test_singleton(self):
        f1 = FileSingletonV2('Test File')
        f2 = FileSingletonV2('Test File')

        self.assertIs(f1, f2)

        file = f1.get_file()
        self.assertEqual(file, 'Test File')
