from random import choice


def run_game():
    word: str = choice(['apple', 'banana', 'orange', 'kiwi', 'pineapple'])
    
    username: str = input('What is your name? >> ')
    print(f'Welcome to hangman, {username}!')
    
    # Setup
    guessed: str = ''
    tries: int = 10
    warn: int = 1
    
    while tries > 0:
        blanks: int = 0
        
        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1
                
        print() # Adds a blank line
        
        if blanks == 0:
            print(f'You got it!')
            break
            
        guess: str = input('Guess a letter: ')
        
        if len(guess) > 1:
            if warn == 1:
                warn -= 1
                print("Please enter a single letter otherwise the game will end.")
                continue
            else:
                print(f"Game over.")
                break
        
        if guess.isnumeric():
            if tries > 1:
                tries -= 1
                print(f"Letters only. {tries} tries left.")
                continue
            else:
                print(f"No more tries left. You lose. The word was: '{word}'.")
                break

                
        if guess in guessed and guess.isalpha():
            tries -= 1
            print(f'You already tried: "{guess}". Please try another letter! {tries} tries left.')
            continue
            
        guessed += guess
        
        
        
        if guess not in word and guess.isalpha():
            tries -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {tries} tries left.")
            continue
            
        if tries == 0:
            print(f"No more tries left. You lose. The word was: '{word}'.")
            break
                
        
            

        
        
                
if __name__ == '__main__':
    run_game()