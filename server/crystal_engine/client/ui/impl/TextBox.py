from crystal_engine.client.ui.UIElement import UIElement

class TextBox(UIElement):
    def __init__(self, x, y, w, h, background_image=None, background_color=None, text_color=(0, 0, 0), text_font="arial", font_size=16, is_sys_font=True, text="", center_text=True) -> None:
        super().__init__(x, y, w, h, background_image, background_color, text_color, text_font, font_size, is_sys_font, text, center_text)

    def loop(self, screen, events, keys, *args):
        super().loop(screen, events, keys, *args)