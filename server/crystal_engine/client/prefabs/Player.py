import random
import uuid
import pygame

from crystal_engine.client.util.Loopable import Loopable

class RawPlayer(Loopable):
    def __init__(self):
        super().__init__()

class Player(RawPlayer):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y

        self.w = 100
        self.h = 100

        self.speed = 0.5

        self.uuid = uuid.uuid4()

        self.color = (random.randrange(0, 100), random.randrange(0, 100), random.randrange(0, 100))
        
    def create(self, game, parent):
        self.update(game)

        parent.entities.append(self)

    def movement(self, keys, game):
        if keys[pygame.K_a]:
            self.x -= self.speed * game.dt

        if keys[pygame.K_d]:
            self.x += self.speed * game.dt

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))

    def update(self, game):
        game.NetworkManager.GameNetworkingObject.set_field("player", self)

    def loop(self, screen, events, keys, game, *args):
        self.movement(keys, game)
        self.update(game)

    @staticmethod
    def from_object(object):
        player = Player(-1, -1)

        for field in dir(object):
            try:
                setattr(player, field, getattr(object, field))
            except:
                pass

        return player