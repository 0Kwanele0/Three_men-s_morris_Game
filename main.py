import pygame as pg
from sys import exit
from time import sleep
from board import Markers
from board import draw_board
from placers import Placers

pg.init()

fps = 60
clock = pg.time.Clock()
screen = pg.display.set_mode((650, 590))
pg.display.set_caption("Three men's morris")

dragging = False
offset_x = 0
offset_y = 0

held_1 = False
held_2 = False
held_3 = False

y_held_1 = False
y_held_2 = False
y_held_3 = False

blue_position_1 = 0
blue_position_2 = 0
blue_position_3 = 0

yellow_position_1 = 0
yellow_position_2 = 0
yellow_position_3 = 0

message_1 = "Blue start"
res_message = "Restart"
quit_message = "Quit"

start_pos = (0, 0)
end_pos = (0, 0)
winner = False

marker = Markers()
placer = Placers()


def draw_line():
    pg.draw.line(screen, "green", start_pos, end_pos, 10)


def draw_status():
    display = pg.Surface((200, 50))
    show = display.get_rect(center=(275, 30))
    pg.draw.rect(screen, (255, 120, 185), show)
    font = pg.font.SysFont("gilroy", 35, 1)
    text = font.render(message_1, True, (255, 255, 255))
    text_rect = text.get_rect(center=(275, 30))
    screen.blit(text, text_rect)


def draw_button():
    global quit_rect, resert_rect

    display = pg.Surface((110, 50))
    show = display.get_rect(center=(550, 235))
    pg.draw.rect(screen, "white", show, border_radius=15)
    font = pg.font.SysFont("gotham", 30, 4)
    resert = font.render(res_message, True, (1, 14, 122))
    resert_rect = resert.get_rect(center=(550, 235))
    screen.blit(resert, resert_rect)

    display = pg.Surface((110, 50))
    show = display.get_rect(center=(550, 310))
    pg.draw.rect(screen, "white", show, border_radius=15)
    font = pg.font.SysFont("gotham", 30, 4)
    quit = font.render(quit_message, True, (1, 14, 122))
    quit_rect = quit.get_rect(center=(550, 310))
    screen.blit(quit, quit_rect)


def check_button_click():
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            if quit_rect.collidepoint(event.pos):
                sleep(.5)
                exit()
            elif resert_rect.collidepoint(event.pos):
                sleep(.5)
                re_start()


