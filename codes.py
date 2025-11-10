#day 2: Data Types and Type Conversion Exercises

#Exercise 1
name = str('Darth Vader')
print(name)

age = int(19)
print(age)

#Exercise 2

i_cannot_do_it=False
print(i_cannot_do_it)

the_answer= float(42.01)

print(the_answer)

#Exercise 3
height = str('1.09')

print(height)

height = float(height)

height = height + 0.66

print(height)



# these are test with chatgpt

# test 1
F = float(2.88)
print(F)
print(type(F))
N = int(5)

print(N)
print(type(N))

#test2 
name = str("hS cooding")

print('Hello, my name is ' + name)

# test 3 

is_sunny = True

if is_sunny:
    print("It's a sunny day!")
else:
 print("It's cloudy.")

# test 4

a = int(20 )       # int
print(type(a))

b = float(4.5)       # float
print(type(b))

c = str("Python")  # str
print(type(c))

d = bool(False)     # bool
print(type(d))

# test 5

num_str = "50"

num_str = int(num_str) * 2

print(num_str)
print(type(num_str))





# day 2: operators and Mathematical Operations Exercises

# Exercise 1

ahsoka_height = 1.70
yoda_height = 0.66
r2d2_height = 1.09
c3p0_height = 1.75

average_height = (ahsoka_height + yoda_height + r2d2_height + c3p0_height) / 4

print("The average height is:", average_height, "meters")




# day 3 : functions exercises



#Exercise 1
name = input("What is your name ")
age = input("What is your age ")

print("your name is "+name+ " your age is " +age)

#Exercise 2

def age_of_rey():
  ray_age = input("How old is Rey? ")
  print(" Rey's age is " + ray_age)



age_of_rey()

#Exercise 2
whoWasOnTitanice = input("who was on the titanic ")
current_year = int(input("what year is it currently "))


def TitanicF(whoWasOnTitanic, current_year):

  brokeYear=1912
  ago = current_year - brokeYear

  print(whoWasOnTitanic + " was on the Titanic, which sunk " + str(ago)+" years ago")

TitanicF(whoWasOnTitanice,current_year)



#Exercise 3

def my_age(age='19'):
  print(" my age is " + age)


my_age("39")
my_age()



# these are test with chatgpt



# Test 1

def say_hello1():
  print("Hello from my function!")

say_hello1()


#Test 2 

def say_hello2(name):
  print("Hello , " + str(name) )

say_hello2("Hossin")



#Test 3

def add(a,b):
 sum = a + b
 print(sum)

add(10,5)


#Test 4


x=10

def multiply_by_two(x):
 mult = x* 2
 print(mult)

multiply_by_two(x)

#Test 5 


def square(number):
 mult = number ** 2
 print(mult)

square(10)



# day 4: Lists and Lists types

# Exercise 1

height = [ 1.7, 0.66 ,1.09]

print(type(height))


print(sum(height))


#day 4: if else 




#Exercise 1
qa= input("is Rose holding a lightsaber ")

if qa == "Yes":
  print("Yes she is ")
else:
  print("No she is not")


#Exercise 2
qa1 = input(' Is the character holding a lightsaber? ')


if qa1 == "Yes":
  print("the character is holding a lightsaber")
  qa2 = input('Is the lightsaber green ')
  if qa2 == "Yes":
    print('The character is Yoda. ')
  else:
    print('the character is not Yoda')

else:
  print("the character is not holding a lightsaber")


#Exercise 3

qa3 = input('Select Team from 1 to 3 ')

if qa3 == "1":
  print('You picked team 1, which has 1 character, which is Yoda ')
elif qa3 =="2":
  print('You picked team 2, which has 2 characters, Jack & Rose ')
elif qa3 == "3":
  print('"You picked team 3, which has 2 characters, Vader & Leah ')
elif qa3 != '1' or qa3 != '2' or qa3 !='3':
  print('please select 1 or 2 or 3 ')

if qa3 == '1' or qa3 =='3':
  print('The number of people on the team you selected is odd.')
else:
  print("The number of people on the team you selected is even.")




# practice with chatgpt

#test 1
qa11 = int(input('select number from 1 to 30 '))

if qa11 > 10:
  print("big Number")
else:
  print("small Number")

#test 2
qa12 = int(input('what is your age '))

if qa12 < 13:
  print("Child")
elif qa12 > 13 and qa12 < 19:
  print("Teenager")
else:
  print('Adult')

#test 3
qa13 = int(input('select number from1 to 20 '))

if qa13 > 5 and qa13 < 15:
  print("Number is in range")
else:
  print('Out of range')



#test 4
qa14 = input('selec a color ')

if qa14 == "red" or qa14 == "blue":
  print("Primary color")
else:
  print('no Primary ')



#test 5
qa15 = input('enter the pass ')

if qa15 != '1234':
  print("Wrong password!")
else:
  print('Access granted!')



# day 5: match and formating exercises

#Exercise 1
selectTeam= int(input('selct 1 or 2 or 3 '))


match selectTeam:
  case 1:
    print('You selected Team 1')
  case 2:
    print('You selected Team 2')
  case 3:
    print('You selected Team 3')
  case _:
    print('and')

#Exercise 2

selectTakit1st= input(' How many 1st tickets do you want to purchase? ')
selectTakit2nd= input(' How many  2nd  tickets do you want to purchase? ')
selectTakit3rd= input(' How many 3rd  tickets do you want to purchase? ')

