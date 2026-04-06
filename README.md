# 💀 GRABER-X v12.7 - Advanced Metadata Capture 💀

![Version](https://img.shields.io/badge/Version-12.7-red.svg)
![Dev](https://img.shields.io/badge/Dev-Anonymous40443-blue.svg)

> **"Control is an illusion."** - Engenharia social avançada para captura de IP e Localização GPS.

---

## 🚀 Novidades da V12.7
* ✅ **Estabilidade Total:** Correção de bugs no túnel Cloudflare.
* ✅ **Iscas Dinâmicas:** 5 opções de templates (Clima, Speedtest, Ofertas, etc).
* ✅ **Logging:** Salvamento automático em `logs_graber_x.txt`.
* ✅ **Multi-Plataforma:** Compatível com **Kali Linux**, **Termux** e **Windows**.

---

## 🛠️ Instalação e Execução

### 🐧 Kali Linux / Termux
```bash
git clone [https://github.com/Anonymous40443/GRABER-X.git](https://github.com/Anonymous40443/GRABER-X.git)
cd GRABER-X
pip install flask requests
python main.py

python main.py

🪟 Windows

    Tenha o Python instalado.

    pip install flask requests

    python main.py

🌐 Configuração do Túnel

Para rodar externamente, use o Cloudflared:
Bash

cloudflared tunnel --url [http://127.0.0.1:5000](http://127.0.0.1:5000) --protocol http2

👨‍💻 Créditos

Desenvolvido por Anonymous40443.
Siga no TikTok para atualizações: @archmodel57.wha
