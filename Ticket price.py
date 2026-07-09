age = int(input("Please enter your age - "))
student = input("Are you a student?").lower().strip()


if age <= 12:
    print("Your ticket is free!")
elif 12 < age <= 17:
    print("Your ticket is $10.")
elif 18 <= age <= 59 and student == "yes":
    print("Your ticket is $15.")
elif 18 <= age <= 59 and student == "no":
    print("Your ticket is $25.")
elif age >= 60:
    print("Your ticket is $8.")