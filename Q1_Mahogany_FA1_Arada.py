import math

#Prompt the user for coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

#Calculate the distance
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

#Display the output
print("The distance between the two points is: ", distance)

#Reflection
"""
Using library is more practical because it provides pre-tested, highly optimized functions like sqrt() and pow(), saving development time and reducing coding errorrs. In this activity, instead of writing complex algorithms from scratch to calcul;ate square roots and exponents manually, I was able to solve the distance formula cleanly in a single line of code. Without these library functions, it would be much more longer and harder.
"""











