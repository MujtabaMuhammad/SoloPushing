# name_list = ['a', 'b', 'c', 'd', 'e']
# salary_list = [100, 200, 300, 400, 500]
# days_missed = [1, 2, 3, 4, 5]
cumulative_dict = {'a': {'salary': 500, 'days_missed': 4},
                   'b': {'salary': 200, 'days_missed': 5},
                   'c': {'salary': 300, 'days_missed': 1},
                   'd': {'salary': 400, 'days_missed': 2},
                   'e': {'salary': 500, 'days_missed': 3}}
new_list = []


def get_days_off(ep):
    return cumulative_dict[ep]['days_missed']


def get_salary(ke):
    return cumulative_dict[ke]['salary']


# for k, v in cumulative_dict.items():
#   new_list.append((k,get_salary(k), get_days_off(k)))


def get_second_element(t):
    return t[1]


smallest_value = min(cumulative_dict, key = get_salary)
print(new_list, smallest_value)
#print(get_salary())
