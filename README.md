# 💀 GRABER-X v12.7 - Advanced Metadata Capture 💀

> "Control is an illusion." - Uma ferramenta avançada de engenharia social para auditoria de redes e captura de geolocalização GPS em ambientes controlados.

---

## 🚀 O que há de novo na V12.7?
* **💎 Interface Moderna:** Nova UI baseada na biblioteca `Rich` com tabelas e painéis dinâmicos.
* **⚡ Automação:** O script agora tenta gerenciar o túnel Cloudflare internamente.
* **🎯 Iscas Realistas:** 5 templates profissionais (Clima, Speedtest, Ofertas, Verificação, Link Encurtado).
* **📊 Logs Inteligentes:** Captura detalhada de IP, Dispositivo e coordenadas GPS com link direto para o Maps.

---

## 🛠️ Instalação e Setup

### 1️⃣ Requisitos de Sistema
Certifique-se de ter o **Python 3.x** e o **Cloudflared** instalados no seu sistema (Kali Linux, Termux ou Windows).

### 2️⃣ Clonando o Repositório (Sem Erros!)
Copie e cole o comando abaixo exatamente como está:

```bash
git clone https://github.com/Anonymous40443/GRABER-X.git
cd GRABER-X

###3️⃣ Instalando Dependências
Bash

pip install flask requests rich

###🌐 Como Usar (Passo a Passo)

Para que a ferramenta funcione para pessoas fora da sua rede Wi-Fi, você precisa de um Túnel.
Passo A: Iniciar o Túnel (Obrigatório)

Abra um novo terminal e execute o Cloudflare para criar o link público:
Bash

cloudflared tunnel --url [http://127.0.0.1:5000](http://127.0.0.1:5000) --protocol http2

Mantenha este terminal aberto! Procure pelo link finalizado em .trycloudflare.com que aparecerá na tela.
Passo B: Iniciar o GRABER-X

No terminal principal (dentro da pasta do projeto), execute:
Bash

python GRABERX.py

Passo C: Configuração

    Selecione a opção [ 1 ] no menu.

    Defina o link de destino (ex: um vídeo do YouTube ou seu TikTok).

    Escolha a Isca que mais combina com seu alvo.

    O script enviará o link pronto para você usar.

📁 Estrutura do Projeto

    GRABERX.py: Script principal com a nova interface moderna.

    logs_graber_x.txt: Arquivo onde todas as capturas bem-sucedidas são salvas.

    cf_log.txt: Arquivo temporário para capturar o link do túnel.

👨‍💻 Créditos & Disclaimer

Desenvolvido por Anonymous40443.

AVISO: Este software foi criado para fins estritamente educacionais e laboratoriais. O uso desta ferramenta para fins maliciosos ou sem o consentimento do alvo é de inteira responsabilidade do usuário. O desenvolvedor não se responsabiliza por mau uso.

Siga no TikTok para atualizações
