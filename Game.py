from Settings import Settings
from Player import Player
import pygame


class Game:
    buttons = []
    settings = Settings()
    screen = pygame.display.set_mode()
    player = Player()

    def __init__(self):
        self.settings.load_settings("settings.txt")
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        if self.settings.full_screen:
            pygame.display.toggle_fullscreen()
        self.player = Player()

    def get_event(self, msg):
        for i in self.buttons:
            if i[0] == msg:
                i[1] += 1

    def add_button(self, button):
        self.buttons.append([button.name, 0])

    def count_of_b_pressed(self, name):
        for i in self.buttons:
            if i[0] == name:
                return i[1]

    def draw_buttons(self):
        for button in self.buttons:
            button.draw_button()

    def load_settings(self, path="settings.txt"):
        self.settings.load_settings(path)

    def print_msg(self, msg, size, color, back_color, coord, font="Mono.ttf"):
        font_obj = pygame.font.Font(font, size)
        text_surface_obj = font_obj.render(msg, True, color, back_color)
        text_react_obj = text_surface_obj.get_rect()
        text_react_obj.midleft = coord
        self.screen.blit(text_surface_obj, text_react_obj)

    def show_progress(self, progress_list):
        i = 0
        for progress in progress_list:
            self.print_msg(str(progress), 15, (255, 255, 255), (0, 0, 0), (200, 10 + i * 30))
            i += 1

    def show_prices(self, price_list, n):
        i = 0
        for price in price_list:
            self.print_msg(str(round(price, 2)) + " x" + str(n), 15, (255, 255, 255), (0, 0, 0), (250, 10 + i * 30))
            i += 1

    def show_names(self, name_list):
        i = 0
        for name in name_list:
            self.print_msg(name + ": ", 15, (255, 255, 255), (0, 0, 0), (0, 10 + i * 30))
            i += 1

    def show_count_of_income(self, count_list):
        i = 0
        for count in count_list:
            self.print_msg(str(count), 15, (255, 255, 255), (0, 0, 0), (150, 10 + i * 30))
            i += 1

    def show_all(self):
        self.show_progress(self.player.get_progress_list())
        self.show_prices(self.player.get_price_list(1), 1)
        self.show_names(self.player.get_names_list())
        self.show_count_of_income(self.player.get_count_list())
