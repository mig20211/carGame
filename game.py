import pygame

pygame.init()


class Game:
    def __init__(self):
        screen_size = [800, 600]
        print('| Screen Size', 'x =', screen_size[0], 'y =', screen_size[1], '|')

        #   colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.ground_color = (26, 26, 26)

        #   necessary
        self.crashed = False
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
        pygame.display.set_caption('pygame game (tutorial)')
        #   extra

        self.car_img = pygame.image.load('assets/imgs/pixil-frame-0.png')

    def car(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.xpos_change = 0
        self.ypos_change = 0

        self.screen.blit(self.car_img, (self.xpos + self.xpos_change, self.ypos + self.ypos_change))

    def Game_loop(self):

        while True:
            self.screen.fill(self.ground_color)
            self.car(xpos=50, ypos=50)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.xpos_change = -5
                    if event.key == pygame.K_RIGHT:
                        self.xpos_change = 5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        self.xpos_change = 0

                if event.type == pygame.QUIT:
                    print('App Closed')
                    pygame.quit()
                    quit()

            pygame.display.update()
            self.clock.tick(60)


Game().Game_loop()
