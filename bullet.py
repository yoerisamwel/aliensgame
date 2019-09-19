# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:29:23 2019

@author: Yoeri
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class to manage the bullets"""
    
    def __init__(self, ai_game):
        """create the bullet at the ships location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        #create a bullet at (0,0) and then correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        #store the bullet postion in decimal value
        self.y = float(self.rect.y)
        
    def update(self):
        """move the bullets up the screen"""
        #update per decimal position of the bullet
        self.y -= self.settings.bullet_speed
        #update the tect position
        self.rect.y = self.y
        
    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        