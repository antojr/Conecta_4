from __future__ import print_function


def line_four(state, move, player, (delta_x, delta_y)):
    if player == 'X':
        enemy = 'O'
    else:
        enemy = 'X'

    x, y = move
    line_of = 0
    value = 0

    while (8 > x > 0) and (7 > y > 0):
        if state.board.get((x, y)) == player:
            line_of += 1
            value += 200
        if state.board.get((x, y)) is None:
            line_of += 1
            value += 10
        if state.board.get((x, y)) == enemy:
            break
        x, y = x + delta_x, y + delta_y

    x, y = move
    x, y = x - delta_x, y - delta_y # Restamos para evitar contarnos a nosotros mismos.

    while (8 > x > 0) and (7 > y > 0):
        if state.board.get((x, y)) == player:
            line_of += 1
            value += 200
        if state.board.get((x, y)) is None:
            value += 1
            line_of += 10
        if state.board.get((x, y)) == enemy:
            break
        x, y = x - delta_x, y - delta_y

    if line_of >= 4:
        return value
    return 0


def run_heuristic(state, player, dificultad):
    if player == 'X':
        enemy = 'O'
    else:
        enemy = 'X'

    if player == 'X' and state.utility != 0:
        return state.utility * 10000000

    if player == 'O' and state.utility != 0:
        return state.utility * -1000000



    heuristic_value = 0
    l_moves = []
    for(x, y) in state.moves:
        if y == 1 or(x, y - 1) in state.board:
            l_moves += [(x, y)]

    for i in l_moves:
        x, y = i

        if dificultad == 2:
            heuristic_value += line_four(state, (x, y), player, (1, 0)) # --
            heuristic_value += line_four(state, (x, y), player, (0, 1)) # |
            heuristic_value += line_four(state, (x, y), player, (1, 1)) # /
            heuristic_value += line_four(state, (x, y), player, (1, -1)) # \

            heuristic_value -= line_four(state, (x, y), enemy, (1, 0))
            heuristic_value -= line_four(state, (x, y), enemy, (0, 1))
            heuristic_value -= line_four(state, (x, y), enemy, (1, 1))
            heuristic_value -= line_four(state, (x, y), enemy, (1, -1))

        if dificultad == 1:
            heuristic_value += line_four(state, (x, y), player, (1, 0))  # --
            heuristic_value += line_four(state, (x, y), player, (0, 1))  # |
            heuristic_value += line_four(state, (x, y), player, (1, 1))  # /
            heuristic_value += line_four(state, (x, y), player, (1, -1))  # \

            heuristic_value -= line_four(state, (x, y), enemy, (1, 0))
            heuristic_value -= line_four(state, (x, y), enemy, (0, 1))

        if dificultad == 0:
            heuristic_value += line_four(state, (x, y), player, (1, 0))  # --
            heuristic_value += line_four(state, (x, y), player, (0, 1))  # |
            heuristic_value += line_four(state, (x, y), player, (1, 1))  # /
            heuristic_value += line_four(state, (x, y), player, (1, -1))  # \

            heuristic_value -= line_four(state, (x, y), enemy, (1, 0))

    return heuristic_value
