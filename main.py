class PasswordValidator:
    pass_len_req = 6
    symbols = ["`", "~", "!", "@", "#", "№", "%", "^", "&", "?", "*", "-", "_", "+", "=", "[", "{", "]", "}", ":", ";",
               "|", "/", "$"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    def __init__(self, password):
        self.password = password

    def check_password(self):
        if self.password:
            symbols_check = any(elem in self.password for elem in PasswordValidator.symbols)
            numbers_check = any(elem in self.password for elem in PasswordValidator.numbers)

            if len(self.password) < PasswordValidator.pass_len_req:
                return "Пароль слишком короткий!"

            if numbers_check is not True:
                return "Пароль должен содержать цифры!"

            if symbols_check is not True:
                return "Пароль должен содержать спецсимволы!"

            return "Пароль соответствует требованиям"


def unit_test(password):
    validator = PasswordValidator(password)
    validator.check_password()
