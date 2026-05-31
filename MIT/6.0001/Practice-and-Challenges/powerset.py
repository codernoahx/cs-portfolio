def main() -> None:
    # list of elements separated by space is splitted and converted into a list of int's
    l: list = list(map(int, input("List of elements: ").strip().split()))
    # call the gen_subset inside print_subset function
    print_susbsets(gen_subsets(l))


# generates all the possible subsets of a given set
def gen_subsets(l: list) -> list:
    # if the list is empty return an empyty list of list, symbolizing a set with null set (base case)
    if len(l) == 0:
        return [[]]
    # generate all the possible subsets of the given set except the the last element (recursive step)
    smaller: list = gen_subsets(l[:-1])
    # store the last element as list
    last: list = l[-1:]
    # create an empty list to store the susbets including the last element
    new: list = []
    # for each set in smaller subset without the last element
    for e in smaller:
        # append the concatenation of smaller list + last list to create a list with the last element and append it to the new list
        new.append(e + last)
    # return the concatenation of smaller list + new list
    return smaller + new


# print the subsets
def print_susbsets(l: list) -> None:
    # print "[" and change the keyword argument end value from '\n' to ' '
    print("[", end=" ")
    # for each element e in l
    for e in l:
        # print e and change the keyword argument end value from '\n' to ', '
        print(e, end=", ")
    # print "]" with a newline
    print("]")
    # return None


if __name__ == "__main__":
    main()
