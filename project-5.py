task_names = []
task_durations = []

num_tasks = int(input("Enter the number of tasks you want to track:"))

for i in range(num_tasks):
    task_names.append(input(f"Enter the name of task {i + 1}:"))
    task_durations.append(float(input(f"Enter the duration of task {task_names[i]} in hours:")))

total_time_per_task = {name: duration for name, duration in zip(task_names, task_durations)}
total_time_spent = sum(task_durations)

threshold = float(input("Enter the threshold duration in hours to identify areas for improvement:"))
areas_for_improvement = [name for name, duration in total_time_per_task.items() if duration > threshold]

print("\nTime Management summary:")
for name,duration in total_time_per_task.items():
    print(f"{name}:{duration} hours")

print("\nTotal Time spent: {0} hours".format(total_time_spent))

if areas_for_improvement:
    print("\nAreas for Improvement (tasks taking more than {0} hours):".format(threshold))
    for task in areas_for_improvement:
        print(task)
else:
    print("\nNo areas for improvement identified.")