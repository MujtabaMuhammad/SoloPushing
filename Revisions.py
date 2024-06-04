employee_name_salary = []
employee_name = []
employee_salary = []
employee_with_highest_salary = ""
'''
def list_creator(str_input):
    global employee_salary
    global employee_name
    data = str_input.strip().split(',')
    employee_name = [data[i].strip() for i in range(0,len(data),2)]
    employee_salary = [data[i+1].strip() for i in range(0,len(data),2)]
    print(employee_name, employee_salary)


def highest_paid_employee(employee_salary):
    #employee_name_clean = employee_name.strip().split(',')
    salary_data = employee_salary.strip().split(',')
    highest_paid = max(salary_data)
    index_of_highest_paid = salary_data.index(max(salary_data))
    print(highest_paid, index_of_highest_paid)

'''

def main():
    global employee_name_salary
    global employee_name
    global employee_salary
    global employee_with_highest_salary
    user_input = input("PLease enter names and salaries of employees separated by commas: ")
    employee_name_salary = user_input.strip().split(',')
    employee_name = [employee_name_salary[i].strip() for i in range(0, len(employee_name_salary), 2)]
    employee_salary = [employee_name_salary[i + 1].strip() for i in range(0, len(employee_name_salary), 2)]
    index_of_highest_paid = employee_salary.index(max(employee_salary))
    #list_of_indexes_of_highest_paid = [for i in employee_salary if i == max(employee_salary)]
    list_of_indexes_of_highest_paid = [index for index, salary in enumerate(employee_salary) if
                                       salary == max(employee_salary)]
    
    for i in list_of_indexes_of_highest_paid:
        print(f"{employee_name[i]} - {employee_salary[i]}")

main()
