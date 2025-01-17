import os,rich,random
from rich.console import Console
from rich.panel import Panel
# ------------------[  indication ]-------------------#
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


# Fungsi untuk menampilkan banner keren bergaya hacktivisme
def title():
    Console().print(
        Panel(
            """
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
    
# Fungsi untuk menginstal paket-paket dengan pip atau pip3
def install_packages(pip_command):
    packages = [
        "cloudscraper", 
        "socks", 
        "pysocks", 
        "colorama", 
        "undetected_chromedriver", 
        "httpx"
    ]
    
    for package in packages:
        os.system(f"{pip_command} install {package}")

# Script utama
title()

print("""[0] pip\n[1] pip3\nPilih yang mana yang kamu gunakan?""")
c = input(">>>: ").strip()

if c == "0":
    pip_command = "pip"
elif c == "1":
    pip_command = "pip3"
else:
    print("Pilihan tidak valid.")
    exit()

# Instalasi paket
install_packages(pip_command)

# Jika sistem adalah Linux, unduh dan instal Google Chrome
if os.name != "nt":
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt-get install -y ./google-chrome-stable_current_amd64.deb")

print("\x1b[38;2;0;255;0mProses setup selesai. Bersiaplah untuk hacktivisme!")
