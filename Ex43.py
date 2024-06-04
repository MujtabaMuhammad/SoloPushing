user_account = {'username': {'password': 'password', 'hasPhoto': True, 'email': 'email'},
                'Mujtaba': {'password': 'abc123',
                            'hasPhoto': False,
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


username = input("Please enter a username: ")
password = input("PLease enter password (must be numbers only): ")
while len(password) < 6 or len(password) > 12 or type(password) != int:
    print("Password must be between 6 to 12 digits")
    password = input(" Try again ")
photo = input("Does the user have a photo (Y/N? ")
email = input("What is the email of the user? ")

user_accout = adding_value_to_dict(username, password, photo, email)
user_account.update(user_accout)

print(user_account)
