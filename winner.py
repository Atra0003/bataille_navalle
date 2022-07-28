


class WINNER:
    def __init__(self, board):
        self.__board = board
        
        
    
    def win(self, cpt_player):
        verification = True
        cpt_player += 1
        cpt_player %= 2
        for i in range(self.__board.taille_p()):
            for j in range(self.__board.taille_p()):
                if cpt_player == 1:
                    char = self.__board.affiche_place((i, j), cpt_player)
                else:
                    char = self.__board.affiche_place((i, j), cpt_player)
                
                if char == "*":
                    verification = None
                    
        return verification
                
                

                    
        