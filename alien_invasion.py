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
from alien import Alien


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
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
    
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
            
            #delete old bullets
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))
            
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
        

    def _create_fleet(self):
        """create the alien fleet"""
        #make a alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        #determine the number of row of aliens on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        #create the full fleet of aliens
        for row_number in range(number_rows):
        
        #create the first row of aliens
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
                
            
    def _create_alien(self, alien_number, row_number):
            #Create a alien and place it in a row
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
            self.aliens.add(alien)
        
        #redraw the screen during each pass through the loop
   
    def _update_screen(self):
        """update images that are on the screen, and flip to new screen"""
        
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
                    
        #Make the most recently drawn screen visible.
        pygame.display.flip()
                
if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
    
    