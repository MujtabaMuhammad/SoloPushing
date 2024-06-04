'''
Create two variables a and b, and initially set them each to a different number. Write a program that swaps both values.

    Example: a = 10, b = 20
    Output: a = 20, b = 10

'''
a = 10
b = 20

def num_swap(a, b):
    temp = a
    a = b
    b = temp
    print("a = " + str(a), "b = " + str(b))


num_swap(4,5)