import pygame as pg

from kb_input import kb_input
from ball_physics import ball_all_bounce
from drawscreen import screen
from entities import player1, ball
from posixpath import relpath
from pygame import mixer


# initialize pygame
pg.init()
clock = pg.time.Clock()


def run_game(bool):
    running = bool
    while running:
        screen.bg_fill(20, 30, 50)

        running = kb_input(running)

        player1.apply_changeXY()
        player1.hard_bounds()
        player1.blit_obj()

        hits = ball_all_bounce(.15)
        ball.apply_changeXY()
        ball.blit_obj()
        #print(f'Collision at {hits}')
        pg.display.update()


if __name__ == '__main__':
    run_game(True)
ball_physics.py
import pygame as pg
import random

from drawscreen import screen
from entities import ball, player1


def ball_wall_bounce(val):
    if ball.x > (screen.w-ball.w):
        ball.collided = True
        ball.cx = -(val)

    if ball.x < 0:
        ball.collided = True
        ball.cx = (val)

    if ball.y > (screen.h-ball.h):
        ball.collided = True
        ball.cy = -(val)

    if ball.y < 0:
        ball.collided = True
        ball.cy = (val)

    # Initial start for ball
    if ball.collided == False:
        ball.cy = (val)


def ball_spacer_bounce(val):
    if player1.rect.colliderect(ball.rect):
        clip = player1.rect.clip(ball.rect)
        cr = abs(clip.left - player1.rect.right) 
        cl = abs(clip.right - player1.rect.left) 
        if (cl) < (cr):
            ball_bounce_right() 
        if cl == cr:
            val = random.randint(0,1)
            if val == 0:
                ball_bounce_right() 
            else:
                ball_bounce_left()
        else:
            ball_bounce_left()

def ball_bounce_left():
    ball.cy = -(.2)
    ball.cx = -(random.randint(15,60)/ 1000) 

def ball_bounce_right():
    ball.cy = -(.2)
    ball.cx = (random.randint(15,60)/ 1000)

def ball_all_bounce(val):
    ball_wall_bounce(val)
    ball_spacer_bounce(val)