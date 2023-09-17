from main import Block, Board, TETROMINO
import numpy as np

def test_spawn():
    board = Board()
    T_block = Block("T")
    board.spawn_block(T_block)
    first_status = board._status[0] == np.array([0, 0, 0, 0, 1, 0, 0, 0, 0, 0]) 
    second_status = board._status[1] == [0, 0, 0, 1, 1, 1, 0, 0, 0, 0]
    correct = False

    correct = all(first_status)
    correct = all(second_status)

    assert correct