# random module to generate random numbers
import random

# generate a random secret_number
secret_number = random.randint(1, 20)
# how many chances
chances_left = 5

print("Hey there! Guess a number b/w 1 to 20 which I am thinking of: ")

# ask the player to guess 5 times
for i in range(1, 6):
  #converts input "string" to int
  guess = int(input("Take a guess: "))
  
  # checking
  if guess < secret_number:
    print("Guess is too low!")
  elif guess > secret_number:
    print("Guess is too high!")
  else:
    # user guessed it correctly, so jump out of the loop
    break

  # before taking next iteration
  # decrease 1 from chances_left
  chances_left = chances_left - 1
  print("Chances Left: " + str(chances_left))


# check if the guess matches the secret_number
if guess == secret_number:
  print("You guessed it right!")
else:
  print("You lose!")
  print("The number I thought was " + str(secret_number))

#Fin
#Happy Hactober🎉🎉
