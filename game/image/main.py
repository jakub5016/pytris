import pygame
from random import choice
from .vis_classes import BLOCK_SIZE, drawingBlock, drawingBoard, drawingElement
from ..main import TETROMINO
import time

GAME_WIDTH = 10 * BLOCK_SIZE
GAME_HEIGHT = 24 * BLOCK_SIZE
MENU_WIDHT = 150

SIZE = WINDTH, HEIGHT = GAME_WIDTH + MENU_WIDHT, GAME_HEIGHT
COLORS = [(38, 70, 83), (42, 157, 143), (233, 196, 106), (244, 162, 97), (231, 111, 81)]
BG_COLOR = COLORS[2]
FONT_SIZE = 20

pygame.init()
pygame.display.set_caption('PyTris')

screen = pygame.display.set_mode((WINDTH, HEIGHT))
font = pygame.font.Font('freesansbold.ttf', FONT_SIZE)
clock = pygame.time.Clock()
border_rect = pygame.Rect(GAME_WIDTH, 0, BLOCK_SIZE, GAME_HEIGHT)

block = drawingBlock()
board = drawingBoard()
board.spawn_block(block=block)
score = font.render(f'Score: {board.calculate_score()}', True, COLORS[4], BG_COLOR)
score_rect = score.get_rect()
score_rect.center = (GAME_WIDTH + BLOCK_SIZE + MENU_WIDHT/2, FONT_SIZE/2)

running = True
while running:
    screen.fill(BG_COLOR)
    
    # Score section
    score = font.render(f'Score: {board.calculate_score()}', True, COLORS[4], BG_COLOR)
    score_rect = score.get_rect()
    score_rect.center = (GAME_WIDTH + BLOCK_SIZE + MENU_WIDHT/2, FONT_SIZE/2)
    pygame.draw.rect(screen,COLORS[0],border_rect)
    screen.blit(score, score_rect)

    # Game sectioon
    for i in board.elements:
        i.draw(surface=screen, color=COLORS[1])
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                board.move_left()
            if event.key == pygame.K_RIGHT:
                board.move_right()
            if event.key == pygame.K_UP:
                board.rotate()

    if not board.move_block_down():
            if board.elements[-1].x == 0:
                break
            random_key = choice(list(TETROMINO.keys())) 
            board.spawn_block(drawingBlock(random_key))

    clock.tick(5)


font = pygame.font.Font('freesansbold.ttf', int(GAME_WIDTH/8))
score = font.render(f'You Lose Score: {board.calculate_score()}', True, COLORS[4])
score_rect = score.get_rect()
score_rect.center = ((GAME_WIDTH+MENU_WIDHT)/2, GAME_HEIGHT/2)
screen.blit(score, score_rect)
pygame.display.update()
time.sleep(5)
pygame.quit()