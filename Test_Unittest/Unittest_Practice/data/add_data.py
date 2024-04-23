import unittest
from parameterized import parameterized

from Test_Unittest.Unittest_Practice.data.read_data import read_data_method
from Test_Unittest.Unittest_Practice.tools import login


class AddDataTest(unittest.TestCase):
    @parameterized.expand(read_data_method())
    def test_add_data(self,desc,username,password,expect):
        self.assertEqual(expect,login(username,password))
        print(f'{username}:{expect},{desc}')


if __name__ == '__main__':
    unittest.main()