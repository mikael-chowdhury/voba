import pygame

from crystal_engine.client.util.Loopable import Loopable
from crystal_engine.client.ui.ScreenPortions import Width, Height, screen_size
import math

class Ball(Loopable):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.radius = 30

        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.rect.center = (self.x, self.y)

        self.fall_speed = 0.25

    @staticmethod
    def from_object(object):
        ball = Ball(-1, -1)

        for field in dir(object):
            try:
                setattr(ball, field, getattr(object, field))
            except:
                pass

        return ball

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.rect.center = (self.x, self.y)

    def loop(self, player, screen, events, keys, game, *args):
        super().loop(screen, *args)
        
        if self.y + self.radius < screen_size()[1]:
            self.y += self.fall_speed * game.dt

        self.update_rect()


        game.NetworkManager.GameNetworkingObject.set_field("ball", self)

        pygame.draw.circle(screen, (255, 255, 255), self.rect.center, self.radius)

        print("before")

        if self.collision(player, self.rect.center, self.radius):
            print("collision")

        print("after")

    def collision(self, player, circle_center, radius):  # circle definition
        pRect = pygame.Rect(player.x, player.y, player.w, player.h)
        cRect = pygame.Rect(circle_center[0] - radius, circle_center[1] - radius, radius * 2, radius * 2)

        return pRect.colliderect(cRect)