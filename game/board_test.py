from .main import Board, Block, TETROMINO
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

def test_move_right():
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


def test_colision():
    board = Board()
    block_1 = Block(type="I")
    block_1.position = [23, 0]
    block_1.x = 23
    block_1.y = 0

    block_2 = Block(type="T")
    block_2.position = [21, 4]
    block_2.x = 21
    block_2.y = 4



    board.spawn_block(block_1)
    board.spawn_block(block_2)

    assert board.move_block_down()
