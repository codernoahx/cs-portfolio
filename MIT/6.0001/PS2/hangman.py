# Problem Set 2, hangman.py
# Name: Noah
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word: str, letters_guessed: list[str]) -> bool:
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """

    # Loops over every letter in secret_word
    for c in secret_word:
        # If the letter isn't in guessed letter list
        if c not in letters_guessed:
            # return False
            return False
    # If the loop completes we return True
    return True


def get_guessed_word(secret_word: str, letters_guessed: list[str]) -> str:
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    # word to store the computed output
    word = ""
    # For every letter in secret_word
    for c in secret_word:
        # If that letter is in guessed letter list append it, else append "_ " (underscore followed by space)
        word = (
            word + c if c in letters_guessed else word + "_ "
        )  # return the computed result
    return word


def get_available_letters(letters_guessed: list[str]) -> str:
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    # Performs a complement of guessed letters wrt all lowercase alphabets. And converting it back to list and sorting it.
    # And converting the list back to a string, separated by nothing.
    return "".join(sorted(list(set(string.ascii_lowercase) - set(letters_guessed))))


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    # Variable to store remaining guessses and warnings. And a list to store guessed letters.
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings_remaining} warnings left.")

    # While there are guesses left and the guessed letters doesn't contain all the secret word letters
    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("-" * 15)
        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        # Take the guessed character input from the user.
        guess = input("Please guess a letter: ").strip().lower()

        # If guess is an alphabet
        if guess.isalpha():
            # If we already guessed the letter
            if guess in letters_guessed:
                # If there are any warnings left, subtract it by 1
                if warnings_remaining:
                    warnings_remaining -= 1
                    print(
                        f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}"
                    )
                # Else subtract 1, from the remaining guesses
                else:
                    guesses_remaining -= 1
                    print(
                        f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}"
                    )
            # Else if letter is in secret word, append it to the guessed letters list
            elif guess in secret_word:
                letters_guessed.append(guess)
                print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
            # Else if this letter isn't guessed before nor part of secret word letter
            else:
                # Append it to the guessed letter list
                letters_guessed.append(guess)
                # If the wrong guessed letter is a vowel, subtract remaining guesses by 2
                if guess in "aeiou":
                    guesses_remaining -= 2
                    print(
                        f"Oops! That letter is not in my word. {get_guessed_word(secret_word, letters_guessed)}"
                    )
                # Else if the wrong guessed letter is a consonant, subtract remaining guesses by 1
                else:
                    guesses_remaining -= 1
                    print(
                        f"Oops! That letter is not in my word. {get_guessed_word(secret_word, letters_guessed)}"
                    )
        # If it isn't an alphabet
        else:
            # If there any warnings left, subtract it by 1
            if warnings_remaining:
                warnings_remaining -= 1
                print(
                    f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left: {get_guessed_word(secret_word, letters_guessed)}"
                )
            # Else subtract 1, from the remaining guesses
            else:
                guesses_remaining -= 1
                print(
                    f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}"
                )
    print("-" * 15)
    if guesses_remaining > 0 and is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print(
            f"Your total score for this game is: {guesses_remaining * len(set(secret_word))}"
        )
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word: str, other_word: str) -> bool:
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    # Replace underscore followed by a space with just underscore
    my_word = my_word.replace("_ ", "_")
    # If the len of my word and other word isn't equal return False
    if len(my_word) != len(other_word):
        return False
    # Loop over every index and letter in my word
    for i, c in enumerate(my_word):
        # If the letter is underscore
        if c == "_":
            # If for that underscore index position in my_word, check if that equivalent position letter of other_word already
            # exists in my_word. If so then that means my_word will have some other letter at ith position (_) compared to
            # other_word. As that letter exists already in my_word but didn't replaced the underscore, which means that
            # letter won't replace the underscore in my_word. And thus, we return False
            if other_word[i] in my_word:
                return False
        # Else if the letter in my_word isn't equivalent to the same position letter in other_word, we return false
        elif c != other_word[i]:
            return False
    # If the loop completes, we have a match and we can return True
    return True


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)
