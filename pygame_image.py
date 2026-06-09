import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_koukaton = pg.image.load("fig/3.png")
    bg_img_koukaton = pg.transform.flip(bg_img_koukaton, True, False)
    bg_rct_koukaton = bg_img_koukaton.get_rect()
    bg_rct_koukaton.center = 300, 200
    screen.blit(bg_img_koukaton, bg_rct_koukaton)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_list = pg.key.get_pressed()
        if key_list[pg.K_UP]:
            bg_rct_koukaton.move_ip((0, -1))
        if key_list[pg.K_DOWN]:
            bg_rct_koukaton.move_ip((0, 1))
        if key_list[pg.K_LEFT]:
            bg_rct_koukaton.move_ip((-1, 0))
        if key_list[pg.K_RIGHT]:
            bg_rct_koukaton.move_ip((1, 0))

        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        bg_img_flipped = pg.transform.flip(bg_img, True, False)
        screen.blit(bg_img_flipped, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bg_img_koukaton, bg_rct_koukaton)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()