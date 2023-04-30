import random

    
def main():
    ...


def play():
    user = input("r for rock, p for paper, s for scissors ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"
    
    if is_win(user, computer):
        return "You won"

    return "You have lost"


def is_win(player, opponent):
    # returns true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True



if __name__ == "__main__":
    main()