def blue_mouse_moves():
    global dragging, offset_x, offset_y, held_1, held_3, held_2, mouse_x, mouse_y, blue_position_1, blue_position_2, blue_position_3, message_1
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            if placer.blue_1.collidepoint(event.pos):
                dragging = True
                held_1 = True
                mouse_x, mouse_y = event.pos
                offset_x = placer.blue_1.x - mouse_x
                offset_y = placer.blue_1.y - mouse_y

            elif placer.blue_2.collidepoint(event.pos):
                dragging = True
                held_2 = True
                mouse_x, mouse_y = event.pos
                offset_x = placer.blue_2.x - mouse_x
                offset_y = placer.blue_2.y - mouse_y

            elif placer.blue_3.collidepoint(event.pos):
                dragging = True
                held_3 = True
                mouse_x, mouse_y = event.pos
                offset_x = placer.blue_3.x - mouse_x
                offset_y = placer.blue_3.y - mouse_y

    elif event.type == pg.MOUSEBUTTONUP:
        if event.button == 1:
            dragging = False

    elif event.type == pg.MOUSEMOTION:
        if held_1 and placer.blue_1.collidepoint(event.pos):
            if dragging:
                mouse_x, mouse_y = event.pos
                placer.blue_1.x = mouse_x + offset_x
                placer.blue_1.y = mouse_y + offset_y

                if placer.blue_1.x in range(70, 130) and placer.blue_1.y in range(70, 130):
                    placer.blue_1.centerx = 100
                    placer.blue_1.centery = 100
                    blue_position_1 = 1
                    message_1 = "Yellow's turn"

                elif placer.blue_1.x in range(70, 130) and placer.blue_1.y in range(430, 480):
                    placer.blue_1.centerx = 100
                    placer.blue_1.centery = 450
                    blue_position_1 = 7
                    message_1 = "Yellow's turn"

                elif placer.blue_1.x in range(420, 480) and placer.blue_1.y in range(70, 130):
                    placer.blue_1.centerx = 450
                    placer.blue_1.centery = 100
                    blue_position_1 = 3
                    message_1 = "Yellow's turn"

                elif placer.blue_1.x in range(420, 480) and placer.blue_1.y in range(420, 480):
                    placer.blue_1.centerx = 450
                    placer.blue_1.centery = 450
                    blue_position_1 = 9
                    message_1 = "Yellow's turn"

                elif placer.blue_1.x in range(70, 130) and placer.blue_1.y in range(245, 315):
                    placer.blue_1.centerx = 100
                    placer.blue_1.centery = 275
                    blue_position_1 = 4
                    message_1 = "Yellow's turn"

                elif placer.blue_1.x in range(245, 315) and placer.blue_1.y in range(70, 130):
                    placer.blue_1.centerx = 275
                    placer.blue_1.centery = 100
                    blue_position_1 = 2
                    message_1 = "Yellow's turn"

                elif placer.blue_1.x in range(245, 315) and placer.blue_1.y in range(420, 480):
                    placer.blue_1.centerx = 275
                    placer.blue_1.centery = 450
                    blue_position_1 = 8
                    message_1 = "Yellow's turn"

                elif placer.blue_1.x in range(420, 480) and placer.blue_1.y in range(245, 315):
                    placer.blue_1.centerx = 450
                    placer.blue_1.centery = 275
                    blue_position_1 = 6
                    message_1 = "Yellow's turn"

                elif placer.blue_1.x in range(245, 315) and placer.blue_1.y in range(245, 315):
                    placer.blue_1.centerx = 275
                    placer.blue_1.centery = 275
                    blue_position_1 = 5
                    message_1 = "Yellow's turn"

        elif held_2 and placer.blue_2.collidepoint(event.pos):
            if dragging:
                mouse_x, mouse_y = event.pos
                placer.blue_2.x = mouse_x + offset_x
                placer.blue_2.y = mouse_y + offset_y

                if placer.blue_2.x in range(70, 130) and placer.blue_2.y in range(70, 130):
                    placer.blue_2.centerx = 100
                    placer.blue_2.centery = 100
                    blue_position_2 = 1
                    message_1 = "Yellow's turn"

                elif placer.blue_2.x in range(70, 130) and placer.blue_2.y in range(430, 480):
                    placer.blue_2.centerx = 100
                    placer.blue_2.centery = 450
                    blue_position_2 = 7
                    message_1 = "Yellow's turn"

                elif placer.blue_2.x in range(420, 480) and placer.blue_2.y in range(70, 130):
                    placer.blue_2.centerx = 450
                    placer.blue_2.centery = 100
                    blue_position_2 = 3
                    message_1 = "Yellow's turn"

                elif placer.blue_2.x in range(420, 480) and placer.blue_2.y in range(420, 480):
                    placer.blue_2.centerx = 450
                    placer.blue_2.centery = 450
                    blue_position_2 = 9
                    message_1 = "Yellow's turn"

                elif placer.blue_2.x in range(70, 130) and placer.blue_2.y in range(245, 315):
                    placer.blue_2.centerx = 100
                    placer.blue_2.centery = 275
                    blue_position_2 = 4
                    message_1 = "Yellow's turn"

                elif placer.blue_2.x in range(245, 315) and placer.blue_2.y in range(70, 130):
                    placer.blue_2.centerx = 275
                    placer.blue_2.centery = 100
                    blue_position_2 = 2
                    message_1 = "Yellow's turn"

                elif placer.blue_2.x in range(245, 315) and placer.blue_2.y in range(420, 480):
                    placer.blue_2.centerx = 275
                    placer.blue_2.centery = 450
                    blue_position_2 = 8
                    message_1 = "Yellow's turn"

                elif placer.blue_2.x in range(420, 480) and placer.blue_2.y in range(245, 315):
                    placer.blue_2.centerx = 450
                    placer.blue_2.centery = 275
                    blue_position_2 = 6
                    message_1 = "Yellow's turn"

                elif placer.blue_2.x in range(245, 315) and placer.blue_2.y in range(245, 315):
                    placer.blue_2.centerx = 275
                    placer.blue_2.centery = 275
                    blue_position_2 = 5
                    message_1 = "Yellow's turn"

        elif held_3 and placer.blue_3.collidepoint(event.pos):
            if dragging:
                mouse_x, mouse_y = event.pos
                placer.blue_3.x = mouse_x + offset_x
                placer.blue_3.y = mouse_y + offset_y

                if placer.blue_3.x in range(70, 130) and placer.blue_3.y in range(70, 130):
                    placer.blue_3.centerx = 100
                    placer.blue_3.centery = 100
                    blue_position_3 = 1
                    message_1 = "Yellow's turn"

                elif placer.blue_3.x in range(70, 130) and placer.blue_3.y in range(430, 480):
                    placer.blue_3.centerx = 100
                    placer.blue_3.centery = 450
                    blue_position_3 = 7
                    message_1 = "Yellow's turn"

                elif placer.blue_3.x in range(420, 480) and placer.blue_3.y in range(70, 130):
                    placer.blue_3.centerx = 450
                    placer.blue_3.centery = 100
                    blue_position_3 = 3
                    message_1 = "Yellow's turn"

                elif placer.blue_3.x in range(420, 480) and placer.blue_3.y in range(420, 480):
                    placer.blue_3.centerx = 450
                    placer.blue_3.centery = 450
                    blue_position_3 = 9
                    message_1 = "Yellow's turn"

                elif placer.blue_3.x in range(70, 130) and placer.blue_3.y in range(245, 315):
                    placer.blue_3.centerx = 100
                    placer.blue_3.centery = 275
                    blue_position_3 = 4
                    message_1 = "Yellow's turn"

                elif placer.blue_3.x in range(245, 315) and placer.blue_3.y in range(70, 130):
                    placer.blue_3.centerx = 275
                    placer.blue_3.centery = 100
                    blue_position_3 = 2
                    message_1 = "Yellow's turn"

                elif placer.blue_3.x in range(245, 315) and placer.blue_3.y in range(420, 480):
                    placer.blue_3.centerx = 275
                    placer.blue_3.centery = 450
                    blue_position_3 = 8
                    message_1 = "Yellow's turn"

                elif placer.blue_3.x in range(420, 480) and placer.blue_3.y in range(245, 315):
                    placer.blue_3.centerx = 450
                    placer.blue_3.centery = 275
                    blue_position_3 = 6
                    message_1 = "Yellow's turn"

                elif placer.blue_3.x in range(245, 315) and placer.blue_3.y in range(245, 315):
                    placer.blue_3.centerx = 275
                    placer.blue_3.centery = 275
                    blue_position_3 = 5
                    message_1 = "Yellow's turn"


