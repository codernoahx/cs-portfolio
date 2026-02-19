def main():
    # n -> Friends, k -> bottles, l -> bottle drink quantity in milliliters, c-> limes, d -> no. of slices for each lemon
    # p -> grams of salt, nl -> milliliters of drink needed for one toast, np ->  grams of salt needed per toast, and each
    # serving of toast requires one slice of lemon
    n, k, l, c, d, p, nl, np = map(int, input().split())
    # Calculate the amount of drink in milliliters
    total_drink = k * l
    # Available slices
    lemon_slices = c * d
    # Number of drink toasts (Int div: Final answer will be an int)
    t_toasts = total_drink // nl
    # Available salt servings (Int Div: Final answer will be an int)
    salt_servings = p // np
    # Pick the minimum of one of them as we'll need all the 3 ingredients to make that no. of toasts, and after getting
    # the minimum value we divide it by total friends to get how many servings each friend gets
    # (Int Div: Final answer will be an int)
    print(min(t_toasts, salt_servings, lemon_slices) // n)


if __name__ == "__main__":
    main()
