# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Employee
import Manage


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


_list = []

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

while True:
    choice = Manage.menu()
    if choice == 1:
        Manage.add_employee(_list)
    elif choice == 2:
        Manage.update_employee(_list)
    elif choice == 3:
        Manage.delete_employee(_list)
    elif choice == 4:
        Manage.search_employee(_list)
    elif choice == 5:
        break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