def yellow_mouse_moves():
    global dragging, offset_x, offset_y, held_1, held_3, held_2, mouse_x, mouse_y, y_held_1, y_held_3, y_held_2, yellow_position_1, yellow_position_2, yellow_position_3, message_1
    if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
            if placer.yellow_1.collidepoint(event.pos):
                dragging = True
                y_held_1 = True
                mouse_x, mouse_y = event.pos
                offset_x = placer.yellow_1.x - mouse_x
                offset_y = placer.yellow_1.y - mouse_y

            elif placer.yellow_2.collidepoint(event.pos):
                dragging = True
                y_held_2 = True
                mouse_x, mouse_y = event.pos
                offset_x = placer.yellow_2.x - mouse_x
                offset_y = placer.yellow_2.y - mouse_y

            elif placer.yellow_3.collidepoint(event.pos):
                dragging = True
                y_held_3 = True
                mouse_x, mouse_y = event.pos
                offset_x = placer.yellow_3.x - mouse_x
                offset_y = placer.yellow_3.y - mouse_y

    elif event.type == pg.MOUSEBUTTONUP:
        if event.button == 1:
            dragging = False

    elif event.type == pg.MOUSEMOTION:
        if held_1 and placer.yellow_1.collidepoint(event.pos):
            if dragging:
                mouse_x, mouse_y = event.pos
                placer.yellow_1.x = mouse_x + offset_x
                placer.yellow_1.y = mouse_y + offset_y

                if placer.yellow_1.x in range(70, 130) and placer.yellow_1.y in range(70, 130):
                    placer.yellow_1.centerx = 100
                    placer.yellow_1.centery = 100
                    yellow_position_1 = 1
                    message_1 = "Blue's turn"

                elif placer.yellow_1.x in range(70, 130) and placer.yellow_1.y in range(430, 480):
                    placer.yellow_1.centerx = 100
                    placer.yellow_1.centery = 450
                    yellow_position_1 = 7
                    message_1 = "Blue's turn"

                elif placer.yellow_1.x in range(420, 480) and placer.yellow_1.y in range(70, 130):
                    placer.yellow_1.centerx = 450
                    placer.yellow_1.centery = 100
                    yellow_position_1 = 3
                    message_1 = "Blue's turn"

                elif placer.yellow_1.x in range(420, 480) and placer.yellow_1.y in range(420, 480):
                    placer.yellow_1.centerx = 450
                    placer.yellow_1.centery = 450
                    yellow_position_1 = 9
                    message_1 = "Blue's turn"

                elif placer.yellow_1.x in range(70, 130) and placer.yellow_1.y in range(245, 315):
                    placer.yellow_1.centerx = 100
                    placer.yellow_1.centery = 275
                    yellow_position_1 = 4
                    message_1 = "Blue's turn"

                elif placer.yellow_1.x in range(245, 315) and placer.yellow_1.y in range(70, 130):
                    placer.yellow_1.centerx = 275
                    placer.yellow_1.centery = 100
                    yellow_position_1 = 2
                    message_1 = "Blue's turn"

                elif placer.yellow_1.x in range(245, 315) and placer.yellow_1.y in range(420, 480):
                    placer.yellow_1.centerx = 275
                    placer.yellow_1.centery = 450
                    yellow_position_1 = 8
                    message_1 = "Blue's turn"

                elif placer.yellow_1.x in range(420, 480) and placer.yellow_1.y in range(245, 315):
                    placer.yellow_1.centerx = 450
                    placer.yellow_1.centery = 275
                    yellow_position_1 = 6
                    message_1 = "Blue's turn"

                elif placer.yellow_1.x in range(245, 315) and placer.yellow_1.y in range(245, 315):
                    placer.yellow_1.centerx = 275
                    placer.yellow_1.centery = 275
                    yellow_position_1 = 5
                    message_1 = "Blue's turn"

        elif held_2 and placer.yellow_2.collidepoint(event.pos):
            if dragging:
                mouse_x, mouse_y = event.pos
                placer.yellow_2.x = mouse_x + offset_x
                placer.yellow_2.y = mouse_y + offset_y

                if placer.yellow_2.x in range(70, 130) and placer.yellow_2.y in range(70, 130):
                    placer.yellow_2.centerx = 100
                    placer.yellow_2.centery = 100
                    yellow_position_2 = 1
                    message_1 = "Blue's turn"

                elif placer.yellow_2.x in range(70, 130) and placer.yellow_2.y in range(430, 480):
                    placer.yellow_2.centerx = 100
                    placer.yellow_2.centery = 450
                    yellow_position_2 = 7
                    message_1 = "Blue's turn"

                elif placer.yellow_2.x in range(420, 480) and placer.yellow_2.y in range(70, 130):
                    placer.yellow_2.centerx = 450
                    placer.yellow_2.centery = 100
                    yellow_position_2 = 3
                    message_1 = "Blue's turn"

                elif placer.yellow_2.x in range(420, 480) and placer.yellow_2.y in range(420, 480):
                    placer.yellow_2.centerx = 450
                    placer.yellow_2.centery = 450
                    yellow_position_2 = 9
                    message_1 = "Blue's turn"

                elif placer.yellow_2.x in range(70, 130) and placer.yellow_2.y in range(245, 315):
                    placer.yellow_2.centerx = 100
                    placer.yellow_2.centery = 275
                    yellow_position_2 = 4
                    message_1 = "Blue's turn"

                elif placer.yellow_2.x in range(245, 315) and placer.yellow_2.y in range(70, 130):
                    placer.yellow_2.centerx = 275
                    placer.yellow_2.centery = 100
                    yellow_position_2 = 2
                    message_1 = "Blue's turn"

                elif placer.yellow_2.x in range(245, 315) and placer.yellow_2.y in range(420, 480):
                    placer.yellow_2.centerx = 275
                    placer.yellow_2.centery = 450
                    yellow_position_2 = 8
                    message_1 = "Blue's turn"

                elif placer.yellow_2.x in range(420, 480) and placer.yellow_2.y in range(245, 315):
                    placer.yellow_2.centerx = 450
                    placer.yellow_2.centery = 275
                    yellow_position_2 = 6
                    message_1 = "Blue's turn"

                elif placer.yellow_2.x in range(245, 315) and placer.yellow_2.y in range(245, 315):
                    placer.yellow_2.centerx = 275
                    placer.yellow_2.centery = 275
                    yellow_position_2 = 5
                    message_1 = "Blue's turn"

        elif held_3 and placer.yellow_3.collidepoint(event.pos):
            if dragging:
                mouse_x, mouse_y = event.pos
                placer.yellow_3.x = mouse_x + offset_x
                placer.yellow_3.y = mouse_y + offset_y

                if placer.yellow_3.x in range(70, 130) and placer.yellow_3.y in range(70, 130):
                    placer.yellow_3.centerx = 100
                    placer.yellow_3.centery = 100
                    yellow_position_3 = 1
                    message_1 = "Blue's turn"

                elif placer.yellow_3.x in range(70, 130) and placer.yellow_3.y in range(430, 480):
                    placer.yellow_3.centerx = 100
                    placer.yellow_3.centery = 450
                    yellow_position_3 = 7
                    message_1 = "Blue's turn"

                elif placer.yellow_3.x in range(420, 480) and placer.yellow_3.y in range(70, 130):
                    placer.yellow_3.centerx = 450
                    placer.yellow_3.centery = 100
                    yellow_position_3 = 3
                    message_1 = "Blue's turn"

                elif placer.yellow_3.x in range(420, 480) and placer.yellow_3.y in range(420, 480):
                    placer.yellow_3.centerx = 450
                    placer.yellow_3.centery = 450
                    yellow_position_3 = 9
                    message_1 = "Blue's turn"

                elif placer.yellow_3.x in range(70, 130) and placer.yellow_3.y in range(245, 315):
                    placer.yellow_3.centerx = 100
                    placer.yellow_3.centery = 275
                    yellow_position_3 = 4
                    message_1 = "Blue's turn"

                elif placer.yellow_3.x in range(245, 315) and placer.yellow_3.y in range(70, 130):
                    placer.yellow_3.centerx = 275
                    placer.yellow_3.centery = 100
                    yellow_position_3 = 2
                    message_1 = "Blue's turn"

                elif placer.yellow_3.x in range(245, 315) and placer.yellow_3.y in range(420, 480):
                    placer.yellow_3.centerx = 275
                    placer.yellow_3.centery = 450
                    yellow_position_3 = 8
                    message_1 = "Blue's turn"

                elif placer.yellow_3.x in range(420, 480) and placer.yellow_3.y in range(245, 315):
                    placer.yellow_3.centerx = 450
                    placer.yellow_3.centery = 275
                    yellow_position_3 = 6
                    message_1 = "Blue's turn"

                elif placer.yellow_3.x in range(245, 315) and placer.yellow_3.y in range(245, 315):
                    placer.yellow_3.centerx = 275
                    placer.yellow_3.centery = 275
                    yellow_position_3 = 5
                    message_1 = "Blue's turn"


