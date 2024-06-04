reference_apt_price = input("Enter values seprated by comma: ")
ref_apt_list = [int(ref) for ref in reference_apt_price.split(',')]
sum = 0
index = 0
result_list = []
for price in ref_apt_list:
    if price > 0:
        sum += price
        index += 1
    else:
        print("Entry is zero, quitting program")

avg_price = sum/index
print(avg_price)

registered_apt_price = input("Enter values of registered apartments separated by commas: ")
reg_apt_list = [int(num) for num in registered_apt_price.split(',')]
for reg_apt in reg_apt_list:
    if reg_apt > avg_price:
        result_list.append("Above average")
    elif reg_apt == avg_price:
        result_list.append("Same as average")
    elif 0 < reg_apt < avg_price:
        result_list.append("Below Average")
    else:
        result_list.append("Quit Program")

print(result_list)
