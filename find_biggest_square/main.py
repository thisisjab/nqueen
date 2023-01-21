from copy import deepcopy


seed_matrix = [
    ['*', '#', '#', '*'],
    ['*', '*', '#', '*'],
    ['#', '*', '#', '#'],
    ['*', '#', '#', '#'],
]


def print_matrix(matrix: list) -> str:
    result = ''
    for row in matrix:
        result += ' '.join(row) + '\n'

    return result[0:-1]


def create_square(matrix: list, size: int, begin_i: int, begin_y: int) -> list:
    square = []
    for _ in range(size):
        square.append(matrix[begin_i][begin_y:begin_y+size])

    return square


def square_is_ok(square_matrix: list) -> bool:
    symbols = set()

    for row in square_matrix:
        symbols = symbols.union(set(row))

    if len(symbols) == 1:
        return True
    return False


def gen_all_n_squares(matrix: list, size: int) -> list:
    matrix_copy = deepcopy(matrix)
    result = []
    for i in range(len(matrix) - size + 1):
        for j in range(len(matrix) - size + 1):
            result.append(create_square(matrix_copy, size, i, j))

    return result


# Simple test
for size in range(len(seed_matrix), 1, -1):
    generated_matrix = gen_all_n_squares(seed_matrix, size)
    for square in generated_matrix:
        if square_is_ok(square):
            print(print_matrix(square))
            break
