# username, a password, salary, and the email.
employee_dict = {'username': {'password': 'password', 'salary': 'salary', 'email': 'email'},
                 'Mujtaba': {'password': 'Bakistan',
                             'salary': 100000,
                             'email': 'mujtaba@gmail.com'}}


def adding_to_dict(username, password, salary, email):
    global employee_dict
    user_creds = {'password': password,
                  'salary': salary,
                  'email': email
                  }
    new_usr = {username: user_creds}

    employee_dict.update(new_usr)

    return new_usr


def check_for_username(user_n):
    global employee_dict
    for user in employee_dict.keys():
        if user_n == user:
            return True
    return False


def check_for_email(email):
    global employee_dict
    for user in employee_dict.values():
        if email == user['email']:
            return True
    return False


username = input("Please enter username: ")
while check_for_username(username):
    print("Username already exists, try again")
    username = input("Enter username: ")

password = input("Please enter Password: ")
salary = input("Please input salary: ")
email = input("Please enter email: ")
while check_for_email(email):
    print("Email already exists, try again")
    email = input("Enter email: ")

new_user = adding_to_dict(username, password, salary, email)
print(new_user)
