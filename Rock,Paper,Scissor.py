import random

game={
    'r':"Rock",
    's':"Scissor",
    'p':"Paper"
}
def play():
    user=input("'r' for Rock,'s'for Scissor,'p' for Paper:").lower()
    computer=random.choice(['r','s','p'])
    print(f'You chose {game.get(user)} and computer chose {game.get(computer)}')
    if user==computer:
        return 'Tie'
    if iswon(user,computer):
        return 'You won'
    return 'You lost'


def iswon(player,opponent):
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True


print(play())