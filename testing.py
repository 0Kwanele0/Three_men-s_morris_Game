import pygame as pg
from sys import exit

pg.init()
width = 750
height = 590
screen = pg.display.set_mode((width, height))

drawn = False
clock = pg.time.Clock()
fps = 60

BLUE1, BLUE2, BLUE3 = False, False, False

YELLOW1, YELLOW2, YELLOW3 = False, False, False


selectable1 = True
selectable2 = True
selectable3 = True
selectable4 = True
selectable5 = True
selectable6 = True
selectable7 = True
selectable8 = True
selectable9 = True

selectable1y = True
selectable2y = True
selectable3y = True
selectable4y = True
selectable5y = True
selectable6y = True
selectable7y = True
selectable8y = True
selectable9y = True


class Placers:
    def __init__(self):
        self.color = (24, 0, 76)
        self.border_pos = (0, 0)
        self.blue_placer1_pos = (350, 550)
        self.blue_placer2_pos = (430, 550)
        self.blue_placer3_pos = (510, 550)

        self.color_yellow = "orange"
        self.yellow_placer1_pos = (70, 550)
        self.yellow_placer2_pos = (150, 550)
        self.yellow_placer3_pos = (230, 550)

        self.border_col = "white"

        self.blue_rect_1 = pg.Surface((50, 50))
        self.blue_placer_1 = self.blue_rect_1.get_rect(center=self.blue_placer1_pos)

        self.blue_rect_1 = pg.Surface((50, 50))
        self.blue_placer_2 = self.blue_rect_1.get_rect(center=self.blue_placer2_pos)

        self.blue_rect_1 = pg.Surface((50, 50))
        self.blue_placer_3 = self.blue_rect_1.get_rect(center=self.blue_placer3_pos)

        self.yellow_rect_1 = pg.Surface((50, 50))
        self.yellow_placer_1 = self.yellow_rect_1.get_rect(center=self.yellow_placer1_pos)

        self.yellow_rect_1 = pg.Surface((50, 50))
        self.yellow_placer_2 = self.yellow_rect_1.get_rect(center=self.yellow_placer2_pos)

        self.yellow_rect_1 = pg.Surface((50, 50))
        self.yellow_placer_3 = self.yellow_rect_1.get_rect(center=self.yellow_placer3_pos)

        # BORDERS
        self.border_surf = pg.Surface((65, 65))
        self.blue_border = self.border_surf.get_rect(center=self.border_pos)

    def draw_blues(self, screen):
        pg.draw.ellipse(screen, self.color, self.blue_placer_1)
        pg.draw.ellipse(screen, self.color, self.blue_placer_2)
        pg.draw.ellipse(screen, self.color, self.blue_placer_3)

    def draw_yellows(self, screen):
        pg.draw.ellipse(screen, self.color_yellow, self.yellow_placer_1)
        pg.draw.ellipse(screen, self.color_yellow, self.yellow_placer_2)
        pg.draw.ellipse(screen, self.color_yellow, self.yellow_placer_3)

    def draw_boarder(self, screen):
        if drawn:
            pg.draw.ellipse(screen, self.border_col, self.blue_border)


placer = Placers()


def draw_board(screen):
    pg.draw.line(screen, "white", (100, 100), (100, 450), 5)
    pg.draw.line(screen, "white", (100, 450), (450, 450), 5)
    pg.draw.line(screen, "white", (100, 100), (450, 100), 5)
    pg.draw.line(screen, "white", (450, 100), (450, 450), 5)

    pg.draw.line(screen, "white", (100, 275), (450, 275), 5)
    pg.draw.line(screen, "white", (275, 100), (275, 450), 5)

    pg.draw.line(screen, "white", (100, 100), (450, 450), 7)
    pg.draw.line(screen, "white", (100, 450), (450, 100), 7)


