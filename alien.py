import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien,self).__init__()
        self.screen =screen
        self.ai_settings= ai_settings

        self.image = pygame.image.load("C:/Users/asus/OneDrive/Documents/drive yang dulu/Algorithm and Programming/Python/week 9/Algorithm_Programming_Week9/images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x+= (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x # pyright: ignore[reportOptionalMemberAccess]

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right: # pyright: ignore[reportOptionalMemberAccess]
            return True
        elif self.rect.left <=0:    # pyright: ignore[reportOptionalMemberAccess]
            return True
        