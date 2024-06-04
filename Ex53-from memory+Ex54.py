name_list = ['a', 'b', 'c', 'd', 'e']
salary_list = [100, 200, 300, 400, 500]
days_missed = [1, 2, 3, 4, 5]

emp_dict = {'a': {'salary': 100, 'days_missed': 1},
            'b': {'salary': 200, 'days_missed': 2},
            'c': {'salary': 300, 'days_missed': 3},
            'd': {'salary': 400, 'days_missed': 4},
            'e': {'salary': 500, 'days_missed': 5}}


def salary(key):
    return emp_dict[key]['salary']




def absences(key):
    return emp_dict[key]['days_missed']

'''
lowest_salary = min(emp_dict,key=salary)
highest_salary = max(emp_dict,key=salary)
fewest_skipped_days = min(emp_dict,key=absences)
most_skipped_days = max(emp_dict,key=absences)
print(lowest_salary,highest_salary,fewest_skipped_days,most_skipped_days)
'''

def razr():
    lowest_salary = min(emp_dict, key=salary)
    fewest_skipped_days = min(emp_dict, key=absences)
    raise_amount = 1.1
    var = int((emp_dict[lowest_salary]['salary'] * raise_amount))
    emp_dict[lowest_salary]['salary'] = var
    var2 = int((emp_dict[fewest_skipped_days]['salary'] * raise_amount))
    emp_dict[fewest_skipped_days]['salary'] = var2
    print(emp_dict)


razr()