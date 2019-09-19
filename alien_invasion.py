# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:46:27 2019

@author: Yoeri
"""

import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """initializes the game and game resources"""

        pygame.init()
        self.settings = Settings()
    
        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
    
        #set background color
        self.bg_color = (230, 230, 230)
    
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
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
                        
    def _check_keyup_events(self, event):
         if event.key == pygame.K_RIGHT:
             self.ship.moving_right = False
         elif event.key == pygame.K_LEFT:
             self.ship.moving_left = False


                    
        #redraw the screen during each pass through the loop
   
    def _update_screen(self):
        """update images that are on the screen, and flip to new screen"""
        
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
                    
        #Make the most recently drawn screen visible.
        pygame.display.flip()
                
if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
    