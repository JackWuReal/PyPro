import unittest

from tools import add


class TestTool(unittest.TestCase):

    def test_1(self):
        # tool1 = Tools()
        self.assertEqual(add(1,3), int(1 + 3),)