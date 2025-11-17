import random

def play():
    choices = ['r', 'p', 's']
    user = input("Choose: (r)ock, (p)aper, (s)cissors: ").lower()

    # Validate input
    if user not in choices:
        return "Invalid choice! Please enter r, p, or s."

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You won!"

    return "You lost!"

def is_win(player, opponent):
    # return True if player wins
    win_conditions = {
        'r': 's',  # rock beats scissors
        's': 'p',  # scissors beat paper
        'p': 'r',  # paper beats rock
    }
    return win_conditions[player] == opponent


print(play())
