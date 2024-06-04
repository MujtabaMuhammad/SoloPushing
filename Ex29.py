net_total = 0
number_of_drivers = 1


def park_garage():
    global net_total
    global number_of_drivers
    fixed_cost = 0
    total_charge = 0
    hourly_charge = 0

    while True:
        user_input = input("Are you a member? type Yes or No ")
        if user_input.lower() == 'yes' or user_input.lower() == 'no':
            hours_parked = input("Enter the number of hours you parked here: ")
            if user_input.lower() == 'yes':
                fixed_cost = 1.5
            else:
                fixed_cost = 3

            if float(hours_parked) == 1:
                hourly_charge = 2
            elif float(hours_parked) == 2:
                hourly_charge = 3.5
            elif float(hours_parked) == 3:
                hourly_charge = 4.5
            elif float(hours_parked) == 4:
                hourly_charge = 5
            elif float(hours_parked) > 4:
                hourly_charge = 5 + ((float(hours_parked) - 4) * 0.5)
            else:
                print("invalid entry try again")

            total_charge = fixed_cost + hourly_charge
            print(total_charge)
            program_continue = input("Do you want to continue the program? enter yes or no : ")
            if program_continue.lower() == 'yes':
                net_total += total_charge
                number_of_drivers += 1
                park_garage()

            elif program_continue.lower() == 'no':
                net_total += total_charge
                print("Number of drivers: " + str(number_of_drivers) + " total earnings: " + str(net_total))
                exit()
            else:
                print("invalid entry, try again: ")


park_garage()
