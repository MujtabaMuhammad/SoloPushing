'''You have started working and you are wondering how many things you can buy with the money you've earned.
A PS4 costs 200$, a Samsung phone 900$, a TV 500$, a game skin 9.99$
Create a program:  Notice that you can't but half TV or 1/4 of PS4. Reads how many hours you've worked Reads your hourly income Prints how many items you can buy
    Output: "I can buy 4 PS4, 1 Samsung, 3 TV, 80 game skin" '''
import math


def coin_budget(hourly_wage, number_of_hours):
    x = hourly_wage * number_of_hours
    ps = 200
    samsung_phone = 900
    tv = 500
    game_skin = 9.99
    num_of_ps = math.floor(x / ps)
    num_of_samsung = math.floor(x / samsung_phone)
    num_of_tv = math.floor(x / tv)
    num_of_game_skin = math.floor(x / game_skin)
    print("I can buy " + str(num_of_ps) + " PS4 " + str(num_of_samsung) + " Samsung " + str(num_of_tv) + " TVs " + str(
        num_of_game_skin) + " 80 game skin")


coin_budget(100, 50)
