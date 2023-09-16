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
            self.position = [0,3]

        else:
            self.representation = [np.array(TETROMINO[type][1])]
            self.position = [0,3]


class Board():
    def __init__(self):
        self._status = np.array([[0]*10]*24) # Array holding current state of every cell, 1 means there is a block 
        self.elements = []
    
    def spawn_block(self, block):
        self.elements.append(block)
        block_arr = block.representation

        if block._type != "I":
            self._status[block.position[0]][block.position[1]:block.position[1]+3] = block_arr[0]
            self._status[block.position[0] + 1][block.position[1]:block.position[1]+3] = block_arr[1]

        else:

            self._status[block.position[0]][block.position[1]:7] = block_arr[0]


    def move_block_down(self):
        self.elements[-1].position[0] += 1
        self.refresh_position()

    def refresh_position(self):
        block = self.elements[-1]
        block_arr = block.representation

        if block._type != "I":
            self._status[block.position[0]][block.position[1]:block.position[1]+3] = block_arr[0]
            self._status[block.position[0] + 1][block.position[1]:block.position[1]+3] = block_arr[1]

        else:

            self._status[block.position[0]][block.position[1]:7] = block_arr[0]

        
if __name__ == "__main__":
    board = Board()
    T_block = Block("T")
    board.spawn_block(T_block)
    board.move_block_down()
    print(board._status)
    print(board.elements[-1].position)