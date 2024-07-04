from os import system
from art import logo, vs

import random
from game_data import data

def get_data():
    """Imports Data from the Game Data directory"""
    return random.choice(data)

def format_data(entry):
    """Formats the data pulled from the Game Data directory"""
    name = entry["name"]
    description = entry["description"]
    country = entry["country"]
    follower_count = entry["follower_count"]
    return (f"{name} is a {description} from {country}.")

def data_compare(guess, entry_a, entry_b):
    """Compares the two accounts, and returns which is higher"""
    if entry_a > entry_b:
        return guess == "A"
    else:
        return guess == "B"


def clear():
    _ = system('cls')

def play_game():
    """Starts the Higher vs Lower Game"""

    player_score = 0
    game_over = False
    print(logo)
    print("Welcome to HIGHER OR LOWER!!!")
    print("-----------------------------")
    print("Can you guess who has more followers on Instagram?")
    input("Press Enter to Begin...\n")
    entry_a = get_data()

    while not game_over:
        print(f"Current Score: {player_score}\n")
        #entry_a = get_data()
        #print(entry_a)
        entry_b = get_data()
        #print(entry_b)
        #input("Press Enter to Begin...")

        print(f"Compare A: {format_data(entry_a)}.")
        print(vs)
        print(f"Compare B: {format_data(entry_b)}.\n")
        player_guess = input("Which has more followers? Enter 'A' or 'B'. \n")
        player_guess = player_guess.upper()
        print(player_guess)

        follower_count_a = int(entry_a["follower_count"])
        follower_count_b = int(entry_b["follower_count"])
        print("-----------------------------------------")
        print(f"A has {follower_count_a} follower.")
        print(f"B has {follower_count_b} follower.")
        is_correct = data_compare(player_guess, follower_count_a, follower_count_b)

        if is_correct:
            player_score += 1
            print(f"You're right! Current score: {player_score}.")
            if follower_count_b > follower_count_a:
                entry_a = entry_b
            input("Press Enter to Continue...\n")
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {player_score}")
            input("Press Enter to Start a New Game...\n")
            play_game()

        # if follower_count_b > follower_count_a:
        #     entry_a = entry_b

play_game()

#input("Press Enter to Continue...")
