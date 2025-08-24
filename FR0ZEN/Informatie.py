import subprocess
import platform
import re
import os
import time
import requests
import time
import colorama
from colorama import Fore
from pystyle import *
import os
from pystyle import Colors, Colorate
import platform
import subprocess
import sys
import sys
import time
import uuid
import requests
from colorama import Fore, init
from datetime import datetime

init(autoreset=True)

# =========================
# SETTINGS
# =========================
WHITELIST = ["E9E07C23-865C-4241-BC79-495616383634"]   # Allowed HWIDs
BLACKLIST = ["XYZ999-BANNED-HWID"]    # Blocked HWIDs
TIME_LIMIT = 30                       # seconds allowed
TAB_COLOR = Fore.CYAN                 # Tab color for allowed users
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1392498264451842139/aaO4ISZQOkYYaqVvxlh2ZFw2oocBGO4PBaa-oRD_mODb9hZTn5o54av-G9k1S9rkOv1M"  # Replace with your webhook
# =========================

# Function to set terminal/tab title
def set_title(title: str):
    sys.stdout.write(f"\33]0;{title}\a")
    sys.stdout.flush()

# Function to get HWID
def get_hwid():
    return hex(uuid.getnode()).upper()

# Function to log HWID to Discord
def log_hwid_to_discord(hwid, status):
    data = {
        "content": f"HWID: `{hwid}` | Status: `{status}` | Time: `{datetime.utcnow()}` UTC"
    }
    try:
        requests.post(DISCORD_WEBHOOK, json=data)
    except Exception as e:
        print(Fore.RED + f"Failed to send webhook: {e}")

def main():
    hwid = get_hwid()

    # Blacklist check
    if hwid in BLACKLIST:
        log_hwid_to_discord(hwid, "Blacklisted")
        print(Fore.RED + f"HWID {hwid} is blacklisted. Closing...")
        sys.exit(0)

    # Whitelist check
    if hwid not in WHITELIST:
        log_hwid_to_discord(hwid, "Not Whitelisted")
        print(Fore.RED + f"HWID {hwid} is not whitelisted. Closing...")
        sys.exit(0)

    # If allowed, log and start countdown
    log_hwid_to_discord(hwid, "Allowed")
    print(TAB_COLOR + f"Access granted for HWID {hwid}. Time limit: {TIME_LIMIT} seconds.")

    start = time.time()
    while True:
        elapsed = int(time.time() - start)
        remaining = TIME_LIMIT - elapsed

        if remaining < 0:
            print(Fore.RED + "Time expired. Closing...")
            sys.exit(0)

        set_title(f"FR0ZEN DDoS - Time Left > {remaining}s")
        time.sleep(1)

if __name__ == "__main__":
    main()


def clear_screen():
    # Clear the screen based on the operating system
    if platform.system().lower() == "windows":
        os.system('cls')
    else:
        os.system('clear')

def print_menu():
    clear_screen()
    print("\033[31m" + r"""
     _____ ____   ___ __________ _   _  
    |  ___|  _ \ / _ \__  / ____| \ | |
    | |_  | |_) | | | |/ /|  _| |  \| | 
    |  _| |  _ <| |_| / /_| |___| |\  | 
    |_|   |_| \_\\___/____|_____|_| \_| 
    """ + "\033[0m")

    print("""
1.  Alle IP's van mensen
2.  FROZEN DoS Aanval
3.  Zoek IP Informatie
4.  IP Pinger
---------------------------
    """)

