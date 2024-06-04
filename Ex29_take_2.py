fixed_cost = 0
hourly_cost = 0
total_cost = fixed_cost+hourly_cost

def member_or_not(input_from_u):
    global fixed_cost
    if input_from_u.lower() == 'yes':
        fixed_cost = 1.5
    elif input_from_u.lower() == 'no':
        fixed_cost = 3
    else:
        print("invalid input")
        return

def number_of_hours(hours):
    global hourly_cost
    if hours == 1:
        global hourly_cost = 4
    elif hours == 2:
        global hourly_cost = 7
    elif hours == 3:
        global hourly_cost = 9
    elif hours == 4:
        global hourly_cost == 10
    else:
        global  hourly_cost = 10 + ((hours - 4) *0.5)