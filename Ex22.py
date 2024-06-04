'''Create a program that reads numbers and sum them until the user inputs a negative value
Create a program that:
    Reads numbers
    Sum them
    Prints the sum

    Input example: 5, 9, 3, 0, 2, 0, 4, -7
    Output: "The sum is 23"
'''

def sum_upto_number():
    numbers_input = input("Enter some numbers separated by commas: ")
    numbers_list = [int(num) for num in numbers_input.split(',')]
    i = 0
    for num in numbers_list:
            if num >=0:
                i += num
                num += 1
    print("List of numbers:", numbers_list, i)

sum_upto_number()