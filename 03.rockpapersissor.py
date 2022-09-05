import random

def play():
    user = input(f"Choose one - Rock(R), Paper(P), Sissor(S) \n")
    print("user: " + user)
    computer = random.choice(['R', 'P', 'S'])
    print("Computer: "+ computer)

    if (user == computer):
        print('It\'s a tie..')
    
    if is_win(user, computer):
        print('You WON !!')
    
    return 'You Lost!'

            

def is_win(player, opponent):
    #S>P, P>R, R>S
    if (player == 'S' and opponent == 'P') or  (player == 'P' and opponent == 'R') or (player == 'R' and opponent == 'S'):
        return True
    else:
        return False
    

play()