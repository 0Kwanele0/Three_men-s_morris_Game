import pygame as pg


class Placers:
    def __init__(self):
        self.color = "yellow"
        self.pos_initial = (70, 550)
        self.pos_initial_1 = (150, 550)
        self.pos_initial_2 = (230, 550)

        self._color = (24, 0, 76)
        self._pos_initial = (350, 550)
        self._pos_initial_1 = (430, 550)
        self._pos_initial_2 = (510, 550)

        self.blue_rect_1 = pg.Surface((50, 50))
        self.blue_1 = self.blue_rect_1.get_rect(center=self._pos_initial)

        self.blue_rect_2 = pg.Surface((50, 50))
        self.blue_2 = self.blue_rect_2.get_rect(center=self._pos_initial_1)

        self.blue_rect_3 = pg.Surface((50, 50))
        self.blue_3 = self.blue_rect_3.get_rect(center=self._pos_initial_2)

        self.yellow_rect_1 = pg.Surface((50, 50))
        self.yellow_1 = self.yellow_rect_1.get_rect(center=self.pos_initial)

        self.yellow_rect_2 = pg.Surface((50, 50))
        self.yellow_2 = self.yellow_rect_2.get_rect(center=self.pos_initial_1)

        self.yellow_rect_3 = pg.Surface((50, 50))
        self.yellow_3 = self.yellow_rect_3.get_rect(center=self.pos_initial_2)

    def draw_yellow(self, screen):
        pg.draw.ellipse(screen, self.color, self.yellow_1)

        pg.draw.ellipse(screen, self.color, self.yellow_2)

        pg.draw.ellipse(screen, self.color, self.yellow_3)

    def draw_blue(self, screen):
        pg.draw.ellipse(screen, self._color, self.blue_1)

        pg.draw.ellipse(screen, self._color, self.blue_2)

        pg.draw.ellipse(screen, self._color, self.blue_3)
