from statistics import mean
'''my_list = [(3, 'c'), (1, 'a'), (2, 'b')]
my_list.sort(key=lambda x: x[0])  # Sorts the list in place based on the first element of each tuple
print(my_list)
def somepower(n):
    return lambda a : a ** n

squared = somepower(2)
cubbed = somepower(3)

print(squared(5))'''
x = lambda *args : print(mean(args))
x(1,2,3,4)
