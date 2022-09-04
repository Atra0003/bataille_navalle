

from board import BOARD
from boot import BOOT_player
from winner import WINNER
from attack import ATTACK

def main():
    # Création et affichage du plateau.
    Board.build_board(1)
    Board.build_board(2)
    
    Board.build_board(3)
    Board.build_board(4)
    
    Board.affiche_board_p1()
    
    ### Positionnement des bâteau. 
    
    for i in range(2):
        print()
        print("PLACEMENT DU JOUEUR.", i)
        print()
        
        boot_1 = B.boot_1()
        #boot_2 = B.boot_2()
        #boot_3 = B.boot_3()
        #boot_4 = B.boot_4()
        
        select_boot_1 = B.select_boot(boot_1, 1)
        positionnement_boot1 = B.select_emplacement()
        B.placement(select_boot_1, positionnement_boot1, i+1)
        Board.affiche_board_p1()
        
        #select_boot_2 = B.select_boot(boot_2, 2)
        #positionnement_boot2 = B.select_emplacement()
        #B.placement(select_boot_2, positionnement_boot2, i+1)
        #Board.affiche_board_p1()
        
        
        #select_boot_3 = B.select_boot(boot_3, 3)
        #positionnement_boot3 = B.select_emplacement()
        #B.placement(select_boot_3, positionnement_boot3, i+1)
        
        #select_boot_4 = B.select_boot(boot_4, 4)
        #positionnement_boot4 = B.select_emplacement()
        #B.placement(select_boot_4, positionnement_boot4, i+1)
        print()
        print("PLACEMENT DU JOUEUR", i, "TERMINER.")
        print()
        
    # lANCEMENT DE LA PARTIE -->
    # ON JOUE SUR LES BOARD VISIBLE
    
    jeu()


def jeu():
    ret_win = None
    cpt_player = 1
    while ret_win == None:
        cpt_player %= 2
        
        if cpt_player == 1:
            ATT.attack(cpt_player)
            ret_win = WIN.win(cpt_player)
            
        else:
            ATT.attack(cpt_player)
            ret_win = WIN.win(cpt_player)
            
        if ret_win != None:
            print("victoire du joueur : ", cpt_player)
        cpt_player += 1
    
    
        
        

if __name__ == "__main__":
    Board = BOARD()
    B = BOOT_player(Board)
    WIN = WINNER(Board)
    ATT = ATTACK(Board, B)

    main()
    
    
    


