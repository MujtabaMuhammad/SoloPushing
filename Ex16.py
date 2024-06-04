'''A fast food chain has these meals
Meal 	Price
Burger 	5$
Pizza 	3$
Hot Dog 	1,5$
Create a program that: Reads the meal the customer wants Prints the cost of the meal Input example: "Hot Dog" Output: "Hot Dog 1,50$"
'''

def order():
    try:
        order = input("Please enter your order : ")
        if order == "Burger" or order == "burger":
            print("Burger 5$")

        elif order == "Pizza" or order == "pizza":
            print("Pizza 3$")

        elif order=="Hotdog" or order == "hotdog":
             print("Hotdog 1.50$")
    except:
        print("invalid entry")


order()

