import pygame as pg
from enum import Enum
from random import randint

class Color:
    WHITE = (255, 255, 255)
    BLACK = (0  , 0  , 0  )

def calc_next(ref, p):
    if p[0] >= ref[0]: x = p[0] - abs(p[0] - ref[0]) // 2
    else:              x = p[0] + abs(p[0] - ref[0]) // 2
    if p[1] >= ref[1]: y = p[1] - abs(p[1] - ref[1]) // 2
    else:              y = p[1] + abs(p[1] - ref[1]) // 2
    return (x,y)

def ref_points(w, h):
    ref_points = [(w//2, 200), (200, h-200), (w-200, h-200)]
    return [p for p in ref_points]

def main():
    pg.init()
    window_size = window_w, window_h = (1000, 1000)
    scr = pg.display.set_mode(window_size)
    scr.fill(Color.BLACK)
    pg.display.update()
    init = (randint(100, 700), randint(100, 700))
    points = ref_points(window_w, window_h) + [init]

    pg.font.init()
    font = pg.font.SysFont("InputMono", 30)
    A = font.render("A", False, Color.WHITE)
    B = font.render("B", False, Color.WHITE)
    C = font.render("C", False, Color.WHITE)
    names = [A, B, C]
    iteration = 0

    while True:
        for event in pg.event.get():
            if (event.type == pg.QUIT): return
            if (event.type == pg.KEYDOWN and
                event.key in (pg.K_ESCAPE, pg.K_q)): return
        ref = randint(0,2)
        new_p = calc_next(points[ref], points[-1])
        points.append(new_p)
        scr.fill(Color.BLACK)
        for p in points:
            scr.set_at(p, Color.WHITE)
        iteration += 1

        scr.blit(names[0], (points[0][0]-10, points[0][1]-45))
        scr.blit(names[1], (points[1][0]-30, points[1][1]))
        scr.blit(names[2], (points[2][0]+10, points[2][1]))

        iteration_text = font.render(f"iteration: {iteration}", False, Color.WHITE)
        scr.blit(iteration_text, (10, 10))
        pg.display.update()

if __name__ == '__main__':
    main()
