age = int(input("What is your age? "))
day = input(" Is it a weekday show or a weekend one? (weekend/weekday) ")

if age < 12:
    print(" Ticket is $15")

elif 12 <= age <= 59:
   if day == "weekday":
       print("The ticket is $30")
   else:
       print("The ticket is $40")

else:
    print(" The ticket is $15")