import sys
import random
random.seed(50)


def ind_flip(target):
    """Handles the actual flip from whatever the element currently is to the opposite value"""
    if target == '.':
        return '*'
    elif target == '*':
        return '.'


def flip(inp, row, column):
    """Flipping a tile from white (.) to black (*), and vice versa. Handling included for
        out-of-bounds elements of the matrix"""
    new_list = inp
    new_list[row][column] = ind_flip(new_list[row][column])
    if column != 0:
        new_list[row][column-1] = ind_flip(new_list[row][column-1])
    if column != 2:
        new_list[row][column+1] = ind_flip(new_list[row][column+1])
    if row != 0:
        new_list[row-1][column] = ind_flip(new_list[row-1][column])
    if row != 2:
        new_list[row+1][column] = ind_flip(new_list[row+1][column])
    return new_list


def solve(target):
    """From a 'blank' white board, use a loop and random guessing to find the target pattern"""
    blank = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    used_targets = []
    counter = 0
    if target == blank:
        return counter
    while target != blank:
        # Loop until the pattern we're manipulating matches the target pattern
        random_row = random.randint(0, 2)
        random_col = random.randint(0, 2)
        if [random_row, random_col] not in used_targets:
            blank = flip(blank, random_row, random_col)
            counter += 1
            used_targets.append([random_row, random_col])
            if target == blank:
                return counter
                break
        elif len(used_targets) == 9:
            # If we hit every target without getting the pattern, reset the counters
            # and blank pattern, then continue looping
            blank = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
            counter = 0
            used_targets = []
        else:
            continue


def solve_handler(target):
    # A handler for invoking the solve method a number of times and printing the lowest result
    results = []
    for _ in range(20):
        results.append(solve(target))
    print(sorted(results)[0])


def parse_input(inp):
    # Parse the raw input from stdin
    last_line = 1
    for ind, x in enumerate(inp):
        if ind != 0 and ind % 3 == 0:
            solve_handler(inp[last_line:ind + 1])
            last_line += 3


if __name__ == '__main__':
    full_input = list()
    for i in sys.stdin:
        if i == '\n':
            break
        full_input.append(list(i.rstrip()))
    parse_input(full_input)
