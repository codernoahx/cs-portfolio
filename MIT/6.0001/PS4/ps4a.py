# Problem Set 4A
# Name: Noah
# Collaborators:
# Time Spent: 00:15


def get_permutations(sequence: str) -> list[str]:
    """
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """
    # if len of the sequence is 1, return the sequence inside a list (base case)
    if len(sequence) == 1:
        return [sequence]
    # generate a smaller list of sequence without the first character
    smaller_sequence: list[str] = get_permutations(sequence[1:])  # inductive hypothesis
    # store the first character to add to the smaller sequence list
    first: str = sequence[:1]
    # create a new list
    new: list = []
    # inductive step starts:
    # for every seq in smaller sequence list
    for seq in smaller_sequence:
        # extend the new list with the generated list comprehension, which appends the first character at different position of i
        # it takes the letter in the sequence upto i, excluding i + the first letter + all the letter after ith position, including i
        # len(seq) + 1: the +1 helps to append the first character at the nth index, which isn't reachable because
        # it'll go till n -  1 th index, as n isn't included in the range function
        new.extend([seq[:i] + first + seq[i:] for i in range(len(seq) + 1)])
    # return the new list, not the concatenation of new + smallter sequence as we only need the sequences that contains all the letters
    # not excluding the first
    return new


if __name__ == "__main__":
    #    #EXAMPLE
    example_input = "abc"
    print("Input:", example_input)
    print("Expected Output:", ["abc", "acb", "bac", "bca", "cab", "cba"])
    print("Actual Output:", get_permutations(example_input))

    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)
    print("-" * 10)
    example_input = "xyz"
    print("Input:", example_input)
    print("Expected Output:", ["xyz", "xzy", "yxz", "yzx", "zxy", "zyx"])
    print("Actual Output:", get_permutations(example_input))
    print("-" * 10)
    example_input = "i"
    print("Input:", example_input)
    print("Expected Output:", ["i"])
    print("Actual Output:", get_permutations(example_input))
    print("-" * 10)
    example_input = "mn"
    print("Input:", example_input)
    print("Expected Output:", ["mn", "nm"])
    print("Actual Output:", get_permutations(example_input))
