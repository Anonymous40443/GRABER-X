# 🦅 GRABER-X v12.7 - LEVIATHAN PROTOCOL

![GRABER-X Banner](https://img.shields.io/badge/SECURITY-AUDIT-red?style=for-the-badge&logo=kali-linux)
![Status](https://img.shields.io/badge/STATUS-ACTIVE-brightgreen?style=for-the-badge)

**GRABER-X** é uma estrutura avançada de Engenharia Social e Reconhecimento de Rede projetada para testes de penetração em ambientes laboratoriais. A ferramenta automatiza a criação de túneis seguros e iscas psicológicas para captura de metadados, geolocalização precisa e identificação de dispositivos.

---

## 🛠️ O QUE HÁ DE NOVO NA v12.7?

* **[NEW] Isca 05:** Otimizador de busca de conteúdo (Engenharia Social refinada).
* **[FIX] Cloudflare Stable:** Lógica de delay integrada para evitar erros de conexão no primeiro acesso.
* **[DEV] Device ID:** Identificação automática do modelo do smartphone/PC (User-Agent Parsing).
* **[UI] Purple Spinner:** Interface de carregamento moderna e limpa.
* **[URL] Ultra Masking:** Sistema de camuflagem de links integrado antes da geração.

---

## 🔐 ACESSO & LICENÇA

O sistema opera sob criptografia de ponta. O acesso ao painel principal é restrito via **IDENTIFICATION TOKEN**.

> [!IMPORTANT]
> **A chave de acesso não é gratuita.** Para adquirir seu token e liberar o uso da ferramenta, entre em contato via TikTok:
> 
> 🔗 **Suporte Oficial:** [CLIQUE AQUI - TIKTOK](https://www.tiktok.com/@archmodel57.wha?_r=1&_t=ZS-94uzsz9ny6x)

---

## 🚀 INSTALAÇÃO POR SISTEMA

### 🐉 Kali Linux / Debian / Ubuntu
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 git cloudflared -y
git clone https://github.com/Anonymous40443/GRABER-X.git
cd GRABER-X
pip3 install -r requirements.txt
python3 GRABERX.py

### 🦅 Arch Linux / Manjaro
```bash
sudo pacman -Syu
sudo pacman -S python git cloudflared
git clone https://github.com/Anonymous40443/GRABER-X.git](https://github.com/Anonymous40443/GRABER-X.git
cd GRABER-X
pip install rich flask requests
python GRABERX.py

### 📱 Termux (Android)
```bash
# Atualize o sistema e instale as dependências básicas
pkg update && pkg upgrade -y
pkg install python git cloudflared -y

# Clone o repositório
git clone [https://github.com/Anonymous40443/GRABER-X.git](https://github.com/Anonymous40443/GRABER-X.git)
cd GRABER-X

# Instale as bibliotecas necessárias
pip install rich flask requests

# Inicie a ferramenta
python GRABERX.py

---

## 🌐 COMO USAR (CLOUDFLARE TUNNEL)

Para que o link funcione externamente, o **Cloudflare** deve estar configurado corretamente no seu sistema:

1. **Inicie o Script:** Escolha a opção `02` no menu principal para garantir que o Cloudflare está instalado e pronto para uso.
2. **Gere o Link:** Ao escolher a Opção `01`, o script abrirá um túnel automático e lerá os logs em tempo real.
3. **Estabilidade:** Se o link apresentar erro na primeira tentativa, aguarde 3 segundos. O script v12.7 limpa o cache de log automaticamente para estabilizar a conexão.
4. **Mascaramento:** Use a opção de masking (`y`) para camuflar o link do Cloudflare com uma URL de engenharia social, tornando-a menos suspeita.

---

## 📸 PREVIEW DO SISTEMA
*(Salve um print do seu terminal como 'preview.png' na pasta do projeto para aparecer aqui)*
![Interface Preview](preview.png)

---

## ⚠️ AVISO LEGAL
O uso desta ferramenta para atacar alvos sem consentimento prévio é estritamente ilegal. O desenvolvedor **Anonymous40443** não se responsabiliza pelo uso indevido deste software. Uso exclusivo para fins acadêmicos e auditorias de Red Team.

---
**Developed by Anonymous40443** | [Github Profile](https://github.com/Anonymous40443)
