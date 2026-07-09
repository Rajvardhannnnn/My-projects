N = input(" What is your name sir/maam?: ")

B = float(input("What was your total bill?"))
S = int(input(" How many people are spitting the bill?: "))

R1 = B * 1.05
R2 = R1 / S
print(f"Hello {N}! Your total bill is ${B} and with including 5% GST it is ${R1}  and each person pays ${R2}.")
