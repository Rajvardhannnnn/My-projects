unit = input("Type in your current unit- ( Celsius , Kelvin, Fahrenheit)").lower().strip()
num = float(input("Type in your temerature- "))

if unit == "celsius":
    result1 = round(num + 273.15, 3)
    result2 = round((num * 1.8) + 32, 3)
    print(f"Your temperature in kelvin scale is {result1}K."
          f"Your temperatre in Fahrenheit scale is {result2}F")
elif unit == "kelvin":
    result1 = round(num - 273.15, 3)
    result2 = round(((num - 273.15) * 1.8) + 32, 3)
    print (f"Your temperature in celsius scale is {result1}."
           f"Your temperature in fahrenheit scale is {result2}F")
elif unit == "fahrenheit":
    result1 = round((num - 32) * 0.55556, 3)
    result2 = round(((num - 32) * 0.55556) + 273.15, 3)
    print(f"Your temperature in celsius scale is {result1}."
          f"Your temperature in Kelvin scale is {result2}K")
else:
    print("you have typed a wrong unit.")