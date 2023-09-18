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

def test_move_down():
    board = Board()
    T_block = Block("T")
    board.spawn_block(T_block)
    board.move_block_down()
    board.move_block_down()  
    board.move_block_down()

    first_status = board._status[3] == np.array([0, 0, 0, 0, 1, 0, 0, 0, 0, 0]) 
    second_status = board._status[4] == [0, 0, 0, 1, 1, 1, 0, 0, 0, 0]

    correct = False

    correct = all(first_status)
    correct = all(second_status)

    assert correct and T_block.position == [3,3]

def test_move_left():
    board = Board()
    T_block = Block("T")
    board.spawn_block(T_block)
    board.move_block_down()
    board.move_left()

    first_status = board._status[1] == np.array([0, 0, 0, 1, 0, 0, 0, 0, 0, 0]) 
    second_status = board._status[2] == [0, 0, 1, 1, 1, 0, 0, 0, 0, 0]

    correct = False

    correct = all(first_status)
    correct = all(second_status)

    assert correct and T_block.position == [1,2]

def test_move_left():
    board = Board()
    T_block = Block("T")
    board.spawn_block(T_block)
    board.move_block_down()
    board.move_right()

    first_status = board._status[1] == np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0]) 
    second_status = board._status[2] == [0, 0, 0, 0, 1, 1, 1, 0, 0, 0]

    correct = False

    correct = all(first_status)
    correct = all(second_status)

    assert correct and T_block.position == [1,4]

    board.move_right()
    board.move_right()
    board.move_right()
    board.move_right()

    assert correct and T_block.position == [1,7]