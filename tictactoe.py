m = []


def action(self):
    if self == 'start':
        return grid()
    elif self == 'X':
        try:
            row, column = input('Enter the coordinates: ').split()
            row, column = int(row), int(column)
            if 3 >= row >= 1 and 3 >= column >= 1 and m[row - 1][column - 1] == " ":
                return coordinates(row, column, 'X')
            elif 3 >= row >= 1 and 3 >= column >= 1 and m[row - 1][column - 1] != " ":
                print("This cell is occupied! Choose another one!")
                return action('X')
            elif row or column != (1, 2, 3):
                print('Coordinates should be from 1 to 3!')
                return action('X')
        except ValueError:
            print("You should enter numbers!")
            return action('X')

    elif self == 'O':
        try:
            row, column = input('Enter the coordinates: ').split()
            row, column = int(row), int(column)
            if 3 >= row >= 1 and 3 >= column >= 1 and m[row - 1][column - 1] == " ":
                return coordinates(row, column, 'O')
            elif 3 >= row >= 1 and 3 >= column >= 1 and m[row - 1][column - 1] != " ":
                print("This cell is occupied! Choose another one!")
                return action('O')
            elif row or column != (1, 2, 3):
                print('Coordinates should be from 1 to 3!')
                return action('O')
        except ValueError:
            print("You should enter numbers!")
            return action('O')

    elif self == 3:
        return grid_call(1)


def grid_call(self):
    print('-' * 9)
    print(f'| {m[0][0]} {m[0][1]} {m[0][2]} |')
    print(f'| {m[1][0]} {m[1][1]} {m[1][2]} |')
    print(f'| {m[2][0]} {m[2][1]} {m[2][2]} |')
    print('-' * 9)
    if self == 'X':
        return action('O')
    elif self == 'O':
        return action('X')
    elif self == 'Draw':
        print('Draw')
    elif self == 'Win1':
        print(m[0][0], 'wins')
    elif self == 'Win2':
        print(m[1][1], 'wins')
    elif self == 'Win3':
        print(m[2][0], 'wins')
    elif self == 'Win4':
        print(m[2][2], 'wins')


def grid():
    global m
    for i in range(3):
        m.append([])
        for j in range(3):
            m[i].append(' ')
    return grid_call('O')


def coordinates(row, column, point):
    global m
    if point == 'X':
        m[row - 1][column - 1] = 'X'
    else:
        m[row - 1][column - 1] = 'O'
    win1 = (m[0][0] == m[0][1] == m[0][2] == 'X') or (m[0][0] == m[0][1] == m[0][2] == 'O')
    win2 = (m[0][0] == m[1][0] == m[2][0] == 'X') or (m[0][0] == m[1][0] == m[2][0] == 'O')
    win3 = (m[0][0] == m[1][1] == m[2][2] == 'X') or (m[0][0] == m[1][1] == m[2][2] == 'O')
    win4 = (m[0][1] == m[1][1] == m[2][1] == 'X') or (m[0][1] == m[1][1] == m[2][1] == 'O')
    win5 = (m[1][0] == m[1][1] == m[1][2] == 'X') or (m[1][0] == m[1][1] == m[1][2] == 'O')
    win6 = (m[2][0] == m[2][1] == m[2][2] == 'X') or (m[2][0] == m[2][1] == m[2][2] == 'O')
    win7 = (m[2][0] == m[1][1] == m[0][2] == 'X') or (m[2][0] == m[1][1] == m[0][2] == 'O')
    win8 = (m[0][2] == m[1][2] == m[2][2] == 'X') or (m[0][2] == m[1][2] == m[2][2] == 'O')
    if win1 or win2 or win3:
        return grid_call('Win1')
    elif win4 or win5:
        return grid_call('Win2')
    elif win6 or win7:
        return grid_call('Win3')
    elif win8:
        return grid_call('Win4')

    if point == 'X':
        if len([c for d in m for c in d if c == " "]) > 0:
            return grid_call('X')
        else:
            return grid_call('Draw')
    elif point == 'O':
        if len([c for d in m for c in d if c == " "]) > 0:
            return grid_call('O')
        else:
            return grid_call('Draw')


action('start')
