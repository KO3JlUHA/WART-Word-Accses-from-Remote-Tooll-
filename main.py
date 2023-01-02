import pyautogui as pg
import keyboard as kb

screen_width, screen_height = pg.size()


def log_keyboard():
    pass


def recreate_keyboard():
    pass


def log_mouse():
    pos = pg.position()
    while not kb.is_pressed('esc'):
        pos_now = (pg.position()[0] * 100 // screen_width, pg.position()[1] * 100 // screen_height)
        if pos_now != pos:
            pos = pos_now
            print(pos)


def recreate_mouse_movement(pos: str):
    x, y = pos.split(', ')
    x = int(x[1:]) * screen_width // 100
    y = int(y[:-1]) * screen_height // 100
    pg.moveTo(x, y)


def main():
    log_mouse()
    recreate_mouse_movement('(50, 50)')


if __name__ == '__main__':
    main()
