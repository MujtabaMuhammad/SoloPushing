# You have two lists.
# The first list has the names of 5 employees and the second list has their salary. Create a dictionary with the names as key and salaries as value.


name_list = ['a', 'b', 'c', 'd', 'e']
salary_list = [100, 200, 300, 400, 500]

cumulative_dict = {}

for i,j in zip(name_list,salary_list):
    cumulative_dict.update({i:j})
print(cumulative_dict)

'''
for i in range(len(name_list)):
    cumulative_dict.update({name_list[i]: salary_list[i]})
print(cumulative_dict)
'''