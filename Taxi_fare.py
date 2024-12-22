def fare(distance):
    base_fare = 50
    distance_fare = 10
    return base_fare + (distance * distance_fare)

trips = [5, 10, 3]
total_fare = 0

for i, distance in enumerate(trips, start=1):
    price = fare(distance)
    print(f"Trip {i}: ${price}")
    total_fare += price

print(f"Total Fare: {total_fare}")