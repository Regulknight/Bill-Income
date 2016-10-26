import pygame


class Button:
    name = ""
    # rect (top left corner), (width, height)
    rect = pygame.Rect((10, 10), (50, 20))
    color = (255, 255, 255)
    listeners = []

    def notify(self):
        for i in self.listeners:
            i.get_event(self.name)
            print("button " + self.name + " was pressed")

    def __init__(self, name, rect, color):
        self.name = name
        self.rect = pygame.Rect(rect)
        self.color = color

    def add_listener(self, listener):
        self.listeners.append(listener)

    def draw_button(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
