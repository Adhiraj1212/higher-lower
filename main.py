from game_data import data
from art import *
import random
import os
def display_data(data):
    score=0
    checker=0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        import_data=random.choices(data,k=2)
        if checker!=0:
            print("Current Score: ",score)
        checker=1
        print(f"Compare A: {import_data[0]['name']}, a {import_data[0]['description']}, from {import_data[0]['country']}")
        print(vs)
        print(f"Against B: {import_data[1]['name']}, a {import_data[1]['description']}, from {import_data[1]['country']}")
        guess=input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess=="a":
            if import_data[0]['follower_count']>import_data[1]['follower_count']:
                print("You are right")
                score+=1
                continue
            else:
                print("You are wrong")
                break
        elif guess=="b":
            if import_data[0]['follower_count']<import_data[1]['follower_count']:
                print("You are right")
                score+=1
                continue
            else:
                print("You are wrong")
                break
        else:
            print("Wrong input")
            break
    print(f"Your score is {score}") 
display_data(data)

