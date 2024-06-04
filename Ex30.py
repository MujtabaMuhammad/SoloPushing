''' A company asked you to create a program that reads an employee name and
salary and store them into proper lists.The number of employees is unknown.
To exit the program the user must input "quit". Before the exit find the employees
with the maximum salary and print who they are.
Create a program that: Reads employee name and salary, store them into different lists
    Asks the user to continue
    If the user wants to exit the program find and print the employees with maximum salary
    Input: [Mary, John, George, Nicole], [2343, 2134, 5342, 5342]
    Output: George - 5342, Nicole - 5432 '''

name_of_employees = input("Please enter employee names and salaries seprated by commas:  ")
employee_salary_list = name_of_employees.split(',')
employee_name = []
salary_list = []
top_paid = []
for i in range(0, len(employee_salary_list), 2):
    # Add employee names to the employee_name list
    employee_name.append(employee_salary_list[i].strip())  # .strip() removes any leading or trailing whitespaces

    # Add salaries to the salary_list after converting to integer
    salary_list.append(float(employee_salary_list[i + 1].strip()))

element_to_find = max(salary_list)
top_paid = [(employee_name, salary_list) for name, salary in zip(employee_name, salary_list) if
            salary == element_to_find]
for name, salary in top_paid:
    print(f"{name} - {salary}")

indexes = []
for index, value in enumerate(salary_list):
    if value == element_to_find:
        indexes.append(index)
#        print(indexes)
# continue_program = input("type exit if you want to close porgram: ")
# if continue_program.lower() == "exit":
for ind in indexes:
    top_paid = employee_name[ind]
    #       print(top_paid, element_to_find)
    quit()
'''
for sal in salary_list:
    for sal1 in salary_list:
        if sal > sal1:
            print(sal)'''
# print (employee_name, salary_list)
