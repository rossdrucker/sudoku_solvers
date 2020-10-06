"""
@author: Ross Drucker
"""
import math

def check_square(n):
    """
    Check if a number is a perfect square to make the board. If it is,
    return True (so that the board creator will create a board), and
    the size of the board (in case it has changed since initial input)
    """
    valid_n = False
    
    # Make sure n is a number
    while not valid_n:
        try:
            # Find the square root of n
            root = math.sqrt(n)
            
            # Find the integer value of n + .5. If this number squared is n,
            # then n must be a perfect square
            if int(root + 0.5) ** 2 == n:
                return True, n
            else:
                return False, n
            
        except TypeError:
            print(f'{n} is not a real number\n')
            n = int(input('Select a size for the board: '))
    
def create_blank_board(size = 9, speak = False):
    """
    Function to create a blank board of size n x n. Since a standard
    sudoku board is typically 9x9, this will be the default.
    
    However, since the general case of a sudoku solution algorithm
    should be able to handle m^2 x m^2, this will allow the program
    to be more flexible.
    
    In this context, a valid board will means that the board follows
    the constraint m^2 = n, and m and n must both be integer numbers
    (i.e. the size n must be a perfect square).
    """
    
    # Check that we will have a viable number of characters (less than 61)
    valid_size = False
    while not valid_size:
        if size > 61:
            print(f'{size} is too big to make a board\n')
            size = int(input('Select different size board: '))
        else:
            valid_size = True
            
    # Assume the board desired is not valid
    valid_size = False
    
    # Check the input size
    while not valid_size:
        # See if the input size is a perfect square
        valid_size, size = check_square(size)
        if valid_size:
            # If so, announce that board is being made
            if speak:
                print(f'Making board of size {size} x {size}')
        else:
            # If not, prompt user to input a new board size. Must be an int
            try:
                print(f'{size} is not a viable board size\n')
                size = int(input('Select different size board: '))
            except ValueError:
                # If user enters something other than an int, alert user and
                # require different size to be supplied
                print(f'{size} is not a number.\n')
                size = int(input('Select different size board: '))
            except TypeError:
                # If something other than an int is supplied at the onset,
                # alert user and require different size to be supplied
                print(f'{size} is not a number.\n')
                size = int(input('Select different size board: '))
            
    # Create a board if 
    board = [[0] * size] * size
    
    return board

def get_characters_to_use(size = 9):
    """
    Function to get characters that will be used in gameplay
    """
    valid_size = False
    
    while not valid_size:
        if size > 61:
            valid_size = False
            print(f'{size} is too big. oard cannot be bigger than 61x61')
            size = int(input('Select different size board: '))
        else:
            valid_size = True
    
    # If the size of the board is less than 10, get the numbers 1-9
    if size <= 9:
        i = 0
        chars = []
        while i < size:
            chars.append(chr(49 + i))
            i += 1
    
    # If the size of the board is bigger than 9 and less than 35, add the
    # capital letters to fill the remaining necessary possible characters
    if size >= 9 and size <= 35:
        i = 0
        chars = []
        while i < 9:
            chars.append(chr(49 + i))
            i += 1
            
        i = 0
        while len(chars) != size and i <= 25:
            chars.append(chr(65 + i))
            i += 1
            
    # If the size of the board is bigger than 35 and less than 51, add the
    # lower case letters to fill the remaining necessary possible characters
    if size >= 35 and size <= 61:
        i = 0
        chars = []
        while i < 9:
            chars.append(chr(49 + i))
            i += 1
            
        i = 0
        while i <= 25:
            chars.append(chr(65 + i))
            i += 1
        
        i = 0
        while len(chars) != size and i <= 25:
            chars.append(chr(97 + i))
            i += 1
    
    return chars

if __name__ == '__main__':
    # Module checks
    create_blank_board()
    create_blank_board(8)
    create_blank_board('a')
    get_characters_to_use()
    get_characters_to_use(25)
    get_characters_to_use(61)