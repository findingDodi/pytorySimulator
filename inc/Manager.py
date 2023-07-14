import pygame

import conf
from .GameLogic import GameLogic


class Manager:

    def __init__(self):
        self.screen = None
        self.screen_width = conf.SCREEN_SIZE[0]
        self.screen_height = conf.SCREEN_SIZE[1]
        self.game_is_running = True
        self.last_event = None
        self.time_passed = 0
        self.background_rect = pygame.Rect(0, 0, self.screen_width, self.screen_height)

        self.game_logic = GameLogic()

    def render_buildings(self):
        for building in self.game_logic.buildings:
            pygame.draw.rect(self.screen, building.color, building.get_rect())

    def render_vehicles(self):
        for vehicle in self.game_logic.vehicles:
            pygame.draw.rect(self.screen, vehicle.color, vehicle.get_rect())

    def run_game(self):

        pygame.init()
        pygame.display.set_caption("Pytory Simulator")
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), 0, 32)
        clock = pygame.time.Clock()
        self.game_is_running = True

        self.game_logic.initialize_game_field()

        while self.game_is_running:
            # limit framespeed to 30fps
            self.time_passed = clock.tick(30)
            self.screen.fill((55, 55, 55), self.background_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_is_running = False
                    else:
                        pass

            self.game_logic.game_tick()

            self.render_buildings()
            self.render_vehicles()
            # final draw
            pygame.display.flip()
