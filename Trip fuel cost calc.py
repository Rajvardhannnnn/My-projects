distance= float(input("Total distance of the trip?: "))
mileage = float(input("Current mileage of the vehicle? (Km/L) "))
price = float(input("Current fuel price per litre?: "))

result1 = float(distance / mileage)
result2 = float(result1 * price)
result3 = float(result2 / distance)

print(f" The total litres of fuel needed is {result1}L.")
print(f"Total fuel cost is ${result2}")
print(f" Cost per kilometre is ${result3}")
