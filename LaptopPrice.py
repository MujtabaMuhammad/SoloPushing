'''
You are interested in buying a new laptop. You check the price and you see that the price is 300$ without the 10% tax.
Create a program that:
    Reads the price of the laptop
    Reads the tax percentage
    Prints the total amount

    Output: "The total price of the laptop is 330$"
'''
def laptop_budget(core_price, tax):
    x = core_price*(1 + (tax/100))
    print("Total price of the laptop is " + str(x))


laptop_budget(300,10)
