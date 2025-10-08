import pygame

pygame.init()
screen = pygame.display.set_mode((400, 700))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (200, 25, 125), pygame.Rect(60, 60, 120, 120))
    pygame.draw.circle(screen, (246, 112, 79), (200, 200), 40)

    pygame.draw.circle(screen, (55, 222, 0), (300, 300), 40, 15)
    pygame.display.flip()