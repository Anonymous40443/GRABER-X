#!/bin/bash
echo "Instalando dependências do GRABER X..."
apt update && apt upgrade -y
apt install python python-pip git -y
pip install flask requests
# Se for Termux, tenta baixar o cloudflared
if [ -d "/data/data/com.termux" ]; then
    pkg install cloudflared -y
fi
chmod +x GRABERX.py
echo "Tudo pronto! Use 'python GRABERX.py' para iniciar."
