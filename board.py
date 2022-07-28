



TAILLE_PLATEAU = 5
BOARD_ONE = 1
BOARD_TWO = 2


class BOARD:
    def __init__(self):
        self.__board_P1 = []
        self.__board_P2 = []
        
    
    def build_board_p1(self):
        for i in range(TAILLE_PLATEAU):
            elem = []
            for j in range(TAILLE_PLATEAU):
                elem.append(0)
            self.__board_P1.append(elem)
        return self.__board_P1
    
    def build_board_p2(self):
        for i in range(TAILLE_PLATEAU):
            elem = []
            for j in range(TAILLE_PLATEAU):
                elem.append(0)
            self.__board_P2.append(elem)
        return self.__board_P2
    
    def affiche_board_p1(self):
        print("  " + " -"*TAILLE_PLATEAU + "  " + " -"*TAILLE_PLATEAU)
        for i in range(TAILLE_PLATEAU):
            print(" | ", end="")
            for j in range(TAILLE_PLATEAU):
                char = self.affiche_place((i, j), BOARD_ONE)
                print(char, end=" ")
            self.affiche_board_p2(i, BOARD_TWO)
    
    def affiche_board_p2(self, i, BOARD_TWO):
        print("| ",end="")
        for j in range(TAILLE_PLATEAU):
            char = self.affiche_place((i, j), BOARD_TWO)
            print(char, end=" ")
        print("| ")
        if j == TAILLE_PLATEAU - 1 and i == TAILLE_PLATEAU - 1:
            print("  " + " -"*TAILLE_PLATEAU + "  " + " -"*TAILLE_PLATEAU)
            print(" "*TAILLE_PLATEAU + " p1 " + " "*2*TAILLE_PLATEAU + "p2")
        
    def affiche_place(self, place, board):
        if board == 1:
            return self.__board_P1[place[0]][place[1]]
        else:
            return self.__board_P2[place[0]][place[1]]
    
    def set_board(self, place, modif, board):
        if board == 1:
            self.__board_P1[place[0]][place[1]] = modif
        else:
            self.__board_P2[place[0]][place[1]] = modif
            
    def taille_p(self):
        #print("%%%%",len(self.__board_P1))
        return len(self.__board_P1)
    
if __name__ == "__main__":
    B = BOARD()
    B.build_board_p1()
    B.build_board_p2()
    B.affiche_board_p1()
