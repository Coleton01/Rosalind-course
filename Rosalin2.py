#Rosalind problem 2"Problem
#ProblemProblem
#Given: Two positive integers a and b each less than 1000.

#Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a
 #and b


from math import sqrt
from random import random, randint



def hypsquared():  'function verify int less then 1000 as input and finding solution for hypo'
    a = 899
    b = 934


    if a < 1000 and b < 1000:
        int(b)
        int(a)
        c = int((a**2) + (b**2))

    else:
        print("no")
    print(a,b,c)
hypsquared()
