A = float(input(" Toal amount to be invested - "))
B = float(input(" Percentage allocated to stocks - "))
C = float(input(" Percentage alocated to bonds - "))
D = float(input(" Annual retrn rate for stocks(%) - ")) / 100
E = float(input(" Annual return rate for bonds(%) - ")) / 100

result1 = round((A * (B / 100)), 2)
result2 = round((A * (C / 100)), 2 )
result3 = round(result1 * ( 1 + D), 2 )
result4 = round(result2 * ( 1 + E), 2 )
result5 = round((result3 + result4), 2)
result6 = round((((result5 - A) / A) * 100), 2)

print(f" Stock amount - ${result1}")
print(f" Bond amount - ${result2} ")
print(f" Stock Value - ${result3}")
print(f" Bond value - ${result4}")
print(f" Total value - ${result5}")
print(f" Blended return - {result6}%")
