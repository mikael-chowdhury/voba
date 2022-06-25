from crystal_engine.client.util.Loopable import Loopable

class Scene(Loopable):
    def __init__(self) -> None:
        super().__init__()

        self.entities = []
        self.ui = []

        self.background = None

        self.loop_stack = []

    def add_to_loop(self, func):
        self.loop_stack.append(func)

    def loop(self, screen, keys, events, game, *args):
        super().loop(self, screen, keys, events, *args)

        if self.background is not None:
            screen.fill(self.background)

        for loopable in self.entities + self.ui + self.loop_stack:
            loopable.loop(screen, keys, events, game, *args)