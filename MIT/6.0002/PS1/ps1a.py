###########################
# 6.0002 Problem Set 1a: Space Cows
# Name: Noah
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

# ================================
# Part A: Transporting Space Cows
# ================================


# Problem 1
def load_cows(filename: str) -> dict[str, int]:
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # a dict to store cow name's and weight's: name -> weight
    cows_dict = {}
    # open file using with and it'll automatically close when the indented with block code ends
    # open to read the file, default mode is read, if no mode value is passed
    with open(filename) as file:
        # keep on looping until readline method returns an empty string
        while line := file.readline():
            # strip any newline characters we get from readline method and split them with ,
            name, number = line.strip().split(",")
            # add them to the dictm, with cow name as key and number converted to int as value for the key
            cows_dict[name] = int(number)
    # return the cow dictionary
    return cows_dict


# Problem 2
def greedy_cow_transport(cows: dict[str, int], limit: int = 10) -> list[list[str]]:
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # an empty list to store all the lists
    trips = []
    # sort the cows, get the key value pairs as tuples and sort them using values by creating a lamda function and passing
    # values as key and reverse will be True to get the sorted dict in descending order based on value (weight)
    sorted_cows = dict(sorted(cows.items(), key=lambda x: x[1], reverse=True))
    # while there are elements in sorted_cow dict
    while sorted_cows:
        # set the space to limit
        space = limit
        # create an empty list to store the cow names to be transported for the current trip
        transport_list = []
        # create a copy of the sorted dict
        sorted_cows_copy = sorted_cows.copy()
        # for each cow key in sorted cows copy
        for cow in sorted_cows_copy:
            # if space - weight of current cow is greater than or equal to 0
            # walrus operator is first subtracting and assigning the value to space_left then comparing it with 0
            if (space_left := space - sorted_cows_copy[cow]) >= 0:
                # set the space to space_left
                space = space_left
                # append the cow name to the transport list
                transport_list.append(cow)
                # since this cow will be transported in the current trip, pop/delete it from the list
                sorted_cows.pop(cow)  # or del sorted_cows[cow]
        # append the new transport list to the list of trips
        trips.append(transport_list)
    # return trips, which is the list of all the transport list
    return trips


# Problem 3
def brute_force_cow_transport(cows: dict[str, int], limit: int = 10) -> list[list[str]]:
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    # if cows is empty return an empty list
    if len(cows) == 0:
        return []

    # A partition of a set X is a set of non-empty subsets of X such that every element x in X is in exactly one of these subsets
    # get_partitions in first iteration yields a list with one element, which is a list of all the keys in cow keys
    # in the second iteration it yeilds list of 2 lists and each of them containing some of the cow keys and no value is repeated
    # and it generates all the possible list containing 2 list with all possible arrangements of keys divided between the 2 list
    # then moves on to the partition of list contains 3 lists with non-repeating key values, and so on.
    # for each partition from the partition set of cow keys
    for partition in get_partitions(cows.keys()):
        # for every trip from that partition
        for trip in partition:
            # if the sum of the transported cows is beyond the limit, break out of the loop.
            # We don't need this partition if any of the trip has weight beyond the limit
            if sum(cows[name] for name in trip) > limit:
                break
        # if a partition doesn't break out the loop prematurely, that means all the trips inside it is within
        # the weightt limit
        else:
            # return the current partition, since it's the one of the best possible partitions
            return partition
    # To satisfy pylance error that the final return statement must return a list, because of type hints
    return []


# Problem 4
def compare_cow_transport_algorithms() -> None:
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    # load the dict
    cow_dict = load_cows("ps1_cow_data.txt")
    # clock the start time for the greedy algorithm
    start_greedy: float = time.time()
    # get the len of trips to determine how many minimum trips we got from our greedy function/algorithm
    greedy_trips: int = len(greedy_cow_transport(cow_dict))
    # clock the end time of the greedy algorithm, after it finished it's execution
    end_greedy: float = time.time()

    # clock the start time for the brute force algorithm
    start_brute: float = time.time()
    # get the len of trips to determine how many minimum trips we got from our brute force function/algorithm
    brute_trips: int = len(brute_force_cow_transport(cow_dict))
    # clock the end time of the brute force algorithm, after it finished it's execution
    end_brute: float = time.time()

    print(
        f"Greedy Cow Transport Algorithm took {end_greedy - start_greedy:.5f} seconds to run.",
        f"Minimum trips it found was {greedy_trips}.",
    )
    print(
        f"Brute Force Cow Transport Algorithm took {end_brute - start_brute:.5f} seconds to run.",
        f"Minimum trips it found was {brute_trips}.",
    )
