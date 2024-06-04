'''You start flipping a coin, count and print how many times the result was head or tails until you enter the word "stop".
 Then find and print the percentage of how many head or tails was the result.
Create a program that: Reads if the flipped coin was head or tails
    If the value is "stop", print proper message and quit program
    While value not "stop", count the result
    Print the proper message
    Calculates the percentage of head and tails
    Prints the proper message
    Input: "head", "tails", "tails", "tails", "head", "head", "tails", "tails", "tails", "head"
    Ouput: "Head won 4 times and tails won 6 times"
    Output: "40% Head, 60% Tails"
'''
#def head_tail_counter():
head = 0
tail = 0
results = input("Enter the results: ")
if results != "stop":
    results_list = results.split() # need a constant criteria to split the statment 
    print(results_list)
    for result in results_list:
        if result == "head" or result == " head":
            head += 1
        elif result == "tail" or result == " tail":
            tail += 1

    print("Heads: " + str(head) + " Tails: " + str(tail))
else:
    print("You entered stop and the program is not working")


