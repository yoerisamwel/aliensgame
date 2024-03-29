# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:01:27 2019

@author: Yoeri
"""

import pygame

class Ship:
    """a class to manage the ship"""
    
    def __init__(self, ai_game):
        """initializes the ship and sets its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #start each new ship at the bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        #store a decimal value for the ship horisontal position
        self.x = float(self.rect.x)
        
        #movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """update the ships position based on the movement flag"""
        #Update the ships x value not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        # Update rect object from self.x
        self.rect.x = self.x
        
    def blitme(self):
        """draw the ship at current location"""
        self.screen.blit(self.image, self.rect)
        
        