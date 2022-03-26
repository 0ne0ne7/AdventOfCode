from pathlib import Path
from functools import reduce

cwd = Path.cwd()
input_path = cwd / "Inputs"


with open(input_path / "day4.txt", "r") as f:
    bingo_numbers, *rest = f.read().split("\n")
    bingo_numbers = list(bingo_numbers.split(","))
    bingo_numbers = [int(i.strip()) for i in bingo_numbers]
    boards = []
    for i in range(len(rest) // 6):
        a = rest[6 * i + 1 : 6 * i + 6]
        a = [int(j) for i in a for j in i.split()]
        boards.append(a)
    # print(bingo_numbers)
    # print(boards)


def parse_board(board, bingo_numbers):
    flags = []
    for i in range(5):
        a = board[5 * i : 5 * i + 5]
        b = [val for idx, val in enumerate(board) if idx % 5 == i]
        flags.append(set(a))
        flags.append(set(b))
    # print(flags)
    for i in range(len(bingo_numbers)):
        test_list = set(bingo_numbers[:i])

        flagged = [len(test_list & flag) for flag in flags]
        # print(flagged)
        if 5 in flagged:
            return i, bingo_numbers[i - 1] * reduce(
                (lambda x, y: x + y), set(board) - test_list
            )


scores = {
    parse_board(board, bingo_numbers)[1]: parse_board(board, bingo_numbers)[0]
    for board in boards
}


def part1():
    print(min(scores, key=scores.get))


def part2():
    print(max(scores, key=scores.get))
