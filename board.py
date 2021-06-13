import pygame as pg


def draw_board(screen):
    pg.draw.line(screen, "white", (100, 100), (100, 450), 5)
    pg.draw.line(screen, "white", (100, 450), (450, 450), 5)
    pg.draw.line(screen, "white", (100, 100), (450, 100), 5)
    pg.draw.line(screen, "white", (450, 100), (450, 450), 5)

    pg.draw.line(screen, "white", (100, 275), (450, 275), 5)
    pg.draw.line(screen, "white", (275, 100), (275, 450), 5)

    pg.draw.line(screen, "white", (100, 100), (450, 450), 7)
    pg.draw.line(screen, "white", (100, 450), (450, 100), 7)


class Markers:
    def __init__(self):

        self.rectangle = pg.Surface((20, 20))
        self.color = "white"

        self.pos_1 = (100, 100)
        self.pos_2 = (100, 450)
        self.pos_3 = (450, 100)
        self.pos_4 = (450, 450)
        self.pos_5 = (100, 275)
        self.pos_6 = (275, 100)
        self.pos_7 = (275, 450)
        self.pos_8 = (450, 275)
        self.pos_9 = (275, 275)
        self.pos = [self.pos_1, self.pos_2, self.pos_3, self.pos_4, self.pos_5,
                    self.pos_6, self.pos_7, self.pos_8, self.pos_9]

    def draw_markers(self, screen):
        for i in range(0, 8):
            for f in self.pos:
                target = self.rectangle.get_rect(center=f)
                pg.draw.ellipse(screen, self.color, target)
