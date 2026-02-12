def main():
    n = int(input())
    # We'll store home and guest uniform of the ith team in two separte lists
    home, guest = [], []
    # Used to count when host team will wear guest uniform, when the guest team will have the same uniform as the host team's
    # home uniform
    host_in_guest = 0
    # Store the ith team uniform values in separte lists
    for _ in range(n):
        h, g = map(int, input().split())
        home.append(h)
        guest.append(g)

    for i in range(n):
        for j in range(n):
            # Whenever any ith teams home uniform matches jth team guest unifrom increment host in guest by 1
            # There can me multiple guest teams that have the same home uniform as ith team
            if home[i] == guest[j]:
                host_in_guest += 1
    print(host_in_guest)


if __name__ == "__main__":
    main()
