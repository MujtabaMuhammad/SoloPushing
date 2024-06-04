from statistics import mean

'''data = [1, 1, 2, 3, 5, 8, 13]
colors = ['red', 'blue', 'green', 'yellow']
water_level = [730, 709, 682, 712, 733, 751, 740]
water_level.insert(2,693)
del water_level[0]
water_level.remove(709)
print(water_level)

tourist_arrivals = [7.8, 9.0, 10.4, 10.9, 14.7, 15.6, 22.7, 22.3, 14.8, 11.4, 8.6, 9.1]
user_input = input("Please enter the number you want to verify:")
number_to_verify = float(user_input)
if number_to_verify in tourist_arrivals:
    print("Value is found")
else:
    print("Value not found")
'''

x = 0.0
y = 0.0
z = 0.0
monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12,
                    1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45, 3000.00, 2000.00]
'''
for ms in monthly_spending:

    if ms <= 1999.99:
        x += 1
    elif 1999.99 < ms <= 3000.00:
        y += 1
    elif 3000.00 < ms:
        z += 1
        
print(f"martha's spending was low in {x} month medium in {y} and high in {z} months")


average_for_first_half = mean(monthly_spending[0:6])
average_for_second_half = mean(monthly_spending[7:])
print(average_for_first_half, average_for_second_half)
sum_expenses = [0, 0]
for index in range(len(monthly_spending)):
    if index < 6:
        sum_expenses[0] += monthly_spending[index]
    else:
        sum_expenses[1] += monthly_spending[index]
print('Average expense Jan-June: {}'.format(sum_expenses[0] / 6))
print('Average expense July-Dec: {}'.format(sum_expenses[1] / 6))

monthly_spending_eurs = []

for i in range(len(monthly_spending)):
    monthly_spending_eurs.append(monthly_spending[i] * 0.88)

for i in range(len(monthly_spending_eurs)):
    monthly_spending_eurs[i] = round(monthly_spending_eurs[i],2)
   


print(round(monthly_spending_eurs[1],2))


spending_card1 = [3231.22, 3039.49, 2813.55, 2271.80, 1922.53, 2335.07]
spending_card2 = [3883.04, 3073.93, 3727.18, 2340.49, 1651.91, 1585.41, 2025.84, 3367.66, 2442.75, 2395.70, 3328.55,
                  3453.42]
total_spending = [spending_card1[i] + spending_card2[i] for i in range(len(spending_card1))]
for j in range((len(spending_card2)-len(spending_card1)), len(spending_card2),1):
    total_spending.append(spending_card2[j])
for j in range(len(total_spending)):
    total_spending[j] = int(total_spending[j])

print(total_spending)



def get_long_words(input_list, min_len):
    output_list = []
    for i in input_list:
        if len(i) <= min_len:
            output_list.append(i)

    print(output_list)

get_long_words(['bird', 'carpet', 'bicycle', 'orange', 'floccinaucinihilipilification'],6)




'''


absolute_values = [13, -15, 42, -165, 32, -678, 1, 41]
def absolute_val(lst):
    new_list = []
    for i in lst:
        new_list.append(abs(i))

    print(new_list)


absolute_val([13, -15, 42, -165, 32, -678, 1, 41])






