def main():
    n = int(input())
    total = sum(map(int, input().split()))
    # Divide the total sum of juices by total number of juices
    print(total / n)
    

if __name__ == "__main__":
    main()
