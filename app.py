# Description: This is the main file for the Rock, Paper, Scissors Mini Game

import random

options = ['rock', 'paper', 'scissors']
play_again = 'yes'

print('Welcome to the Rock, Paper, Scissors Mini Game!')

# add a score variable to keep track of the user's score
score = 0
computer_score = 0
tie = 0

while play_again == 'yes':
        # randomly select an option from the list and save it to a variable called computer_choice
        computer_choice = random.choice(options)

        print('Please choose either "rock", "paper", or "scissors".')

        # get users input. Save it to a variable called selection
        selection = input()
        # put the selection to all lowercase
        selection = selection.lower() # force it to lower case so selection is not case sensitive

        while selection not in options:
            print('Invalid selection. Please choose either "rock", "paper", or "scissors".')
            selection = input()
            selection = selection.lower()

        # check if the user's selection is equal to the computer's selection
        if selection == computer_choice:
            print(f'\nThe computer ALSO chose {computer_choice}. It is a tie!')
            tie += 1
        # check if the user's selection is rock
        elif selection == 'rock':
            # check if the computer's selection is scissors
            if computer_choice == 'scissors':
                print(f'\nThe computer chose {computer_choice}. You WIN!')
                score += 1
            # check if the computer's selection is paper
            else:
                print(f'\nThe computer chose {computer_choice}. You LOSE!')
                computer_score += 1
        # check if the user's selection is paper
        elif selection == 'paper':
            # check if the computer's selection is rock
            if computer_choice == 'rock':
                print(f'\nThe computer chose {computer_choice}. You WIN!')
                score += 1
            # check if the computer's selection is scissors
            else:
                print(f'\nThe computer chose {computer_choice}. You LOSE!')
                computer_score += 1
        # check if the user's selection is scissors
        elif selection == 'scissors':
            # check if the computer's selection is paper
            if computer_choice == 'paper':
                print(f'\nThe computer chose {computer_choice}. You WIN!')
                score += 1
            # check if the computer's selection is rock
            else:
                print(f'\nThe computer chose {computer_choice}. You LOSE!')
                computer_score += 1

        # add the option to play again
        print('\nWould you like to play again? (yes/no)')
        play_again = input()
        play_again = play_again.lower()
        while play_again != 'yes' and play_again != 'no':
            print('Invalid selection. Please choose either "yes" or "no".')
            play_again = input()
            play_again = play_again.lower()
        print()

print(f'Here are the stats from your battle against the computer:')
print(f'Total games played: {score + computer_score + tie}')
print(f'Wins: {score}')
print(f'Losses: {computer_score}')
print(f'Ties: {tie}')

if score > computer_score:
    print('Congratulations! You are the winner!')
elif score < computer_score:
    print('Unfortunately, the computer is the winner...')
else:
    print('Overall, it was a tie!')

print('\nThank you for playing the Rock, Paper, Scissors Mini Game!')

# End of app.py
