import pygame

SIZE = WINDTH, HEIGHT = 1280, 720

pygame.init()
pygame.display.set_caption('PyTris')

screen = pygame.display.set_mode((WINDTH, HEIGHT))
font = pygame.font.Font('freesansbold.ttf', 32)
clock = pygame.time.Clock()
text = font.render('TEXT', True, (0,255,0), (0,0,255))
textRect = text.get_rect()
textRect.center = (WINDTH // 2, HEIGHT // 2)


running = True
while running:
    screen.blit(text, textRect)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(100)

pygame.quit()