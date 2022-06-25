import pygame
from crystal_engine.client.util.Loopable import Loopable

class UIElement(Loopable):
    def __init__(self, x, y, w, h, background_image=None, background_color=(255, 255, 255), text_color=(0, 0, 0), text_font="arial", font_size=16, is_sys_font=True, text="", center_text=True) -> None:
        super().__init__()

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
        self.background_image = pygame.transform.smoothscale(background_image, (self.w, self.h)) if background_image is not None else None
        self.background_color = background_color

        self.text_color = text_color
        self.text_font = text_font
        self.is_sys_font = is_sys_font
        self.font_size = font_size
        self.text = text
        self.center_text = center_text
        self.text_center_rect = None

        self.background_color_hovering = self.background_color

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        self.center_x = self.rect.centerx
        self.center_y = self.rect.centery

        if self.text != "":
            if self.is_sys_font:
                self.font = pygame.font.SysFont(self.text_font, self.font_size)
            else:
                self.font = pygame.font.Font(self.text_font, self.font_size)

        self.text_surf = self.font.render(self.text, True, self.text_color)

        self.update_text_surf()

    def update_text_surf(self):
        if self.center_text:
            self.text_surf = self.font.render(self.text, True, self.text_color)
            self.text_center_rect = self.text_surf.get_rect()
            self.text_center_rect.center = self.rect.center

        else:
            self.text_surf = self.font.render(self.text, True, self.text_color)

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

        self.update_text_surf()

    def set_text(self, text):
        self.text = text
        self.text_surf = self.font.render(self.text, True, self.text_color)

    def set_x(self, x):
        self.x = x
        self.update_rect()

    def set_y(self, y):
        self.y = y
        self.update_rect()

    def set_w(self, w):
        self.w = w
        self.update_rect()

    def set_h(self, h):
        self.h = h
        self.update_rect()

    def mouse_hovering(self):
        mouse = pygame.mouse.get_pos()

        sx = self.rect.x
        sy = self.rect.y
        sw = self.rect.w
        sh = self.rect.h

        x = mouse[0]
        y = mouse[1]

        if x >= sx and x <= sx + sw and y >= sy and y <= sy + sh:
            return True
        else:
            return False

    def loop(self, screen, *args):
        super().loop(screen, *args)

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

        if self.background_image is not None:
            screen.blit(self.background_image, (self.x, self.y))

        elif not self.mouse_hovering():
            if self.background_color:
                pygame.draw.rect(screen, self.background_color, self.rect)
        else:
            if self.background_color_hovering:
                pygame.draw.rect(screen, self.background_color_hovering, self.rect)


        if self.text != "":
            screen.blit(self.text_surf, (self.text_center_rect.x, self.text_center_rect.y) if self.center_text and self.text_center_rect is not None else (self.x, self.y))