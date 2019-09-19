# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:29:38 2019

@author: Yoeri
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""
    
    def __init__(self, ai_game):
        """De start positie van de alien"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #load the alien
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #start the new alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #store the alien's exact horizontal position
        self.x = float(self.rect.x)


    def update(self):
        """move the aliens to the right"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x
        