# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:46:27 2019

@author: Yoeri
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet



class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """initializes the game and game resources"""

        pygame.init()
        self.settings = Settings()
        
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
    
        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
    
        #set background color
        self.bg_color = (230, 230, 230)
    
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            #watch for keyboard and mouse events.
            
    def _check_events(self):        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                    
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                        
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
             self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
             self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
                        
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
             self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
             self.ship.moving_left = False
        
    def _fire_bullet(self): 
        """Create a new bullet and add it to the bullets group."""

        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()


                    
        #redraw the screen during each pass through the loop
   
    def _update_screen(self):
        """update images that are on the screen, and flip to new screen"""
        
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
                    
        #Make the most recently drawn screen visible.
        pygame.display.flip()
                
if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
    
    