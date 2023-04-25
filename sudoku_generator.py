import math,random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = list[]
        self.box_length = math.sqrt(self.row_length)

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''

    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        print(self.board)

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
        self.row = row
        self.num = num
        # Added a for statement which should iterate through each number in the specified row of the board.
        for i in self.board[self.row]:
            # If the number is already in that row, return False
            if self.num == i:
                return False
        # Otherwise return True
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num):
        self.col = col
        self.num = num
        # Here i is a row in the board, this iterates through each row.
        for i in self.board:
            # This if statement checks if the given number matches the number in the self.col position of each row.
            # Returns false if the number is already anywhere in that column.
            if self.num == i[self.col]:
                return False
        # Otherwise returns true.
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        # Sets the row and column indices for the box
        row_indices = range(row_start, row_start + 3)
        col_indices = range(col_start, col_start + 3)
        # Gets the values of the cells in the given box, and places them in a list.
        box_values = [self.board[row][col] for row in row_indices for col in col_indices]
        # Checks if the number is already in the box, if so it returns False
        if num in box_values:
            return False
        # Otherwise returns True
        else:
            return True
    
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num):
        self.row = row
        self.col = col
        self.num = num

        # Chooses which row to begin drawing the box, based on the inputted row.
        if self.row >= 0 and self.row <= 2:
            self.row_start = 0
        elif self.row >= 3 and self.row <= 5:
            self.row_start = 3
        elif self.row >= 6 and self.row <= 8:
            self.row_start = 6

        # Chooses which column to begin drawing the box, based on the inputted column.
        if self.col >= 0 and self.col <= 2:
            self.col_start = 0
        elif self.col >= 3 and self.col <= 5:
            self.col_start = 3
        elif self.col >= 6 and self.col<= 8:
            self.col_start = 6

        # If the row, column, and box are valid, returns True, else False.
        if self.valid_in_row(self.row, self.num) and self.valid_in_col(self.col, self.num) \
                and self.valid_in_box(self.row_start, self.col_start, self.num):
            return True
        else:
            return False

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    def fill_box(self, row_start, col_start):
        pass
    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        pass

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        pass

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board
    sudoku.remove_cells()
    board = sudoku.get_board
    return board


class Cell:
    '''
    This class represents a single cell in the Sudoku board
    There are 81 Cells in a Board.
    '''
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        '''
        Constructor for the Cell class
        '''
    def set_cell_value(self, value):
        pass
        '''
        setter for this cell's value
        '''

    def set_sketched_value(self, value):
        pass
        '''
        Setter for this cell’s sketched value
        '''

    def draw(self):
        pass
        '''
        Draws this cell, along with the value inside it.
        If this cell has a nonzero value, that value is displayed.
        Otherwise, no value is displayed in the cell.
        The cell is outlined red if it is currently selected
        '''

class Board:
    def __init__(self, width, height, screen, difficulty):
        pass
        '''
        Constructor for the Board class.
        screen is a window from PyGame.
        difficulty is a variable to indicate if the 
        user chose easy, medium, or hard. 
        '''
    def draw(self):
        pass
        '''
        Draws an outline of the Sudoku grid, with 
        bold lines to delineate the 3x3 boxes.
        Draws every cell on this board.
        '''

    def select(self,row,col):
        pass
        '''
        Marks the cell at (row, col) in the board 
        as the current selected cell.
        Once a cell has been selected, the user can 
        edit its value or sketched value. 
        '''

    def click(self,x,y):
        pass
        '''
        If a tuple of (x, y) coordinates is within 
        the displayed board, this function returns 
        a tuple of the (row, col)
        of the cell which was clicked. Otherwise, 
        this function returns None. 
        '''

    def clear(self):
        pass
        '''
        Clears the value cell. Note that the user can 
        only remove the cell values and sketched value that are
        filled by themselves.
        '''

    def sketch(self,value):
        pass
        '''
        Sets the sketched value of the current selected cell
        equal to user entered value.
        It will be displayed at the top left corner of the 
        cell using the draw() function.
        '''

    def place_number(self,value):
        pass
        '''
        Sets the value of the current selected cell 
        equal to user entered value.
        Called when the user presses the Enter key.
        '''

    def reset_to_origional(self):
        pass
    '''
    Reset all cells in the board to their original values
    (0 if cleared, otherwise the corresponding digit). 
    '''

    def is_full(self):
        pass
    '''
    returns a boolean value indicating whether the board is full or not
    '''

    def update_baord(self):
        pass
        '''
        Updates the underlying 2D board with the values in all cells. 
        '''

    def find_empty(self):
        pass
        '''
        Finds an empty cell and returns its row and col as a tuple (x, y). 
        '''

    def check_board(self):
        pass
        '''
        Check whether the Sudoku board is solved correctly. 
        '''

def main():
    ''''
    main function will run here
    '''


if __name__ == '__main__':
    main()