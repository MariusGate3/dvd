import pygame
import random
import config

pygame.font.init()
font = pygame.font.Font(None, 36)


class Dvd:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.text = font.render("DVD", True, color)
        self.rect = self.text.get_rect()
        self.rect.topleft = (x, y)
        self.direction = (random.choice([-1, 1]), random.choice([-1, 1]))

    def update(self):
        self.rect.topleft = (
            self.rect.topleft[0] + self.direction[0],
            self.rect.topleft[1] + self.direction[1],
        )

        if self.rect.left <= 0 or self.rect.right >= config.window_x:
            self.direction = (-self.direction[0], self.direction[1])
            self.updateFont()

        if self.rect.top <= 0 or self.rect.bottom >= config.window_y:
            self.direction = (self.direction[0], -self.direction[1])
            self.updateFont()

    def updateFont(self):
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        self.text = font.render("DVD", True, self.color)

    def draw(self, screen):
        screen.blit(self.text, self.rect)