class Marker:
    def __init__(self):
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

        self.marker_rect_1 = pg.Surface((25, 25))
        self.marker_1 = self.marker_rect_1.get_rect(center=self.pos_1)

        self.marker_rect_12 = pg.Surface((25, 25))
        self.marker_2 = self.marker_rect_12.get_rect(center=self.pos_2)

        self.marker_rect_13 = pg.Surface((25, 25))
        self.marker_3 = self.marker_rect_13.get_rect(center=self.pos_3)

        self.marker_rect_13 = pg.Surface((25, 25))
        self.marker_4 = self.marker_rect_13.get_rect(center=self.pos_4)

        self.marker_rect_13 = pg.Surface((25, 25))
        self.marker_5 = self.marker_rect_13.get_rect(center=self.pos_5)

        self.marker_rect_13 = pg.Surface((25, 25))
        self.marker_6 = self.marker_rect_13.get_rect(center=self.pos_6)

        self.marker_rect_13 = pg.Surface((25, 25))
        self.marker_7 = self.marker_rect_13.get_rect(center=self.pos_7)

        self.marker_rect_13 = pg.Surface((25, 25))
        self.marker_8 = self.marker_rect_13.get_rect(center=self.pos_8)

        self.marker_rect_13 = pg.Surface((25, 25))
        self.marker_9 = self.marker_rect_13.get_rect(center=self.pos_9)

    def draw_marker(self, screen):
        pg.draw.ellipse(screen, self.color, self.marker_1)

        pg.draw.ellipse(screen, self.color, self.marker_2)

        pg.draw.ellipse(screen, self.color, self.marker_3)

        pg.draw.ellipse(screen, self.color, self.marker_4)

        pg.draw.ellipse(screen, self.color, self.marker_5)

        pg.draw.ellipse(screen, self.color, self.marker_6)

        pg.draw.ellipse(screen, self.color, self.marker_7)

        pg.draw.ellipse(screen, self.color, self.marker_8)

        pg.draw.ellipse(screen, self.color, self.marker_9)


