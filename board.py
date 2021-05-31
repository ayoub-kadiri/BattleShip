class Board :
    cases = {}
    lettre = 'ABCDEFGHIJ'
    
    # fonction pour creer un dictionnaire {case : coordoones, touche ou pas}
    def __init__(self, x_start_pos): 
        for i in range(10):
            for j in range(1,11):
                cases[lettre[i]+str(j)] = () #tuples [rect,frappé]
    
    # fonction pour rendre la case comme toucher
    def update(self, case):
        cases[case][1] = True
        
    # fonction pour dessiner la grille de jeu
    def drawGrid():
        pass
