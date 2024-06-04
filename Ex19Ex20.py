
def sum_upto_number(max):
    i = 1
    j = 0
    while i <= max:
        j += i
        i += 1
    avg = j/max
    print("Sum = " + str(j) + " Avg of the number = " + str(avg))

sum_upto_number(200)