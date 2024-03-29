import numpy as np
import os
from random import choice

try:
    LOG_FILE = open("./log/colision_log.txt", "w")
    LOG_FILE.write("EVERY COLLISION FOR LAST GAME PLAYED\n")
finally:
    pass # Some handle for not able to achive log file


TETROMINO = {"I": [[0,0,0,0],[1,1,1,1]], 
             "J": [[1,0,0,0],[1,1,1,0]],
             "L": [[0,0,1,0],[1,1,1,0]],
             "O": [[0,1,1,0],[0,1,1,0]],
             "S": [[0,1,1,0],[1,1,0,0]],
             "T": [[0,1,0,0],[1,1,1,0]],
             "Z": [[1,1,0,0],[0,1,1,0]]} # Types of blocks in Tetris represented by 2x4 np array 

class Block():
    """
    Definition for blocks used in game. All of the blocks are represented by Tetromino.
    
    type - this variable is used to define type of the block used
    """
    def __init__(self, type="I"):
        self._type = type

        # We are using the smallest type of representation as we can, so in "I" type of block
        # we simply use only one dimensional array.
        # Also we want to shrik the array for 2x3 type of blocks. 
        if type != "I" and type != "O":
            self.representation =[np.array(TETROMINO[type][0][0:3]), np.array(TETROMINO[type][1][0:3])]
        elif type == "O":
            self.representation =[np.array(TETROMINO[type][0][1:3]), np.array(TETROMINO[type][1][1:3])]
        else:
            self.representation = [np.array(TETROMINO[type][1])]


        self.position = [0,3]

        self.x=self.position[0]
        self.y=self.position[1]
        
        self.width = len(self.representation[0])
        self.height = len(self.representation)

    def rotate(self):
        """
        Rotate block using transposition
        """
        to_transpose = self.representation 
        self.representation  = (np.array(to_transpose).T).tolist()

        self.width = len(self.representation[0])
        self.height = len(self.representation)


class Board():
    def __init__(self):
        """
        Representing a board on witch game in perfomed. 
        Contains:
        _status - 2D np.array that shows 1 if this place is occupied and 0 if not
        elements - list of elements (blocks) that are on the board
        """
        self._status = np.array([[0]*10]*24) # Array holding current state of every cell, 1 means there is a block 
        self.elements = []
    
    def calculate_score(self):
        return np.sum(self._status)

    def spawn_block(self, block):
        self.elements.append(block)
        block_arr = block.representation

        for i in range(block.height):
            self._status[block.x +i][block.y:block.y+block.width] = block_arr[i]


    def move_block_down(self):
        last_elem = self.elements[-1]
        if (last_elem.x + last_elem.height) <= (len(self._status) -1): # Assertion from hitting floor
            self.clear_elem()
            # print(self._status)
            self.elements[-1].x += 1
            self.refresh_position()

            is_touched=False

            for i in self._status:
                for j in i:
                    if j >= 2:
                        is_touched=True # After colision try to write it to logs
                        try:
                            LOG_FILE.write("\n---------------------------------------------\n")
                            LOG_FILE.write(str(self._status))
                        finally:
                            pass # Some handle for not able to achive log file
                        
                        self.clear_elem()
                        self.elements[-1].x -= 1
                        self.refresh_position()

            if is_touched:
                for i in self.elements:
                    self.clear_elem(i)
                    self.refresh_position(i,addition=False)

            return not is_touched

        return False


    def clear_elem(self, block=None):
        """
        Delete element from _status array but NOT FROM LIST OF ELEMENTS.
        You should use this func to delete one of the elements from screen but not from elements at all. 
        If block is not provided it clears last elem from list.
        """
        if block == None:
            block = self.elements[-1]

        for i in range(block.height):
            for j in range(block.width):
                if block.representation[i][j] == 1:
                    self._status[block.x +i][block.y +j] = 0




    def refresh_position(self, block=None, addition=True):
        """
        Should be called after "clear_elem" function when changes are already created.
        If block is not provided it uses last elem from list.
        You can change behaviour of this func, if it should add block representation to 
        current status array, or just change values.
        You can do it by changing "addition" parameter 
        """
        if block == None:
            block = self.elements[-1]
        
        block_arr = block.representation
        try:    
            if addition:
                for i in range(block.height):
                    for j in range(block.width):
                        self._status[block.x +i][block.y + j] += block_arr[i][j]
            else:
                for i in range(block.height):
                    self._status[block.x +i][block.y:block.y+block.width] = block_arr[i]

            block.position = [block.x, block.y]       
        except:
            return 1 # Cannot rotate

    def move_left(self):
        self.clear_elem()
        if (self.elements[-1].y - 1) >= 0:  # Assertion from hitting wall
            self.elements[-1].y -= 1
            self.refresh_position()
        print(self.elements[-1].representation)
    def move_right(self):
        self.clear_elem()
        if (self.elements[-1].y + 1) <= (len(self._status[0]) - len(self.elements[-1].representation[0])):  # Assertion from hitting wall
            self.elements[-1].y += 1
            self.refresh_position()

    def rotate(self):
        self.clear_elem()
        self.elements[-1].rotate()
        if (self.refresh_position()): #Caanot rotate, try again to not hit wall
            self.elements[-1].rotate()

if __name__ == "__main__":
    board = Board()
    T_block = Block("I")
    board.spawn_block(T_block)

    while True:
        print(board._status)
        move = input()

        os.system('clear') # Fix later, works only for Linux 
        
        if not board.move_block_down():
            random_key = choice(list(TETROMINO.keys())) 
            board.spawn_block(Block(random_key))
            print(board.elements[-1].representation)

        if move == "d":
            board.move_right()
        
        elif move == "a":
            board.move_left()

        elif move == "q":
            board.clear_elem()
            board.elements[-1].rotate()
            board.refresh_position()
