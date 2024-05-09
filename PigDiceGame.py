import random

def roll_dice():
    """Simulate rolling a six-sided dice."""
    return random.randint(1, 6)

def player_turn(player_name, player_score):
    """Simulate a player's turn."""
    print(f"It's {player_name}'s turn.")
    turn_score = 0
    while True:
        roll = roll_dice()
        print(f"{player_name} rolled: {roll}")
        if roll == 1:
            print("Oops! You rolled a 1. Turn over.")
            return 0
        else:
            turn_score += roll
            print(f"Your current score this turn: {turn_score}")
            choice = input("Roll again? (yes/no): ").lower()
            if choice != 'yes':
                return turn_score

def pig_game():
    """Main function to play the Pig dice game."""
    print("Welcome to Pig Dice Game!")
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")
    player1_score = 0
    player2_score = 0

    while True:
        player1_score += player_turn(player1_name, player1_score)
        print(f"{player1_name}'s total score: {player1_score}\n")

        if player1_score >= 100:
            print(f"Congratulations! {player1_name} wins!")
            break

        player2_score += player_turn(player2_name, player2_score)
        print(f"{player2_name}'s total score: {player2_score}\n")

        if player2_score >= 100:
            print(f"Congratulations! {player2_name} wins!")
            break

pig_game()