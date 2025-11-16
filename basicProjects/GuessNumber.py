import random



def guss(x):
  random_number = random.randint(1,x)
  geuss = 0
  while geuss != random_number:
    geuss = int(input(f"Guess a number between 1 and {x} "))
    if geuss < random_number:
      print("Sorry, guess again. Too low")
    elif geuss > random_number:
      print('Sorry, guess again. Too high.')
  
  print(f'Yay, conrats. You have guessed the number {random_number} correctly!!')
 

guss(10)




