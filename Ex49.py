# bank has users. users info are name, id, balance.
# Create, read info(id, balance), check if user already exists.
# if user has 0 balance, copy to a new list , delete account from active list.

BankUsersActive = [(1, 'mm', 0), (2, 'mujm', 100), (3, 'Ali', 404)]
DeletedUsers = []


def reading_info(id):
    for i in BankUsersActive:
        if id == i[0]:
            print(i)
        break
    print("User Id does not exist")
    return


def reading_info_three(user_id):
    for user in BankUsersActive:
        if user_id == user[0]:
            print(user)
            return
    print("User Id does not exist")


def reading_info_two(user_id):
    found = False
    for user in BankUsersActive:
        if user_id == user[0]:
            print(user)
            found = True
            break
    if not found:
        print("User Id does not exist")
    return


def people_bal_zero():
    for i in BankUsersActive:
        if i[2] == 0:
            DeletedUsers.append(i)
            BankUsersActive.remove(i)
    print(DeletedUsers, BankUsersActive)
    return


people_bal_zero()
