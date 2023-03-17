import pygame.font


class Scores:
    # output game data and scores
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.font = pygame.font.SysFont(None, 36)
        self.ImgScore()

    def ImgScore(self):
        # translate text into image
        self.score_img = self.font.render(str(self.stats.score), True, "green", (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def ShowScore(self):
        self.screen.blit(self.score_img, self.score_rect)
