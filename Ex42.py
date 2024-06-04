Login_creds = {'user1': {'password': 'password',
                         'hasPhoto': False,
                         'email': 'baberuth@gmail.com'},

               'user2': {'password': 'passwrd',
                         'hasPhoto': True,
                         'email': 'user3@gmail.com'},

                'user3': {'password': 'pass789',
                          'hasPhoto': True,
                          'email': 'user3@example.com'
    }
               }
# Update the dictionary with the new user

user4= {'user4':{'password': 'psd', 'hasPhoto':True, 'email':'gmail@gmail.com'}}

Login_creds['user5'] = {'password': 'pass', 'hasPhoto': False, 'email': 'andy@gmail.com'}
#Login_creds.update(user4)
print(Login_creds)
