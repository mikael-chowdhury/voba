import time
import pygame

from crystal_engine.client.managers.NetworkManager import NetworkManager
from crystal_engine.client.managers.SceneManager import SceneManager
from crystal_engine.client.managers.UIManager import UIManager
from crystal_engine.client.ConfigurationManager import ConfigurationManager

class Game:
    def __init__(self, screensize) -> None:
        self.entities = []
        self.scenes = []
        self.managers = []

        self.running = True

        self.background_fill_colour = None
        
        pygame.init()

        self.screen = pygame.display.set_mode(screensize)

        ConfigurationManager.set("screensize", screensize)

        self.frames_played = 0

        self.start_time = time.time()
        self.time_now = time.time()

        self.frames_per_second = -1

        self.frames_per_second_reset_time = 0.6

        self.load_managers()

        self.clock = pygame.time.Clock()

        self.dt = -1

    def close(self):
        self.running = False
        
    def loop(self, args=[]):
        self.dt = self.clock.tick()

        events = pygame.event.get()
        pressed_keys = pygame.key.get_pressed()

        if self.background_fill_colour is not None:
            self.screen.fill(self.background_fill_colour)
        
        for loopable in self.entities + self.scenes + self.managers:
            if loopable is not None:
                loopable.loop(self.screen, events, pressed_keys, self, *args)

        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

        return events, pressed_keys

    def load_managers(self):
        SceneManager(self)
        UIManager(self)
        NetworkManager(self)

    def load_manager(self, manager):
        manager()

    def unload_manager(self, manager):
        manager.unload()

    def end_loop(self, args=[]):
        pygame.display.update()

        self.frames_played += 1
        self.time_now = time.time()

        self.frames_per_second = self.frames_played / self.time_now - self.start_time