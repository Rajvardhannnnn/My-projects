print("Please enter your marks for the following subjects")
math = int(input("mathematics- "))
phy = int(input("Physics- "))
chem = int(input("Chemistry- "))
opt = int(input("Optional subject- "))
eng = int(input("English- "))

result = math + phy + chem + opt + eng
print(f"Your total marks is {result}.")

result1 = result / 5
print(f"Your total percentage is {result1}%")

if result1 >= 90:
    print("Congratulations! You are well done! Your overall grade is A.")
elif result1 >= 75:
    print(f"You are well done! Your overall grade is B.")
elif result1 >= 60:
    print(f"Need to work a little harder! Your overall grade is C.")
elif result1 >= 40:
    print(f"Need to work harder! Your overall grade is D.")
else:
    print(f"WE NEED TO TALK ASAP! Your overall grade is F.")

