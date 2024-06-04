'''An internet cafe has 2 ways of charging. If the user is a member pays 2$/hour, Else the user pays 5$.
Find if someone is a member or not and calculate the price based on how many hours the user spend.
If the user is a member the tax is 10% else the tax is 20%.
Create a program that:
    Reads how many hours the user spend
    Check if is a member
    Add the proper tax fee
    Print the total amount the user has to pay
    Output: "The user is a member stayed 2 hours for 2$/hour plus the 10% the total amount is 4.4$"
'''
def internet_cafe_rates(hours, member):
    rate = 0
    if not member:
        rate = (hours*5 + 0.2*hours)
        print("The user is not a member stayed "+ str(hours) + " hours" + "for 5$/hour plus the 20% the total amount is " + str(rate) + " $")
    else:
        rate = (hours * 2 + 0.1 * hours)
        print("The user is a member stayed " + str(hours) + " hours" + "for 2$/hour plus the 10% the total amount is " + str(rate) + " $")

internet_cafe_rates(20.75,False)