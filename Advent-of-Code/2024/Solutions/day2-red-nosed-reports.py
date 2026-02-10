from pathlib import Path

def main():
    # Initialize counters for safe and tolerated safe reports
    safe_reports_counter, tolerated_safe_reports_counter = 0, 0
    # Open the input file
    with open(Path(__file__).parent.parent / "inputs" / "day2.txt") as file:
        # Iterate through each line in the file
        for line in file:
            # Convert the line to a list of integers
            report = list(map(int, line.strip().split()))
            # Check if the report is safe
            if check_safe_report(report):
                # Increment safe report counter
                safe_reports_counter += 1
                # Increment tolerated safe report counter
                tolerated_safe_reports_counter += 1
            # Check if the report is tolerated safe
            elif check_tolerated_safe_report(report):
                # Increment tolerated safe report counter
                tolerated_safe_reports_counter += 1
    # Print the number of safe reports
    print("Safe reports:", safe_reports_counter)
    # Print the number of tolerated safe reports
    print("Tolerated safe reports:", tolerated_safe_reports_counter)


def check_safe_report(report: list[int]) -> bool:
    # Check if the report is sorted in ascending order but not strictly ascending
    if report[1] > report[0] and report != sorted(report):
        return False
    # Check if the report is sorted in descending order but not strictly descending
    elif report[0] > report[1] and report != sorted(report, reverse=True):
        return False
    # Check if the absolute difference between adjacent elements is within the allowed range
    for i in range(len(report) - 1):
        if abs(report[i + 1] - report[i]) not in [1, 2, 3]:
            return False
    # Return True if all checks pass
    return True


def check_tolerated_safe_report(report: list[int]) -> bool:
    # Iterate through each element in the report
    for i in range(len(report)):
        # Create a copy of the report without the current element
        report_copy = report[:i] + report[i + 1 :]
        # Check if the report copy is safe
        if check_safe_report(report_copy):
            return True
    # Return False if no safe report copy is found
    return False


if __name__ == "__main__":
    # Call the main function
    main()
