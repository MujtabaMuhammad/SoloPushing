# bank has users. users info are name, id, balance. Create users and ask for id number and balance.

bank_customers = {'id': { 'name': 'name',
                  'balance': 000}}

id = input('Please enter the id: ')
id_int = int(id)
name = input('Please enter name: ')
balance = input('What is the balance associated with this account? ')
balance_int = int(balance)

new_user = {'name': name,
            'balance': balance_int}

bank_customers[id_int] = new_user


print(bank_customers)
