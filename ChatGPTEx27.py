def register_user():
    print("Welcome! Please register a username and password.")
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password

def login(username, password):
    attempts = 0
    while attempts < 3:
        entered_username = input("Enter username: ")
        entered_password = input("Enter password: ")
        if entered_username == username and entered_password == password:
            print("Login successful!")
            return
        else:
            print("Invalid username or password. Please try again.")
            attempts += 1
    print("Too many failed login attempts. Exiting program.")

def main():
    registered_username, registered_password = register_user()
    login(registered_username, registered_password)

if __name__ == "__main__":
    main()
