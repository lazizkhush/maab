from random import choice

user_score = 0
comp_score = 0

while user_score!=5 and comp_score!=5:
    user_choice = input('rock, paper, scissors?')
    comp_choice = choice(['rock', 'paper', 'scissors'])
    if user_choice == comp_choice:
        print('Tie, you both chose the same thing')
    else:
        if comp_choice== 'rock' and user_choice =='scissors':
            comp_score+=1
            print(f'Computer Won, computer chose {comp_choice}')
        elif comp_choice== 'paper' and user_choice =='rock':
            comp_score+=1
            print(f'Computer Won, computer chose {comp_choice}')
        elif comp_choice== 'scissors' and user_choice =='paper':
            comp_score+=1
            print(f'Computer Won, computer chose {comp_choice}')
        else:
            user_score+=1
            print(f'You won, computer chose {comp_choice}')

    print(f'Computer | {comp_score} vs {user_score} | User')

if comp_score>user_score:
    print('Absolute winner: Computer')
else:
    print('Absolute winner: You')
print(f'Computer | {comp_score} vs {user_score} | User')

