import pygame
from Button import Button


class Game:
    buttons = []

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


# bikes - it's fun, but pygame have function to do it
def is_into(dot, rect):
    if dot[0] < rect[0][0] or dot[0] > rect[0][0] + rect[1][0] or dot[1] < rect[0][1] or dot[1] > rect[0][1] + rect[1][1]:
        return False
    return True

pygame.init()
screen = pygame.display.set_mode((640, 480))


def print_msg(msg, size, color, back_color, coord, font="Mono.ttf"):
    font_obj = pygame.font.Font(font, size)
    text_surface_obj = font_obj.render(msg, True, color, back_color)
    text_react_obj = text_surface_obj.get_rect()
    text_react_obj.midleft = coord
    screen.blit(text_surface_obj, text_react_obj)

game = Game()

button = Button("example", ((50, 20), (120, 120)), (0, 120, 255))
button.add_listener(game)
game.add_button(button)


cycle = True

while cycle:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if is_into(pygame.mouse.get_pos(), button.rect):
                button.notify()

    screen.fill((0, 0, 0))
    print_msg(str(game.count_of_b_pressed("example")), 30, (255, 255, 255), (0, 0, 0), (150, 300))
    pygame.draw.rect(screen, (0, 255, 0), button.rect)
    pygame.display.flip()
