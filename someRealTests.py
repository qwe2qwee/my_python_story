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
