def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long")
    print("_ _ _ _ _ _ _ _ _")

    lettersGuessed = []
    attempts = 8

    while not isWordGuessed(secretWord, lettersGuessed) and attempts > 0:
        print("You have " + str(attempts) + " guesses left")
        print("Available letters: " + getAvailableLetters(lettersGuessed))

        while True:
            guessLetter = str(input("Please guess a letter: ").lower())
            if guessLetter in lettersGuessed:
                print("Oops! You've already guessed that letter: " +
                      getGuessedWord(secretWord, lettersGuessed))
                print("_ _ _ _ _ _ _ _ _")
                print("You have " + str(attempts) + " guesses left")
                print("Available letters: " +
                      getAvailableLetters(lettersGuessed))
            else:
                break
        lettersGuessed += guessLetter

        if isWordGuessed(secretWord, lettersGuessed):
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print("_ _ _ _ _ _ _ _ _")
            print("Congratulations, you won!")

        elif guessLetter in secretWord:
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
            print("_ _ _ _ _ _ _ _ _")

        else:
            print("Oops! That letter is not in my word: " +
                  getGuessedWord(secretWord, lettersGuessed))
            print("_ _ _ _ _ _ _ _ _")
            attempts -= 1

        if attempts == 0:
            print("Sorry, you ran out of guesses. The word was", secretWord)