def win_blue():
    global winner, start_pos, end_pos, message_1
    # row 1
    if blue_position_1 == 1 and blue_position_2 == 2 and blue_position_3 == 3:
        start_pos = (100, 100)
        end_pos = (450, 100)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 2 and blue_position_2 == 1 and blue_position_3 == 3:
        start_pos = (100, 100)
        end_pos = (450, 100)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 1 and blue_position_2 == 3 and blue_position_3 == 2:
        start_pos = (100, 100)
        end_pos = (450, 100)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 3 and blue_position_2 == 2 and blue_position_3 == 1:
        start_pos = (100, 100)
        end_pos = (450, 100)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 2 and blue_position_2 == 3 and blue_position_3 == 1:
        start_pos = (100, 100)
        end_pos = (450, 100)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"

    # row 2
    if blue_position_1 == 4 and blue_position_2 == 5 and blue_position_3 == 6:
        start_pos = (100, 275)
        end_pos = (450, 275)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 5 and blue_position_2 == 4 and blue_position_3 == 6:
        start_pos = (100, 275)
        end_pos = (450, 275)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 4 and blue_position_2 == 6 and blue_position_3 == 5:
        start_pos = (100, 275)
        end_pos = (450, 275)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 6 and blue_position_2 == 5 and blue_position_3 == 4:
        start_pos = (100, 275)
        end_pos = (450, 275)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 5 and blue_position_2 == 6 and blue_position_3 == 4:
        start_pos = (100, 275)
        end_pos = (450, 275)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"

    # row 3
    if blue_position_1 == 7 and blue_position_2 == 8 and blue_position_3 == 9:
        start_pos = (100, 450)
        end_pos = (450, 450)
        winner = True
        if winner:
            draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 8 and blue_position_2 == 7 and blue_position_3 == 9:
        start_pos = (100, 450)
        end_pos = (450, 450)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 7 and blue_position_2 == 9 and blue_position_3 == 8:
        start_pos = (100, 450)
        end_pos = (450, 450)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 9 and blue_position_2 == 8 and blue_position_3 == 7:
        start_pos = (100, 450)
        end_pos = (450, 450)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 8 and blue_position_2 == 9 and blue_position_3 == 7:
        start_pos = (100, 450)
        end_pos = (450, 450)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"

    # column 1
    if blue_position_1 == 1 and blue_position_2 == 4 and blue_position_3 == 7:
        start_pos = (100, 100)
        end_pos = (100, 450)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 4 and blue_position_2 == 1 and blue_position_3 == 7:
        start_pos = (100, 100)
        end_pos = (100, 450)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 1 and blue_position_2 == 7 and blue_position_3 == 4:
        start_pos = (100, 100)
        end_pos = (100, 450)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 7 and blue_position_2 == 4 and blue_position_3 == 1:
        start_pos = (100, 100)
        end_pos = (100, 450)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 4 and blue_position_2 == 7 and blue_position_3 == 1:
        start_pos = (100, 100)
        end_pos = (100, 450)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"

    # column 2
    if blue_position_1 == 2 and blue_position_2 == 5 and blue_position_3 == 8:
        start_pos = (275, 100)
        end_pos = (275, 450)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 5 and blue_position_2 == 2 and blue_position_3 == 8:
        start_pos = (275, 100)
        end_pos = (275, 450)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 2 and blue_position_2 == 8 and blue_position_3 == 5:
        start_pos = (275, 100)
        end_pos = (275, 450)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 8 and blue_position_2 == 5 and blue_position_3 == 2:
        start_pos = (275, 100)
        end_pos = (275, 450)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"
    if blue_position_1 == 5 and blue_position_2 == 8 and blue_position_3 == 2:
        start_pos = (275, 100)
        end_pos = (275, 450)
        winner = True
        draw_line()
        message_1 = "Blue won!!!"

    # column 3
    if blue_position_1 == 3 and blue_position_2 == 6 and blue_position_3 == 9:
        start_pos = (450, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Blue won!!!"
    if blue_position_1 == 6 and blue_position_2 == 3 and blue_position_3 == 9:
        start_pos = (450, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Blue won!!!"
    if blue_position_1 == 3 and blue_position_2 == 9 and blue_position_3 == 6:
        start_pos = (450, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Blue won!!!"
    if blue_position_1 == 9 and blue_position_2 == 6 and blue_position_3 == 3:
        start_pos = (450, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Blue won!!!"
    if blue_position_1 == 6 and blue_position_2 == 9 and blue_position_3 == 3:
        start_pos = (450, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Blue won!!!"

    # cross 1
    if blue_position_1 == 1 and blue_position_2 == 5 and blue_position_3 == 9:
        start_pos = (100, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Blue won!!!"
    if blue_position_1 == 5 and blue_position_2 == 1 and blue_position_3 == 9:
        start_pos = (100, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Blue won!!!"
    if blue_position_1 == 1 and blue_position_2 == 9 and blue_position_3 == 5:
        start_pos = (100, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Blue won!!!"
    if blue_position_1 == 9 and blue_position_2 == 5 and blue_position_3 == 1:
        start_pos = (100, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Blue won!!!"
    if blue_position_1 == 5 and blue_position_2 == 9 and blue_position_3 == 1:
        start_pos = (100, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Blue won!!!"

    # cross 2
    if blue_position_1 == 3 and blue_position_2 == 5 and blue_position_3 == 7:
        start_pos = (450, 100)
        end_pos = (100, 450)
        draw_line()
        winner = True
        message_1 = "Blue won!!!"
    if blue_position_1 == 5 and blue_position_2 == 3 and blue_position_3 == 7:
        start_pos = (450, 100)
        end_pos = (100, 450)
        draw_line()
        winner = True
        message_1 = "Blue won!!!"
    if blue_position_1 == 3 and blue_position_2 == 7 and blue_position_3 == 5:
        start_pos = (450, 100)
        end_pos = (100, 450)
        draw_line()
        winner = True
        message_1 = "Blue won!!!"
    if blue_position_1 == 7 and blue_position_2 == 5 and blue_position_3 == 3:
        start_pos = (450, 100)
        end_pos = (100, 450)
        draw_line()
        winner = True
        message_1 = "Blue won!!!"
    if blue_position_1 == 5 and blue_position_2 == 7 and blue_position_3 == 3:
        start_pos = (450, 100)
        end_pos = (100, 450)
        draw_line()
        winner = True
        message_1 = "Blue won!!!"


def win_yellow():
    global winner, start_pos, end_pos, message_1
    # row 1
    if yellow_position_1 == 1 and yellow_position_2 == 2 and yellow_position_3 == 3:
        start_pos = (100, 100)
        end_pos = (450, 100)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 2 and yellow_position_2 == 1 and yellow_position_3 == 3:
        start_pos = (100, 100)
        end_pos = (450, 100)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 1 and yellow_position_2 == 3 and yellow_position_3 == 2:
        start_pos = (100, 100)
        end_pos = (450, 100)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 3 and yellow_position_2 == 2 and yellow_position_3 == 1:
        start_pos = (100, 100)
        end_pos = (450, 100)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 2 and yellow_position_2 == 3 and yellow_position_3 == 1:
        start_pos = (100, 100)
        end_pos = (450, 100)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"

    # row 2
    if yellow_position_1 == 4 and yellow_position_2 == 5 and yellow_position_3 == 6:
        start_pos = (100, 275)
        end_pos = (450, 275)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 5 and yellow_position_2 == 4 and yellow_position_3 == 6:
        start_pos = (100, 275)
        end_pos = (450, 275)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 4 and yellow_position_2 == 6 and yellow_position_3 == 5:
        start_pos = (100, 275)
        end_pos = (450, 275)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 6 and yellow_position_2 == 5 and yellow_position_3 == 4:
        start_pos = (100, 275)
        end_pos = (450, 275)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 5 and yellow_position_2 == 6 and yellow_position_3 == 4:
        start_pos = (100, 275)
        end_pos = (450, 275)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"

    # row 3
    if yellow_position_1 == 7 and yellow_position_2 == 8 and yellow_position_3 == 9:
        start_pos = (100, 450)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 8 and yellow_position_2 == 7 and yellow_position_3 == 9:
        start_pos = (100, 450)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 7 and yellow_position_2 == 9 and yellow_position_3 == 8:
        start_pos = (100, 450)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 9 and yellow_position_2 == 8 and yellow_position_3 == 7:
        start_pos = (100, 450)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 8 and yellow_position_2 == 9 and yellow_position_3 == 7:
        start_pos = (100, 450)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"

    # column 1
    if yellow_position_1 == 1 and yellow_position_2 == 4 and yellow_position_3 == 7:
        start_pos = (100, 100)
        end_pos = (100, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 4 and yellow_position_2 == 1 and yellow_position_3 == 7:
        start_pos = (100, 100)
        end_pos = (100, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 1 and yellow_position_2 == 7 and yellow_position_3 == 4:
        start_pos = (100, 100)
        end_pos = (100, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 7 and yellow_position_2 == 4 and yellow_position_3 == 1:
        start_pos = (100, 100)
        end_pos = (100, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 4 and yellow_position_2 == 7 and yellow_position_3 == 1:
        start_pos = (100, 100)
        end_pos = (100, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"

    # column 2
    if yellow_position_1 == 2 and yellow_position_2 == 5 and yellow_position_3 == 8:
        start_pos = (275, 100)
        end_pos = (275, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 5 and yellow_position_2 == 2 and yellow_position_3 == 8:
        start_pos = (275, 100)
        end_pos = (275, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 2 and yellow_position_2 == 7 and yellow_position_3 == 4:
        start_pos = (275, 100)
        end_pos = (275, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 8 and yellow_position_2 == 5 and yellow_position_3 == 2:
        start_pos = (275, 100)
        end_pos = (275, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 5 and yellow_position_2 == 8 and yellow_position_3 == 2:
        start_pos = (275, 100)
        end_pos = (275, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"

    # column 3
    if yellow_position_1 == 3 and yellow_position_2 == 6 and yellow_position_3 == 9:
        start_pos = (450, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 6 and yellow_position_2 == 3 and yellow_position_3 == 9:
        start_pos = (450, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 3 and yellow_position_2 == 9 and yellow_position_3 == 6:
        start_pos = (450, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 9 and yellow_position_2 == 6 and yellow_position_3 == 3:
        start_pos = (450, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 6 and yellow_position_2 == 9 and yellow_position_3 == 3:
        start_pos = (450, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"

    # cross 1
    if yellow_position_1 == 1 and yellow_position_2 == 5 and yellow_position_3 == 9:
        start_pos = (100, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 5 and yellow_position_2 == 1 and yellow_position_3 == 9:
        start_pos = (100, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 1 and yellow_position_2 == 9 and yellow_position_3 == 5:
        start_pos = (100, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 9 and yellow_position_2 == 5 and yellow_position_3 == 1:
        start_pos = (100, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 5 and yellow_position_2 == 9 and yellow_position_3 == 1:
        start_pos = (100, 100)
        end_pos = (450, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"

    # cross 2
    if yellow_position_1 == 3 and yellow_position_2 == 5 and yellow_position_3 == 7:
        start_pos = (450, 100)
        end_pos = (100, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 5 and yellow_position_2 == 3 and yellow_position_3 == 7:
        start_pos = (450, 100)
        end_pos = (100, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 3 and yellow_position_2 == 7 and yellow_position_3 == 5:
        start_pos = (450, 100)
        end_pos = (100, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 7 and yellow_position_2 == 5 and yellow_position_3 == 3:
        start_pos = (450, 100)
        end_pos = (100, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"
    if yellow_position_1 == 5 and yellow_position_2 == 7 and yellow_position_3 == 3:
        start_pos = (450, 100)
        end_pos = (100, 450)
        draw_line()
        winner = True
        message_1 = "Yellow won!!!"


def re_start():
    global winner, message_1, blue_position_3, blue_position_2, blue_position_1
    global yellow_position_3, yellow_position_2, yellow_position_1
    winner = False

    blue_position_1 = 0
    blue_position_2 = 0
    blue_position_3 = 0

    yellow_position_1 = 0
    yellow_position_2 = 0
    yellow_position_3 = 0

    message_1 = "Blue start!"
    placer.blue_rect_2 = pg.Surface((50, 50))
    placer.blue_2 = placer.blue_rect_2.get_rect(center=placer._pos_initial_1)

    placer.blue_rect_1 = pg.Surface((50, 50))
    placer.blue_1 = placer.blue_rect_1.get_rect(center=placer._pos_initial)

    placer.blue_rect_3 = pg.Surface((50, 50))
    placer.blue_3 = placer.blue_rect_3.get_rect(center=placer._pos_initial_2)

    placer.yellow_rect_1 = pg.Surface((50, 50))
    placer.yellow_1 = placer.yellow_rect_1.get_rect(center=placer.pos_initial)

    placer.yellow_rect_2 = pg.Surface((50, 50))
    placer.yellow_2 = placer.yellow_rect_2.get_rect(center=placer.pos_initial_1)

    placer.yellow_rect_3 = pg.Surface((50, 50))
    placer.yellow_3 = placer.yellow_rect_3.get_rect(center=placer.pos_initial_2)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    blue_mouse_moves()
    yellow_mouse_moves()
    check_button_click()

    screen.fill((222, 14, 122))
    draw_board(screen)
    marker.draw_markers(screen)
    placer.draw_yellow(screen)
    placer.draw_blue(screen)
    draw_status()
    draw_button()
    win_yellow()
    win_blue()

    pg.display.update()
    clock.tick(fps)
