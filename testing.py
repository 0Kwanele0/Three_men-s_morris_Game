import pygame as pg
from sys import exit

pg.init()
width = 750
height = 590
window = pg.display.set_mode((width, height))

drawn = False
clock = pg.time.Clock()
fps = 260

BLUE1, BLUE2, BLUE3 = False, False, False

YELLOW1, YELLOW2, YELLOW3 = False, False, False


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
    global drawn, BLUE1, BLUE2, BLUE3
    # FOR SELECTING
    def moveMove(drawn, placer, marker, border, move):
        if drawn:
            if move:
                placer.centerx = marker.centerx
                placer.centery = marker.centery
                drawn = False
                border.centerx = marker.centerx
                border.centery = marker.centery
                move = False 
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            # BLUE ONE
            if placer.blue_placer_1.collidepoint(event.pos):
                placer.blue_border.centerx = placer.blue_placer_1.centerx
                placer.blue_border.centery = placer.blue_placer_1.centery
                if not drawn:
                    placer.border_col = 'white'
                    placer.draw_boarder(window)
                    drawn = True
                    BLUE1 = True
                else:
                    placer.border_col = 'darkblue'
                    placer.draw_boarder(window)
                    drawn = False

            # BLUE TWO
            if placer.blue_placer_2.collidepoint(event.pos):
                placer.blue_border.centerx = placer.blue_placer_2.centerx
                placer.blue_border.centery = placer.blue_placer_2.centery
                if not drawn:
                    placer.border_col = 'white'
                    placer.draw_boarder(window)
                    drawn = True
                    BLUE2 = True
                else:
                    placer.border_col = 'darkblue'
                    placer.draw_boarder(window)
                    drawn = False

            # BLUE THREE
            if placer.blue_placer_3.collidepoint(event.pos):
                placer.blue_border.centerx = placer.blue_placer_3.centerx
                placer.blue_border.centery = placer.blue_placer_3.centery
                if not drawn:
                    placer.border_col = 'white'
                    placer.draw_boarder(window)
                    drawn = True
                    BLUE3 = True
                else:
                    placer.border_col = 'darkblue'
                    placer.draw_boarder(window)
                    drawn = False

    # FOR MOVING
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            # BLUE ONE
            
            if marker.marker_1.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_1, placer.blue_border, BLUE1)
            if marker.marker_2.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_2, placer.blue_border, BLUE1)
            if marker.marker_3.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_3, placer.blue_border, BLUE1)
            if marker.marker_4.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_4, placer.blue_border, BLUE1)
            if marker.marker_5.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_5, placer.blue_border, BLUE1)
            if marker.marker_6.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_6, placer.blue_border, BLUE1)
            if marker.marker_7.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_7, placer.blue_border, BLUE1)
            if marker.marker_8.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_8, placer.blue_border, BLUE1)
            if marker.marker_9.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_9, placer.blue_border, BLUE1)
                
            # BLUE TWO
            if marker.marker_1.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_1, placer.blue_border, BLUE2)
            if marker.marker_2.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_2, placer.blue_border, BLUE2)
            if marker.marker_3.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_3, placer.blue_border, BLUE2)
            if marker.marker_4.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_4, placer.blue_border, BLUE2)
            if marker.marker_5.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_5, placer.blue_border, BLUE2)
            if marker.marker_6.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_6, placer.blue_border, BLUE2)
            if marker.marker_7.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_7, placer.blue_border, BLUE2)
            if marker.marker_8.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_8, placer.blue_border, BLUE2)
            if marker.marker_9.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_9, placer.blue_border, BLUE2)
            
            # BLUE THREE
            if marker.marker_1.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_1, placer.blue_border, BLUE3)
            if marker.marker_2.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_2, placer.blue_border, BLUE3)
            if marker.marker_3.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_3, placer.blue_border, BLUE3)
            if marker.marker_4.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_4, placer.blue_border, BLUE3)
            if marker.marker_5.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_5, placer.blue_border, BLUE3)
            if marker.marker_6.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_6, placer.blue_border, BLUE3)
            if marker.marker_7.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_7, placer.blue_border, BLUE3)
            if marker.marker_8.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_8, placer.blue_border, BLUE3)
            if marker.marker_9.collidepoint(event.pos):
                moveMove(drawn, placer.blue_placer_1, marker.marker_9, placer.blue_border, BLUE3)
            


