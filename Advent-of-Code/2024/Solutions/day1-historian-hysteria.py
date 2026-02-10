from pathlib import Path

def main():
    # Initialize empty lists to store numbers from the left and right columns of the input file
    # Initialize variables to store total similarity and distance between the two lists
    left_list, right_list, similarity, distance = [], [], 0, 0

    # Open and read the input file
    with open(Path(__file__).parent.parent / "inputs" / "day1.txt", "r") as file:
        # Iterate over each line in the input file
        for line in file:
            # Split each line into two numbers, convert them to integers and append to the corresponding lists
            num1, num2 = map(int, line.split())
            # Append the numbers to the corresponding lists
            left_list.append(num1)
            right_list.append(num2)

    # Sort the left and right lists in ascending order
    left_list.sort()
    right_list.sort()

    # Calculate the total similarity and distance between the two lists
    for num in left_list:
        # For each number in the left list, add the product of the number and its frequency in the right list to the total similarity
        similarity += num * right_list.count(num)

        # Calculate the absolute difference between the number and the corresponding number in the right list, add it to the total distance
        distance += abs(num - right_list[left_list.index(num)])
    # Print the distance and total similarity
    print("Distance:", distance)
    print("Similarity:", similarity)


if __name__ == "__main__":
    main()