def blue_mousing():
    global drawn, selectable1, BLUE1, BLUE2, BLUE3, selectable2, selectable3, selectable4, selectable5, selectable6, selectable7, selectable8, selectable9
    # FOR SELECTING
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            # BLUE ONE
            if placer.blue_placer_1.collidepoint(event.pos):
                placer.blue_border.centerx = placer.blue_placer_1.centerx
                placer.blue_border.centery = placer.blue_placer_1.centery
                if not drawn:
                    placer.border_col = 'white'
                    placer.draw_boarder(screen)
                    drawn = True
                    BLUE1 = True
                else:
                    placer.border_col = 'darkblue'
                    placer.draw_boarder(screen)
                    drawn = False

            # BLUE TWO
            if placer.blue_placer_2.collidepoint(event.pos):
                placer.blue_border.centerx = placer.blue_placer_2.centerx
                placer.blue_border.centery = placer.blue_placer_2.centery
                if not drawn:
                    placer.border_col = 'white'
                    placer.draw_boarder(screen)
                    drawn = True
                    BLUE2 = True
                else:
                    placer.border_col = 'darkblue'
                    placer.draw_boarder(screen)
                    drawn = False

            # BLUE THREE
            if placer.blue_placer_3.collidepoint(event.pos):
                placer.blue_border.centerx = placer.blue_placer_3.centerx
                placer.blue_border.centery = placer.blue_placer_3.centery
                if not drawn:
                    placer.border_col = 'white'
                    placer.draw_boarder(screen)
                    drawn = True
                    BLUE3 = True
                else:
                    placer.border_col = 'darkblue'
                    placer.draw_boarder(screen)
                    drawn = False

    # FOR MOVING
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            # BLUE ONE
            if selectable1 and selectable1y:
                if marker.marker_1.collidepoint(event.pos):
                    if drawn:
                        if BLUE1:
                            placer.blue_placer_1.centerx = marker.marker_1.centerx
                            placer.blue_placer_1.centery = marker.marker_1.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_1.centerx
                            placer.blue_border.centery = marker.marker_1.centery
                            selectable1 = False
                            selectable9 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE1 = False

            if selectable2 and selectable2y:
                if marker.marker_2.collidepoint(event.pos):
                    if drawn:
                        if BLUE1:
                            placer.blue_placer_1.centerx = marker.marker_2.centerx
                            placer.blue_placer_1.centery = marker.marker_2.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_2.centerx
                            placer.blue_border.centery = marker.marker_2.centery
                            selectable2 = False
                            selectable1 = True
                            selectable9 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE1 = False

            if selectable3 and selectable3y:
                if marker.marker_3.collidepoint(event.pos):
                    if drawn:
                        if BLUE1:
                            placer.blue_placer_1.centerx = marker.marker_3.centerx
                            placer.blue_placer_1.centery = marker.marker_3.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_3.centerx
                            placer.blue_border.centery = marker.marker_3.centery
                            selectable3 = False
                            selectable1 = True
                            selectable2 = True
                            selectable9 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE1 = False

            if selectable4 and selectable4y:
                if marker.marker_4.collidepoint(event.pos):
                    if drawn:
                        if BLUE1:
                            placer.blue_placer_1.centerx = marker.marker_4.centerx
                            placer.blue_placer_1.centery = marker.marker_4.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_4.centerx
                            placer.blue_border.centery = marker.marker_4.centery
                            selectable4 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable9 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE1 = False

            if selectable5 and selectable5y:
                if marker.marker_5.collidepoint(event.pos):
                    if drawn:
                        if BLUE1:
                            placer.blue_placer_1.centerx = marker.marker_5.centerx
                            placer.blue_placer_1.centery = marker.marker_5.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_5.centerx
                            placer.blue_border.centery = marker.marker_5.centery
                            selectable5 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable9 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE1 = False

            if selectable6 and selectable6y:
                if marker.marker_6.collidepoint(event.pos):
                    if drawn:
                        if BLUE1:
                            placer.blue_placer_1.centerx = marker.marker_6.centerx
                            placer.blue_placer_1.centery = marker.marker_6.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_6.centerx
                            placer.blue_border.centery = marker.marker_6.centery
                            selectable6 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable9 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE1 = False

            if selectable7 and selectable7y:
                if marker.marker_7.collidepoint(event.pos):
                    if drawn:
                        if BLUE1:
                            placer.blue_placer_1.centerx = marker.marker_7.centerx
                            placer.blue_placer_1.centery = marker.marker_7.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_7.centerx
                            placer.blue_border.centery = marker.marker_7.centery
                            selectable7 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable9 = True
                            selectable8 = True
                            BLUE1 = False

            if selectable8 and selectable7y:
                if marker.marker_8.collidepoint(event.pos):
                    if drawn:
                        if BLUE1:
                            placer.blue_placer_1.centerx = marker.marker_8.centerx
                            placer.blue_placer_1.centery = marker.marker_8.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_8.centerx
                            placer.blue_border.centery = marker.marker_8.centery
                            selectable8 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable9 = True
                            BLUE1 = False
            if selectable9 and selectable9y:
                if marker.marker_9.collidepoint(event.pos):
                    if drawn:
                        if BLUE1:
                            placer.blue_placer_1.centerx = marker.marker_9.centerx
                            placer.blue_placer_1.centery = marker.marker_9.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_9.centerx
                            placer.blue_border.centery = marker.marker_9.centery
                            selectable9 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE1 = False

            # BLUE TWO
            if selectable1 and selectable1y:
                if marker.marker_1.collidepoint(event.pos):
                    if drawn:
                        if BLUE2:
                            placer.blue_placer_2.centerx = marker.marker_1.centerx
                            placer.blue_placer_2.centery = marker.marker_1.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_1.centerx
                            placer.blue_border.centery = marker.marker_1.centery
                            selectable1 = False
                            selectable9 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE2 = False

            if selectable2 and selectable2y:
                if marker.marker_2.collidepoint(event.pos):
                    if drawn:
                        if BLUE2:
                            placer.blue_placer_2.centerx = marker.marker_2.centerx
                            placer.blue_placer_2.centery = marker.marker_2.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_2.centerx
                            placer.blue_border.centery = marker.marker_2.centery
                            selectable2 = False
                            selectable1 = True
                            selectable9 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE2 = False

            if selectable3 and selectable3y:
                if marker.marker_3.collidepoint(event.pos):
                    if drawn:
                        if BLUE2:
                            placer.blue_placer_2.centerx = marker.marker_3.centerx
                            placer.blue_placer_2.centery = marker.marker_3.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_3.centerx
                            placer.blue_border.centery = marker.marker_3.centery
                            selectable3 = False
                            selectable1 = True
                            selectable2 = True
                            selectable9 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE2 = False

            if selectable4 and selectable4y:
                if marker.marker_4.collidepoint(event.pos):
                    if drawn:
                        if BLUE2:
                            placer.blue_placer_2.centerx = marker.marker_4.centerx
                            placer.blue_placer_2.centery = marker.marker_4.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_4.centerx
                            placer.blue_border.centery = marker.marker_4.centery
                            selectable4 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable9 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE2 = False

            if selectable5 and selectable5y:
                if marker.marker_5.collidepoint(event.pos):
                    if drawn:
                        if BLUE2:
                            placer.blue_placer_2.centerx = marker.marker_5.centerx
                            placer.blue_placer_2.centery = marker.marker_5.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_5.centerx
                            placer.blue_border.centery = marker.marker_5.centery
                            selectable5 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable9 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE2 = False

            if selectable6 and selectable6y:
                if marker.marker_6.collidepoint(event.pos):
                    if drawn:
                        if BLUE2:
                            placer.blue_placer_2.centerx = marker.marker_6.centerx
                            placer.blue_placer_2.centery = marker.marker_6.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_6.centerx
                            placer.blue_border.centery = marker.marker_6.centery
                            selectable6 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable9 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE2 = False

            if selectable7 and selectable7y:
                if marker.marker_7.collidepoint(event.pos):
                    if drawn:
                        if BLUE2:
                            placer.blue_placer_2.centerx = marker.marker_7.centerx
                            placer.blue_placer_2.centery = marker.marker_7.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_7.centerx
                            placer.blue_border.centery = marker.marker_7.centery
                            selectable7 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable9 = True
                            selectable8 = True
                            BLUE2 = False

            if selectable8 and selectable8y:
                if marker.marker_8.collidepoint(event.pos):
                    if drawn:
                        if BLUE2:
                            placer.blue_placer_2.centerx = marker.marker_8.centerx
                            placer.blue_placer_2.centery = marker.marker_8.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_8.centerx
                            placer.blue_border.centery = marker.marker_8.centery
                            selectable8 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable9 = True
                            BLUE2 = False
            if selectable9 and selectable9y:
                if marker.marker_9.collidepoint(event.pos):
                    if drawn:
                        if BLUE2:
                            placer.blue_placer_2.centerx = marker.marker_9.centerx
                            placer.blue_placer_2.centery = marker.marker_9.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_9.centerx
                            placer.blue_border.centery = marker.marker_9.centery
                            selectable9 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE2 = False

            # BLUE THREE
            if selectable1 and selectable1y:
                if marker.marker_1.collidepoint(event.pos):
                    if drawn:
                        if BLUE3:
                            placer.blue_placer_3.centerx = marker.marker_1.centerx
                            placer.blue_placer_3.centery = marker.marker_1.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_1.centerx
                            placer.blue_border.centery = marker.marker_1.centery
                            selectable1 = False
                            selectable9 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE3 = False

            if selectable2 and selectable2y:
                if marker.marker_2.collidepoint(event.pos):
                    if drawn:
                        if BLUE3:
                            placer.blue_placer_3.centerx = marker.marker_2.centerx
                            placer.blue_placer_3.centery = marker.marker_2.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_2.centerx
                            placer.blue_border.centery = marker.marker_2.centery
                            selectable2 = False
                            selectable1 = True
                            selectable9 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE3 = False

            if selectable3 and selectable3y:
                if marker.marker_3.collidepoint(event.pos):
                    if drawn:
                        if BLUE3:
                            placer.blue_placer_3.centerx = marker.marker_3.centerx
                            placer.blue_placer_3.centery = marker.marker_3.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_3.centerx
                            placer.blue_border.centery = marker.marker_3.centery
                            selectable3 = False
                            selectable1 = True
                            selectable2 = True
                            selectable9 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE3 = False

            if selectable4 and selectable4y:
                if marker.marker_4.collidepoint(event.pos):
                    if drawn:
                        if BLUE3:
                            placer.blue_placer_3.centerx = marker.marker_4.centerx
                            placer.blue_placer_3.centery = marker.marker_4.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_4.centerx
                            placer.blue_border.centery = marker.marker_4.centery
                            selectable4 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable9 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE3 = False

            if selectable5 and selectable5y:
                if marker.marker_5.collidepoint(event.pos):
                    if drawn:
                        if BLUE3:
                            placer.blue_placer_3.centerx = marker.marker_5.centerx
                            placer.blue_placer_3.centery = marker.marker_5.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_5.centerx
                            placer.blue_border.centery = marker.marker_5.centery
                            selectable5 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable9 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE3 = False

            if selectable6 and selectable6y:
                if marker.marker_6.collidepoint(event.pos):
                    if drawn:
                        if BLUE3:
                            placer.blue_placer_3.centerx = marker.marker_6.centerx
                            placer.blue_placer_3.centery = marker.marker_6.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_6.centerx
                            placer.blue_border.centery = marker.marker_6.centery
                            selectable6 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable9 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE3 = False

            if selectable7 and selectable7y:
                if marker.marker_7.collidepoint(event.pos):
                    if drawn:
                        if BLUE3:
                            placer.blue_placer_3.centerx = marker.marker_7.centerx
                            placer.blue_placer_3.centery = marker.marker_7.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_7.centerx
                            placer.blue_border.centery = marker.marker_7.centery
                            selectable7 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable9 = True
                            selectable8 = True
                            BLUE3 = False

            if selectable8 and selectable8y:
                if marker.marker_8.collidepoint(event.pos):
                    if drawn:
                        if BLUE3:
                            placer.blue_placer_3.centerx = marker.marker_8.centerx
                            placer.blue_placer_3.centery = marker.marker_8.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_8.centerx
                            placer.blue_border.centery = marker.marker_8.centery
                            selectable8 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable9 = True
                            BLUE3 = False
            if selectable9 and selectable9y:
                if marker.marker_9.collidepoint(event.pos):
                    if drawn:
                        if BLUE3:
                            placer.blue_placer_3.centerx = marker.marker_9.centerx
                            placer.blue_placer_3.centery = marker.marker_9.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_9.centerx
                            placer.blue_border.centery = marker.marker_9.centery
                            selectable9 = False
                            selectable1 = True
                            selectable2 = True
                            selectable3 = True
                            selectable4 = True
                            selectable5 = True
                            selectable6 = True
                            selectable7 = True
                            selectable8 = True
                            BLUE3 = False


