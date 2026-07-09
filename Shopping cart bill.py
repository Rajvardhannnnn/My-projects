# Exercise 2 Shopping cart program

print("Welcome to Raj General Store!")
n = input("What is your name?: ")
b = input("What would you like to buy?")
p = input("What is the price? ")
q = input("what is the quantity you need?")

p = float(p)
q = float(q)

r = p * q
print(f" Hello {n}! Your total bill for {q} {b}'s is ${r}")