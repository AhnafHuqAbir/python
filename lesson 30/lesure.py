import pygame
import random

pygame.init()
sprite_color_change_event = pygame.USEREVENT + 1
background_color_change_event = pygame.USEREVENT + 2

# background colors
light_blue = pygame.Color("lightblue")
navy = pygame.Color('navy')
black = pygame.Color('black')

# sprite colors
white = pygame.Color('white')
orange = pygame.color("orange")
gray = pygame.Color('gray')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, hight, width):
        super(). __init__()
        self.image = pygame.Surface([width, hight])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move__ip(self.velocity)
        boundary_hit = False

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        
        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_color_change_event))
            pygame.event.post(pygame.event.Event(background_color_change_event))
        
        def change_background_color():
            global bg_color 
            bg_color = random.choice([light_blue, navy, black])

        all_aprites_list = pygame.sprite.Group()
        sp1 = Sprite(white, 20, 30)
        sp1.rect.x = random.randint(0, 480)
        sp1.rect.y = random.randint(0, 370)
        all_aprites_list.add(sp1)

        screen = pygame.display.set_mode([500, 400])
        pygame.display.set_caption("Vajaliya Activity")
        bg_color = light_blue
        screen.fill(bg_color)
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
            
            all_aprites_list.update()
            screen.fill(bg_color)
            all_aprites_list.draw(screen)

            pygame.display.flip()
            clock.tick(220)

pygame.quit()