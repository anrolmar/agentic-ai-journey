name = "Angel"
age = 47
weekly_distance = 20.5
is_running = True

print(name)
print(age)
print(weekly_distance)
print(is_running)

print(type(name))
print(type(age))
print(type(weekly_distance))
print(type(is_running))

print(int(3.9))
print(float("12.5"))

distance_km = 5.5
duration_minutes = 38

pace = duration_minutes / distance_km

print(
    f"{name} runs {distance_km} kilometers in {duration_minutes} minutes. The pace is {pace:.2f} minutes per kilometer."
)
print(f"Distance: {distance_km:.2f} km")
print(f"Duration: {duration_minutes} minutes")

message = "  Learning Python is fun!  "
print(message.strip())
print(message.lower())
print(message.upper())
print(len(message))

language = "Python"
print("I'm learning", f"{language}", "and I know the variables")
