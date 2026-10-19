# Travel Fare Calculator
FARE_RATE = 14

while True:
    name = input("Enter passenger name: ")
    
    if name.strip() != "":
        break
    else:
        print("Invalid name, cannot be empty.")


while True:
    try:    
        distance = float(input("Enter distance (km): "))
    
        if distance > 0: 
            break
        else:
            print("Inavlid input, the distance must be greater than zero")
        
    except ValueError:
            print("Invalid input. Please enter a number.")


while True:
    try:
        passengers = int(input("Enter number of passengers: "))
        if passengers > 0:
            break
        else:    
            print("Invalid number of passengers. Please enter a positive whole number.")
    except ValueError:
            print("Invalid input. Please enter a number.")


total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))


# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number# Travel Fare Calculator
