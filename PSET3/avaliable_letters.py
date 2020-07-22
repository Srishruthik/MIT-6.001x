def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    string_comprised = string.ascii_lowercase

    available_Letters = []

    for letter in string_comprised:
        if letter not in lettersGuessed:
            available_Letters.append(letter)
    return ''.join(available_Letters)
