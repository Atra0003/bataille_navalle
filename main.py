

from board import BOARD
from boot import BOOT_player

def main():
    # Création et affichage du plateau.
    Board.build_board_p1()
    Board.build_board_p2()
    Board.affiche_board_p1()
    
    ### Positionnement des bâteau. 
    
    for i in range(2):
        boot_1 = B.boot_1()
        boot_2 = B.boot_2()
        #boot_3 = B.boot_3()
        #boot_4 = B.boot_4()
        
        select_boot_1 = B.select_boot(boot_1, 1)
        positionnement_boot1 = B.select_emplacement()
        B.placement(select_boot_1, positionnement_boot1, i+1)
        Board.affiche_board_p1()
        
        select_boot_2 = B.select_boot(boot_2, 2)
        positionnement_boot2 = B.select_emplacement()
        B.placement(select_boot_2, positionnement_boot2, i+1)
        Board.affiche_board_p1()
        
        
        #select_boot_3 = B.select_boot(boot_3, 3)
        #positionnement_boot3 = B.select_emplacement()
        #B.placement(select_boot_3, positionnement_boot3, i+1)
        
        #select_boot_4 = B.select_boot(boot_4, 4)
        #positionnement_boot4 = B.select_emplacement()
        #B.placement(select_boot_4, positionnement_boot4, i+1)
        
        #Board.affiche_board_p1()

if __name__ == "__main__":
    Board = BOARD()
    B = BOOT_player(Board)

    main()
    
    
    


