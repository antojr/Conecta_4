# coding=utf-8
from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
import heu as heuristic
import games
import heu

# game = games.TicTacToe(h=3,v=3,k=3)
game = games.ConnectFour()

state = game.initial
dificultad = int(-1)

def play(state, player):
    while True:
        if player == 'X':
            print ("Jugador a mover:", game.to_move(state))

        else:
            print ("Jugador a mover:", game.to_move(state))


        game.display(state)

        if player == 'O':
            col_str = raw_input("Movimiento: ")
            coor = int(str(col_str).strip())
            x = coor
            y = -1
            legal_moves = game.legal_moves(state)
            for lm in legal_moves:
                if lm[0] == x:
                    y = lm[1]

            state = game.make_move((x, y), state)
            player = 'X'
        else: # Máquina.
            print("\nThinking...")
            # move = games.minimax_decision(state, game)
            # move = games.alphabeta_full_search(state, game)
            # state, game, d=4, cutoff_test=None, eval_fn=None, player='X', dificultad=2
            if dificultad == 2:
                move = games.alphabeta_search(state, game, d=3, eval_fn=heu.run_heuristic, player=player,
                                              dificultad=dificultad)
            if dificultad == 1:
                move = games.alphabeta_search(state, game, d=2, eval_fn=heu.run_heuristic, player=player,
                                              dificultad=dificultad)
            if dificultad == 0:
                move = games.alphabeta_search(state, game, d=1, eval_fn=heu.run_heuristic, player=player,
                                              dificultad=dificultad)
            state = game.make_move(move, state)
            player = 'O'
        print("-------------------")
        if game.terminal_test(state):
            game.display(state)
            print("Final de la partida")
            break

while True:
    string_input = raw_input(
        "Escoja la dificultad con la que desea enfrentarse a la máquina, fácil(0), medio(1) o difícil(2)")
    dificultad = int(string_input)
    if dificultad == int(1):
        break
    if dificultad == int(0):
        break
    if dificultad == int(2):
        break

player = ''
while True:
    string_input = raw_input("¿Quién desea que empiece, máquina('1') o el jugador('2')?")
    if string_input == '1':
        player = 'X'
        break
    if string_input == '2':
        player = 'O'
        break

if player == 'X':
    play(state, 'X')
if player == 'O':
    play(state, 'O')
