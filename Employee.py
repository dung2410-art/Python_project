

class Employee:

    def __init__(self, code, name, email, phone):

        self._code = code
        self._name = name
        self._email = email
        self._phone = phone

    def get_code(self):
        return self._code

    def set_code(self, code):
        self._code = code

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_phone(self):
        return self._phone

    def set_phone(self, phone):
        self._phone = phone

    def __str__(self):
        return self._name + " " \
            + self._code + " " \
            + self._email + " " \
            + self._phone + " "
