def main():
    n = int(input())
    # Keep on printing I love that or hate that based on whether i is odd or even, starting from 1
    # Note: When input is 1, loop won't execute and we'll go to the last print statement
    for i in range(1, n):
        print("I love that" if i % 2 == 0 else "I hate that", end=" ")
    # And at last based on odd or even value of n, print love or hate ending with it
    print("I love it" if n % 2 == 0 else "I hate it")
    
    
if __name__ == "__main__":
    main()