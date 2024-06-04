'''
    Reads employee name and salary, store them into different lists
    Asks the user to continue
    If the user wants to exit the program find and print the total number of employees and total amount of salaries
    Input: [Mary, John, George, Nicole], [2343, 2134, 5342, 5342]
    Output: "4 employees and the total amount of salaries is 15161$"
'''
import statistics
def main():
    user_input = input("Please enter the name and salaries of employees: ")
    employee_names_salaries = user_input.strip().split(',')
    employee_names = [employee_names_salaries[i] for i in range(0, len(employee_names_salaries), 2)]
    employee_salaries = [employee_names_salaries[i + 1] for i in range(0, len(employee_names_salaries), 2)]
    emp_salaries_float = [float(i) for i in employee_salaries]
    avg_salary = statistics.mean(emp_salaries_float)
    comparative_list = [avg_salary - i for i in emp_salaries_float]
    higher_than_average_salary_list = []
    concatenated_list = []
    for i, x in enumerate(comparative_list):
        if x > 0:
            higher_than_average_salary_list.append(employee_names[i])
            del employee_names[i]

    asking_user_to_quit = input("would you like to quit the program ? ")
    if asking_user_to_quit.lower() == "quit":
        print("The average salary is " + str(avg_salary) + " ")
        print(higher_than_average_salary_list)
        print(employee_names)
        print("Number of employees removed: " + str(len(higher_than_average_salary_list)))
    else:
        return

    # print(len(employee_names_salaries)/2, sum(emp_salaries_float), avg_salary, comparative_list)

main()
