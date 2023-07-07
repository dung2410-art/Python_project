import re
import Employee


_employee = Employee.Employee


# check number to enter into the menu
def input_integer_limit(_min, _max):
    while True:
        try:

            result = int(input().strip())

            if result < _min or result > _max:
                raise ValueError

            return result

        except ValueError:

            print("Please input number in range {} {}".format(_min, _max))
            print("Enter again")


# check input string
def input_string():
    while True:
        result = input().strip()

        if result == "":

            print("Not empty")
            print("Please try again")

        else:

            return result


# check input integer

def input_int():
    while True:
        try:

            result = (int(input().strip()))
            return result

        except ValueError:

            print("Please  enter an integer number")
            print("Please enter again")


# check input yes or no

def check_yn():
    while True:
        result = input_string()

        if result.lower() == "y":

            return True

        if result.lower() == "n":

            return False

        print("Please input only Y or N")
        print("Enter again")


# check if code exist in list

def code_exist(_list, code):
    for employee in _list:

        if code.lower() == employee.get_code().lower():
            return True

        return False


# check if element in list

def check_duplicate(_list, code, name, email, phone):

    for employee in _list:

        if code.lower() == employee.get_code().lower() \
                and name.lower() == employee.get_name().lower() \
                and email.lower() == employee.get_email().lower() \
                and phone == employee.get_phone():
            return True

        return False


# check info to update
def change_info(employee, code, name, email, phone):

    if code.lower() == employee.get_code.lower() \
            and name.lower() == employee.get_name().lower() \
            and email.lower() == employee.get_email().lower() \
            and phone == employee.get_phone():
        return False

    return True


# check regex to validate email

def check_email(mess, regex):

    print(mess)

    while True:

        _input = input()

        if not re.match(mess, _input):

            print("Invalid, please enter a valid email!!!")
            continue

        return _input


# check regex to validate phone

def check_phone(mess, regex):

    print(mess)

    while True:

        _input = input()

        if not re.match(mess, _input):

            print("Invalid, please enter a valid phone!!!")
            continue

        return _input




