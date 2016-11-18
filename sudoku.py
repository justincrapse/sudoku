"""
SUDOKU PROBLEM:
0 = blank
605 708 291
390 000 874
000 002 003

200 000 740
059 304 610
017 000 009

500 800 936
783 000 425
964 503 187
"""

# I chose to organize the puzzle by 3x3 boxes. Perhaps it would have been easier to do by row.
sudoku_list = [
    [6, None, 5, 3, 9, None, None, None, None],
    [7, None, 8, None, None, None, None, None, 2],
    [2, 9, 1, 8, 7, 4, None, None, 3],
    [2, None, None, None, 5, 9, None, 1, 7],
    [None, None, None, 3, None, 4, None, None, None],
    [7, 4, None, 6, 1, None, None, None, 9],
    [5, None, None, 7, 8, 3, 9, 6, 4],
    [8, None, None, None, None, None, 5, None, 3],
    [None, None, None, None, 2, 5, 1, None, 7]
]

new_entry_list = []

def solve_sudoku(sudoku_list, last_change=None):

    if last_change:
        try:
            new_value = last_change[2].pop(0)
            sudoku_list[last_change[0]][last_change[1]] = new_value
            solve_sudoku(sudoku_list=sudoku_list)
        except IndexError:
            sudoku_list[last_change[0]][last_change[1]] = None
            new_entry_list.pop()
            solve_sudoku(sudoku_list=sudoku_list, last_change=new_entry_list[-1])

    for key, box in enumerate(sudoku_list):
        for entry_position, entry in enumerate(box):
            if entry == None:
                entry_position += 1
                entry_box = key + 1
                entry_row = get_entry_row(box=entry_box, entry_position=entry_position)
                row_list = get_row_list(entry_row=entry_row)
                entry_column = get_entry_column(box=entry_box, entry_position=entry_position)
                column_list = get_column_list(entry_column=entry_column)

                possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for entry in box:
                    if entry in possible_numbers:
                        possible_numbers.remove(entry)
                # same row:
                for entry in row_list:
                    if entry in possible_numbers:
                        possible_numbers.remove(entry)
                # same column:
                for entry in column_list:
                    if entry in possible_numbers:
                        possible_numbers.remove(entry)
                try:
                    new_value = possible_numbers.pop(0)
                    sudoku_list[key][entry_position -1] = new_value
                    new_entry_list.append([key, entry_position -1, possible_numbers])
                except IndexError:
                    solve_sudoku(sudoku_list=sudoku_list, last_change=new_entry_list[-1])


def get_row_list(entry_row):
    if entry_row == 1:
        row_list = []
        row_list.extend(sudoku_list[0][0:3])
        row_list.extend(sudoku_list[1][0:3])
        row_list.extend(sudoku_list[2][0:3])
        return row_list
    elif entry_row == 2:
        row_list = []
        row_list.extend(sudoku_list[0][3:6])
        row_list.extend(sudoku_list[1][3:6])
        row_list.extend(sudoku_list[2][3:6])
        return row_list
    elif entry_row == 3:
        row_list = []
        row_list.extend(sudoku_list[0][6:9])
        row_list.extend(sudoku_list[1][6:9])
        row_list.extend(sudoku_list[2][6:9])
        return row_list

    elif entry_row == 4:
        row_list = []
        row_list.extend(sudoku_list[3][0:3])
        row_list.extend(sudoku_list[4][0:3])
        row_list.extend(sudoku_list[5][0:3])
        return row_list
    elif entry_row == 5:
        row_list = []
        row_list.extend(sudoku_list[3][3:6])
        row_list.extend(sudoku_list[4][3:6])
        row_list.extend(sudoku_list[5][3:6])
        return row_list
    elif entry_row == 6:
        row_list = []
        row_list.extend(sudoku_list[3][6:9])
        row_list.extend(sudoku_list[4][6:9])
        row_list.extend(sudoku_list[5][6:9])
        return row_list

    elif entry_row == 7:
        row_list = []
        row_list.extend(sudoku_list[6][0:3])
        row_list.extend(sudoku_list[7][0:3])
        row_list.extend(sudoku_list[8][0:3])
        return row_list
    elif entry_row == 8:
        row_list = []
        row_list.extend(sudoku_list[6][3:6])
        row_list.extend(sudoku_list[7][3:6])
        row_list.extend(sudoku_list[8][3:6])
        return row_list
    elif entry_row == 9:
        row_list = []
        row_list.extend(sudoku_list[6][6:9])
        row_list.extend(sudoku_list[7][6:9])
        row_list.extend(sudoku_list[8][6:9])
        return row_list

