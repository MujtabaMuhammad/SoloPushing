# You have two lists.
# The first list has the names of 5 employees and the second list has their salary. Create a dictionary with the names as key and salaries as value.


name_list = ['a', 'b', 'c', 'd', 'e']
salary_list = [100, 200, 300, 400, 500]
days_missed = [1, 2, 3, 4, 5]

cumulative_dict = {}

for i, j, k in zip(name_list, salary_list, days_missed):
    cumulative_dict[i] = {'salary': j, 'days_missed': k}
print(cumulative_dict)


