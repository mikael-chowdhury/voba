import random
from crystal_engine.client.ui.Scene import Scene
from crystal_engine.client.prefabs.Player import Player
from crystal_engine.client.ui.ScreenPortions import Width, Height, screen_size

from entities.Ball import Ball

class S_MultiplayerGameScene(Scene):
    def __init__(self) -> None:
        super().__init__()

        self.first_loop = True

        self.background = (0, 0, 0)

        self.player = Player(0, screen_size()[1] - 100)

        self.ball = Ball(Width.half(), Height.half())

    def loop(self, screen, events, keys, game, *args):
        super().loop(screen, events, keys, game, *args)

        if self.first_loop:
            self.first_loop = False

            self.player.create(game, self)

        self.player.loop(screen, events, keys, game)

        for connection in game.NetworkManager.connections:
            if connection is not None:
                temp_player = Player.from_object(connection)
                temp_player.draw(screen)

        self.ball.loop(self.player, screen, events, keys, game, *args)