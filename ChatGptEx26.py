apt_prices = input("Enter apt prices separated by commas: ")
price_list = [int(num) for num in apt_prices.split(',')]

total_price = 0
num_registered = 0
for price in price_list:
    if price > 0:
        total_price += price
        num_registered += 1
    else:
        print("Entry is 0 or negative. Exiting program.")
        exit()

if num_registered == 0:
    print("No apartments registered.")
    exit()

avg_price = total_price / num_registered
print(str(num_registered) + " apartments have registered. The average price for rent is " + str(avg_price))

reg_apt_prices = input("Enter prices of registered apartments separated by commas: ")
reg_price_list = [int(nu) for nu in reg_apt_prices.split(',')]

for price in reg_price_list:
    if price > avg_price:
        print("Above average price")
    elif price == avg_price:
        print("Same as average price")
    else:
        print("Below average price")
