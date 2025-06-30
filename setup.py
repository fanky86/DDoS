import os, rich, random, platform
from rich.console import Console
from rich.panel import Panel

console = Console()

# ------------[ WARNA ]---------------#
M2 = "[#FF0000]"
H2 = "[#00FF00]"
K2 = "[#FFFF00]"
B2 = "[#00C8FF]"
P2 = "[#FFFFFF]"
U2 = "[#AF00FF]"
O2 = "[#FF8F00]"

# ------------[ LOAD TEMA WARNA ]---------------#
try:
    with open("data/theme_color", "r") as file_color:
        color_text, color_panel = file_color.read().split("|")
except:
    color_text = "[#00FF00]"
    color_panel = "#00FF00"

# ------------[ BANNER ]---------------#
def print_banner():
    console.print(
        Panel(
            """
[bold red]███████████████████████ [bold yellow]NOTE  : [bold green]BY FANKY  
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

# ------------[ INSTALL PIP PACKAGE ]---------------#
def install_packages(pip_command):
    packages = [
        "cloudscraper",
        "socks",
        "pysocks",
        "colorama",
        "undetected_chromedriver",
        "httpx"
    ]
    for pkg in packages:
        os.system(f"{pip_command} install {pkg}")

# ------------[ CEK OS DAN PIP ]---------------#
def detect_pip_command():
    pip_variants = ["pip3", "pip"]
    for pip_cmd in pip_variants:
        try:
            if os.system(f"{pip_cmd} --version >nul 2>&1" if os.name == "nt" else f"{pip_cmd} --version >/dev/null 2>&1") == 0:
                return pip_cmd
        except:
            continue
    return "pip"

# ------------[ INSTAL CHROME JIKA LINUX ]---------------#
def install_chrome_linux():
    distro = platform.system().lower()
    if "linux" in distro:
        termux = os.getenv("PREFIX")  # Jika di Termux, biasanya ada PREFIX=/data/data/com.termux/files/usr
        if termux:
            console.print(Panel("[bold yellow]Kamu menggunakan Termux, lewati instalasi Google Chrome.[/bold yellow]", style="yellow"))
        else:
            os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
            os.system("sudo apt install -y ./google-chrome-stable_current_amd64.deb")

# ------------[ MAIN ]---------------#
print_banner()

console.print(Panel(f"{H2}1. {P2}pip\n{H2}2. {P2}pip3", width=60, title="PILIH INSTALASI", style=f"{color_panel}"))
c = console.input(f"{H2}• {P2}Pilih (1/2 atau Enter untuk otomatis): ").strip()

if c == "1":
    pip_command = "pip"
elif c == "2":
    pip_command = "pip3"
else:
    pip_command = detect_pip_command()
    console.print(f"{K2}Menggunakan pip default: {P2}{pip_command}")

console.print(Panel(f"{B2}Menginstal paket menggunakan: {pip_command}", style="blue"))
install_packages(pip_command)

if os.name != "nt":
    install_chrome_linux()

console.print(Panel(f"{H2}✅ Proses setup selesai. Semua siap digunakan!", style="green"))
