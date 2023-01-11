import os


queen_icon = '*'
no_icon = 'O'


def create_empty_table(size: int):
    return [[no_icon] * size for i in range(size)]


def print_table(table: str) -> None:
    for row in table:
        print(*row)    


def queen_is_safe(queen_i: int, queen_j: int, table: list) -> bool:
    # First check if table[queen_i][queen_j] is actually a queen
    if table[queen_i][queen_j] != queen_icon:
        return (True, -1, -1)

    # Check queen's state in a column
    for i in range(len(table)):
        if i == queen_i:
            continue
        if table[i][queen_j] == queen_icon:
            # print('queen is not safe (state in a column)')
            # print(f'queen at ({i}, {queen_j}) hits ({queen_i}, {queen_j}).')
            return (False, i, queen_j)

    # Check queen's state in a row
    for j in range(len(table)):
        if j == queen_j:
            continue
        if table[queen_i][j] == queen_icon:
            # print('queen is not safe (state in a row)')
            # print(f'queen at ({queen_i}, {j}) hits ({queen_i}, {queen_j}).')
            return (False, queen_i, j)

    # Check queen's diagonal state
    # ltr: left to right
    # rtl: right to left
    # ttb: top to bottom
    # btt: botton to top
    # 1: ltr - ttb
    i = queen_i
    j = queen_j
    try:
        i += 1
        j += 1
        while i < n and j < n:
            if table[i][j] == queen_icon:
                # print('queen is not safe (ltr-ttb)')
                # print(f'queen at ({i}, {j}) hits ({queen_i}, {queen_j}).')
                return (False, i, j)
            i += 1
            j += 1
    except IndexError:
        pass

    # 2: ltr - btt
    i = queen_i
    j = queen_j
    try:
        i -= 1
        j -= 1
        while i >= 0 and j >= 0:
            if table[i][j] == queen_icon:
                # print('queen is not safe (ltr-btt)')
                # print(f'queen at ({i}, {j}) hits ({queen_i}, {queen_j}).')
                return (False, i, j)
            i -= 1
            j -= 1
    except IndexError:
        pass

    # 3: rtl - ttb
    i = queen_i
    j = queen_j
    try:
        i += 1
        j -= 1
        while i < n and j >= 0:
            if table[i][j] == queen_icon:
                # print('queen is not safe (rtl-ttb)')
                # print(f'queen at ({i}, {j}) hits ({queen_i}, {queen_j}).')
                return (False, i, j)
            i += 1
            j -= 1
    except IndexError:
        pass

    # 4: rtl - bbt
    i = queen_i
    j = queen_j
    try:
        i -= 1
        j += 1
        while i >= 0 and j < n:
            if table[i][j] == queen_icon:
                # print('queen is not safe (rtl-btt)')
                # print(f'queen at ({i}, {j}) hits ({queen_i}, {queen_j}).')
                return (False, i, j)
            i -= 1
            j += 1
    except IndexError:
        pass
    
    return (True, -1, -1)

# Game
if __name__ == '__main__':
    print('Chess Queen Placement')
    print('Find all possible placements of n queens in an n*n chess table')
    n = int(input('n>> '))
    table = create_empty_table(n)
    print_table(table)
    print('Ok! Here\'s the table. Tell where to put or take out the queens (enter e for end).')
    user_input = ''
    while user_input != 'e':
        user_input = input('Enter i and j starting from zero: ')
        os.system('clear')
        try:
            input_i, input_j = [int(value) for value in user_input.split(' ')]
            if not (0 <= input_i < n) and not (0 <= input_j < n):
                os.system('clear')
                print(f'Only numbers from 0 to {n} are allowed.')
                continue
        except Exception:
            os.system('clear')
            print('Enter only indexes.')
            continue

        if queen_icon in table[input_i]:
            print('Only one queens per row is allowed.')
            continue

        if table[input_i][input_j] == queen_icon:
            table[input_i][input_j] = no_icon
        else:
            table[input_i][input_j] = queen_icon
        print('queen safety:', queen_is_safe(input_i, input_j, table))
        print_table(table)

    print('Done.')
    states = [queen_is_safe(i, j, table) for i in range(n) for j in range(n)]
    print_table(table)
    print(all(states))

    