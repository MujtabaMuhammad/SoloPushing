#This code for part one of exercise 50 did not work. It is not verifying unique id properly.
'''directory = {0: {'name': 'name',
                 'balance': 000},
             1: {'name': 'abc',
                 'balance': 100}}
usr_id = input("usr id please: ")
usr_id = input("Please enter Id: ")
ur_id = int(usr_id)
while True:
    if ur_id in directory:
        print("This id is already taken, try again")
        ur_id = input("Id: ")
        try:
            ur_id = int(usr_id)  # Convert user input to an integer
        except ValueError:
            print("Please enter a valid integer ID.")
            continue
    else:
        break
        '''

directory = {
    0: {'name': 'name', 'balance': 0},
    1: {'name': 'abc', 'balance': 100}
}

user_id = input('Please enter the user id: ')
try:
    user_id_int = int(user_id)
except ValueError:
    print("Please enter a valid integer ID.")
    quit()

# Check if the ID exists in the directory
if user_id_int in directory:
    new_balance = input("Enter the new balance: ")
    try:
        new_balance_float = float(new_balance)
        directory[user_id_int]['balance'] = new_balance_float
        print(f"Updated user {user_id_int}: {directory[user_id_int]}")
    except ValueError:
        print("Please enter a valid number for the balance.")
else:
    print("Invalid ID")
