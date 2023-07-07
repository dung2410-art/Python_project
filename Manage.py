import Employee
import Validate


employee = Employee.Employee
validate = Validate
regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
regex_phone = "^\\+?[1-9][0-9]{7,14}$"


def menu():
    print("=====Employee Management=====")
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. Search Employee")
    print("5. Exit")
    choice = validate.input_integer_limit(1, 5)
    return choice


def add_employee(_list):

    # Enter code

    print("Enter code: ")
    code = input()
    if code == validate.input_string():
        print("Invalid!!!")
        return

    if not validate.code_exist(_list, code):
        print("Code exist")
        return

    # Enter name

    print("Enter name: ")
    name = input()
    if name == validate.input_string():
        print("Invalid!!!")
        return

    # Enter email

    print("Enter  email: ")
    email = input()
    if validate.check_email(email, regex_email):
        print("Invalid!!!")
        return

    # Enter phone

    print("Enter phone: ")
    phone = input()
    if validate.check_phone(phone, regex_phone):
        print("Invalid!!!")
        return

    if not validate.check_duplicate(_list, code, name, email, phone):
        print("Duplicate")
        return

    _list.append(employee(code, name, email, phone))
    print("Add successful")


def update_employee(_list):

    # Enter code

    print("Enter code: ")
    code = input()
    if code == validate.input_string():
        return

    if validate.code_exist(_list, code):
        print("Code not found")
        return

    # Enter code update

    print("Enter code update: ")
    code_update = input()
    if code_update == validate.input_string():
        return

    _employee = get_employee_by_code(_list, code)

    # Enter name

    print("Enter name: ")
    name = input()
    if name == validate.input_string():
        return

    # Enter email

    print("Enter email: ")
    email = input()
    if validate.check_email(email, regex_email):
        print("Invalid!!!")
        return

    # Enter phone

    print("Enter phone: ")
    phone = input()
    if validate.check_phone(phone, regex_phone):
        print("Invalid!!!")
        return

    if not validate.change_info(_employee, code, name, email, phone):
        print("Nothing change")
        return

    _employee.set_code(code)
    _employee.set_name(name)
    _employee.set_email(email)
    _employee.set_phone(phone)
    print("Update Successfully")


def delete_employee(_list):

    # Enter code

    print("Enter code: ")
    code = input()
    if code == validate.input_string():
        return

    _employee = get_employee_by_code(_list, code)

    if _employee is None:
        print("Employee not found")
        return
    else:
        _list.remove(_employee)
    print("Delete successfully")


def search_employee(_list):

    # enter name

    print("Enter name: ")
    name = input()
    if name == validate.input_string():
        return

    list_found_by_name = list_found(_list, name)

    if len(list_found_by_name) == 0:
        print("List empty")
    else:
        print("%-10s%-15s%-25s%-20s", "Code", "Name", "Email", "Phone")

        for employee in list_found_by_name:

            print("%-10s%-15s%-25s%-20s", employee.get_code(),
                  employee.get_name(),
                  employee.set_email(),
                  employee.get_phone())


def get_employee_by_code(_list, code):

    for employee in _list:

        if employee.get_code().lower() == code.lower():
            return employee

        return


def list_found(_list, name):

    list_found_by_name = []

    for employee in _list:

        if name == employee.get_name():
            list_found_by_name.append(employee)

    return list_found_by_name
