import numpy as np
import os

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
        if (self.elements[-1].position[0] + 1) <= (len(self._status) - len(self.elements[-1].position)): # Assertion from hitting floor
            self.clear_last_elem()
            self.elements[-1].position[0] += 1
            self.refresh_position()

            is_touched=False
            for i in self._status:
                for j in i:
                    if j >= 2:
                        is_touched=True
                        self.clear_last_elem()
                        self.elements[-1].position[0] -= 1
                        self.refresh_position()

            # if is_touched:
            #     for i in self.elements:
            #         self.refresh_position(i)

            return True

        return False


    def clear_last_elem(self):
        block = self.elements[-1]

        if block._type != "I":
            self._status[block.position[0]][block.position[1]:block.position[1]+3] = 0
            self._status[block.position[0] + 1][block.position[1]:block.position[1]+3] = 0

        else:

            self._status[block.position[0]][block.position[1]:7] = 0


    def refresh_position(self, block=None):
        if block == None:
            block = self.elements[-1]
        block_arr = block.representation

        if block._type != "I":
            self._status[block.position[0]][block.position[1]:block.position[1]+3] += block_arr[0]
            self._status[block.position[0] + 1][block.position[1]:block.position[1]+3] += block_arr[1]

        else:

            self._status[block.position[0]][block.position[1]:7] += block_arr[0]

    def move_left(self):
        self.clear_last_elem()
        if (self.elements[-1].position[1] - 1) >= 0:  # Assertion from hitting wall
            self.elements[-1].position[1] -= 1
            self.refresh_position()
        
    def move_right(self):
        self.clear_last_elem()
        if (self.elements[-1].position[1] + 1) <= (len(self._status[0]) - len(self.elements[-1].representation[0])):  # Assertion from hitting wall
            self.elements[-1].position[1] += 1
            self.refresh_position()

if __name__ == "__main__":
    board = Board()
    T_block = Block("T")
    board.spawn_block(T_block)

    while True:
        print(board._status)
        move = input()

        os.system('clear') # Fix later, works only for Linux 

        if move == "d":
            board.move_right()
        
        elif move == "a":
            board.move_left()

        if not board.move_block_down():
            board.spawn_block(Block("T"))
        