from random import randint

random_num = randint(1, 100)
attempts = 0
found = False

while not found:
    guess = int(input('Guess a number between 1 and 100: '))
    attempts += 1
    if attempts<10:
        if guess == random_num:    
            print(f'You won! You found in {attempts} attempts!')
            found = True
        elif guess < random_num:
            print('Too low')
        else:
            print('Too high')
            
    else:
        print('You lost!')
        play_again = input('Wanna play again[y/n]: ')
        if play_again.lower == 'n':
            found = True
        elif play_again.lower() == 'y':
            attempts = 0
        else:
            found = True
            print('wrong input, game ended')