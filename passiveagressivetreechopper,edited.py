# Import the random module to generate random numbers
import random

# Initialize the game variables
num_trees = 10
num_cuts = 0

# Game loop
while num_trees > 0:
  # Check if the player has made enough cuts
  if num_cuts == 9:
    print("You cut down all but 1 tree. Because your lazy you took a break. When your asleep the trees grow back, get to work again.")
    break

  # Prompt the player to make a cut
  print(f"There are {num_trees} trees left. Get to work lazy type a random number to chop, why? I was to lazy to develop a good game so just shut up and play.")
  user_input = input()

  # Generate a random number between 1 and 100
  random_num = random.randint(1, 100)

  # Check if the random number is less than or equal to 50
  if random_num <= 50:
    # If it is, cut down a tree
    num_trees -= 1
    print("Finnally You have successfully cut down a tree!")
    num_cuts += 1
  else:
    # If it's not, let the player know they missed
    print("Stupid head. You missed! Try again.")

# Check if the player has cut down all the trees
if num_trees == 0:
  print("You have cut down all the trees. You did your job, go to bed come back later!")
else:
  print("Game over.")
