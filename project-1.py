daily_steps = int(input("Enter daily steps:"))
distance_walked = float(input("Enter distance walked (in kilometers):"))
calories_burned = int(input("Enter calories burned:"))

average_steps_per_week = (7 * daily_steps) / 7

total_distance_in_a_month = 30 * distance_walked

print(f"Average steps per week: {average_steps_per_week}")
print(f"Total distance covered in a month: {total_distance_in_a_month}Kilometers")