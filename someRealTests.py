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

 


# ---------------------------------------------------------------------------------------------------------


# Restaurant Menu Management


# Step 1: Initial menu

menu = {
    "Burger":("Main",10.5),
    "Soup":('Appetizer',5.0),
    "Ice Cream":("basken",8.0),
    "Salad":("oino",4.0)
}

# Step 2: Add dishes
menu.update({"Stake":("pig",40), 'Soda':('Cola',30)})
print(menu)
# Step 3: Remove dish

menu.pop('Stake')
print(menu)

# Step 4: Display menu function
def display_menu(menu):
    print("📋 Menu:\n")
    for item, (category, price) in menu.items():
        print(f"{item:<12} | Category: {category:<10} | Price: ${price:.2f}")


# Step 5: Count dish types function
def count_dish_types(menu):
    dish_counts = {}  # empty dictionary to store results

    for dish, (dish_type, price) in menu.items():
        if dish_type in dish_counts:
            dish_counts[dish_type] += 1
        else:
            dish_counts[dish_type] = 1

    return dish_counts



# Step 6: Update price function

def update_price(menu, dish_name, new_price):
    if dish_name in menu:
        dish_type, _ = menu[dish_name]  # unpack the old tuple
        menu[dish_name] = (dish_type, new_price)  # replace with updated tuple
        print(f"✅ Updated {dish_name} price to ${new_price:.2f}")
    else:
        print(f"❌ Dish '{dish_name}' not found in the menu.")



# Step 7: Use all functions to manage menu


# --- MAIN PROGRAM ---
print("🔹 Original Menu:")
display_menu(menu)

# Update some prices
update_price(menu, "Burger", 12.0)
update_price(menu, "Soup", 6.5)
update_price(menu, "Soda", 25.0)

# Display updated menu
print("\n🔹 Updated Menu:")
display_menu(menu)

# Count dish types
dish_summary = count_dish_types(menu)
print("🍽️ Dish Type Summary:")
for dish_type, count in dish_summary.items():
    print(f"- {dish_type}: {count} item(s)")

