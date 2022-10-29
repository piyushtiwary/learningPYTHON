#importing random 
import random

#taking user input
user_action = input("Enter a choice (rock, paper, scissors): ")

# deciding computer's choice
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)


print("Computer choses:",computer_action)

#checking tie conditions
if user_action == computer_action:
	print("Tie")

#checking computer winning condition
elif user_action == "paper" and computer_action == "scissors":
	print("Computer wins")

elif user_action == "scissors" and computer_action == "rock":
	print("computer wins")

elif user_action == "rock" and computer_action == "paper":
	print("computer wins")

#checking user win condition
else: print("user wins")