totals= int(selectTakit1st)*870 + int(selectTakit2nd)* 100.42 +int(selectTakit3rd)*7

print(f"the totals are {totals:.2f}") 




# these are test with chatgpt

#Test 1

name = "Hossin"
age = 20


print(f"My name is {name} I'M {age} Years old")

#Test 2

price = 45.6789
 
print(f'{price:.2f} SR')


#Test 3 

PickNum = int(input('select number from 1 to 3'))

match PickNum:
  case 1:
    print(f"you select class {PickNum}")
  case 2:
    print(f"you select class {PickNum}")
  case 3:
    print(f"you select class {PickNum}")
  case _:
    print('Invalid choice')


#Test 4

age = int(input('what is your age '))

match age:
  case _ if age < 13:
    print("Child")
  case _ if age < 20:
    print('Teenager')
  case _:
    print('adult')


#Test 5
ticket = int(input('Select a ticket class (1, 2, or 3).'))


match ticket:
  case 1:
    price = 870
    print(f"You selected class {ticket}, the price is {price:.2f} pounds.")
  case 2:
    price = 100.42
    print(f"You selected class {ticket}, the price is {price:.2f} pounds.")
  case 3:
    price = 7
    print(f"You selected class {ticket}, the price is {price:.2f} pounds.")



# day 6 : lopps exercises

#Exercise 1
listss = ["Leia I am your father.","Luka I am your father."]

for x in listss:
  print(x)





# tests with chatgpt


# Test 1
 
for a in range(1,6):
  print(a)


# Test 2

for a in range(2,11,2):
  print(a)

# Test 3


names = ["Hossin", "Yoda", "Ahsoka"]

for n in names:
  print(f"hello , {n}")


# Test 4

for d in range(1,10):
  if d == 5:
    continue;
  if d == 8:
    break
  print(d)


for d in range(1,10):

  match d:
    case 5:
      continue
    case 8:
      break
    case _:
      print(d)

# Test 5 

nums = [1, 2, 4, 5]

for dd in nums:
  if dd == 3:
    print("Found 3!")
    break
else:
  print("3 not found!")

# day 7: dictionaries exercises and tuples


#Exercise 1

# Original tuple
characters = ("Han Solo", "Yoda", "R2d2", "C3P0")

forgotten_character = "Darth Vader"

characters = list(characters)

characters.append(forgotten_character)

characters = tuple(characters)

print(type(characters))



#Exercise 2

allegiances = {"Luke Skywalker":"Rebel Alliance","Darth Vader":" Galactic Empire", " Obi-Wan Kenobi":" Jedi Order" }

print(allegiances['Darth Vader'])

allegiances['Darth Vader'] = 'Sith Order'

allegiances['Leia'] = 'Rebel Alliance'

print(allegiances)


# tests with chatgpt

# Test 1 
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020,
}

print(car.get('brand'))

# Test 2

car['color'] = "Blue"
car['year'] = 2025

print(car)


# Test 3

for key, value in car.items():
  print(f" { key}: {value}")

# Test 4 

print(car.values())
print(car.keys())
print(car.items())


# Test 5 

car.pop('color')
print(car)

car.clear()

print(car)



# Test with chatgpt level up


# Test 1

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020,
    "price": 24000
}

askUser = input("do you want to udate the car price ?: yes/no ")
if askUser.lower() == "yes":
  new_price = input("Enter the new price: ")
  car['price'] = int(new_price)

for key , value in car.items():
  print(f"{key}:{value}")

# Test 2

grades = {"Ali": 90, "Sara": 80, "Yoda": 100}

nn = 0

for d in grades.values():
  nn += d

total = sum(grades.values())
average = total / len(grades)
print(f"The average is {average:.2f}")


# Test 3

users = {"hossin": "1234", "yoda": "9999", "luke": "0000"}
askUser1 = input('search the user ')

if askUser1 in users:
  print('User found!')
else:
  print('User not found!')


# Test 4

allSen = {}

sentes = input('enter stences')

words = sentes.lower().split()


for n in words:
  if n in allSen:
    allSen[n] += 1
  else:
    allSen[n] = 1
  
print(allSen)




# Test 5

car1 = {"brand": "Toyota", "year": 2020}
car2 = {"color": "Red", "price": 85000}

car_full = {}

for key, value in car1.items():
    car_full.update({key: value})

for key, value in car2.items():   
    car_full.update({key: value})

print(car_full)



# day 8: set exercises

#Exercise 1

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set3 = set1.union(set2)

print(set3)



#Exercise 2

storm_troopers_group1= ["trooper_1","trooper_2","trooper_3","trooper_4"]
storm_troopers_group2= ["trooper_5","trooper_2","trooper_34","trooper_46"]


storm_set1 = set(storm_troopers_group1)

InAllClasses = storm_set1.intersection(storm_troopers_group2)

print(InAllClasses)


# test with chatgpt

# test 1
fruits = {"apple", "banana", "orange"}
more_fruits = {"banana", "kiwi", "mango"}


unique = fruits.union(more_fruits)

print(unique)

# test 2 

comon = fruits.intersection(more_fruits)
print(comon)

# test 3 

defrent = fruits.difference(more_fruits)
print(defrent)

# test 4 

fruits.add("grape")

fruits.remove('orange')

print(fruits)

# test 5 

tropical = {"mango", "kiwi", "pineapple"}

Inboth = tropical.intersection(more_fruits)

print(Inboth)