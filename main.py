import numpy as np

TETROMINO = {"I": [[0,0,0,0],[1,1,1,1]], 
             "J": [[1,0,0,0],[1,1,1,0]],
             "L": [[0,0,0,1],[1,1,1,0]],
             "O": [[0,1,1,0],[0,1,1,0]],
             "S": [[0,1,1,0],[1,1,0,0]],
             "T": [[0,1,0,0],[1,1,1,0]],
             "Z": [[1,1,0,0],[0,1,1,0]]} # Types of blocks in Tetris represented by 2x4 np array 

class Block():
    def __init__(self, type="I"):
        self._type = type

        if type != "I":
            self.representation = [np.array(TETROMINO[type][0][0:3]), np.array(TETROMINO[type][1][0:3])]
        else:
            self.representation = [np.array(TETROMINO[type][1])]

class Board():
    def __init__(self):
        self._status = np.array([[0]*10]*24) # Array holding current state of every cell, 1 means there is a block 

    def spawn_block(self, block_arr):
        if len(block_arr) > 1: # Other than "I" type
            print(self._status[0])
        else:

            self._status[0][0:4] = block_arr[0]


    def move_block():
        pass
        
if __name__ == "__main__":
    board = Board()
    T_block = Block("I")
    board.spawn_block(T_block.representation)
    print(board._status)