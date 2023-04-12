import pygame
import pygame as pg
import random
import math
from typing import Tuple

def clamp(i: int, under: int, over: int) -> int:
    return min(max(i, under), over)

WIDTH = 800
HEIGHT = 600
FPS = 60.0

pg.init()
pg.mixer.init()
pg.mixer.music.load("resources/liedje.mp3")
pg.mixer.music.play()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
running = True

circle1_color = (12, 183, 245)
circle2_color = (240, 7, 178)

# Set the initial position of the circle1
circle1_pos = [WIDTH / 2 + 1 , HEIGHT / 2 + 1]
circle2_pos = [WIDTH / 2, HEIGHT / 2]

# Set the radius of the circle1
circle1_radius = 55
circle2_radius = 85

# Set the speed of the circle1
circle1_speed = 10
circle2_speed = 5

def draw_circles():
    # Move the circle1
    circle1_pos[0] += random.randint(-circle1_speed, circle1_speed)
    circle1_pos[1] += random.randint(-circle1_speed, circle1_speed)

    circle2_pos[0] += random.randint(-circle2_speed, circle2_speed)
    circle2_pos[1] += random.randint(-circle2_speed, circle2_speed)
    
    # Check if the circle1 is out of bounds
    if circle1_pos[0] < circle1_radius:
        circle1_pos[0] = circle1_radius
    elif circle1_pos[0] > WIDTH - circle1_radius:
        circle1_pos[0] = WIDTH - circle1_radius
    if circle1_pos[1] < circle1_radius:
        circle1_pos[1] = circle1_radius
    elif circle1_pos[1] > HEIGHT - circle1_radius:
        circle1_pos[1] = HEIGHT - circle1_radius
    

    if circle2_pos[0] < circle2_radius:
        circle2_pos[0] = circle2_radius
    elif circle2_pos[0] > WIDTH - circle2_radius:
        circle2_pos[0] = WIDTH - circle2_radius
    if circle2_pos[1] < circle2_radius:
        circle2_pos[1] = circle2_radius
    elif circle2_pos[1] > HEIGHT - circle2_radius:
        circle2_pos[1] = HEIGHT - circle2_radius
    

    # Draw the circle1
    pygame.draw.circle(screen, circle1_color, (int(circle1_pos[0]), int(circle1_pos[1])), circle1_radius)
    pygame.draw.circle(screen, circle2_color, (int(circle2_pos[0]), int(circle2_pos[1])), circle2_radius)


def draw_arthurs_demo(screen, counter):
    rect_pos_x = counter % 800
    
    pg.draw.rect(
        screen, 
        (255, 0, 0), 
        [
            150 + clamp(rect_pos_x, 0, 400) - clamp(rect_pos_x - 400, 0, 400), 
            150, 
            150, 
            150,
        ]
    )
    
    line_pos_y = counter % 1200
    pg.draw.line(
        screen, 
        (255, 255, 255), 
        (0, clamp(line_pos_y, 0, 600) - clamp(line_pos_y - 600, 0, 600)), 
        (800, clamp(line_pos_y, 0, 600) - clamp(line_pos_y - 600, 0, 600)), 
        3
    )


def draw_rect(screen, screen_width, screen_height, timer, color) -> None:
    pygame.draw.rect(
        screen,
        color,
        [
            screen_width / 2.0 - screen_width / 2.0 * timer,
            screen_height / 2.0 - screen_height / 2.0 * timer,
            screen_width * timer,
            screen_height * timer,
        ],
    )


def make_rect_timers(time_proportion: float) -> Tuple[float, float]:
    if time_proportion < 1.0:
        time_proportion *= 2.0
    else:
        time_proportion = math.sin((time_proportion - 0.5) * 2.0 * math.pi)
    rect1_timer = min(1.0, 2.0 * (time_proportion % 1.0))
    rect2_timer = min(1.0, 2.0 * ((time_proportion - 0.5) % 1.0))
    return (rect1_timer, rect2_timer)


def draw_rect_effect(
    timer, duration: float, screen_width, screen_height, screen, color1, color2
) -> None:
    rect_time_proportion = (timer / duration) % 2.0
    rect1_timer, rect2_timer = make_rect_timers(rect_time_proportion)
    draw_rect(screen, screen_width, screen_height, rect1_timer, color1)
    if rect2_timer < rect1_timer:
        draw_rect(screen, screen_width, screen_height, rect2_timer, color2)

timer: float = 0.0
counter = 0
duration = 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
    screen.fill(WHITE)

    draw_rect_effect(timer, duration, WIDTH, HEIGHT, screen, BLACK, WHITE)
    draw_circles()
    draw_arthurs_demo(screen, counter)
    
    pg.display.flip()
    timer += 1.0/FPS
    print(timer)
    counter += 1
    clock.tick(FPS)

pg.quit()

