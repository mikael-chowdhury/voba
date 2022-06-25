import pygame
from crystal_engine.client.Game import Game
from scenes.S_ServerSelectMenu import S_ServerSelectMenu

game = Game((1920, 1080))

ssm = S_ServerSelectMenu()

ssm.connect_to_server("192.168.178.22", 5555, game)

while game.running:
    events, keys = game.loop()

    game.end_loop()