import unittest
from py.CSP import CSP


class TestCSP(unittest.TestCase):

    def test_should_return_false(self):
        csp = CSP()
        self.assertEqual(True, False, "this is the message")


if __name__ == '__main__':
    unittest.main()
