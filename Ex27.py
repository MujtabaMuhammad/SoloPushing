import time

try:
    seconds = int(input("Please enter the number of seconds : "))
    if seconds > 0:
        while seconds > 0:
            print(seconds)
            time.sleep(1)
            seconds -= 1
        print("Time is up, Go")

    else:
        print("Entry is invalid")
except:
    print("Invalid entry")



