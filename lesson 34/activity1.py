import pygame
import random

pygame.init()

sprite_color_change_event = pygame.USEREVENT + 1
background_color_change_event = pygame.USEREVENT + 2

# backgrounfd colors

blue = pygame.Color('blue')
lightblue = pygame.Color('lightblue')
navyblue = pygame.Color('navyblue')
maroon = pygame.color('maroon')
magenta = pygame.Color('magenta')

# Sprite colors

white = pygame.Color('white')
gray = pygame.Color('gray')
white_smoke = pygame.Color('whitesmoke')
black = pygame.Color('black')
rose = pygame.Color('rose')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, hight, width):
        super(). __init__()
        self.image = pygame.Surface([width, hight])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.victory = [random.choice([-1, 1]), random.choice([-1, 1])]

        def update(self):
            self.rect.move_ip(self.victory)
            boundery_hit = False

            if self.rect.left < 0 or self.rect.bottom >= 400:
                self.victory[1] = -self.victory[1]
                boundery_hit = True
            
            if boundery_hit:
                pygame.event.post(pygame.event.Event(sprite_color_change_event))
                pygame.event.post(pygame.event.Event(background_color_change_event))

        def change_color(self, color):
            self.image.fill(random.choice([white, gray, white_smoke, black, rose]))

    def change_background_color():
        global bg_color
        bg_color = random.choice([blue, lightblue, navyblue, maroon, magenta])

    all_sprites = pygame.sprite.Group()
    sp1 = Sprite(white, 50, 50)
    sp1.rect.x = random.randint(0, 480)
    sp1.rect.y = random.randint(0, 370)
    all_sprites.add(sp1)

    screen = pygame.display.set_mode([500, 400])
    pygame.display.set_caption('Sprite and Background Color Change')
    bg_color = blue
    screen.full(bg_color)
    exit = False
    clock = pygame.time.Clock()

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == sprite_color_change_event:
                sp1.change_color()
            elif event.type == background_color_change_event:
                change_background_color()

        all_sprites.update()
        screen.fill(bg_color)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        pygame.quit()

        
