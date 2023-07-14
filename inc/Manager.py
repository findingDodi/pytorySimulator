import pygame
import conf


class Manager:

    def __init__(self):
        self.screen = None
        self.screen_width = conf.SCREEN_SIZE[0]
        self.screen_height = conf.SCREEN_SIZE[1]
        self.game_is_running = True
        self.last_event = None
        self.time_passed = 0
        self.background_rect = pygame.Rect(0, 0, self.screen_width, self.screen_height)

    def run_game(self):

        pygame.init()
        pygame.display.set_caption("Pytory Simulator")
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), 0, 32)
        clock = pygame.time.Clock()
        self.game_is_running = True

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

            # final draw
            pygame.display.flip()
