#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      akppa
#
# Created:     10-09-2024
# Copyright:   (c) akppa 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
options = ["rock","paper","scissor"]

print("Game starts...!!")
print("You have 3 choices:rock,paper and scissor")

user_score = 0
computer_score = 0
rounds = 3

running=True
while running:
    for _ in range(rounds):
        computer = random.choice(options)
        player =("")

        while player not in options:
            player = input("Enter a choice:")

            print(f"Player:{player}")
            print(f"Computer:{computer}")

            if player == computer:
                print("Its a tie !!")

            elif player == "rock" and computer == "scissor":
                print("You win !!")
                user_score += 1
            elif player == "paper" and computer == "rock":
                print("You win !!")
                user_score += 1
            elif player == "scissor" and computer == "paper":
                print("You win !!")
                user_score += 1
            else:
                print("You lose")
                computer_score += 1

    print("\nGame over!")
    print("Your score:", user_score)
    print("Computer's score:", computer_score)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "no":
        break

