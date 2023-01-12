from utilities import *
from copy import deepcopy


# TODO: remove this function and use utilities.print_table function instead
def tprint(chess_table: list) -> str:
    result = ''
    for current_row in chess_table:
        result += ' '.join(current_row) + '\n'

    print(result[0:-1])
    return result[0:-1]


def next_possible_position(row_index, column_index, table_size: int) -> tuple:
    """
    Find next possible position in a chess board

    :param row_index: row of the queen
    :param column_index: column of the queen
    :param table_size: if table is n*n, the table_size is n
    :return: a tuple: (next_row_index, next_column_index)
    """
    if row_index == table_size - 1 and column_index == table_size - 1:
        return 0, 0

    if column_index < table_size - 1:
        column_index += 1
    else:
        row_index += 1
        column_index = 0

    return row_index, column_index


def find_all_placements(chess_board: list, row_index: int) -> list:
    """
    Find all possible positions that a queen can be placed at and return them as a list of chess boards

    :param chess_board: a 2d list in which the queen is going to be placed
    :param row_index: the row that queen should be placed
    :return: a list of chess boards
    """
    tables_list = []  # all generated chess boards
    for j in range(len(chess_board)):
        table_copy = deepcopy(chess_board)
        table_copy[row_index][j] = queen_icon
        if queen_is_safe(row_index, j, table_copy)[0]:
            tables_list.append(table_copy)

    return tables_list


def first_empty_column_index(chess_table: list) -> int:
    """
    Iterate through rows of a chess board and find the one with no queens placed on

    :param chess_table: a 2d list as a chess board
    :return: row's index or -1 if all rows have one queen
    """
    for row_index, current_row in enumerate(chess_table):
        if queen_icon not in current_row:
            return row_index
    return -1


def find_all_possible_placements(chess_board_size: int) -> list:
    """
    Find all possible queen placements and return a list of 2d lists
    :param chess_board_size: n if the board is n*n
    :return: a 3d list consisting of 2d lists
    """
    initial_table = create_empty_table(chess_board_size)
    possible_tables = [initial_table]
    row = 0
    current_index = 0
    while current_index < len(possible_tables):
        while current_index < len(possible_tables):
            current_table = possible_tables[current_index]
            possible_queens = find_all_placements(current_table, first_empty_column_index(current_table))
            possible_tables += possible_queens
            if first_empty_column_index(current_table) != -1:
                possible_tables.remove(current_table)
            else:
                current_index += 1
    return possible_tables
