# circumference of a circle
print("Circumference and area calculator")
import math
R = float(input("What is the radius of the circle in cm?"))

result1 = R * 2 * math.pi
result2 = math.pi * R ** 2

R1 = round(result1, 2)
R2 = round(result2, 2)
print(f" The cicumference of the circle is {R1}cm.")
print(f" The area of the circle is {R2}cm.")