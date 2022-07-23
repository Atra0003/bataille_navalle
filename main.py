

from board import BOARD
from boot import BOOT_player




if __name__ == "__main__":
    Board = BOARD()
    Board.build_board_p1()
    Board.build_board_p2()
    Board.affiche_board_p1()
    
    B = BOOT_player(Board)
    
    boot_1 = B.boot_1()
    #boot_2 = B.boot_2()
    #boot_3 = B.boot_3()
    #boot_4 = B.boot_4()
    
    select_boot_1 = B.select_boot(boot_1, 1)
    #select_boot_2 = B.select_boot(boot_2, 2)
    #select_boot_3 = B.select_boot(boot_3, 3)
    #select_boot_4 = B.select_boot(boot_4, 4)
    
    print(select_boot_1)
    
    
    
    