def get_column_list(entry_column):
    if entry_column == 1:
        row_list = []
        row_list.extend(sudoku_list[0][:9:3])
        row_list.extend(sudoku_list[3][:9:3])
        row_list.extend(sudoku_list[6][:9:3])
        return row_list
    elif entry_column == 2:
        row_list = []
        row_list.extend(sudoku_list[0][1:9:3])
        row_list.extend(sudoku_list[3][1:9:3])
        row_list.extend(sudoku_list[6][1:9:3])
        return row_list
    elif entry_column == 3:
        row_list = []
        row_list.extend(sudoku_list[0][2:9:3])
        row_list.extend(sudoku_list[3][2:9:3])
        row_list.extend(sudoku_list[6][2:9:3])
        return row_list

    elif entry_column == 4:
        row_list = []
        row_list.extend(sudoku_list[1][:9:3])
        row_list.extend(sudoku_list[4][:9:3])
        row_list.extend(sudoku_list[7][:9:3])
        return row_list
    elif entry_column == 5:
        row_list = []
        row_list.extend(sudoku_list[1][1:9:3])
        row_list.extend(sudoku_list[4][1:9:3])
        row_list.extend(sudoku_list[7][1:9:3])
        return row_list
    elif entry_column == 6:
        row_list = []
        row_list.extend(sudoku_list[1][2:9:3])
        row_list.extend(sudoku_list[4][2:9:3])
        row_list.extend(sudoku_list[7][2:9:3])
        return row_list

    elif entry_column == 7:
        row_list = []
        row_list.extend(sudoku_list[2][:9:3])
        row_list.extend(sudoku_list[5][:9:3])
        row_list.extend(sudoku_list[8][:9:3])
        return row_list
    elif entry_column == 8:
        row_list = []
        row_list.extend(sudoku_list[2][1:9:3])
        row_list.extend(sudoku_list[5][1:9:3])
        row_list.extend(sudoku_list[8][1:9:3])
        return row_list
    elif entry_column == 9:
        row_list = []
        row_list.extend(sudoku_list[2][2:9:3])
        row_list.extend(sudoku_list[5][2:9:3])
        row_list.extend(sudoku_list[8][2:9:3])
        return row_list


def get_entry_row(box, entry_position):
    if entry_position in [1, 2, 3] and box in [1, 2, 3]:
        return 1
    elif entry_position in [4, 5, 6] and box in [1, 2, 3]:
        return 2
    elif entry_position in [7, 8, 9] and box in [1, 2, 3]:
        return 3

    elif entry_position in [1, 2, 3] and box in [4, 5, 6]:
        return 4
    elif entry_position in [4, 5, 6] and box in [4, 5, 6]:
        return 5
    elif entry_position in [7, 8, 9] and box in [4, 5, 6]:
        return 6

    elif entry_position in [1, 2, 3] and box in [7, 8, 9]:
        return 7
    elif entry_position in [4, 5, 6] and box in [7, 8, 9]:
        return 8
    elif entry_position in [7, 8, 9] and box in [7, 8, 9]:
        return 9

def get_entry_column(box, entry_position):
    if entry_position in [1, 4, 7] and box in [1, 4, 7]:
        return 1
    elif entry_position in [2, 5, 8] and box in [1, 4, 7]:
        return 2
    elif entry_position in [3, 6, 9] and box in [1, 4, 7]:
        return 3

    elif entry_position in [1, 4, 7] and box in [2, 5, 8]:
        return 4
    elif entry_position in [2, 5, 8] and box in [2, 5, 8]:
        return 5
    elif entry_position in [3, 6, 9] and box in [2, 5, 8]:
        return 6

    elif entry_position in [1, 4, 7] and box in [3, 6, 9]:
        return 7
    elif entry_position in [2, 5, 8] and box in [3, 6, 9]:
        return 8
    elif entry_position in [3, 6, 9] and box in [3, 6, 9]:
        return 9

if __name__ == "__main__":
    solve_sudoku(sudoku_list)
    print("{} {} {}".format(''.join(str(x) for x in sudoku_list[0][:3]),
                            ''.join(str(x) for x in sudoku_list[1][:3]),
                            ''.join(str(x) for x in sudoku_list[2][:3])))
    print("{} {} {}".format(''.join(str(x) for x in sudoku_list[0][3:6]),
                            ''.join(str(x) for x in sudoku_list[1][3:6]),
                            ''.join(str(x) for x in sudoku_list[2][3:6])))
    print("{} {} {}".format(''.join(str(x) for x in sudoku_list[0][6:9]),
                            ''.join(str(x) for x in sudoku_list[1][6:9]),
                            ''.join(str(x) for x in sudoku_list[2][6:9])))

    print("{} {} {}".format(''.join(str(x) for x in sudoku_list[3][:3]),
                            ''.join(str(x) for x in sudoku_list[4][:3]),
                            ''.join(str(x) for x in sudoku_list[5][:3])))
    print("{} {} {}".format(''.join(str(x) for x in sudoku_list[3][3:6]),
                            ''.join(str(x) for x in sudoku_list[4][3:6]),
                            ''.join(str(x) for x in sudoku_list[5][3:6])))
    print("{} {} {}".format(''.join(str(x) for x in sudoku_list[3][6:9]),
                            ''.join(str(x) for x in sudoku_list[4][6:9]),
                            ''.join(str(x) for x in sudoku_list[5][6:9])))

    print("{} {} {}".format(''.join(str(x) for x in sudoku_list[6][:3]),
                            ''.join(str(x) for x in sudoku_list[7][:3]),
                            ''.join(str(x) for x in sudoku_list[8][:3])))
    print("{} {} {}".format(''.join(str(x) for x in sudoku_list[6][3:6]),
                            ''.join(str(x) for x in sudoku_list[7][3:6]),
                            ''.join(str(x) for x in sudoku_list[8][3:6])))
    print("{} {} {}".format(''.join(str(x) for x in sudoku_list[6][6:9]),
                            ''.join(str(x) for x in sudoku_list[7][6:9]),
                            ''.join(str(x) for x in sudoku_list[8][6:9])))
