class Settings:
    screen_width = 640
    screen_height = 480
    full_screen = False

    def load_settings(self, path='settings.txt'):
        f = open(path, 'r')
        parameter = f.readline()
        self.screen_width = int(parameter.split(' ')[1])
        self.screen_height = int(parameter.split(' ')[2])

        parameter = f.readline()
        if int(parameter.split(' ')[1]) == 1:
            self.full_screen = True
        else:
            self.full_screen = False



