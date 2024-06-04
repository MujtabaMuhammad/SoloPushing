user_account = {'username': {'password': 'password', 'hasPhoto': True, 'email': 'email'},
                'Mujtaba': {'password': 'abc123',
                            'hasPhoto': False ,
                            'email': 'mujtaba@gmail.com'}
                }


def adding_value_to_dict(username, password, hasPhoto, email):
    if photo.lower() == "yes":
        hasPhoto = True
    else:
        hasPhoto = False

    user_info = {'password': password,
                 'hasPhoto': hasPhoto,
                 'email': email}

    new_user = {username: user_info}

    return new_user


def email_already_exists(email):
    global user_account
    for user in user_account.values():
        if email == user['email']:
            return True
    return False


username = input("Please enter a username: ")
password = input("PLease enter password: ")
photo = input("Does the user have a photo (Y/N? ")
email = input("What is the email of the user? ")

while email_already_exists(email):
    print("This email is already in use please try again")
    email = input("Please enter a valid email: ")


user_accout = adding_value_to_dict(username, password, photo, email)
user_account.update(user_accout)

print(user_account)
