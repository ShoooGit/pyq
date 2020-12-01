import unittest


def fizzbuzz(num):
    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)


class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz_fizz(self):
        """3の倍数のテスト."""
        self.assertEqual(fizzbuzz(6), 'Fizz')

    def test_fizzbuzz_buzz(self):
        """5の倍数のテスト."""
        self.assertEqual(fizzbuzz(25), 'Buzz')

    def test_fizzbuzz_fizzbuzz(self):
        """15の倍数のテスト."""
        self.assertEqual(fizzbuzz(30), 'FizzBuzz')

    def test_fizzbuzz_not_fizzbuzz(self):
        """3と5の倍数以外のテスト."""
        self.assertEqual(fizzbuzz(11), '11')