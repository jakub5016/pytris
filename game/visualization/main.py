import pygame
from .vis_classes import BLOCK_SIZE, drawingBlock, drawingBoard

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

running = True
while running:
    screen.fill(BG_COLOR)
    block.draw(surface=screen, color=COLORS[1])
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(100)

pygame.quit()