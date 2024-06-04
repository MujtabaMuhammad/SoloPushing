'''Create a program that register a user with a username and a password. Then the user will try to login with the login credentials. If the user make 3 wrong attempts exit program with proper message.

Create a program that:
    Reads the username and the password
    Then the user try to login
    If the user makes 3 wrong attempts exit with proper message'''
print("Please create Credentials.")
name = input("Please enter username: ")
password = input("Please enter password: ")

login_attempts = 0
#username_input = input("Username = ")

while login_attempts < 3:
    user_name = input("UserName: ")
    user_password = input("Password: ")
    if user_password == password and user_name == name:
        print("Login Successful")
        exit()
    else:
        login_attempts += 1

print("Out of login attempts. Exiting program")
exit("Stop")

''' Compared to the program on the 4 hour long tutorial of python how is my code better or worst'''