'''
You've bought a Bitcoin and now it's on the rise!!!
Create a program that:
    Reads the value of the bitcoin at the time of purchase
    Reads the percentage of increase (or decrease)
    Prints the total value of your bitcoin
    Prints the increase or decrease value
    Example: bitcoin_value = 10000, bitcoin_increase = 10
    Output: total_bitcoin_value = 11000, bitcoin_increase_value = 1000
'''


def bitcoin_price(current_price, btc_increase):

    new_prc = current_price + current_price * (btc_increase / 100)
    print(new_prc)
    print("total_bitcoin_value = " + str(new_prc) + " bitcoin_increase_value = ")


bitcoin_price(900, 10)