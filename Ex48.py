# users info are name, id, balance.
# Create check if user already exists.
bank_customers = {1: {'name': 'mm', 'balance': 43},
                  2: {'name': 'mm', 'balance': 0}}
to_delete = []


def adding_to_dictionary(id, name, balance):
    customer_credientials = {'name': name,
                             'balance': balance}
    new_customer = {id: customer_credientials}
    bank_customers.update(new_customer)

    print(new_customer)


def delete_people_with_zero_bal():
    for custs, vals in bank_customers.items():
        if vals['balance'] == 0:
            to_delete.append(custs)
    for i in to_delete:
        del bank_customers[i]

    print(to_delete, bank_customers)
    return


def user_already_exists(ur_id):
    return ur_id in bank_customers


def read_info(ur_id):
    for customers, values in bank_customers.items():
        if customers == ur_id:
            print(customers, values)
        else:
            print("User ID not found")
    return


usr_id = input("Please enter Id: ")
while user_already_exists(usr_id):
    print("This id is already taken, try again")
    usr_id = input("Id: ")

name = input("What is the name of the account holder? ")
balance = input("Balance with which user starting the account: ")

adding_to_dictionary(usr_id, name, balance)
