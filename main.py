# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from src import Sudoku


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = [[0, 9, 8, 7, 4, 3, 1, 6, 2],
             [7, 6, 4, 2, 9, 1, 5, 3, 8],
             [1, 3, 2, 6, 5, 8, 4, 7, 9],
             [8, 7, 0, 9, 0, 2, 3, 4, 5],
             [3, 4, 9, 8, 0, 5, 7, 2, 6],
             [2, 5, 6, 4, 3, 7, 8, 9, 1],
             [4, 2, 7, 5, 8, 6, 9, 1, 3],
             [9, 1, 5, 3, 2, 4, 6, 8, 7],
             [6, 8, 3, 1, 7, 9, 2, 5, 4]
             ]

    sudoku = Sudoku(board)
    a = sudoku.check_sudoku_sol(board)
    b = sudoku.create_sudoku_candidates(board)
    print(a)
    print(b)
    for c in sudoku.find_unico_oculto(board):
        print(c)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
