import random

def play(): 
    user = input("What do you choose? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Its a tie'

# r > s, s > p, p > r
    if has_won(user, computer):
        return 'You Won! Good Job!'

    return 'You Lost, Try again?'
def has_won(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())














