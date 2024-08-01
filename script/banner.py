from rich.console import Console
from rich.panel import Panel as Panel
#------------[ INDICATION ]---------------#
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE


def title():
  Console().print(Panel("""
  [bold red]███████████████████████    
  [bold red]███████████████████████ [bold yellow]Github : [bold green]
  [bold red]███████████████████████ [bold yellow]Wa     : [bold green]+628953596111**
  [bold white]███████████████████████          
  [bold white]███████████████████████          
  [bold white]███████████████████████ 
  [bold white]""",width=60,style=f"bold cyan"))
