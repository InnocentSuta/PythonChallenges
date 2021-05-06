from player import HumanPlayer,RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]: #printing the board
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3,(j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        
        # moves = []
        # for (i , spot) in enumerate(self.board):
        #     if spot == ' ': 
        #         moves.append(i)
        # return moves
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_Squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        #check winner in a row
        row_index = square // 3
        row = self.board[row_index * 3: (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        #check column
        col_index = square % 3
        column = [self.board[col_index + i * 3] for i in range(3)]
        if all(spot == letter for spot in column):  
            return True
        #check winner in diagonal  
        if square % 2 == 0:
            diagonal1 = [self.board[1] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[1] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False
        
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
            
    letter = 'x'
    
    while game.empty_squares():
        if letter == '0':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game) 
        
        if game.make_move(square,letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print(letter + 'wins!')
                return letter
            letter = 'o' if letter == 'x' else 'x'
    if print_game:
        print('It\'s a tie')


if __name__ == '__main__':
    x_player = HumanPlayer('x')
    o_player = RandomComputerPlayer('o')
    tictac = TicTacToe()
    play(tictac, x_player,o_player,print_game=True)