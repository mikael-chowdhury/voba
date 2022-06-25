import pygame
from crystal_engine.client.Game import Game
from scenes.S_MainMenu import S_Mainmenu

game = Game((1920, 1080))

game.SceneManager.set_scene(S_Mainmenu())

while game.running:
    events, keys = game.loop()

    game.end_loop()