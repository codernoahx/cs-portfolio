import math


def main():
    x = int(input("Enter number x: "))
    y = int(input("Enter number y: "))

    # x raised to the power y
    print(f"X**y = {x ** y}")
    # log base 2 of x
    print(f"log(x) = {int(math.log2(x))}")


if __name__ == "__main__":
    main()
