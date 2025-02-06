
def init():

    while True:
        # unit_test(input())
        validator = PasswordValidator(input())
        validator.check_password()


class PasswordValidator:
    pass_len_req = 6
    symbols = ["`", "~", "!", "@", "#", "№", "%", "^", "&", "?", "*", "-", "_", "+", "=", "[", "{", "]", "}", ":", ";",
               "|", "/", "$"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    def check_password(self, password):
        if password:
            symbols_check = any(elem in password for elem in PasswordValidator.symbols)
            numbers_check = any(elem in password for elem in PasswordValidator.numbers)

            if len(password) < PasswordValidator.pass_len_req:
                print("Пароль слишком короткий!")
                return "Пароль слишком короткий!"

            if numbers_check is not True:
                print("Пароль должен содержать цифры!")
                return "Пароль должен содержать цифры!"

            if symbols_check is not True:
                print("Пароль должен содержать спецсимволы!")
                return "Пароль должен содержать спецсимволы!"

            print("Пароль соответствует требованиям")
            return "Пароль соответствует требованиям"

if __name__ == "__main__":
    init()
