import numpy as np


def check_vertical(arr, errors=0):
    for row in range(1, arr.shape[0]):
        if row <= arr.shape[0] // 2:
            arr_Up, arr_Down = arr[:row, :], arr[row: row + row, :]
            cols, rows = np.where(arr_Up != arr_Down[::-1])
            if len(cols) == errors:
                return row
        else:
            delta = arr.shape[0] - row
            arr_Up, arr_Down = arr[row - delta: row, :], arr[row:, :]
            cols, rows = np.where(arr_Up[::-1] != arr_Down)
            if len(cols) == errors:
                return row
    return 0


def check_horizontal(arr, errors=0):
    for col in range(1, arr.shape[1]):
        if col <= arr.shape[1] // 2:
            arr_Left, arr_Right = arr[:, :col], arr[:, col: col + col]
            cols, rows = np.where(arr_Left != arr_Right[:, ::-1])
            if len(cols) == errors:
                return col
        else:
            delta = arr.shape[1] - col
            arr_Left, arr_Right = arr[:, col - delta: col], arr[:, col:]
            cols, rows = np.where(arr_Left[:, ::-1] != arr_Right)
            if len(cols) == errors:
                return col
    return 0


file = 'input.txt'
# file = 'test.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

rows_pt1, cols_pt1, rows_pt2, cols_pt2, arr = 0, 0, 0, 0, []
for row in data:
    if row == '':
        arr = np.array(arr)
        rows_pt1 += check_vertical(arr)
        cols_pt1 += check_horizontal(arr)
        rows_pt2 += check_vertical(arr, 1)
        cols_pt2 += check_horizontal(arr, 1)
        arr = []
    else:
        arr.append(list(row))
# check last entry
arr = np.array(arr)
rows_pt1 += check_vertical(arr)
cols_pt1 += check_horizontal(arr)
rows_pt2 += check_vertical(arr, 1)
cols_pt2 += check_horizontal(arr, 1)
print(f'Part 1: {100 * rows_pt1 + cols_pt1}')
print(f'Part 2: {100 * rows_pt2 + cols_pt2}')

