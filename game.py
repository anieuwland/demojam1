import pygame as pg

def clamp(i: int, under: int, over: int) -> int:
    return min(max(i, under), over)

pg.init()
pg.mixer.init()
pg.mixer.music.load("liedje.mp3")
pg.mixer.music.play()
screen = pg.display.set_mode((800,600))
clock = pg.time.Clock()
running = True

counter = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
    screen.fill((0, 0, 0))
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
    pg.display.flip()
    counter += 1
    clock.tick(60)

pg.quit()

