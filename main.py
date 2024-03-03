# Imports
import numpy  # for arrays
from colorama import Style, Fore  # for coloring
import os  # for clearing the screen


# Gameboard class used for the connect4 board
class gameBoard:
    
    # takes in columns and rows to create the game
    def __init__(self, COLUMNS, ROWS):
        self.COLUMNS = COLUMNS
        self.ROWS = ROWS
        
        self.EMPTY = " - "  # what the empty square looks like
        self.X = Fore.RED + " x "  # what the x looks like
        self.O = Fore.YELLOW + " o "  # what the o looks like
        
        self.board = self.create_blank(self.ROWS, self.COLUMNS)  # create a blank board of zeros
        self.board = self.convert_empty(self.board, self.EMPTY)  # convert the zeros to empty
    
    # creates a blank board of zeros
    @staticmethod
    def create_blank(ROWS, COLUMNS):
        return numpy.zeros((ROWS, COLUMNS))
    
    # displays the board
    @staticmethod
    def display(board):
        for y in board:
            for x in y:
                print(Style.BRIGHT + x + Fore.WHITE, end = "")  # print out each index with Style.BRIGHT
            print()
        
        for i in range(1, len(board[0]) + 1):
            print(Fore.BLUE + " " + str(i) + " " + Fore.WHITE, end="")  # print out each number
        print()

    # converts a zeros board to a board with the empty string in it
    @staticmethod
    def convert_empty(board, EMPTY):
        return numpy.where(board == 0, EMPTY, board)
    
    # inserts a piece into the board
    def insert_to_column(self, symbol, column):
        for i in reversed(range(0, self.ROWS)):
            if self.board[i][column] == self.EMPTY:
                self.board[i][column] = symbol
                break
    
    # check who wins the game
    def check_win(self):
        
        # First check horizontal
        for row in self.board:
            stringRow = "".join(row)  # create a string with all the row data
            
            if "".join([self.X for i in range(4)]) in stringRow: # if xxxx is anywhere in the string
                return True
            
            if "".join([self.O for i in range(4)]) in stringRow: # if oooo is anywhere in the string
                return True
            
        # Second check vertical
        verticals = []
        for column in range(self.COLUMNS):  # get the index of which vertical 
            vert = []
            
            for row in self.board:  # for every row add the vertical index for the row
                vert.append(row[column])
                
            verticals.append(vert)
                
        for vert in verticals:
            stringRow = "".join(vert)
            
            if "".join([self.X for i in range(4)]) in stringRow:
                return True
            
            if "".join([self.O for i in range(4)]) in stringRow:
                return True
            
        # Third check diagonal
        diagonals = []
        
        # too complicated to explain XD | I wrote it and I don't even understand it
        for row in range(self.ROWS):
            for column in range(self.COLUMNS):
                d = []
                for row2 in range(self.ROWS - row):
                    if column + row2 + row < self.COLUMNS:
                        d.append(self.board[row2 + row][column + row2 + row])
                diagonals.append(d)
                
        for row in range(self.ROWS):
            for column in range(self.COLUMNS):
                d = []
                for row2 in range(self.ROWS - row):
                    if column - row2 - row < self.COLUMNS:
                        d.append(self.board[row2 + row][column - row2 - row])
                diagonals.append(d)

        for dia in diagonals:
            stringRow = "".join(dia)
            
            if "".join([self.X for i in range(4)]) in stringRow:
                return True
            
            if "".join([self.O for i in range(4)]) in stringRow:
                return True

        return False


def main():
    # create the board and line stuff
    connect4_board = gameBoard(7, 6)
    line = "".join(["---" for i in range(connect4_board.COLUMNS)])
    player = 1
    
    while True:
        answer = "BLANK"  # make sure answer is not in the condition
        
        while answer not in [str(i) for i in range(1, connect4_board.COLUMNS + 1)]:  # make sure the answer is always 1-7
            os.system('clear')
            print(f"{Style.BRIGHT}Welcome to {Fore.BLUE}CONNECT 4{Fore.WHITE}!")
            
            print()
            print(line)
            connect4_board.display(connect4_board.board)
            print(line)
            print()
            
            print(f"{Fore.RED if player == 1 else Fore.YELLOW}Player {player}{Fore.WHITE} it's your turn!")  # yellow if it's player 2 | red if it's player 1
            print(f"Type a number from {Fore.BLUE}1-7{Fore.WHITE} to place your piece")
            
            answer = input(">>> ")  # get input
        
        connect4_board.insert_to_column(connect4_board.X if player == 1 else connect4_board.O, int(answer) - 1)  # insert the right piece
        won = connect4_board.check_win()
        
        if won != False:  # win condition
            os.system('clear')
            print(f"{Style.BRIGHT}Welcome to {Fore.BLUE}CONNECT 4{Fore.WHITE}!")
            
            print()
            print(line)
            connect4_board.display(connect4_board.board)
            print(line)
            print()
            
            print(f"{Fore.RED if player == 1 else Fore.YELLOW}Player {player}{Fore.WHITE} WON!")
            
            break
            
        player = 2 if player == 1 else 1

if __name__ == "__main__":
    main()
