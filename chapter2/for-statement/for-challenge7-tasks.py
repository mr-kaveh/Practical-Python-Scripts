# Simulated list of tasks with their status (completed or not)
# purpose is to learn how  BREAK & CONTINUE in for loop works
tasks = [
    {"id": 1, "description": "Task 1", "completed": False},
    {"id": 2, "description": "Task 2", "completed": True},
    {"id": 3, "description": "Task 3", "completed": False},
    {"id": 4, "description": "Task 4", "completed": True},
    {"id": 5, "description": "Task 5", "completed": False},
]

# Task we want to find and break the loop when encountered
target_task_id = 3

# Process the list of tasks
for task in tasks:
    # Skip completed tasks using 'continue'
    if task["completed"]:
        print(f"Skipping completed task: {task['description']}")
        continue

    # Check if the task matches the target and break the loop if found
    if task["id"] == target_task_id:
        print(f"Found the target task: {task['description']}")
        break

    # Perform other processing on the current task
    print(f"Processing task: {task['description']}")

# Continue with additional tasks if needed
print("Continuing with other tasks...")
