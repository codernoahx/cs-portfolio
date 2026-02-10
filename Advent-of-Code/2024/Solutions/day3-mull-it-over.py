from pathlib import Path
import re


def main():
    # Initialize variables to store total sum, enabled sum, and a flag for calculation.
    total_sum, enabled_sum, enabled = 0, 0, True
    # Open and read the input file.
    with open(Path(__file__).parent.parent / "inputs" / "day3.txt") as file:
        # Read the content of the file into a variable.
        data = file.read()

        # Find all matches of the specified pattern in the input data.
        if matches := re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data):
            # Iterate over each match found.
            for match in matches:
                # If the match is "do()", enable calculations.
                if "do()" == match:
                    # Set the enabled flag to True.
                    enabled = True
                # If the match is "don't()", disable calculations.
                elif "don't()" == match:
                    # Set the enabled flag to False.
                    enabled = False
                # If the match is a multiplication operation.
                elif "mul" in match:
                    # Calculate the product from the multiplication operation and add it to the total sum.
                    product = calculate_product(match)
                    total_sum += product
                    # If calculations are currently enabled, add the product to the enabled sum.
                    if enabled:
                        enabled_sum += product
    # Print the total sum.
    print("Total sum:", total_sum)
    # Print the enabled sum.
    print("Enabled sum:", enabled_sum)


# Function to calculate the product from a given pattern.
def calculate_product(pattern: str) -> int:
    # Extract the two numbers from the pattern using regular expression.
    a, b = map(int, re.findall(r"\d+", pattern))
    # Return the product of the two numbers.
    return a * b


if __name__ == "__main__":
    main()
