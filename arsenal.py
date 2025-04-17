import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()
    
    def update_arsenal(self):
        self.arsenal.update()


    def _remove_bullets_offscreen(self):
         for bullet in self.arsenal:
            if bullet.rect.top <= 0:  # Check top of the bullet, not bottom
                print("Removing bullet!")
                self.arsenal.remove(bullet)

    def draw(self):
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False