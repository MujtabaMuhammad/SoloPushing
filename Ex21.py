def avg_of_numbers(num1,num2, num3, num4, num5):
    average = (num1+num2+num3+num4+num5) / 5
    print("the average is = " + str(average))


def positive_or_negative(num1,num2, num3, num4, num5):
    numbers =(num1,num2,num3,num4,num5)
    for nums in numbers:
        if nums < 0:
            print("negative")
        else:
            print("positive")


positive_or_negative(4,11,-4,-9,9)




