import pygame
import time
import random
from tkinter import *

WIDTH = 900
HEIGHT = 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong!')

SPACE = pygame.image.load('space.png')

BLUE = (0, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


def display(blue_rect, red_rect, ball):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLUE, blue_rect)
    pygame.draw.rect(WIN, RED, red_rect)
    pygame.draw.rect(WIN, YELLOW, ball)
    pygame.display.update()


def blue_rect_touch_ball(blue_rect, ball):
    if blue_rect.colliderect(ball):
        return True


def red_rect_touch_ball(red_rect, ball):
    if red_rect.colliderect(ball):
        return True


def main(tk):
    tk.destroy()
    blue_rect = pygame.Rect(10, 200, 20, 100)
    red_rect = pygame.Rect(WIDTH - 30, 200, 20, 100)
    ball = pygame.Rect(440, 240, 20, 20)

    X_BALL = random.choice((-4, -3, -2, -4, 3, 2))
    Y_BALL = random.choice((-4, -3, -2, 3, 2, 4))

    Y_RED = 0
    Y_BLUE = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    Y_RED = -3
                if event.key == pygame.K_DOWN:
                    Y_RED = 3
                if event.key == pygame.K_w:
                    Y_BLUE = -3
                if event.key == pygame.K_s:
                    Y_BLUE = 3

        if red_rect.y + red_rect.height >= HEIGHT - 20:
            Y_RED = -3
        if red_rect.y <= 20:
            Y_RED = 3
        if blue_rect.y + blue_rect.height >= HEIGHT - 20:
            Y_BLUE = -3
        if blue_rect.y <= 20:
            Y_BLUE = 3

        if ball.y <= 10:
            X_BALL = random.choice((-4, -3, -2, 4, 3, 2))
            Y_BALL = 1
        elif ball.y >= HEIGHT - 20:
            Y_BALL = -1
            X_BALL = random.choice((-4, -3, -2, 4, 3, 2))

        elif ball.x <= 10:
            start('CONTINUE')
            pygame.quit()
        elif ball.x >= WIDTH - 20:
            start('CONTINUE')
            pygame.quit()

        elif blue_rect_touch_ball(blue_rect, ball):
            X_BALL = 2
            Y_BALL = random.choice((-4, -3, -2, 2, 3, 4))
        elif red_rect_touch_ball(red_rect, ball):
            X_BALL = -2
            Y_BALL = random.choice((-4, -3, -2, 2, 3, 4))

        ball.x += X_BALL
        ball.y += Y_BALL

        red_rect.y += Y_RED
        blue_rect.y += Y_BLUE

        display(blue_rect, red_rect, ball)
        time.sleep(0.01)


def start(text):
    if __name__ == '__main__':
        tk = Tk()
        tk.wm_attributes('-topmost', 1)
        but = Button(tk, text=text, command=lambda: main(tk))
        but.pack(side="bottom", fill="none", expand=True)
        but1 = Button(tk, text='NO', command=lambda: tk.destroy())
        but1.pack(side="top", fill="none", expand=True)
        tk.mainloop()


start('START')
