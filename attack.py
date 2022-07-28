

from boot import BOOT_player
from board import BOARD


class ATTACK:
    def __init__(self, board, boot):
        self.__board = board
        self.__boot = boot
        
        
        
    def attack(self, cpt_player):
        if cpt_player == 1:
            print("attaque du joueur", cpt_player)
            cpt_player = 2
        else:
            cpt_player : 1
            print("attaque du joueur", 2)
        pos_attacked = self.__boot.select_emplacement()
        if self.__board.affiche_place(pos_attacked, cpt_player) == "*":
            print()
            print("bateau toucher")
            self.__board.set_board(pos_attacked, "#", cpt_player)
        elif self.__board.affiche_place(pos_attacked, cpt_player) == "#":
            print()
            print("position déjà attaquer.")
        else:
            print()
            print("pas de bateau toucher")
            self.__board.set_board(pos_attacked, "/", cpt_player)
        self.__board.affiche_board_p1()
        
            
        