def yellow_mousing():
    global drawn, BLUE1, BLUE2, BLUE3, YELLOW1, YELLOW2, YELLOW3
    # FOR SELECTING
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            # YELLOW ONE
            if placer.yellow_placer_1.collidepoint(event.pos):
                placer.blue_border.centerx = placer.yellow_placer_1.centerx
                placer.blue_border.centery = placer.yellow_placer_1.centery
                if not drawn:
                    placer.border_col = 'white'
                    placer.draw_boarder(window)
                    drawn = True
                    YELLOW1 = True
                else:
                    placer.border_col = 'darkblue'
                    placer.draw_boarder(window)
                    drawn = False

            # YELLOW TWO
            if placer.yellow_placer_2.collidepoint(event.pos):
                placer.blue_border.centerx = placer.yellow_placer_2.centerx
                placer.blue_border.centery = placer.yellow_placer_2.centery
                if not drawn:
                    placer.border_col = 'white'
                    placer.draw_boarder(window)
                    drawn = True
                    YELLOW2 = True
                else:
                    placer.border_col = 'darkblue'
                    placer.draw_boarder(window)
                    drawn = False

            # YELLOW THREE
            if placer.yellow_placer_3.collidepoint(event.pos):
                placer.blue_border.centerx = placer.yellow_placer_3.centerx
                placer.blue_border.centery = placer.yellow_placer_3.centery
                if not drawn:
                    placer.border_col = 'white'
                    placer.draw_boarder(window)
                    drawn = True
                    YELLOW3 = True
                else:
                    placer.border_col = 'darkblue'
                    placer.draw_boarder(window)
                    drawn = False

    # FOR MOVING
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:

            # YELLOW ONE
            if marker.marker_1.collidepoint(event.pos):
                if drawn:
                    if YELLOW1:
                        placer.yellow_placer_1.centerx = marker.marker_1.centerx
                        placer.yellow_placer_1.centery = marker.marker_1.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_1.centerx
                        placer.blue_border.centery = marker.marker_1.centery
                        YELLOW1 = False

            if marker.marker_2.collidepoint(event.pos):
                if drawn:
                    if YELLOW1:
                        placer.yellow_placer_1.centerx = marker.marker_2.centerx
                        placer.yellow_placer_1.centery = marker.marker_2.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_2.centerx
                        placer.blue_border.centery = marker.marker_2.centery
                        YELLOW1 = False

            if marker.marker_3.collidepoint(event.pos):
                if drawn:
                    if YELLOW1:
                        placer.yellow_placer_1.centerx = marker.marker_3.centerx
                        placer.yellow_placer_1.centery = marker.marker_3.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_3.centerx
                        placer.blue_border.centery = marker.marker_3.centery
                        YELLOW1 = False

            if marker.marker_4.collidepoint(event.pos):
                if drawn:
                    if YELLOW1:
                        placer.yellow_placer_1.centerx = marker.marker_4.centerx
                        placer.yellow_placer_1.centery = marker.marker_4.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_4.centerx
                        placer.blue_border.centery = marker.marker_4.centery
                        YELLOW1 = False

            if marker.marker_5.collidepoint(event.pos):
                if drawn:
                    if YELLOW1:
                        placer.yellow_placer_1.centerx = marker.marker_5.centerx
                        placer.yellow_placer_1.centery = marker.marker_5.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_5.centerx
                        placer.blue_border.centery = marker.marker_5.centery
                        YELLOW1 = False

            if marker.marker_6.collidepoint(event.pos):
                if drawn:
                    if YELLOW1:
                        placer.yellow_placer_1.centerx = marker.marker_6.centerx
                        placer.yellow_placer_1.centery = marker.marker_6.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_6.centerx
                        placer.blue_border.centery = marker.marker_6.centery
                        YELLOW1 = False

            if marker.marker_7.collidepoint(event.pos):
                if drawn:
                    if YELLOW1:
                        placer.yellow_placer_1.centerx = marker.marker_7.centerx
                        placer.yellow_placer_1.centery = marker.marker_7.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_7.centerx
                        placer.blue_border.centery = marker.marker_7.centery
                        YELLOW1 = False

            if marker.marker_8.collidepoint(event.pos):
                if drawn:
                    if YELLOW1:
                        placer.yellow_placer_1.centerx = marker.marker_8.centerx
                        placer.yellow_placer_1.centery = marker.marker_8.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_8.centerx
                        placer.blue_border.centery = marker.marker_8.centery
                        YELLOW1 = False

            if marker.marker_9.collidepoint(event.pos):
                if drawn:
                    if YELLOW1:
                        placer.yellow_placer_1.centerx = marker.marker_9.centerx
                        placer.yellow_placer_1.centery = marker.marker_9.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_9.centerx
                        placer.blue_border.centery = marker.marker_9.centery
                        YELLOW1 = False

            # YELLOW TWO
            if marker.marker_1.collidepoint(event.pos):
                if drawn:
                    if YELLOW2:
                        placer.yellow_placer_2.centerx = marker.marker_1.centerx
                        placer.yellow_placer_2.centery = marker.marker_1.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_1.centerx
                        placer.blue_border.centery = marker.marker_1.centery
                        YELLOW2 = False

            if marker.marker_2.collidepoint(event.pos):
                if drawn:
                    if YELLOW2:
                        placer.yellow_placer_2.centerx = marker.marker_2.centerx
                        placer.yellow_placer_2.centery = marker.marker_2.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_2.centerx
                        placer.blue_border.centery = marker.marker_2.centery
                        YELLOW2 = False

            if marker.marker_3.collidepoint(event.pos):
                if drawn:
                    if YELLOW2:
                        placer.yellow_placer_2.centerx = marker.marker_3.centerx
                        placer.yellow_placer_2.centery = marker.marker_3.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_3.centerx
                        placer.blue_border.centery = marker.marker_3.centery
                        YELLOW2 = False

            if marker.marker_4.collidepoint(event.pos):
                if drawn:
                    if YELLOW2:
                        placer.yellow_placer_2.centerx = marker.marker_4.centerx
                        placer.yellow_placer_2.centery = marker.marker_4.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_4.centerx
                        placer.blue_border.centery = marker.marker_4.centery
                        YELLOW2 = False

            if marker.marker_5.collidepoint(event.pos):
                if drawn:
                    if YELLOW2:
                        placer.yellow_placer_2.centerx = marker.marker_5.centerx
                        placer.yellow_placer_2.centery = marker.marker_5.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_5.centerx
                        placer.blue_border.centery = marker.marker_5.centery
                        YELLOW2 = False

            if marker.marker_6.collidepoint(event.pos):
                if drawn:
                    if YELLOW2:
                        placer.yellow_placer_2.centerx = marker.marker_6.centerx
                        placer.yellow_placer_2.centery = marker.marker_6.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_6.centerx
                        placer.blue_border.centery = marker.marker_6.centery
                        YELLOW2 = False

            if marker.marker_7.collidepoint(event.pos):
                if drawn:
                    if YELLOW2:
                        placer.yellow_placer_2.centerx = marker.marker_7.centerx
                        placer.yellow_placer_2.centery = marker.marker_7.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_7.centerx
                        placer.blue_border.centery = marker.marker_7.centery
                        YELLOW2 = False

            if marker.marker_8.collidepoint(event.pos):
                if drawn:
                    if YELLOW2:
                        placer.yellow_placer_2.centerx = marker.marker_8.centerx
                        placer.yellow_placer_2.centery = marker.marker_8.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_8.centerx
                        placer.blue_border.centery = marker.marker_8.centery
                        YELLOW2 = False

            if marker.marker_9.collidepoint(event.pos):
                if drawn:
                    if YELLOW2:
                        placer.yellow_placer_2.centerx = marker.marker_9.centerx
                        placer.yellow_placer_2.centery = marker.marker_9.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_9.centerx
                        placer.blue_border.centery = marker.marker_9.centery
                        YELLOW2 = False

            # YELLOW THREE
            if marker.marker_1.collidepoint(event.pos):
                if drawn:
                    if YELLOW3:
                        placer.yellow_placer_3.centerx = marker.marker_1.centerx
                        placer.yellow_placer_3.centery = marker.marker_1.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_1.centerx
                        placer.blue_border.centery = marker.marker_1.centery
                        YELLOW3 = False

            if marker.marker_2.collidepoint(event.pos):
                if drawn:
                    if YELLOW3:
                        placer.yellow_placer_3.centerx = marker.marker_2.centerx
                        placer.yellow_placer_3.centery = marker.marker_2.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_2.centerx
                        placer.blue_border.centery = marker.marker_2.centery
                        YELLOW3 = False

            if marker.marker_3.collidepoint(event.pos):
                if drawn:
                    if YELLOW3:
                        placer.yellow_placer_3.centerx = marker.marker_3.centerx
                        placer.yellow_placer_3.centery = marker.marker_3.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_3.centerx
                        placer.blue_border.centery = marker.marker_3.centery
                        YELLOW3 = False

            if marker.marker_4.collidepoint(event.pos):
                if drawn:
                    if YELLOW3:
                        placer.yellow_placer_3.centerx = marker.marker_4.centerx
                        placer.yellow_placer_3.centery = marker.marker_4.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_4.centerx
                        placer.blue_border.centery = marker.marker_4.centery
                        YELLOW3 = False

            if marker.marker_5.collidepoint(event.pos):
                if drawn:
                    if YELLOW3:
                        placer.yellow_placer_3.centerx = marker.marker_5.centerx
                        placer.yellow_placer_3.centery = marker.marker_5.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_5.centerx
                        placer.blue_border.centery = marker.marker_5.centery
                        YELLOW3 = False

            if marker.marker_6.collidepoint(event.pos):
                if drawn:
                    if YELLOW3:
                        placer.yellow_placer_3.centerx = marker.marker_6.centerx
                        placer.yellow_placer_3.centery = marker.marker_6.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_6.centerx
                        placer.blue_border.centery = marker.marker_6.centery
                        YELLOW3 = False

            if marker.marker_7.collidepoint(event.pos):
                if drawn:
                    if YELLOW3:
                        placer.yellow_placer_3.centerx = marker.marker_7.centerx
                        placer.yellow_placer_3.centery = marker.marker_7.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_7.centerx
                        placer.blue_border.centery = marker.marker_7.centery
                        YELLOW3 = False

            if marker.marker_8.collidepoint(event.pos):
                if drawn:
                    if YELLOW3:
                        placer.yellow_placer_3.centerx = marker.marker_8.centerx
                        placer.yellow_placer_3.centery = marker.marker_8.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_8.centerx
                        placer.blue_border.centery = marker.marker_8.centery
                        YELLOW3 = False

            if marker.marker_9.collidepoint(event.pos):
                if drawn:
                    if YELLOW3:
                        placer.yellow_placer_3.centerx = marker.marker_9.centerx
                        placer.yellow_placer_3.centery = marker.marker_9.centery
                        drawn = False
                        placer.blue_border.centerx = marker.marker_9.centerx
                        placer.blue_border.centery = marker.marker_9.centery
                        YELLOW3 = False


marker = Marker()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        blue_mousing()
        yellow_mousing()

    window.fill((222, 14, 188))
    draw_board(window)
    placer.draw_boarder(window)
    marker.draw_marker(window)
    placer.draw_blues(window)
    placer.draw_yellows(window)
    pg.display.update()
    clock.tick(fps)
