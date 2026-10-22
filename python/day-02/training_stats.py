activity_name = "Running"
distance_km = 5.5
duration_minutes = 38
average_heart_rate = 148

pace_minutes = duration_minutes / distance_km
hours = int(duration_minutes // 60)
remaining_minutes = duration_minutes % 60

calories = 323
weather = "It is a sunny day with a temperature of 22°C."

distance_meters = distance_km * 1000

print("=== Training Stats ===")
print(f"Activity: {activity_name}")
print(f"Distance: {distance_km:.2f} km ({distance_meters:.0f} meters)")
print(f"Duration: {hours} h and {remaining_minutes:.0f} min")
print(f"Average pace: {pace_minutes:.2f} min/km")
print(f"Average heart rate: {average_heart_rate} bpm")
print(f"Calories burned: {calories} kcal")
print(weather)
