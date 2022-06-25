from crystal_engine.client.ui.Scene import Scene
from crystal_engine.client.ui.impl.Clickable import Clickable
from scenes.S_ServerSelectMenu import S_ServerSelectMenu

class S_Mainmenu(Scene):
    def __init__(self) -> None:
        super().__init__()

        self.background = (0, 0, 0)

        self.play_button = Clickable(0, 0, 150, 50, background_color=None, text="Play", font_size=48, on_click=self.on_click, text_color=(255, 255, 255))
        self.play_button.center_x = int(1920 / 2)
        self.play_button.center_y = int(1080 / 2)
        self.play_button.update_rect()
        self.play_button.update_text_surf()

        self.play_button.center_text = True

        self.ui.append(self.play_button)

    def on_click(self, screen, keys, events, game, *args):
        game.SceneManager.set_scene(S_ServerSelectMenu())

    def loop(self, screen, events, keys, game, *args):
        super().loop(screen, events, keys, game, *args)