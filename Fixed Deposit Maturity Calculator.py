principal = float(input(" What is the principal amount invested? "))
rate = float(input(" What is the Annual Interest rate %? "))
time= float(input(" Number of years?"))
frequency = float(input(" What is the Compounding frequency per year? "))

rate1 = rate / 100
result1 = float(principal * ((1 + (rate1 / frequency)) ** (time * frequency)))
result2 = float(result1 - principal)
result3 = float((((result1 / principal) ** (1 / time)) - 1) * 100)

print(f" The Maturity amount is ${result1}")
print(f" Total Interest earned is ${result2}")
print(f" Effective annual yield is {result3}%")