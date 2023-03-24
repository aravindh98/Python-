# Rock Paper Scissor Game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

# User Choice
user_response = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(user_response)
choice_list = [rock, paper, scissors]
if user_choice == 0:
    print(choice_list[0])
elif user_choice == 1:
    print(choice_list[1])
else:
    print(choice_list[2])

# Computer choice
print("computer chose")
computer_choice = random.choice(choice_list)
print(computer_choice)

# Comparison Rules

if computer_choice == choice_list[0] and user_choice == 1:
    print("You won!")
elif computer_choice == choice_list[1] and user_choice == 2:
    print("You won!")
elif computer_choice == choice_list[2] and user_choice == 0:
    print("You won!")
elif computer_choice == choice_list[0] and user_choice == 0:
    print("Game drawn")
elif computer_choice == choice_list[1] and user_choice == 1:
    print("Game Drawn")
elif computer_choice == choice_list[2] and user_choice == 2:
    print("Game Drawn")
else:
    print("You lose")
