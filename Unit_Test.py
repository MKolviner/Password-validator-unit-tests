from unittest import TestCase
from main import PasswordValidator


class TestPasswordValidator(TestCase):

    def test_password_validator_0(self):
        pas = PasswordValidator()
        actual = pas.check_password("123")
        expected = "Пароль слишком короткий!"
        self.assertEqual(actual, expected)

    def test_password_validator_2(self):
        pas = PasswordValidator()
        actual = pas.check_password("qwerty")
        expected = "Пароль должен содержать цифры!"
        self.assertEqual(actual, expected)

    def test_password_validator_3(self):
        pas = PasswordValidator()
        actual = pas.check_password("qwerty123")
        expected = "Пароль должен содержать спецсимволы!"
        self.assertEqual(actual, expected)

    def test_password_validator_4(self):
        pas = PasswordValidator()
        actual = pas.check_password("qwerty1@2#3")
        expected = "Пароль соответствует требованиям"
        self.assertEqual(actual, expected)