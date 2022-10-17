import random
from art import logo

random_num=random.randint(1,100)
tries=0
is_choice_difficult=False
def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Psst, the correct answer is {random_num}")
    
    
def check_choice():
    choice=input("Choose a difficulty. Type 'easy' or 'hard': ").lower() 
    if choice=="easy":
        is_choice_difficult=False
    else:
        is_choice_difficult=True
    return is_choice_difficult
    

play_game()


if check_choice == is_choice_difficult:
    tries=10
    print("You have 10 attempts remaining to guess the number")
    while tries!=0:
        guess=int(input("Make a guess: "))
        if guess > random_num:
            print("Too high.")
            print("Guess again.")
            tries-=1
            print(f"You have {tries} attempts remaining to guess the number")
        elif guess < random_num:
            print("Too low.")
            print("Guess again.")
            tries-=1
            print(f"You have {tries} attempts remaining to guess the number")
        else:
            print(f"You got it! The answer was {random_num}")
            break
else:
    tries=5
    print("You have 5 attempts remaining to guess the number")
    while tries!=0:
        guess=int(input("Make a guess: "))
        if guess > random_num:
            print("Too high.")
            print("Guess again.")
            tries-=1
            print(f"You have {tries} attempts remaining to guess the number")
        elif guess < random_num:
            print("Too low.")
            print("Guess again.")
            tries-=1
            print(f"You have {tries} attempts remaining to guess the number")
        else:
            print(f"You got it! The answer was {random_num}")
            break
if tries==0:
    print("You've run out of guesses, you lose")




