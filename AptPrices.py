
apt_prices = input("Enter apt prices seprated by commas: ")
price_list = [int(num) for num in apt_prices.split(',')]
index = 0
j = 0
for price in price_list:
    if price > 0:
        j += price
        index += 1
    else:
        print("Entry is 0 or negative. Exiting program")
avg_price = j/index
print(str(index) + " apartments have registered. The average price for rent is " + str(avg_price))
reg_apt_prices = input("Enter prices of registered apts separated by commas: ")
reg_price_list = [int(nu) for nu in reg_apt_prices.split(',')]

result = [avg_price - x for x in reg_price_list]
output_list = []
for reg_price in reg_price_list:
    if reg_price > avg_price:
        output_list.append("Above average")
    elif reg_price == avg_price:
        output_list.append("Same as average")
    elif 0 < reg_price < avg_price:
        output_list.append("Below average")
    else:
        output_list.append("Quit Program")

print(output_list)
print(result)

