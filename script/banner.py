import os

# Fungsi untuk menampilkan banner keren bergaya hacktivisme
def print_banner():
    print("""
\x1b[38;2;0;255;0m╔═╗╔═╗╦  ╔═╗╦╔╦╗╦╔═╗╔╗╔
\x1b[38;2;0;255;0m╚═╗╠═╣║  ║ ║║ ║ ║║ ║║║║
\x1b[38;2;0;255;0m╚═╝╩ ╩╩═╝╚═╝╩ ╩ ╩╚═╝╝╚╝
\x1b[38;2;255;20;147m╔═╗╔═╗╦╔═╗╦ ╦╦ ╦╔╦╗╔═╗
\x1b[38;2;255;20;147m╠═╣╚═╗║╠═╣║║║╚╦╝ ║ ╠═╣
\x1b[38;2;255;20;147m╩ ╩╚═╝╩╩ ╩╚╩╝ ╩  ╩ ╩ ╩
\x1b[38;2;255;255;0m        >[ H A C K T I V I S M E ]
    """)

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
print_banner()

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
