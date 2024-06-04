'''A cell phone company has the following billing policy
	Fixed cost 25$
Call duration(in seconds) 	Charge($/per second)
1-500 	0,01
501-800 	0,008
801+ 	0,005
Create a program that: Reads how many seconds was the calls duration Calculates the monthly bill for the subscriber
    Prints the total amount
    Output: "total amount: 48$"
'''
def phone_bill(seconds):

    t = seconds
    cost_of_x = 0
    if t <= 500:
        cost_of_x = t * 0.01
    elif t<=800:
        cost_of_x = (t-500) * 0.08 + 5
    else:
        cost_of_x = (t-800) * 0.005 + 23.92 + 5

    print(cost_of_x)

phone_bill(2000)