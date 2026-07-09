w1 = (input("Please enter the unit you are converting from- (Kg, Lbs) ")).strip().lower()
w2 = (input("Please enter the unit you are converting to - (Kg,Lbs)"))
weight = float(input("Please enter the weight- "))

if w1 == "kg":
    r1 = round(weight * 2.20462, 3)
    print(f"Your weight in Lbs is {r1}.")
elif w1 == "lbs":
    r2 = round(weight / 2.20462, 3)
    print(f" Your weight in Kg is {r2}.")
else:
    print("Your enetered unit is not valid.")