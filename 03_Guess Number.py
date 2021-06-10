import random

# Simple guess a number game 


def guessNumber(guessed_number):
    random_number = random.randint(1, guessed_number)
    
    guess = 0
    
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {guessed_number}: ' ))
        
        if guess < random_number:
            print ('Sorry, Please guess again. Number Guessed is Too low')
        
        elif guess > random_number:
            print('Sorry , Please try again, Nunber Guessed is too High: ')
            
    print(f'Congrats! You guessed a correct number {random_number}')
    
guessNumber(100)