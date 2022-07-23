
from board import BOARD


class BOOT_player:
    def __init__(self, board):
        self.board = board
    

    def boot_1(self):
        self.boot_1_v =[["*","*","*"],
                       ["*","*","*"],
                       [0,"*",0],
                       ["*","*","*"],
                       ["*","*","*"]]
        
        
        self.boot_1_h = [["*","*",0,"*","*"],
                         ["*","*","*","*","*"],
                         ["*","*",0,"*","*"]]
        
        return [self.boot_1_v, self.boot_1_h]
        
        
    def boot_2(self):
        self.boot_2_v = [[0,0,"*",0,0],
                         [0,"*",0,"*",0],
                         ["*","*",0,"*","*"],
                         [0,"*",0,"*",0],
                         [0,0,"*",0,0]]
        
        
        self.boot_2_h = [[0,0,"*",0,0],
                         [0,"*","*","*",0],
                         ["*",0,0,0,"*"],
                         [0,"*","*","*",0],
                         [0,0,"*",0,0]]
        
        return [self.boot_2_v, self.boot_2_h]
        
        
    def boot_3(self):
        self.boot_3_v = [["*"],
                         ["*"],
                         ["*"],
                         ["*"],
                         ["*"]]
        
        self.boot_3_h = [["*","*","*","*","*"]]
        
        return [self.boot_3_v, self.boot_3_h]
        

    def boot_4(self):
        self.boot_4_v = [[0,"*",0,"*",0],
                         [0,"*",0,"*",0],
                         ["*","*",0,"*","*"],
                         ["*","*","*","*","*"]]
        
        self.boot_4_h = [["*","*",0,0],
                         ["*","*","*","*"],
                         ["*",0,0,0],
                         ["*","*","*","*"],
                         ["*","*",0,0]]


        return [self.boot_4_v, self.boot_4_h]


    def affiche_boot(self, schema):
        for elem in schema:
            for j in elem:
                print(j, end="")
            print()
                    
            
    def select_boot(self, list_boot, i):
        print()
        print("selection du baoot : " , i)
        print()
        print("entrer y pour selectionner votre")
        print("entrer l pour aller à droit")
        print("entrer i pour aller à gauche")
        
        print()
        self.affiche_boot(list_boot[0])
        print()
        choix = input("votre choix : ")
        print()
        cpt = 0
        while choix != "y":
            if choix == "l":
                idx = (cpt + 1) % len(list_boot)
                self.affiche_boot(list_boot[idx])
                print()
                choix = input("votre choix : ")
            
            elif choix == "j":
                idx = (cpt - 1) % len(list_boot)
                self.affiche_boot(list_boot[idx])
                print()
                choix = input("votre choix : ")
            
            else:
                print("se caractère n'est pas valide")
                choix = input("votre choix : ")
            cpt += 1
        return list_boot[cpt]
    """
    def is_in_board(self, pos):
        pos_l = pos[0]
        pos_c = pos[1]
        if 0 <= pos[0] < 3 and 0 <= pos[1] < 3:
            return True
        else:
            return False
    
    def checking(self):
        ligne = int(input("entrer la ligne de la board : "))
        colonne = int(input("entrer la colonne de la board : "))
        
        self.is_in_board((ligne, colonne))
        
        while :
        return 

    """
    
    def positionnement(self, boot):
        #self.checking()
        print("A")
        for i in range(len(boot)):
            for j in range(len(boot[0])):
                char = boot[i][j]
                self.board.set_board((i, j), char)
                
                
    
    
if __name__ == "__main__":
    Board = BOARD()
    Board.build_board_p1()
    Board.build_board_p2()
    Board.affiche_board_p1()
    
    B = BOOT_player(Board)
    
    boot_1 = B.boot_1()
    boot_2 = B.boot_2()
    boot_3 = B.boot_3()
    boot_4 = B.boot_4()
    
    select_boot_1 = B.select_boot(boot_1, 1)
    select_boot_2 = B.select_boot(boot_2, 2)
    select_boot_3 = B.select_boot(boot_3, 3)
    select_boot_4 = B.select_boot(boot_4, 4)
    
    print(select_boot_1)
    #print(select_boot_2)
    #print(select_boot_3)
    #print(select_boot_4)
    





