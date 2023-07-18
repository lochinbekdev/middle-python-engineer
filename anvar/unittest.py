import unittest
from anvar.test import get_full_name


class NameTest(unittest.TestCase):
    def test_full_name(self):
        name = get_full_name('lochinbek','abduvoitov')
        self.assertEqual(name,"Lochinbek Abduvoitov")

unittest.main()