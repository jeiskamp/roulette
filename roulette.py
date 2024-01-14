#Roulette
import random
import time

# Function to display the wheel and its corresponding numbers
def display_wheel():
    print('|------|=================================================================================')
    print('|      |  3  |■■6■■|  9  |  12  |■■15■■|  18  |  21  |■■24■■|  27  |  30  |■■33■■|  36  |')
    print('|  00  ==================================================================================')
    print('|------|■■2■■|  5  |■■8■■|■■11■■|  14  |■■17■■|■■20■■|  23  |■■26■■|■■29■■|  32  |■■35■■|')
    print('|   0  ==================================================================================')
    print('|      |  1  |■■4■■|  7  |■■10■■|■■13■■|  16  |  19  |■■22■■|  25  |■■28■■|■■31■■|  34  |')
    print('|______==================================================================================')
    print('       |         1st 12         |          2nd 12           |          3rd 12           |')
    print('       |________________________|___________________________|___________________________|')
    print('       |   1to18   |     EVEN   |      RED    |■■■■BLACK■■■■|      ODD    |    19to36   |')
    print('       |____LOW____|____________|_____________|■■■■■■■■■■■■■|_____________|_____HIGH____|')

# Function to place a bet on a number and validate the input
bet_text = ["1st 12", "2nd 12", "3rd 12", "LOW", "EVEN", "RED", "BLACK", "GREEN", "ODD", "HIGH",
            "0", "00", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", 
            "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", 
            "29", "30", "31", "32", "33", "34", "35", "36"]

def place_bet(balance):
    while True:
        try:
            bet_number = (input("Enter the number you want to bet on (Any Text From Board): "))

            if isinstance(bet_number, str):
                if bet_number not in bet_text:
                    print("Invalid text. Please enter text exactly as board shows.")
                    continue

            #Check bet amount    
            bet_amount = int(input(f"Your balance is ${balance}. Place your bet amount: $"))
            if bet_amount > balance or bet_amount < 0:
                print("Invalid bet amount. Please enter a valid amount.")
                continue
            else:
                return bet_number, bet_amount
        except ValueError:
            print("Invalid input. Please enter a valid bet number and amount.")

# Function to spin the roulette wheel and determine the winning number
def spin_wheel():
    print("Spinning the wheel...")
    time.sleep(1.25)
    return random.randint(0, 37)

# Function to determine if the user wins or loses the bet
def determine_win(bet_number, bet_amount, winning_number):

    red_bet = ["1", "3", "5", "7", "9", "12", "14", "16", "18", "19", "21", "23", "25", "27", "30", "32", "34", "36"]
    black_bet = ["2", "4", "6", "8", "10", "11", "13", "15", "17", "20", "22", "24", "26", "28", "29", "31", "33", "35"]
    green_bet = ["0", "37"]
    first12 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    second12 = ["13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
    third12 = ["25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"]

    if bet_number == "RED":
        if str(winning_number) in red_bet:
            print(f"Congratulations! The winning number is {winning_number} & RED. You win ${(bet_amount*2)-bet_amount}!")
            return (bet_amount*2)-bet_amount
    elif bet_number == "BLACK":
        if str(winning_number) in black_bet:
            print(f"Congratulations! The winning number is {winning_number} & BLACK. You win ${(bet_amount*2)-bet_amount}!")
            return (bet_amount*2)-bet_amount
    elif bet_number == "GREEN":
        if str(winning_number) in green_bet:
            print(f"Congratulations! The winning number is {winning_number} & GREEN. You win ${(bet_amount*18)-bet_amount}!")
            return (bet_amount*2)-bet_amount
    elif bet_number == "EVEN":
        if winning_number % 2 == 0:
            print(f"Congratulations! The winning number is {winning_number} & EVEN. You win ${(bet_amount*2)-bet_amount}!")
            return (bet_amount*2)-bet_amount
    elif bet_number == "ODD":
        if winning_number % 2 != 0:
            print(f"Congratulations! The winning number is {winning_number} & ODD. You win ${(bet_amount*2)-bet_amount}!")
            return (bet_amount*2)-bet_amount
    elif bet_number == "LOW":
        if 1 <= winning_number <= 18:
            print(f"Congratulations! The winning number is {winning_number} & LOW. You win ${(bet_amount*2)-bet_amount}!")
            return (bet_amount*2)-bet_amount
    elif bet_number == "HIGH":
        if 19 <= winning_number <= 36:
            print(f"Congratulations! The winning number is {winning_number} & HIGH. You win ${(bet_amount*2)-bet_amount}!")
            return (bet_amount*2)-bet_amount
    elif bet_number == "1st 12":
        if str(winning_number) in first12:
            print(f"Congratulations! The winning number is {winning_number} & within 1st 12. You win ${(bet_amount*3)-bet_amount}!")
            return (bet_amount*3)-bet_amount
    elif bet_number == "2nd 12":
        if str(winning_number) in second12:
            print(f"Congratulations! The winning number is {winning_number} & within 2nd 12. You win ${(bet_amount*3)-bet_amount}!")
            return (bet_amount*3)-bet_amount
    elif bet_number == "3rd 12":
        if str(winning_number) in third12:
            print(f"Congratulations! The winning number is {winning_number} & within third 12. You win ${(bet_amount*3)-bet_amount}!")
            return (bet_amount*3)-bet_amount
    elif bet_number == winning_number:
        print(f"Congratulations! The winning number is {winning_number}. You win ${(bet_amount*36)-bet_amount}!")
        return (bet_amount*36)-bet_amount

    # You can add more conditions here for other types of bets

    print(f"Sorry! The winning number is {winning_number}. You lose ${bet_amount}.")
    return -bet_amount

# Function to track the history of winning colors
def game_history(history, winning_number):
    if winning_number in ["1", "3", "5", "7", "9", "12", "14", "16", "18", "19", "21", "23", "25", "27", "30", "32", "34", "36"]:
        history.append("RED")
    elif winning_number in ["2", "4", "6", "8", "10", "11", "13", "15", "17", "20", "22", "24", "26", "28", "29", "31", "33", "35"]:
        history.append("BLACK")
    elif winning_number in ["0", "37"]:
        history.append("GREEN")
    return history

# Main function to play the game
def play_roulette():
    balance = 100  # Initial balance
    color_history = []  # Initialize color history list
    while balance > 0:
        print(f"\nBalance: ${balance}")
        display_wheel()
        bet_number, bet_amount = place_bet(balance)
        
        # Track color history before spinning the wheel
        winning_number = spin_wheel()
        color_history = game_history(color_history, str(winning_number))
        
        balance += determine_win(bet_number, bet_amount, winning_number)
        
        # Count RED and BLACK appearances
        red_count = color_history.count("RED")
        black_count = color_history.count("BLACK")
        green_count = color_history.count("GREEN")
        total_games = len(color_history)
        print(f"RED appeared {red_count} times out of {total_games} games.")
        print(f"BLACK appeared {black_count} times out of {total_games} games.")
        print(f"GREEN appeared {green_count} times out of {total_games} games.")
        
    print("\nGame Over. You ran out of balance.")

# Run the game
if __name__ == "__main__":
    play_roulette()