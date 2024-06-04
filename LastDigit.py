'''Create a program that prints the last digit of a given integer
Create a program that:
    Reads the integer
    Prints the last digit
'''
from decimal import Decimal
import math

def last_digit(integer):
    a = float(integer)
    #way1
    div_by_ten = integer/10
    c = round(Decimal(div_by_ten) % 1,1)
    d = c * 10
    #way2
    e = math.floor(div_by_ten) * 10
    decimal_part = a - e

    print(d, decimal_part)

last_digit(1398)