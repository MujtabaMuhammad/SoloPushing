def add_user_to_dict(username, password, has_photo, email):
    # Convert has_photo to a boolean value
    has_photo = True if has_photo.lower() == 'yes' else False
    # Create the user dictionary
    user_info = {
        'password': password,
        'hasPhoto': has_photo,
        'email': email
    }
    # Create the main dictionary with the username as the key
    user_dict = {
        username: user_info
    }

    return user_dict


# Input values
username = input("Enter username: ")
password = input("Enter password: ")
has_photo = input("Has uploaded photo (Yes/No): ")
email = input("Enter email: ")

# Create the user dictionary
user_account = add_user_to_dict(username, password, has_photo, email)

# Output the user dictionary
print(user_account)