def yellow_mousing():
    global drawn, selectable1, BLUE1, BLUE2, BLUE3, YELLOW1, YELLOW2, YELLOW3, selectable2, selectable3, selectable4, selectable5, selectable6, selectable7, selectable8, selectable9
    global selectable1y, selectable2y, selectable3y, selectable4y, selectable5y, selectable6y, selectable7y, selectable8y, selectable9y
    # FOR SELECTING
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            # YELLOW ONE
            if placer.yellow_placer_1.collidepoint(event.pos):
                placer.blue_border.centerx = placer.yellow_placer_1.centerx
                placer.blue_border.centery = placer.yellow_placer_1.centery
                if not drawn:
                    placer.border_col = 'white'
                    placer.draw_boarder(screen)
                    drawn = True
                    YELLOW1 = True
                else:
                    placer.border_col = 'darkblue'
                    placer.draw_boarder(screen)
                    drawn = False

            # YELLOW TWO
            if placer.yellow_placer_2.collidepoint(event.pos):
                placer.blue_border.centerx = placer.yellow_placer_2.centerx
                placer.blue_border.centery = placer.yellow_placer_2.centery
                if not drawn:
                    placer.border_col = 'white'
                    placer.draw_boarder(screen)
                    drawn = True
                    YELLOW2 = True
                else:
                    placer.border_col = 'darkblue'
                    placer.draw_boarder(screen)
                    drawn = False

            # YELLOW THREE
            if placer.yellow_placer_3.collidepoint(event.pos):
                placer.blue_border.centerx = placer.yellow_placer_3.centerx
                placer.blue_border.centery = placer.yellow_placer_3.centery
                if not drawn:
                    placer.border_col = 'white'
                    placer.draw_boarder(screen)
                    drawn = True
                    YELLOW3 = True
                else:
                    placer.border_col = 'darkblue'
                    placer.draw_boarder(screen)
                    drawn = False

    # FOR MOVING
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:

            # YELLOW ONE
            if selectable1:
                if marker.marker_1.collidepoint(event.pos):
                    if drawn:
                        if YELLOW1:
                            placer.yellow_placer_1.centerx = marker.marker_1.centerx
                            placer.yellow_placer_1.centery = marker.marker_1.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_1.centerx
                            placer.blue_border.centery = marker.marker_1.centery
                            selectable1, selectable1y = False, False
                            selectable9, selectable9y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable6, selectable6y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW1 = False

            if selectable2:
                if marker.marker_2.collidepoint(event.pos):
                    if drawn:
                        if YELLOW1:
                            placer.yellow_placer_1.centerx = marker.marker_2.centerx
                            placer.yellow_placer_1.centery = marker.marker_2.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_2.centerx
                            placer.blue_border.centery = marker.marker_2.centery
                            selectable2, selectable2y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable9y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable6, selectable6y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW1 = False

            if selectable3:
                if marker.marker_3.collidepoint(event.pos):
                    if drawn:
                        if YELLOW1:
                            placer.yellow_placer_1.centerx = marker.marker_3.centerx
                            placer.yellow_placer_1.centery = marker.marker_3.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_3.centerx
                            placer.blue_border.centery = marker.marker_3.centery
                            selectable3, selectable3y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable9, selectable9y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable6, selectable6y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW1 = False

            if selectable4:
                if marker.marker_4.collidepoint(event.pos):
                    if drawn:
                        if YELLOW1:
                            placer.yellow_placer_1.centerx = marker.marker_4.centerx
                            placer.yellow_placer_1.centery = marker.marker_4.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_4.centerx
                            placer.blue_border.centery = marker.marker_4.centery
                            selectable4, selectable4y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable9, selectable9y = True, True
                            selectable5, selectable5y = True, True
                            selectable6, selectable6y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW1 = False

            if selectable5:
                if marker.marker_5.collidepoint(event.pos):
                    if drawn:
                        if YELLOW1:
                            placer.yellow_placer_1.centerx = marker.marker_5.centerx
                            placer.yellow_placer_1.centery = marker.marker_5.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_5.centerx
                            placer.blue_border.centery = marker.marker_5.centery
                            selectable5, selectable5y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable9, selectable9y = True, True
                            selectable6, selectable6y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW1 = False

            if selectable6:
                if marker.marker_6.collidepoint(event.pos):
                    if drawn:
                        if YELLOW1:
                            placer.yellow_placer_1.centerx = marker.marker_6.centerx
                            placer.yellow_placer_1.centery = marker.marker_6.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_6.centerx
                            placer.blue_border.centery = marker.marker_6.centery
                            selectable6, selectable6y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable9, selectable9y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW1 = False

            if selectable7:
                if marker.marker_7.collidepoint(event.pos):
                    if drawn:
                        if YELLOW1:
                            placer.yellow_placer_1.centerx = marker.marker_7.centerx
                            placer.yellow_placer_1.centery = marker.marker_7.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_7.centerx
                            placer.blue_border.centery = marker.marker_7.centery
                            selectable7, selectable7y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable6, selectable6y = True, True
                            selectable9, selectable9y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW1 = False

            if selectable8:
                if marker.marker_8.collidepoint(event.pos):
                    if drawn:
                        if YELLOW1:
                            placer.yellow_placer_1.centerx = marker.marker_8.centerx
                            placer.yellow_placer_1.centery = marker.marker_8.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_8.centerx
                            placer.blue_border.centery = marker.marker_8.centery
                            selectable8, selectable8y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable6, selectable6y = True, True
                            selectable7, selectable7y = True, True
                            selectable9, selectable9y = True, True
                            YELLOW1 = False
            if selectable9:
                if marker.marker_9.collidepoint(event.pos):
                    if drawn:
                        if YELLOW1:
                            placer.yellow_placer_1.centerx = marker.marker_9.centerx
                            placer.yellow_placer_1.centery = marker.marker_9.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_9.centerx
                            placer.blue_border.centery = marker.marker_9.centery
                            selectable9, selectable9y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable6, selectable6y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW1 = False

            # YELLOW TWO
            if selectable1:
                if marker.marker_1.collidepoint(event.pos):
                    if drawn:
                        if YELLOW2:
                            placer.yellow_placer_2.centerx = marker.marker_1.centerx
                            placer.yellow_placer_2.centery = marker.marker_1.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_1.centerx
                            placer.blue_border.centery = marker.marker_1.centery
                            selectable1, selectable1y = False, False
                            selectable6, selectable6y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable9, selectable9y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW2 = False

            if selectable2:
                if marker.marker_2.collidepoint(event.pos):
                    if drawn:
                        if YELLOW2:
                            placer.yellow_placer_2.centerx = marker.marker_2.centerx
                            placer.yellow_placer_2.centery = marker.marker_2.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_2.centerx
                            placer.blue_border.centery = marker.marker_2.centery
                            selectable2, selectable2y = False, False
                            selectable1, selectable1y = True, True
                            selectable6, selectable6y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable9, selectable9y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW2 = False

            if selectable3:
                if marker.marker_3.collidepoint(event.pos):
                    if drawn:
                        if YELLOW2:
                            placer.yellow_placer_2.centerx = marker.marker_3.centerx
                            placer.yellow_placer_2.centery = marker.marker_3.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_3.centerx
                            placer.blue_border.centery = marker.marker_3.centery
                            selectable3, selectable3y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable6, selectable6y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable9, selectable9y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW2 = False

            if selectable4:
                if marker.marker_4.collidepoint(event.pos):
                    if drawn:
                        if YELLOW2:
                            placer.yellow_placer_2.centerx = marker.marker_4.centerx
                            placer.yellow_placer_2.centery = marker.marker_4.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_4.centerx
                            placer.blue_border.centery = marker.marker_4.centery
                            selectable4, selectable4y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable6, selectable6y = True, True
                            selectable5, selectable5y = True, True
                            selectable9, selectable9y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW2 = False

            if selectable5:
                if marker.marker_5.collidepoint(event.pos):
                    if drawn:
                        if YELLOW2:
                            placer.yellow_placer_2.centerx = marker.marker_5.centerx
                            placer.yellow_placer_2.centery = marker.marker_5.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_5.centerx
                            placer.blue_border.centery = marker.marker_5.centery
                            selectable5, selectable5y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable6, selectable6y = True, True
                            selectable9, selectable9y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW2 = False

            if selectable6:
                if marker.marker_6.collidepoint(event.pos):
                    if drawn:
                        if YELLOW2:
                            placer.yellow_placer_2.centerx = marker.marker_6.centerx
                            placer.yellow_placer_2.centery = marker.marker_6.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_6.centerx
                            placer.blue_border.centery = marker.marker_6.centery
                            selectable6, selectable6y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable9, selectable9y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW2 = False

            if selectable7:
                if marker.marker_7.collidepoint(event.pos):
                    if drawn:
                        if YELLOW2:
                            placer.yellow_placer_2.centerx = marker.marker_7.centerx
                            placer.yellow_placer_2.centery = marker.marker_7.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_7.centerx
                            placer.blue_border.centery = marker.marker_7.centery
                            selectable7, selectable7y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable9, selectable9y = True, True
                            selectable6, selectable6y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW2 = False

            if selectable8:
                if marker.marker_8.collidepoint(event.pos):
                    if drawn:
                        if YELLOW2:
                            placer.yellow_placer_2.centerx = marker.marker_8.centerx
                            placer.yellow_placer_2.centery = marker.marker_8.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_8.centerx
                            placer.blue_border.centery = marker.marker_8.centery
                            selectable8, selectable8y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable9, selectable9y = True, True
                            selectable7, selectable7y = True, True
                            selectable6, selectable6y = True, True
                            YELLOW2 = False
            if selectable9:
                if marker.marker_9.collidepoint(event.pos):
                    if drawn:
                        if YELLOW2:
                            placer.yellow_placer_2.centerx = marker.marker_9.centerx
                            placer.yellow_placer_2.centery = marker.marker_9.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_9.centerx
                            placer.blue_border.centery = marker.marker_9.centery
                            selectable9, selectable9y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable6, selectable6y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW2 = False

            # YELLOW THREE
            if selectable1:
                if marker.marker_1.collidepoint(event.pos):
                    if drawn:
                        if YELLOW3:
                            placer.yellow_placer_3.centerx = marker.marker_1.centerx
                            placer.yellow_placer_3.centery = marker.marker_1.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_1.centerx
                            placer.blue_border.centery = marker.marker_1.centery
                            selectable1, selectable1y = False, False
                            selectable9, selectable9y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable9, selectable9y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW3 = False

            if selectable2:
                if marker.marker_2.collidepoint(event.pos):
                    if drawn:
                        if YELLOW3:
                            placer.yellow_placer_3.centerx = marker.marker_2.centerx
                            placer.yellow_placer_3.centery = marker.marker_2.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_2.centerx
                            placer.blue_border.centery = marker.marker_2.centery
                            selectable2, selectable2y = False, False
                            selectable1, selectable1y = True, True
                            selectable9, selectable9y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable9, selectable9y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW3 = False

            if selectable3:
                if marker.marker_3.collidepoint(event.pos):
                    if drawn:
                        if YELLOW3:
                            placer.yellow_placer_3.centerx = marker.marker_3.centerx
                            placer.yellow_placer_3.centery = marker.marker_3.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_3.centerx
                            placer.blue_border.centery = marker.marker_3.centery
                            selectable3, selectable3y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable9, selectable9y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable9, selectable9y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW3 = False

            if selectable4:
                if marker.marker_4.collidepoint(event.pos):
                    if drawn:
                        if YELLOW3:
                            placer.yellow_placer_3.centerx = marker.marker_4.centerx
                            placer.yellow_placer_3.centery = marker.marker_4.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_4.centerx
                            placer.blue_border.centery = marker.marker_4.centery
                            selectable4, selectable4y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable9, selectable9y = True, True
                            selectable5, selectable5y = True, True
                            selectable9, selectable9y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW3 = False

            if selectable5:
                if marker.marker_5.collidepoint(event.pos):
                    if drawn:
                        if YELLOW3:
                            placer.yellow_placer_3.centerx = marker.marker_5.centerx
                            placer.yellow_placer_3.centery = marker.marker_5.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_5.centerx
                            placer.blue_border.centery = marker.marker_5.centery
                            selectable5, selectable5y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable9, selectable9y = True, True
                            selectable9, selectable9y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW3 = False

            if selectable6:
                if marker.marker_6.collidepoint(event.pos):
                    if drawn:
                        if YELLOW3:
                            placer.yellow_placer_3.centerx = marker.marker_6.centerx
                            placer.yellow_placer_3.centery = marker.marker_6.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_6.centerx
                            placer.blue_border.centery = marker.marker_6.centery
                            selectable6, selectable6y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable9, selectable9y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW3 = False

            if selectable7:
                if marker.marker_7.collidepoint(event.pos):
                    if drawn:
                        if YELLOW3:
                            placer.yellow_placer_3.centerx = marker.marker_7.centerx
                            placer.yellow_placer_3.centery = marker.marker_7.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_7.centerx
                            placer.blue_border.centery = marker.marker_7.centery
                            selectable7, selectable7y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable6, selectable6y = True, True
                            selectable9, selectable9y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW3 = False

            if selectable8:
                if marker.marker_8.collidepoint(event.pos):
                    if drawn:
                        if YELLOW3:
                            placer.yellow_placer_3.centerx = marker.marker_8.centerx
                            placer.yellow_placer_3.centery = marker.marker_8.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_8.centerx
                            placer.blue_border.centery = marker.marker_8.centery
                            selectable8, selectable8y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable6, selectable6y = True, True
                            selectable7, selectable7y = True, True
                            selectable9, selectable9y = True, True
                            YELLOW3 = False
            if selectable9:
                if marker.marker_9.collidepoint(event.pos):
                    if drawn:
                        if YELLOW3:
                            placer.yellow_placer_3.centerx = marker.marker_9.centerx
                            placer.yellow_placer_3.centery = marker.marker_9.centery
                            drawn = False
                            placer.blue_border.centerx = marker.marker_9.centerx
                            placer.blue_border.centery = marker.marker_9.centery
                            selectable9, selectable9y = False, False
                            selectable1, selectable1y = True, True
                            selectable2, selectable2y = True, True
                            selectable3, selectable3y = True, True
                            selectable4, selectable4y = True, True
                            selectable5, selectable5y = True, True
                            selectable6, selectable6y = True, True
                            selectable7, selectable7y = True, True
                            selectable8, selectable8y = True, True
                            YELLOW3 = False


marker = Marker()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        blue_mousing()
        yellow_mousing()

    screen.fill((222, 14, 188))
    draw_board(screen)
    placer.draw_boarder(screen)
    marker.draw_marker(screen)
    placer.draw_blues(screen)
    placer.draw_yellows(screen)
    pg.display.update()
    clock.tick(fps)
