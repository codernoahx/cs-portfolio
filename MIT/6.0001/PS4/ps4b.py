# Problem Set 4B
# Name: Noah
# Collaborators:
# Time Spent: x:xx

import string


### HELPER CODE ###
def load_words(file_name):
    """
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, "r")
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(" ")])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    """
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


### END HELPER CODE ###

WORDLIST_FILENAME = "words.txt"


class Message(object):
    def __init__(self, text: str) -> None:
        """
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self) -> str:
        """
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        """
        return self.message_text

    def get_valid_words(self) -> list[str]:
        """
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        """
        return self.valid_words[:]  # or self.valid_words.copy()

    def build_shift_dict(self, shift: int) -> dict[str, str]:
        """
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        """
        # create an empty dict
        encryption_dict: dict = {}
        # for every letter in the lowercase alphabet string
        for char in string.ascii_lowercase:
            # add the char/char.upper() key mapped to their shifted value determined by the shift variable
            # RHS expression: ascii value of a/A is subtracted by char/char.upper() ascii value + shift and then doing the modulo
            # of that value which will give us a value lying between 0 <= value <=25 and then we add the ascii value of a/A to it
            # and finally convert the ascii value to it's equivalent character and assign it to the char/char.upper() key
            encryption_dict[char] = chr(
                ((ord(char) - ord("a")) + shift) % 26 + ord("a")
            )
            encryption_dict[char.upper()] = chr(
                ((ord(char.upper()) - ord("A")) + shift) % 26 + ord("A")
            )
        # return the encryption dict which contains mapping: letter -> shifted letter
        return encryption_dict

    def apply_shift(self, shift: int) -> str:
        """
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        """
        # call the build_shift_dict function to create shift letter mapping
        encryption_dict: dict[str, str] = self.build_shift_dict(shift)
        # create an empty string variable to store the encrypted text
        encrypted_message: str = ""
        # for every character in message
        for char in self.message_text:
            # append the values to the right, if it is an alphabet append the mapped shifted letter
            # corresponding to the char letter key, else if it isn't an alphabet append it as it is
            encrypted_message += encryption_dict[char] if char.isalpha() else char
        # return the encrypted message
        return encrypted_message


class PlaintextMessage(Message):
    def __init__(self, text: str, shift: int) -> None:
        """
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        """
        Message.__init__(self, text)
        self.shift: int = shift
        self.encryption_dict: dict[str, str] = self.build_shift_dict(shift)
        self.message_text_encrypted: str = self.apply_shift(shift)

    def get_shift(self):
        """
        Used to safely access self.shift outside of the class

        Returns: self.shift
        """
        return self.shift

    def get_encryption_dict(self):
        """
        Used to safely access a copy self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        """
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        """
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        """
        return self.message_text_encrypted

    def change_shift(self, shift: int) -> None:
        """
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift.

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        """
        # updates the shift value
        self.shift: int = shift
        # update the encryption dict mapped using the new shift
        self.encryption_dict: dict[str, str] = self.build_shift_dict(shift)
        # update the encrypted text using the new encryption dict based on the new shift value
        self.message_text_encrypted: str = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text: str) -> None:
        """
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        Message.__init__(self, text.strip())

    def decrypt_message(self) -> tuple[int, str]:
        """
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create
        the maximum number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        """
        # a list to store the tuples containing: no. of matched words, best shift value, decrypted message
        guesses: list[tuple] = []
        # for shift values ranging from 0 to 25, why not 26 because our algorithm will convert 26 to 0
        # since we're passing 0 as s in the loop, we aren't passing 0 to the apply_shift method, since
        # passing 26 and 0 will be the same thing. (% 26)
        for s in range(26):
            # subtract s from 26 to find the best_shift, in order to rotate back to the mapping of the original letters
            # but in reverse: encrypted letter -> decrypted letter
            best_shift: int = 26 - s
            # to store the matched words count
            matched_words: int = 0
            # convert the message into decrypted message using best_shift and store it
            decryted_message: str = self.apply_shift(best_shift)
            # for every word in decrypted message, we split the message based on space, tab, and newline
            for word in decryted_message.split():
                # if it is a valid word
                if is_word(self.valid_words, word):
                    # increment word matched by 1
                    matched_words += 1
            # append the tuple containing: (matched_words, best_shift, decrypted_message) to the guesses list
            guesses.append((matched_words, best_shift, decryted_message))
        # sort the guesses list based on the first value of the tuple in descending order
        # and return the first tuple of the list containing (best_shift, decrypted_message) as the tuple values
        # excluding matched_words
        return sorted(guesses, reverse=True)[0][1:]


if __name__ == "__main__":

    # Example test case (PlaintextMessage)
    plaintext = PlaintextMessage("hello", 2)
    print("Expected Output: jgnnq")
    print("Actual Output:", plaintext.get_message_text_encrypted())

    # Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage("jgnnq")
    print("Expected Output:", (24, "hello"))
    print("Actual Output:", ciphertext.decrypt_message())

    print("-" * 15)

    plaintext = PlaintextMessage("yellow", 4)
    print("Expected Output: cippsa")
    print("Actual Output:", plaintext.get_message_text_encrypted())

    ciphertext = CiphertextMessage("cippsa")
    print("Expected Output:", (22, "yellow"))
    print("Actual Output:", ciphertext.decrypt_message())

    print("-" * 15)

    plaintext = PlaintextMessage("Python", 26)
    print("Expected Output: Python")
    print("Actual Output:", plaintext.get_message_text_encrypted())

    ciphertext = CiphertextMessage("Python")
    print("Expected Output:", (26, "Python"))
    print("Actual Output:", ciphertext.decrypt_message())

    print("-" * 15)

    plaintext = PlaintextMessage("Math", 25)
    print("Expected Output: Lzsg")
    print("Actual Output:", plaintext.get_message_text_encrypted())

    ciphertext = CiphertextMessage("Lzsg")
    print("Expected Output:", (1, "Math"))
    print("Actual Output:", ciphertext.decrypt_message())

    print("-" * 15)

    ciphertext = CiphertextMessage(get_story_string())
    decrypted_tuple = ciphertext.decrypt_message()
    print(f"Best Shift Value: {decrypted_tuple[0]}")
    print(f"Decrypted Story: {decrypted_tuple[1]}")
