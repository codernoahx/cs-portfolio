from pathlib import Path
import re


def main():
    with open(Path(__file__).parent.parent / "inputs" / "day4.txt") as file:
        matrix = list(map(str.strip, file.readlines()))
    word = "XMAS"
    print(f"Total: {find_word(matrix=matrix, word=word)}")


def find_word(matrix: list, word: str) -> int:
    directions = [(0, 1), (0, -1), (1, 0), [-1, 0], (1, 1), (1, -1), (-1, 1), (-1, -1)]
    count = 0
    rows, cols = len(matrix), len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            for dir_row, dir_col in directions:
                if check_word(matrix, word, row, col, dir_row, dir_col):
                    count += 1
    return count


def check_word(
    matrix: list, word: str, row: int, col: int, dir_row: int, dir_col: int
) -> bool:
    for i in range(len(word)):
        new_row, new_col = row + i * dir_row, col + i * dir_col
        if not (0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0])):
            return False
        if matrix[new_row][new_col] != word[i]:
            return False
    return True


if __name__ == "__main__":
    main()
