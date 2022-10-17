from art import logo
import random
from art import vs
import game_data
import os

def compare(guess):
    global random_val_b
    global random_val_a
    if guess=='A' and game_data.data[random_val_a].get('follower_count') > game_data.data[random_val_b].get('follower_count'):
        random_val_b=random_select()
        return guess
    elif guess=='B' and game_data.data[random_val_b].get('follower_count') > game_data.data[random_val_a].get('follower_count'):
        random_val_a=random_select()
        return guess
    else:
        return False

def random_select():
    return random.randint(1,len(game_data.data)-2)

random_val_a=random_select()
random_val_b=random_select()
counter=0
i=1


guess=''
while i in range(i,len(game_data.data)-2):
    os.system('cls')
    if random_val_a==random_val_b:
        continue
    print(logo)
    if compare(guess)=='A':
        print(f"You're right! Current score: {counter}")
    print(f"Compare A: {game_data.data[random_val_a].get('name')}, a {game_data.data[random_val_a].get('description')}, from {game_data.data[random_val_a].get('country')}.")
    print(vs)
    print(f"Against B: {game_data.data[random_val_b].get('name')}, a {game_data.data[random_val_b].get('description')}, from {game_data.data[random_val_b].get('country')}.")
    guess=input("Who has more followers? Type 'A' or 'B': ").upper()
    if compare(guess)=='A':
        counter+=1
        i+=1
    elif compare(guess)=='B':
        counter+=1 
        print(f"You're right! Current score: {counter}")
        random_val_a=random_val_b
        random_val_b=random_select()
        i+=1
    else:
        print(f"Sorry, that's wrong. Final score: {counter}")
        break



# def compare(person1,person2):
# game_data.data[i].get("name")
# listName.append(dictName)
# print(listName)