from socket import socket
from colorama import Back, Style, Fore
from os import remove

host = input("{}{}Enter server ip >> {}".format("\033[1m", Fore.CYAN, Style.RESET_ALL))
min= input("{}{}Enter min port >> {}".format("\033[1m", Fore.CYAN, Style.RESET_ALL))
max = input("{}{}Enter max port >> {}".format("\033[1m", Fore.CYAN, Style.RESET_ALL))
min = int(min)
max = int(max)

ip = host
port = min
count = 0

try:
    remove(ip)
except FileNotFoundError:
    pass

while port != max + 1:
    try:
        serv = socket()
        serv.settimeout(0.25)
        serv.connect((ip, port))
        print("{}{}{}:{} is valid!{}".format("\033[1m", Back.GREEN, ip, port, Style.RESET_ALL))
        with open("{}.txt".format(ip), "a") as w:
            w.write("{}:{}\n".format(ip, port))
            w.close()
        port += 1
        count += 1
    except ConnectionError:
        print("{}{}{}:{} is invalid!{}".format("\033[1m", Back.RED, ip, port, Style.RESET_ALL))
        port += 1
        count += 1
    except Exception as err:
        count += 1
        port += 1
        print(port, count, err)


