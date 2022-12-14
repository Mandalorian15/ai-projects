import time
import random

# Set the number of days the game will take
num_days = 20

# Set the initial day to 1
day = 1

# Define a list of challenges and minigames
challenges = [
  "Complete a puzzle",
  "Solve a math problem",
  "Run a mile",
  "Play a game of chess",
  "Memorize a poem",
  "Write a short story",
  "Learn a new skill",
  "Cook a meal",
  "Draw a picture",
  "Perform a magic trick"
]

# Print a message to start the game
print("Welcome to the game! You have 20 days to complete all the challenges.")

# Continuously loop until the day reaches the number of days in the game
while day <= num_days:
  # Print a message indicating the current day
  print(f"Day {day}:")

  # Select a random challenge or minigame from the list
  challenge = random.choice(challenges)

  # Print the selected challenge or minigame
  print(f"Today's challenge is: {challenge}")

  # Prompt the user to complete the challenge
  print("Complete the challenge and press enter to continue.")
  input()

  # Increment the day
  day += 1

  # Wait one day before moving on to the next challenge
  time.sleep(86400)

# Print a message indicating that the game has been completed
print("Congratulations! You have completed the game!")
