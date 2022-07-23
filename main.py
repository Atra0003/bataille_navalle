

from board import BOARD
from play_move import PlayMove
from winner import WINNER

def main():
    cpt = 0
    ret_win = None 
    while cpt < 9 and ret_win == None:
        if cpt % 2 == 0:
            print("j1")
        else:
            print("j2")
        PM.placement()
        if cpt >= 4:
            ret_win = W.win()
        if ret_win != None:
            if ret_win == "X" or ret_win == "x":
                print("*** victoire joueur 1 ***")
            else:
                print("*** victoire joueur 2 ***")
        cpt += 1


if __name__ == "__main__":
    T_BOARD = 3
    M = BOARD(T_BOARD)
    M.build_board()
    M.affiche_board()
    PM = PlayMove(M)
    W = WINNER(M)
    main()



