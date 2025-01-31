from unittest import TestCase
from main import unit_test


class TestPasswordValidator(TestCase):

    def test_password_validator(self):
        self.assertNotEqual(unit_test("123"), "Пароль слишком короткий!")

    def test_password_validator_2(self):
        self.assertNotEqual(unit_test("qwerty"), "Пароль должен содержать цифры!")

    def test_password_validator_3(self):
        self.assertNotEqual(unit_test("qwerty123"), "Пароль должен содержать спецсимволы!")
