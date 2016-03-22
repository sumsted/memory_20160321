from unittest import TestCase, main
from demo3_client import *


class TestDemo3(TestCase):
    def test_hi(self):
        name = 'bob'
        self.assertEqual(hi(name), None)

    def test_bye(self):
        name = 'felicia'
        self.assertEqual(bye(name), None)

if __name__ == '__main__':
    main()
