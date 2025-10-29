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


