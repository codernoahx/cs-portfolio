def is_weight_even(w):
    # If the weight is even, one of it's pair of distributions will have even pairs. Ex: 12 = 9+3 or 6+6 or 8+4, 6 = 3+3 or 4+2
    # 2 is the only even number which have no even distribution pairs. Ex: 2 = 1 + 1 or 0 + 2 etc.
    # Since we have to divide weight (int) in two parts and those two parts doesn't need to be in equal proportion.
    # We have to make sure both pairs in the distribution are even, doesn't matter how much difference exists in the two proportions.
    if w > 2 and w % 2 == 0:
        return "YES"
    return "NO"


print(is_weight_even(int(input())))
