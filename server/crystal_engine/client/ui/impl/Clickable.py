import pygame
from crystal_engine.client.ui.UIElement import UIElement

class Clickable(UIElement):
    def __init__(self, x, y, w, h, background_image=None, background_color=(255, 255, 255), text_color=(0, 0, 0), text_font="arial", font_size=16, is_sys_font=True, text="", on_click=None) -> None:
        super().__init__(x, y, w, h, background_image=background_image, background_color=background_color, text_color=text_color, text_font=text_font, font_size=font_size, is_sys_font=is_sys_font, text=text)
        
        self.on_click = on_click

    def set_on_click_listener(self, on_click):
        self.on_click = on_click

    def loop(self, screen, events, keys, *args):
        super().loop(screen, *args)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.mouse_hovering():
                    if self.on_click is not None:
                        self.on_click(screen, events, keys, *args)