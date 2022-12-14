# Import the time module to track time
import time
import random

# Initialize the game variables
energy = 100
time_passed = 0

# Generate a random number between 1 and 10
random_num = random.randint(1, 10)

# Game loop
while energy > 0 and time_passed < 8:
  # Prompt the player to guess a number
  print(f"You have {energy} energy left. Guess a number between 1 and 10, if you get it right you sleep, this game is so fun.")
  user_input = input()

  # Check if the player's guess is correct
  if int(user_input) == random_num:
    # If it is, sleep for 1 hour
    time.sleep(3600)
    time_passed += 1

    # Regain some energy
    energy += 10
  else:
    # If it's not, lose some energy
    energy -= 10

    # Generate a random number between 1 and 100
    random_num_2 = random.randint(1, 100)

    # Check if the random number is less than or equal to 10
    if random_num_2 <= 10:
      # If it is, insult the player's intelligence
      print("You have the intelligence of a brick. Why did i make this. Try again.")

    # Check if the player has run out of energy
    if energy == 0:
      print("You have run out of energy.try again stupid.")
      break

# Check if the player has slept for 8 hours
if time_passed == 8:
  print("You have slept for 8 hours. Imagine being so bored you tried to win this!")
else:
  print("Game over try this again, How are you so bad at this game about sleeping bruh.")