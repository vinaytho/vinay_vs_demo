import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    print("I'm thinkin of a number can you guess it correct. Let's see..")
    while guess != random_number:
        guess = int(input(f"The number is between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
        
    print('Yay, congrats. You have guessed the number.')

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high b/c low = high
        feedback = input(f'Is {guess} too high(H), too low(L), or correct(C)?').lower()
        if feedback == 'h':
            high = guess -1
        elif feedback =='l':
            low = guess + 1
    print(f'Hey! The computer guessed your number, {guess}, correctly!')

computer_guess(100)
#guess(10)