# Problem Set 4C
# Name: Noah
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations


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


### END HELPER CODE ###

WORDLIST_FILENAME = "words.txt"

# you may find these constants helpful
VOWELS_LOWER = "aeiou"
VOWELS_UPPER = "AEIOU"
CONSONANTS_LOWER = "bcdfghjklmnpqrstvwxyz"
CONSONANTS_UPPER = "BCDFGHJKLMNPQRSTVWXYZ"


class SubMessage(object):
    def __init__(self, text: str) -> None:
        """
        Initializes a SubMessage object

        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        self.message_text: str = text
        self.valid_words: list[str] = load_words(WORDLIST_FILENAME)

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
        return self.valid_words.copy()  # or self.valid_words[:]

    def build_transpose_dict(self, vowels_permutation: str) -> dict[str, str]:
        """
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)

        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled
        according to vowels_permutation. The first letter in vowels_permutation
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        """
        # create an empty dict to store the mapping
        transposed_dict: dict[str, str] = {}
        # for every letter in VOWELS_LOWER and vowels_permuation
        for vowel, vowel_map in zip(VOWELS_LOWER, vowels_permutation):
            # map vowel from VOWELS_LOWER -> vowel_map from vowels_permutation
            # the key will be the vowel and the value will be mapped letter at the same position in vowel_permuation
            transposed_dict[vowel] = vowel_map
            # similar mapping for uppercase vowels
            transposed_dict[vowel.upper()] = vowel_map.upper()
        # for every consonant in CONSONANTS_LOWER
        for consonant in CONSONANTS_LOWER:
            # map the consonant to itself
            # the key and value will be the same for both key and pair which is consonant
            transposed_dict[consonant] = consonant
            # similar mapping for uppercase consonants
            transposed_dict[consonant.upper()] = consonant.upper()
        # return the transposed_dict
        return transposed_dict

    def apply_transpose(self, transpose_dict: dict[str, str]) -> str:
        """
        transpose_dict (dict): a transpose dictionary

        Returns: an encrypted version of the message text, based
        on the dictionary
        """
        # create an empty str variable to store the transposed word
        transposed_word: str = ""
        # for every character in message text
        for char in self.get_message_text():
            # if the char is an alphabet append it's mapped char using transposed dict else append it as it
            transposed_word += transpose_dict[char] if char.isalpha() else char
        # return the transposed_word
        return transposed_word


class EncryptedSubMessage(SubMessage):
    def __init__(self, text: str) -> None:
        """
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        SubMessage.__init__(self, text)

    def decrypt_message(self) -> str:
        """
        Attempt to decrypt the encrypted message

        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.

        If no good permutations are found (i.e. no permutations result in
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message

        Hint: use your function from Part 4A
        """
        # create an empty list to store all the tuples of (matched_words (count), decrypted_message)
        guess_list: list[tuple] = []
        # get a list of all possible permutations of lowercase vowels, because we can create uppercase vowels mapping
        # in the build_transpose_dict method
        permutations: list[str] = get_permutations(VOWELS_LOWER)
        # for every permutation in permutations
        for permutation in permutations:
            # a tracker variable to keep the count of number of matched words
            matched_words = 0
            # decrypt the message by calling build_transpose_dict method with permutation inside apply_transpose method to
            # decrypt the message
            decrypted_message = self.apply_transpose(
                self.build_transpose_dict(permutation)
            )
            # for every word in decrypted message (the words are splitted by using space/tabs/newline as the separator string)
            for word in decrypted_message.split():
                # if the word is valid
                if is_word(self.get_valid_words(), word):
                    # increment matched words by 1
                    matched_words += 1
            # append the tuple of matched words count and the decrypted message: (matched_words, decrypted_message)
            guess_list.append((matched_words, decrypted_message))
            # sort the list in descending order, using the first element of each tuple
        guess_list.sort(reverse=True)
        # if the matched_words count is greater than 0: return the decrypted_message, else: return the original encrypted text
        return guess_list[0][1] if guess_list[0][0] > 0 else self.get_message_text()


if __name__ == "__main__":

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())

    # TODO: WRITE YOUR TEST CASES HERE
