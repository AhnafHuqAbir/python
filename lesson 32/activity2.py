import pygame

pygame.init()
screen_width, screen_height = 500, 500

display_surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Panguin said Hellow word")

background_image = pygame.transform.scale(
    pygame.image.load("images/background.png").convert(), (screen_width, screen_height))

penguin_image = pygame.transform.scale(
    pygame.image.load("images/penguin.png").convert_alpha(), (300, 300))

penguin_rect = penguin_image.get_rect(center= (screen_width // 2, screen_height // 2 - 30))

text = pygame.font.Font(None, 36).render("Hi, I am Tilak Varma", True, pygame.color("black"))
text_rect = text.get_rect(center = (screen_width // 2, screen_height // 2 + 110))