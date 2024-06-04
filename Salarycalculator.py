''' The exercise is almost identical to a previous exercise with a minor change. In a company the monthly salary of an employee is calculated by
minimum wage 400$ per month, plus 20$ multiply by the employment years, plus 30$ for each employee kid, plus 100$ if the employee didn't miss 1 day of work.
Create a program that: Reads the employment years, Reads the number of each employee kids, Prints the total amount the employee must take
Output: "The total amount is 660$, 400$ minimum wage + 100$ for 5 years experience + 60$ for 2 kids + 100$ for not missing a day at work"
'''
def salary_calculator(min_wage, number_of_years, number_of_kids, missed_a_day):
    y = number_of_years * 20
    z = number_of_kids * 30
    if not missed_a_day:
        x = min_wage + y + z + 100
    else:
        x = min_wage + y + z
    print("Total wage is " + str(x) + " : " + str(min_wage) + " $ is the minimum wage + " + str(y) + "  for " + str(
        number_of_years) + " years of service and " + str(z) + " for " + str(number_of_kids) + " kids" +
          " + 100 $ for not missing a day." if missed_a_day == False else "Total wage is " + str(x) + " : "
        + str(min_wage) + " $ is the minimum wage + " + str(y) + "  for " + str(number_of_years)
          + " years of service and " + str(z) + " for " + str(number_of_kids) + " kids")
salary_calculator(400, 11, 2, False)
