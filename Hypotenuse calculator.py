# hypotenuse of a right angled triangle

import math
print("Welcome to the hypotenuse calculator")
P = float(input("What is the length of perpendicular in cm? "))
B = float(input("What is the length of base in cm? "))

result = P ** 2 + B  ** 2
result1 = math.sqrt(result)

print(f" Te hypotenuse of the triangle is {result1}cm.")