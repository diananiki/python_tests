import pygame as pg
import math
import sys

pg.init()
screen = pg.display.set_mode((600, 400))
pg.display.set_caption("Анимированный график")
screen.fill((255, 255, 255))
font = pg.font.Font(None, 14)
pg.draw.line(screen, (0, 0, 0), (0, 200), (600, 200))
pg.draw.line(screen, (0, 0, 0), (10, 0), (10, 400))
text = font.render('0', True, (0, 0, 0))
screen.blit(text, (15, 185))
for i in range(1, 600 // 30):
    text = font.render(str(i), True, (0, 0, 0))
    screen.blit(text, (i * 30 + 10, 210))
for i in range(1, 200 // 30):
    text = font.render(str(i), True, (0, 0, 0))
    screen.blit(text, (15, 200 - i * 30 - 5))
    text = font.render(str(-i), True, (0, 0, 0))
    screen.blit(text, (15, 200 + i * 30 - 5))
paused = False
p_but = pg.Rect(500, 10, 90, 30)
font_b = pg.font.Font(None, 22)
text_b = font_b.render('pause', True, (255, 255, 255))

i = 0
while i < 600:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if p_but.collidepoint(event.pos):
                paused = not paused
    if not paused:
        i += 0.1
        pg.time.delay(50)
    pg.draw.circle(screen, (255, 0, 0), (30 * i + 10, 30 * math.cos(i) + 200), 3)
    pg.draw.circle(screen, (255, 140, 0), (30 * i + 10 + 5, 30 * math.cos(i) + 200), 3)
    pg.draw.circle(screen, (255, 215, 0), (30 * i + 10 + 10, 30 * math.cos(i) + 200), 3)
    pg.draw.circle(screen, (50, 205, 50), (30 * i + 10 + 15, 30 * math.cos(i) + 200), 3)
    pg.draw.circle(screen, (0, 206, 209), (30 * i + 10 + 20, 30 * math.cos(i) + 200), 3)
    pg.draw.circle(screen, (30, 144, 255), (30 * i + 10 + 25, 30 * math.cos(i) + 200), 3)
    pg.draw.circle(screen, (123, 104, 238), (30 * i + 10 + 30, 30 * math.cos(i) + 200), 3)
    if paused:
        pg.draw.rect(screen, (0, 0, 255), p_but)
    else:
        pg.draw.rect(screen, (255, 0, 0), p_but)
    screen.blit(text_b, (525, 17))
    pg.display.update()