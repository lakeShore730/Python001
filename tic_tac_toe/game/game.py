class TicTocToe:
    def __init__(self):
        self.board = [" " for _ in range(8)]
        self.current_winner = None # keep track of winner!    
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
            
