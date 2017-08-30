from collections import defaultdict

# http://www.websudoku.com/?level=1&set_id=9584958293
puzzle = [[0, 5, 0, 0, 0, 4, 0, 3, 9],
          [7, 4, 0, 6, 0, 0, 0, 0, 0],
          [0, 0, 3, 0, 0, 0, 0, 0, 7],
          [3, 0, 5, 7, 4, 0, 8, 9, 0],
          [0, 9, 0, 3, 2, 1, 0, 5, 0],
          [0, 7, 6, 0, 8, 9, 3, 0, 4],
          [9, 0, 0, 0, 0, 0, 4, 0, 0],
          [0, 0, 0, 0, 0, 3, 0, 6, 8],
          [4, 3, 0, 2, 0, 0, 0, 1, 0]]


def fetch_section_values(row_set, col_set):
    new_section = []
    for row, col in zip([i for i in range(row_set, 3 + row_set) for _ in range(3)],
                        [i for i in range(col_set, 3 + col_set)] * 3):
        value = puzzle[row][col]
        if value != 0:
            new_section.append(value)
    return new_section


def solve_sudoku(puzzle):
    section_values = defaultdict(list)
    solve_list = []

    for row_set in range(0, 7, 3):
        for col_set in range(0, 7, 3):
            for row, col in zip([i for i in range(row_set, 3 + row_set) for _ in range(3)],
                                [i for i in range(col_set, 3 + col_set)]*3):
                value = puzzle[row][col]
                if value != 0:
                    section_values[(row_set, col_set)].append(puzzle[row][col])
                else:
                    solve_list.append({'row': row, 'col': col, 'sec': (row_set, col_set)})

    finished = False
    entry = 0
    first_guess = True

    while not finished:
        rows = puzzle
        columns = list(zip(*puzzle))
        row = solve_list[entry]['row']
        col = solve_list[entry]['col']

        if first_guess:
            row_values = set(rows[row])
            col_values = set(columns[col])
            sec_values = set(section_values[solve_list[entry]['sec']])
            possible_values = set(range(1, 10)) - (row_values | col_values | sec_values)

            if possible_values:
                solve_list[entry]['possible_values'] = possible_values
            else:
                entry -= 1
                first_guess = False
                continue

        if solve_list[entry]['possible_values']:
            solve_list[entry]['current_value'] = solve_list[entry]['possible_values'].pop()
        else:
            puzzle[row][col] = 0
            section_values[solve_list[entry]['sec']] = fetch_section_values(*solve_list[entry]['sec'])
            entry -= 1
            first_guess = False
            continue

        puzzle[row][col] = solve_list[entry]['current_value']
        section_values[solve_list[entry]['sec']] = fetch_section_values(*solve_list[entry]['sec'])
        first_guess = True
        entry += 1
        if len(solve_list) == entry:
            finished = True

    return puzzle

results = solve_sudoku(puzzle)
for i in results:
    print(i)
