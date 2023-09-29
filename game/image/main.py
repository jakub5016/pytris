import pygame
from .vis_classes import BLOCK_SIZE, drawingBlock, drawingBoard, drawingElement

GAME_WIDTH = 10 * BLOCK_SIZE
GAME_HEIGHT = 24 * BLOCK_SIZE
MENU_WIDHT = 100

SIZE = WINDTH, HEIGHT = GAME_WIDTH + MENU_WIDHT, GAME_HEIGHT
COLORS = [(38, 70, 83), (42, 157, 143), (233, 196, 106), (244, 162, 97), (231, 111, 81)]
BG_COLOR = COLORS[2]

pygame.init()
pygame.display.set_caption('PyTris')

screen = pygame.display.set_mode((WINDTH, HEIGHT))
font = pygame.font.Font('freesansbold.ttf', 32)
clock = pygame.time.Clock()

block = drawingBlock()
board = drawingBoard()
board.spawn_block(block=block)

# point = drawingElement()

running = True
while running:
    screen.fill(BG_COLOR)
    board.elements[-1].draw(surface=screen, color=COLORS[1])
    # point.draw(surface=screen, color=COLORS[4])
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    board.move_block_down()
    # points.y += 1
    # point.ref_pos()
    clock.tick(1)

pygame.quit()