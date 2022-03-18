import unittest
from vanilla_pkg import Dog


class Dog_test(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.Dog = Dog("Kirby")

    def test_get_has_a_name(self):
        self.assertIsInstance(self.Dog.name, str), "got the data file"

    def test_tricks(self):
        self.assertIsInstance(self.Dog.tricks, list), "tricks is a list"
        self.assertFalse(self.Dog.tricks), "list is empty"
        self.Dog.add_trick("roll over")
        self.Dog.add_trick("play dead")
        self.assertEqual(len(self.Dog.tricks), 2), "Dog now knows 2 tricks"
