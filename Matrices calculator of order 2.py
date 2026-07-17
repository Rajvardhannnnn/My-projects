print("Welcome to the matrices calculator of square matrix of order 2")

print("Please enter the numbers of the first matrix below")
num1 = int(input("Enter the number of A11 - "))
num2 = int(input("Enter the number of A12 - "))
num3 = int(input("Enter the number of A21 - "))
num4 = int(input("Enter the number of A22 - "))

print("Please enter the numbers of the second matrix below")
num5 = int(input("Enter the number of A11 - "))
num6 = int(input("Enter the number of A12 - "))
num7 = int(input("Enter the number of A21 - "))
num8 = int(input("Enter the number of A22 - "))

op = input("Please enter your desired operator (+,-,*)  ")
while op not in ("+","-","*"):
    print(f"{op} is not a valid operator.")
    op = input("Please enter your desired operator (+,-,*)  ")

if op == "+":
    result1 = num1 + num5 , num2 + num6 , num3 + num7 , num4 + num8
    print(result1)
elif op == "-":
    result2 = num1 - num5 , num2 - num6 , num3 - num7 , num4 - num8
    print(result2)
elif op == "*":
    result3 = (num1 * num5) + (num2 * num7),(num1 * num6) + (num2 * num8),(num3 * num5) + (num4 * num7),(num3 * num6) + (num4 * num8)
    print(result3)


