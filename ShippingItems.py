'''
You want to buy something from Amazon.
The seller charges different prices for shipping cost based on location.
For US it's 5$ for Europe it's 7$ for Canada it's 3$ for other places it's 9$
Create a program that:
    Reads the cost of the product
    Reads your location
    Print the amount of money you have to pay
    Ouput: "You have to pay 23$, 20$ for the product and 3$ for shipping cost"
'''

def shipment_function(location):
    product = 20
    total_cost = 0
    if location == "US" or "us":
        total_cost = product + 5
        print("You have to pay " + str(total_cost) + " 20$ for the product and 5 $ for shipping cost")
    elif location == "Europe":
        total_cost = product + 7
        print("You have to pay " + str(total_cost) + " 20$ for the product and 7 $ for shipping cost")
    elif location == "Canada":
        total_cost = product + 3
        print("You have to pay " + str(total_cost) + " 20$ for the product and 3 $ for shipping cost")
    else:
        total_cost = product + 9
        print("You have to pay " + str(total_cost) + " 20$ for the product and 9 $ for shipping cost")


shipment_function("us")
