from copy import deepcopy
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

        self.speed = 0.01

        self.vy = 0

        self.launched = False

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
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and player.has_possession_of_ball and not self.launched:
                if event.button == 1:
                    self.vy = 0.05
                    self.launched = True
                    player.has_possession_of_ball = False
        

        if not player.has_possession_of_ball:
            if self.launched:
                self.vy += 0.005

                if self.vy >= 1:
                    self.launched = False

                self.y -= self.vy * game.dt
            
            else:
                if self.y + self.radius < screen_size()[1]:
                    self.vy -= self.speed

                    self.y -= self.vy * game.dt
                else:
                    self.vy = 0
        else:
            self.x = player.x + player.w / 2
            self.y = player.y + player.h / 2
                
        self.update_rect()

        game.NetworkManager.GameNetworkingObject.set_field("ball", self)

        pygame.draw.circle(screen, (255, 255, 255), self.rect.center, self.radius)

        if self.collision(player, self.rect.center, self.radius) and not self.launched:
            player.has_possession_of_ball = True

    def collision(self, player, circle_center, radius):  # circle definition
        pRect = pygame.Rect(player.x, player.y, player.w, player.h)
        cRect = pygame.Rect(circle_center[0] - radius, circle_center[1] - radius, radius * 2, radius * 2)

        return pRect.colliderect(cRect)