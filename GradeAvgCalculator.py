'''
It's the end of the semester and you got your grades from three classes: Geometry, Algebra, and Physics.
Create a program that:
    Reads the grades of these 3 classes (Grades range from 0 - 10)
    Calculate the average of your grades
    Example: Geometry = 6, Algebra = 7, Physics = 8
    Output: average_score = 7
'''
from statistics import mean

def avg_calculator(geomtry, algebra, physics):
    inp_lst = [float(geomtry), float(algebra), float(physics)]
    avg_grade = mean(inp_lst)

    print(avg_grade)

avg_calculator(4,6,2)