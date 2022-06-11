from unittest import TestCase

from context import hello


class TestHello(TestCase):
    """
    testing sample hello function
    """

    def test_simple_scenario(self):
        """
        test with simple scenario
        """
        self.assertEqual("Hello, World!", hello.hello())
        self.assertEqual("Hello, python!", hello.hello("python"))

    def test_some_error_case(self):
        """
        test some error case
        """
        self.assertEqual("Hello, None!", hello.hello(None), "Who is None")
        self.assertEqual("Hello, 1000!", hello.hello(1000), "Who is number")
        self.assertEqual("Hello, (0, 1)!", hello.hello((0, 1)), "Who is tuple")
