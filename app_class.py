import pygame
from settings import *

class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.setmode((WIDTH, HEIGHT))
        self.running = True

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            