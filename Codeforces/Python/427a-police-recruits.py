def main():
    n = input()
    events = input().split()
    untreated_crimes, police_officers = 0, 0
    for event in events:
        # If event is a crime
        if event == "-1":
            # And police officers are available (> 0), decrement their count by 1
            if police_officers:
                police_officers -= 1
            # Else increment untreated crimes by 1
            else:
                untreated_crimes += 1
        # Else if it's a hiring event, increment police by the event number which is the number of hires
        else:
            police_officers += int(event)
    print(untreated_crimes)


if __name__ == "__main__":
    main()
