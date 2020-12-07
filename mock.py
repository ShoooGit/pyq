import unittest
from unittest import mock

from user import get_username, get_sign


class TestGetUsername(unittest.TestCase):
    def test__get(self):
        dummy_user = mock.Mock()
        dummy_user.username = 'john'

        self.assertEqual(get_username(dummy_user), 'john')


class TestGetSign(unittest.TestCase):
    def test__get(self):
        dummy_user = mock.Mock()
        dummy_user.get_fullname.return_value = 'John Doe'
        dummy_user.email = 'john@example.com'

        self.assertEqual(get_sign(dummy_user),
                         'John Doe <john@example.com>')
        dummy_user.get_fullname.assert_called_with()