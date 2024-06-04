# bank users, info balance everything provided.
# Ask program for options. create user(check if user exit) if update user id(check if exist) balance(check not to be negative),
# if result = 0(warning! might deactivate the account, are you sure you want to procceed?)---(if no, ask for new amount ot leave). name etc.
def bank_program():
    directory = {0: {'name': 'name',
                     'balance': 000},
                 1: {'name': 'abc',
                     'balance': 100}}
    action = input("What would you like to do today? (create, check balance, update existing id, update balance)")
    if action.strip().lower() == "create":
        while True:
            usr_id = input("Please enter Id: ")
            try:
                ur_id = int(usr_id)  # Convert user input to an integer
            except ValueError:
                print("Please enter a valid integer ID.")
                continue  # Continue the loop to re-prompt for ID

            if ur_id in directory:
                print("This id is already taken, try again")
            else:
                break
        name = input("What is the name of the account holder? ")
        balance = input("Balance with which user starting the account: ")
        directory.update({usr_id: {'name': name,
                                   'balance': balance}})
        print(directory)
    elif action.lower() == "cb":
        user_id = input('Please enter the user id : ')
        user_id_int = int(user_id)
        for k, v in directory.items():
            if user_id_int == k:
                print(v)
                break
        else:
            print("invalid id")
    elif action.lower() == "ub":
        user_id = input("Please enter the id of the user for which to update the balance:")
        user_id_int = int(user_id)
        if user_id_int in directory:
            new_balance = input("What is the new balance: ")
            new_balance_float = float(new_balance)
            #directory[user_id_int]['balance'] = new_balance_float
            directory[user_id_int]['balance'] = new_balance_float

            print(directory)
    elif action.lower() == "ueid":
        user_id = input("Please enter the id of the user for which to update the balance:")
        user_id_int = int(user_id)
        if user_id_int in directory:
            new_id = input("What is the new balance: ")
            new_id_int = int(new_id)
            directory[new_id_int] = directory.pop(user_id_int)

            print(directory)
    else:
        print("invalid input, quitting program")
        quit()


bank_program()