print(Fore.RED + "")
print("Starting FR0ZEN [|]")
time.sleep(0.2)
os.system("cls")
print("Starting FR0ZEN [/]")
time.sleep(0.2)
os.system("cls")
print("Starting FR0ZEN [-]")
time.sleep(0.2)
os.system("cls")
print("Starting FR0ZEN [\]")
time.sleep(0.2)
os.system("cls")
print("Starting FR0ZEN [|]")
time.sleep(0.2)
os.system("cls")
print("Starting FR0ZEN [/]")
time.sleep(0.2)
os.system("cls")
print("Starting FR0ZEN [-]")
time.sleep(0.2)
os.system("cls")
print("Starting FR0ZEN [\]")
time.sleep(0.2)
os.system("cls")
print("Starting FR0ZEN [|]")
time.sleep(0.2)
print("FR0ZEN Is ingeladen. Je gaat het programma in om 5 seconden")
time.sleep(1.0)
print("FR0ZEN Is ingeladen. Je gaat het programma in om 4 seconden")
time.sleep(1.0)
print("FR0ZEN Is ingeladen. Je gaat het programma in om 3 seconden")
time.sleep(1.0)
print("FR0ZEN Is ingeladen. Je gaat het programma in om 2 seconden")
time.sleep(1.0)
print("FR0ZEN Is ingeladen. Je gaat het programma in om 1 seconden")
time.sleep(1.0)
print("Starting FR0ZEN")
time.sleep(2.5)
print_menu()


















def optie_1():
    print("Dacrocco: 217.105.84.225")
    print("Domingo: 31.151.103.157")
    print("Envy: 86.95.255.143")
    print("Kaaskop: 84.83.65.215")
    print("Karma: 86.95.255.143")
    print("Nasim: 85.145.251.143")
    print("Mick: 80.56.38.222")
    print("Hassan FiveR Eigenaar: 94.157.251.78")
    print("Stefano: 217.121.134.67")
    print("gwnscooby: 77.170.74.193 ")
    print("mathiesdani1: 77.165.225.28")
    print("Sander Sloks Eigenaar: 217.122.134.208")
    print("Jayden_de_madfut: 84.241.171.228")
    print("Kevinstorm15: 86.90.211.151")
    time.sleep(5)

def optie_2():
    import subprocess

    # Use Windows-style path for local use
    file_path = "C:/Users/desny/OneDrive/Desktop/FR0ZEN/udpflood.py"

    # Check if the file exists
    if os.path.isfile(file_path):
        print(f"Opening {file_path} with Python...")
        try:
            subprocess.run(["python", file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running the script: {e}")
    else:
        print(f"File not found: {file_path}")


def optie_3():
    ip_address = input("Voer het IP-adres in om informatie op te zoeken: ")
    
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip_address):
        print("Ongeldig IP-adres formaat. Probeer het opnieuw.")
        return
    
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        
        if data['status'] == 'success':
            print(f"IP-adres: {data['query']}")
            print(f"Land: {data['country']}")
            print(f"Regio: {data['regionName']}")
            print(f"Stad: {data['city']}")
            print(f"Postcode: {data['zip']}")
            print(f"Tijdzone: {data['timezone']}")
            print(f"ISP: {data['isp']}")
            print(f"Organisatie: {data['org']}")
            print(f"AS: {data['as']}")
            time.sleep(500)
        else:
            print("Kon geen informatie ophalen voor dit IP-adres.")
    except requests.exceptions.RequestException as e:
        print(f"Er is een fout opgetreden bij het opvragen van informatie: {e}")

def optie_4():
    ip_address = input("Voer het IP-adres in om te pingen: ")
    
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip_address):
        print("Ongeldig IP-adres formaat. Probeer het opnieuw.")
        return

    try:
        if platform.system().lower() == "windows":
            command = ['ping', '-t', ip_address]
        else:
            command = ['ping', ip_address]

        print(f"Pingen {ip_address} ... Druk op Ctrl + C om te stoppen.")
        
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        for line in iter(process.stdout.readline, ''):
            print(line, end='')

    except subprocess.CalledProcessError as e:
        print(f"Fout bij het pingen van {ip_address}: {e}")
    except KeyboardInterrupt:
        print("\nPingen gestopt door gebruiker. Terug naar menu.")
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")
    finally:
        if process:
            process.terminate()
            process.wait()

def main_menu():
    clear_screen()
    print_menu()
    keuze = input("Maak een keuze (1-4): ")
    
    if keuze == '1':
        optie_1()
    elif keuze == '2':
        optie_2()
    elif keuze == '3':
        optie_3()
    elif keuze == '4':
        optie_4()
    else:
        print("Ongeldige keuze. Probeer het opnieuw.")

while True:
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nTerug naar het hoofdmenu...")
        time.sleep(1)  # Optionally pause before clearing the screen


