class Board :
    cases = {}
    lettre = 'ABCDEFGHIJ'

    def __init__(self, x_start_pos):
        for i in range(10):
            for j in range(1,11):
                cases[lettre[i]+str(j)] = () #tuples [rect,frappé]
    
    def update(self, case):
        cases[case][1] = True