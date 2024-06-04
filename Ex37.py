'''
Create a program that:

    Orders the salaries by biggest salary first
    Prints all employees in order by lowest salary first
    Output: "later when I run the script"

'''
from operator import itemgetter
def main():
    user_input = input("Please enter the name and salaries of employees: ")
    employee_names_salaries = user_input.strip().split(',')
    employee_names = [employee_names_salaries[i] for i in range(0, len(employee_names_salaries), 2)]
    employee_salaries = [employee_names_salaries[i + 1] for i in range(0, len(employee_names_salaries), 2)]
    data = list(zip(employee_names, employee_salaries))
    ordered_list = sorted(data, key = lambda x: x[1])
    ordered_names = list(map(itemgetter(0), ordered_list))
    ordered_salaries = list(map(itemgetter(1),ordered_list))
    print(data, ordered_names, ordered_salaries)


main()
