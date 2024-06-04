# a function to feed values into the dictionary
# Check if the username or email is already taken and inform user if that is the case

employee_database = {'username': {'email': 'email',
                                  'password': 'password'},
                     'Mujtaba': {'email': 'mujtaba@gmail.com',
                                 'password': 'abc123'}
                     }


def adding_to_dictionary(username, email, password):
    emp_creds = {
                'email': email,
                 'password': password
                 }
    new_emp = {username: emp_creds}

    employee_database.update(new_emp)
    print(new_emp)
    print(employee_database)
    return new_emp


def existing_email(email):
    for emps in employee_database.values():
        if email == emps['email']:
            return True
    return False


def existing_username(usr_nm):
    for keys, value in employee_database.items():
        if usr_nm == keys:
            return True
    return False


username = input("Please enter the username: ")
while existing_username(username):
    print("username not available, try again")
    username = input("Username: ")

email = input("Please enter email")
while existing_email(email):
    print("email already in use, try a different one")
    email = input("Email: ")
password = input("Please enter the password: ")

adding_to_dictionary(username, email, password)
