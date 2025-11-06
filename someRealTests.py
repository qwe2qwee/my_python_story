# Shopping List Management TEST

# Step 1: Create the initial shopping list
shopping_list=["Milk","Eggs","Bread","Bananas"]
# Step 2: Add "Apples" to the list

shopping_list.append("Apples")
# Step 3: Remove "Bread" from the list

shopping_list.remove("Bread")

# Step 4: Create the show_list function
def show_list(shopList):
  print("Your shopping list:")
  for index, fruit in enumerate(shopList):
    
    print(index, fruit)

# Step 5: Create the total_items function
def total_items(shopList):
  print("Total items")
  print(len(shopList))


# Step 6: Display the shopping list and the total number of items
show_list(shopping_list)
total_items(shopping_list)












#---------------------------------------------------------------------------------------------------------

# Time Tracking Application TEST

# Step 1: Initial list of tasks
tasks = ["Planning", "Design", "Coding", "Testing"]

# Step 2: Initial list of time spent on tasks (list)
time_spent = [0, 0, 0, 0]
# Step 3: Log time function
def log_time(task_name, hours):
    if task_name in tasks:
        index = tasks.index(task_name)  # find where the task is
        time_spent[index] += hours      # add hours to that position
    else:
        print("Task not found.")


# Step 4: User input and loop
while True:
    task = input("Enter a task name (or type 'exit' to quit): ")
    if task.lower() == "exit":
        break

    time = float(input("Enter hours spent on this task: "))
    log_time(task, time)


# Step 5: Summary of time spent


print("\n--- Time Summary ---")
for i in range(len(tasks)):
    print(f"{tasks[i]}: {time_spent[i]} hours")
