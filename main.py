import pygame as pg

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 640
DISPLAY_RESOLUTION = (DISPLAY_WIDTH, DISPLAY_HEIGHT)


pg.init()

display_screen = pg.display.set_mode(DISPLAY_RESOLUTION)

clock = pg.clock.Clock()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_ESCAPE]):
            running = False
            break
    
    clock.tick(60)
    print(clock.get_fps())

pg.quit()