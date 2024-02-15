import random

word_list = ['elephant', 'computer', 'sunshine', 'love', 'butterfly', 'bread',
             'mountain', 'chocolate', 'firework', 'Telephone', 'Cupcake',
             'Cupboard', 'Snowman', 'Notebook', 'python', 'statistics']


def get_word():
    word = random.choice(word_list)
    return word.upper()


def display_hangman(tries):
    stages = ["""
                    ________
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
                    -                    
                  """
        ,
              """
                    ________
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     /
                    -                    
                  """
        ,
              """
                    ________
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     
                    -                    
                  """
        ,
              """
                    ________
                    |      |
                    |      O
                    |     \\|
                    |      |
                    |     
                    -                    
                  """
        ,
              """
                    ________
                    |      |
                    |      O
                    |      |
                    |      |
                    |     
                    -                    
                  """
        ,
              """
                    ________
                    |      |
                    |      O
                    |     
                    |      
                    |     
                    -                    
                  """
        ,
              """
                    ________
                    |      |
                    |      
                    |     
                    |      
                    |     
                    -                    
                  """
              ]
    return stages[tries]


def play(word):
    word_complete = '_ ' * len(word)
    guessed = False
    guessed_letters = []
    guessed_word = []
    tries = 6
    print("Let's play Hangman! ")
    print(display_hangman(tries))
    print(word_complete)
    print('\n')
    while not guessed and tries > 0:
        guess = input('Please guess a letter or word: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You already guessed the letter.', guess)
            elif guess not in word:
                print(guess, ' is not in the word.')
                guessed_letters.append(guess)
                tries -= 1  # Decrement tries only for incorrect guesses
            else:
                print('Good job,', guess, 'is in the word!')
                word_as_list = list(word_complete)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index * 2] = guess
                word_complete = ''.join(word_as_list)
                if '_' not in word_complete:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_word:
                print(guess, 'is not the word.')
                tries -= 1  # Decrement tries only for incorrect guesses
                guessed_word.append(guess)
            else:
                guessed = True
        else:
            print('Not a valid guess.')
        print(display_hangman(tries))
        print(word_complete)
        print('\n')
    if guessed:
        print('Congrats, you guessed the word!')
    else:
        print('Sorry, you ran out of tries. The word was ', word, '. Maybe next time!')


def main():
    word = get_word()
    play(word)
    while input('Play again?(Y/N) ').upper() == 'Y':
        word = get_word()
        play(word)


if __name__ == '__main__':
    main()
