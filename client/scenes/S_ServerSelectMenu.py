from crystal_engine.client.ui.Scene import Scene
from crystal_engine.client.ui.impl.Clickable import Clickable
from crystal_engine.client.ui.impl.TextBox import TextBox
from crystal_engine.client.ui.impl.InputBox import InputBox
from crystal_engine.client.ui.ScreenPortions import Width, Height

from scenes.S_MultiplayerGameScene import S_MultiplayerGameScene

class S_ServerSelectMenu(Scene):
    def __init__(self) -> None:
        super().__init__()

        self.background = (23, 0, 0)

        self.title = TextBox(0, 0, 100, 100, text="Server Selection Menu", text_color=(255, 255, 255), font_size=64)
        self.title.center_x = Width.half()
        self.title.center_y = Height.quarter()
        self.title.update_rect()

        self.server_ip_input = InputBox(0, 0, 350, 75, placeholder="server ip address", text_color=(255, 255, 255), font_size=36)
        self.server_ip_input.center_x = Width.half()
        self.server_ip_input.center_y = Height.half()
        self.server_ip_input.background_color = (50, 0, 0)
        self.server_ip_input.background_color_hovering = (75, 0, 0)
        self.server_ip_input.update_rect()

        self.server_port_input = InputBox(0, 0, 350, 75, placeholder="server port", text_color=(255, 255, 255), font_size=36)
        self.server_port_input.center_x = Width.half()
        self.server_port_input.center_y = Height.half() + Height.quarter() / 2
        self.server_port_input.background_color = (50, 0, 0)
        self.server_port_input.background_color_hovering = (75, 0, 0)
        self.server_port_input.update_rect()

        self.join_server = Clickable(0, 0, 400, 100, text="Join Server", text_color=(255, 255, 255), font_size=48)
        self.join_server.center_x = Width.half()
        self.join_server.center_y = Height.half() + Height.quarter()
        self.join_server.background_color = (50, 0, 0)
        self.join_server.background_color_hovering = (85, 0, 0)
        self.join_server.update_rect()
        self.join_server.set_on_click_listener(lambda screen, events, keys, game, *args: self.connect_to_server(self.server_ip_input.text, int(self.server_port_input.text), game))

        self.ui.append(self.title)
        self.ui.append(self.server_ip_input)
        self.ui.append(self.server_port_input)
        self.ui.append(self.join_server)

    def connect_to_server(self, ip, port, game):
        game.NetworkManager.connect_to_server(ip, port)

        if game.NetworkManager.connected_to_server:
            game.SceneManager.set_scene(S_MultiplayerGameScene())