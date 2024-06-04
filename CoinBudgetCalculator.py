'''
You are interested in buying crypto-currencies. You want to check the current amount of money you have and see how many coins you can buy in Bitcoin, Ethereum, and Litecoin.

Create a program that:

    Reads the total amount of money you have
    Reads the price of Bitcoin, Ethereum, and Litecoin
    Prints the amount of Bitcoin, Ethereum, and Litecoin you can buy

    Example: money = 100, bitcoin_price = 50, ethereum_price = 25, litecoin_price = 10
    Output: "With 100$ you can buy: 2 Bitcoins, 4 Ethereum, and 10 Litecoins"

'''

def coin_budget(money, bitcoin_price, ethereum_price, litecoin_price):
    x = 1/(bitcoin_price/money)
    y = 1/(ethereum_price/money)
    z = 1/(litecoin_price/money)
    print("With " + str(money) + " $ you can buy : " + str(x) + " Bitcoins, " + str(y) + " Ethereum " + str(z) + " Litecoins" )


coin_budget(100,50,25,10)

