'''Create a program that:
    Calculates the sum of 1+2+3+4...+98+99
    Prints the sum of 1+2+3+4...+98+99
    Output: "The sum is 4950"

    Calculates the sum of 1+3+5+7...+99+101
    Prints the sum of 1+3+5+7...+99+101
    Output: "The sum is 2601"

'''

i = 1
j = 0
while i < 100: #change to  101 for second condition
  j += i
  i += 2  #change to 1 for first condition

print(j)
