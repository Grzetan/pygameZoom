import pygame
import math
import sys
from pygameZoom import PygameZoom


class Window:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 1000, 800
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.CLOCK = pygame.time.Clock()
        self.FPS = 30
        self.run = True
        self.pygameZoom = PygameZoom(500, 400)
        self.pygameZoom.set_background((255, 0, 0))
        self.loop()

    def drawTree(self, a, b, pos, deepness):
        if deepness:
            c = a + int(math.cos(math.radians(pos)) * deepness * 10.0)
            d = b + int(math.sin(math.radians(pos)) * deepness * 10.0)
            self.pygameZoom.draw_line((127, 255, 0), a, b, c, d, 1)
            self.drawTree(c, d, pos - 25, deepness - 1)
            self.drawTree(c, d, pos + 25, deepness - 1)

    def refresh_window(self):
        self.WIN.fill(0)
        # self.drawTree(500, 800, -90, 12)
        # self.pygameZoom.draw_ellipse((255, 255, 0), (200, 200, 100, 100))
        # self.pygameZoom.draw_circle((255, 255, 0), 200, 200, 20)
        # self.pygameZoom.draw_rect((0, 0, 0), 100, 100, 100, 100)
        # self.pygameZoom.draw_line((255, 255, 255), 0, 0, 200, 200)
        # self.pygameZoom.draw_polygon((0,0,255), [(200,400),(300,2),(400,400)])
        surface = pygame.image.load("download.jpeg")
        self.pygameZoom.blit(surface, (100, 100))
        self.pygameZoom.render(self.WIN, (100, 100))
        pygame.display.update()

    def events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.run = False

    def loop(self):
        while self.run:
            self.refresh_window()
            self.events()
            self.CLOCK.tick(self.FPS)
        pygame.quit()
        sys.exit()


win = Window()
