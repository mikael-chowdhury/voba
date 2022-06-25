import pygame
from crystal_engine.client.ui.impl.Clickable import Clickable

class InputBox(Clickable):
    InputBoxes = []

    def __init__(self, x, y, w, h, background_image=None, background_color=None, text_color=(0, 0, 0), text_font="arial", font_size=16, is_sys_font=True, placeholder="") -> None:
        super().__init__(x, y, w, h, background_image, background_color, text_color, text_font, font_size, is_sys_font, placeholder)

        self.placeholder = placeholder
        
        self.activated = False

        self.input_text = ""

        self.resctricted_keys = [pygame.K_BACKSPACE, pygame.K_RETURN, pygame.K_ESCAPE, pygame.K_TAB, pygame.K_CAPSLOCK, pygame.K_LCTRL, pygame.K_RCTRL]

        InputBox.InputBoxes.append(self)

    def activate(self):
        for input_box in InputBox.InputBoxes:
            input_box.deactivate()

        self.activated = True

    def deactivate(self):
        self.activated = False

    def loop(self, screen, events, keys, *args):

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.mouse_hovering():
                        self.activate()
                    else:
                        self.deactivate()

            if event.type == pygame.KEYDOWN:
                if self.activated:
                    if event.key == pygame.K_BACKSPACE and len(self.input_text) > 0:
                        self.input_text = self.input_text[:-1]
                    else:
                        if not event.key in self.resctricted_keys:
                            self.input_text += event.unicode
            
        self.text = self.input_text if len(self.input_text) > 0 else self.placeholder
        self.update_text_surf()

        super().loop(screen, events, keys, *args)
