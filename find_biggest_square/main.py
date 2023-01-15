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
    # TODO: complete this function
    pass
