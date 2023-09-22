from genericpath import exists
import json
from socket import timeout
from types import EllipsisType
import unicodedata

letras = 'abcdefghijklmnopqrstuvwxyz'

try:
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ModuleNotFoundError:
    import subprocess
    import sys

    subprocess.run(['venv/scripts/activate.bat'], shell=True)
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
    subprocess.run(['deactivate'], shell=True)
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
try:
    import requests
except ModuleNotFoundError:
    import subprocess
    import sys

    subprocess.run(['venv/scripts/activate.bat'], shell=True)
    subprocess.run(['pip', 'install', 'requests'])
    subprocess.run(['deactivate'], shell=True)
    import requests

    sg.theme('DarkGrey14')
    layout = [[sg.Text("Bot atualizado com sucesso.", font=('Open Sans', 10))],
              [sg.Text("Abra novamente.", font=('Open Sans', 10))],
              [sg.Button("OK", button_color='#1c2024')]]
    window = sg.Window("Atualização", layout)
    event, values = window.read()
    window.close()

try:
    from faker import Faker

    fake = Faker('pt_BR')
except ModuleNotFoundError:
    import subprocess
    import sys

    subprocess.run(['venv/scripts/activate.bat'], shell=True)
    subprocess.run(['pip', 'install', 'Faker'])
    subprocess.run(['deactivate'], shell=True)
    from faker import Faker

    fake = Faker('pt_BR')

    sg.theme('DarkGrey14')
    layout = [[sg.Text("Bot atualizado com sucesso.", font=('Open Sans', 10))],
              [sg.Text("Abra novamente.", font=('Open Sans', 10))],
              [sg.Button("OK", button_color='#1c2024')]]
    window = sg.Window("Atualização", layout)
    event, values = window.read()
    window.close()

try:
    import pytz
except ModuleNotFoundError:
    import subprocess
    import sys

    subprocess.run(['venv/scripts/activate.bat'], shell=True)
    subprocess.run(['pip', 'install', 'pytz'])
    subprocess.run(['deactivate'], shell=True)
    import pytz

    sg.theme('DarkGrey14')
    layout = [[sg.Text("Bot atualizado com sucesso.", font=('Open Sans', 10))],
              [sg.Text("Abra novamente.", font=('Open Sans', 10))],
              [sg.Button("OK", button_color='#1c2024')]]
    window = sg.Window("Atualização", layout)
    event, values = window.read()
    window.close()
tz = pytz.timezone('America/Sao_Paulo')
try:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
except ModuleNotFoundError:
    import subprocess
    import sys

    subprocess.run(['venv/scripts/activate.bat'], shell=True)
    subprocess.run(['pip', 'install', 'gspread'])
    subprocess.run(['deactivate'], shell=True)
    subprocess.run(['venv/scripts/activate.bat'], shell=True)
    subprocess.run(['pip', 'install', 'oauth2client'])
    subprocess.run(['deactivate'], shell=True)
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    sg.theme('DarkGrey14')
    layout = [[sg.Text("Bot atualizado com sucesso.", font=('Open Sans', 10))],
              [sg.Text("Abra novamente.", font=('Open Sans', 10))],
              [sg.Button("OK", button_color='#1c2024')]]
    window = sg.Window("Atualização", layout)
    event, values = window.read()
    window.close()

from datetime import datetime
import time

now = datetime.now()
agora = datetime.now().strftime("[%H:%M:%S] ")

import hashlib
import os

if not os.path.exists("relatorio.json"):
    # se o arquivo não existe, pede o nome do arquivo ao usuário e armazena em uma variável global
    with open("relatorio.json", "w") as f:
        pass
else:
    pass

try:
    import PySimpleGUI as sg
except ModuleNotFoundError:
    import subprocess
    import sys

    subprocess.run(['venv/scripts/activate.bat'], shell=True)
    subprocess.run(['pip', 'install', 'PySimpleGUI'])
    subprocess.run(['deactivate'], shell=True)
    import PySimpleGUI as sg

    sg.theme('DarkGrey14')
    layout = [[sg.Text("Bot atualizado com sucesso.", font=('Open Sans', 10))],
              [sg.Text("Abra novamente.", font=('Open Sans', 10))],
              [sg.Button("OK", button_color='#1c2024')]]
    window = sg.Window("Atualização", layout)
    event, values = window.read()
    window.close()

base_url = 'https://raw.githubusercontent.com/wnx3/Creator2.0/main/'

# Lista de arquivos que você deseja verificar e atualizar
file_list = ['relatorio.json', 'requirements.txt', 'CREATOR.pyw']
for file_name in file_list:
    # Caminho local do seu arquivo Python
    local_path = file_name

    # URL completa do arquivo no GitHub
    url = base_url + file_name
    # Obtenha a última versão do arquivo do GitHub
    response = requests.get(url)
    github_version = response.content.decode('utf-8')
    # Verifique se o arquivo local tem a mesma versão do GitHub
    with open(local_path, 'r', encoding='utf-8') as f:
        local_version = f.read()
    local_hash = hashlib.sha256(local_version.encode()).hexdigest()
    github_hash = hashlib.sha256(github_version.encode()).hexdigest()
    if local_hash != github_hash:
        # Baixe a nova versão do GitHub e salve-a localmente
        with open(local_path, 'w', encoding='utf-8') as f:
            f.write(github_version)
        sg.theme('DarkGrey14')
        layout = [[sg.Text("Bot atualizado com sucesso.", font=('Open Sans', 10))],
                  [sg.Text("Abra novamente.", font=('Open Sans', 10))],
                  [sg.Button("OK", button_color='#1c2024')]]
        window = sg.Window("Atualização", layout)
        event, values = window.read()
        window.close()
    else:
        pass
try:
    from minuteinbox import Inbox
except ModuleNotFoundError:
    import subprocess
    import sys

    subprocess.run(['venv/scripts/activate.bat'], shell=True)
    subprocess.run(['pip', 'install', 'minuteinbox'])
    subprocess.run(['deactivate'], shell=True)

    sg.theme('DarkGrey14')
    layout = [[sg.Text("Bot atualizado com sucesso.", font=('Open Sans', 10))],
              [sg.Text("Abra novamente.", font=('Open Sans', 10))],
              [sg.Button("OK", button_color='#1c2024')]]
    window = sg.Window("Atualização", layout)
    event, values = window.read()
    from minuteinbox import Inbox

    window.close()

import multiprocessing
import os
import PySimpleGUI as sg
import time
from datetime import datetime

import threading
import asyncio
import concurrent.futures
import re

try:
    with open("config.json", "r") as f:
        config = json.load(f)
except FileNotFoundError:
    config = {}

import PySimpleGUI as sg

# Tenta abrir o arquivo token.json
try:
    with open("credentials.json", "r") as f:
        # Se o arquivo existir, lê o conteúdo
        content = f.read()
except FileNotFoundError:
    # Se o arquivo não existir, abre uma GUI para informar o usuário
    sg.theme('DarkGrey14')
    layout = [[sg.Text("Arquivo credentials.json não encontrado.", font=('Open Sans', 10))],
              [sg.Button("OK", button_color='#1c2024')]]
    window = sg.Window("Erro", layout)
    event, values = window.read()
    window.close()

sg.theme('DarkGrey14')
# Define a janela de diálogo com um input e um botão

check_img = 'storage\\img\\total.png'
criada_img = 'storage\\img\\check.png'
button_color = sg.theme_background_color()
inicio = [
    [sg.Frame('WNx3 CREATOR', [
        [sg.Button("CREATOR", font=('Open Sans', 9), button_color='#1c2024', border_width=0, size=(35, 1))],
        [sg.Button("CREATOR 2NR", font=('Open Sans', 9), button_color='#1c2024', border_width=0, size=(35, 1))],
        [sg.Button("DIVISOR", font=('Open Sans', 9), button_color='#1c2024', border_width=0, size=(35, 1))],
        [sg.Button("MONTADOR", font=('Open Sans', 9), disabled=True, button_color='#1c2024', border_width=0,
                   size=(35, 1))],
        [sg.Button("CRIAR POR CIMA", font=('Open Sans', 9), disabled=False, button_color='#1c2024', border_width=0,
                   size=(35, 1))]

    ], border_width=3, title_location='n')
     ]]
try:
    state = config['fixtop']
    if state:
        inicio = sg.Window(f'WNx3 CREATOR', inicio, keep_on_top=True)
    else:
        inicio = sg.Window(f'WNx3 CREATOR', inicio, keep_on_top=False)
except:
    inicio = sg.Window(f'WNx3 CREATOR', inicio, keep_on_top=False)

sg.theme('DarkGrey14')
sg.SetOptions(font=('Open Sans', 10))
# Define a janela com uma Multiline e um botão
check_img = 'storage\\img\\total.png'
criada_img = 'storage\\img\\check.png'
# config_img = 'storage/img/config.png'


vpn_list = ["Nenhuma", "AVG", "Avast", "SurfShark", "ExpressVPN", "PiaVPN", "BetterNet", "NordVPN", "CyberGhost",
            "HotspotShield", "HmaVPN", "WindscribeVPN"]
# Definir o layout da GUI de configuração
layout_configuracoes = [
    [sg.Text("Senha dos perfis: ", font=('Open Sans', 12)),
     sg.InputText(key="-senha-", default_text=config.get("senha", ""))],
    [sg.Text('VPN: ', font=('Open Sans', 12)),
     sg.OptionMenu(vpn_list, size=(7, 19), key="-vpn-", default_value=config.get("vpn", ""))],
    [sg.Text('Email ou número: ', font=('Open Sans', 12)),
     sg.Radio('Mail.TM', 'RADIO1', key='-mailtm-', default=config.get("email", "") == "-mailtm-"),
     sg.Radio('MinuteInBox', 'RADIO1', key='-minuteinbox-', default=config.get("email", "") == "-minuteinbox-"),
     sg.Radio('2NR', 'RADIO1', key='-2nr-', default=config.get("email", "") == "-2nr-"),
     sg.Radio('Free SMS', 'RADIO1', key='-freesms-', default=config.get("email", "") == "-freesms-")],
    [sg.Radio('Instagram Lite', 'RADIO2', key='-instalite-', default=config.get("app", "") == "-instalite-"),
     sg.Radio('Instagram', 'RADIO2', key='-insta-', default=config.get("app", "") == "-insta-")],
    [sg.HorizontalSeparator()],
    [sg.Text("Nome da maquina: "), sg.InputText(key="maquina", default_text=config.get("maquina", ""))],
    [sg.Text("SpreadsheetID: "), sg.InputText(key="spreadsheet", default_text=config.get("spreadsheet", ""))],
    [sg.Text("Planilha 2NR: "), sg.InputText(key="2nr", default_text=config.get("2nr", ""))],
    [sg.Button("Salvar", button_color='#1c2024')]
]

# Criar a janela da GUI de configuração
janela_configuracoes = sg.Window("Configurações", layout_configuracoes)

contagem = 0
import subprocess

try:
    comando = f"adb connect 127.0.0.1:{porta}"
    subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
    subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server.test',
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server',
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
except:
    pass


def contagem():
    global nome
    global sobrenome
    contagem += 1
    window['contagem'].update(contagem)
    window.Refresh()


def free_sms_beta():
    SPREADSHEET_ID = config['spreadsheet']
    conteudo = config['vpn']
    senha = config['senha']
    maquina = config['maquina']
    email = 'Free SMS'
    tentativa = False
    seguido = False
    app = 'Normal'
    global sms
    global nomes
    global sobrenomes
    global nome
    global contagem
    global sobrenome
    global lista_user
    window['Executar'].update(disabled=True)
    window.Refresh()
    # Código que gera a saída
    import os
    import time
    import requests
    import hashlib
    from datetime import datetime
    import subprocess

    # verifica se o arquivo existe na pasta do bot

    try:
        import undetected_chromedriver as uc
    except:
        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        subprocess.run(['pip', 'install', 'undetected_chromedriver'])
        subprocess.run(['deactivate'], shell=True)
        import undetected_chromedriver as uc
    try:
        import uiautomator2 as u2
    except:
        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        subprocess.run(['pip', 'install', 'uiautomator2'])
        subprocess.run(['deactivate'], shell=True)
        subprocess.run(['pip', 'install', '--upgrade', 'requests'])
        import requests
        time.sleep(10)
        import uiautomator2 as u2

    try:
        from rich.console import Console
    except ModuleNotFoundError:
        import subprocess
        import sys

        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instalando dependências...')
        window.Refresh()
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
        subprocess.run(['deactivate'], shell=True)
        from rich.console import Console
    try:
        from webdriver_manager.chrome import ChromeDriverManager
    except ModuleNotFoundError:
        import subprocess
        import sys

        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instalando dependências...')
        window.Refresh()
        subprocess.run(['pip', 'install', 'webdriver-manager'])
        subprocess.run(['deactivate'], shell=True)
        from webdriver_manager.chrome import ChromeDriverManager

    d = u2.connect(f'127.0.0.1:{porta}')
    import os
    import time
    import requests
    import hashlib
    import subprocess
    from colorama import init, Fore, Back, Style
    from faker import Faker
    # teste
    init(autoreset=True)
    console = Console()
    from termcolor import colored

    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.rule import Rule

    linha_ret = '_________________________________________________\n'
    window.Refresh()
    import random

    import string
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.common.exceptions import NoSuchElementException
    from selenium import webdriver
    from mailtm import Email
    import re
    import logging

    logger = logging.getLogger(__name__)

    handler = logging.FileHandler('log.txt')
    handler.setLevel(logging.ERROR)

    logger.addHandler(handler)

    # RANGE_NAME = 'contas!A:D'
    #
    # SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    def vpn_avast():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da Avast', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_start("com.avast.android.vpn", ".app.wizard.WizardActivity")
            time.sleep(10)
        except Exception as e:
            print(e)

        abc = False

    def vpn_hotspotshield():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da HotspotShield',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_start("hotspotshield.android.vpn")
        except Exception as e:
            pass
        d(resourceId='hotspotshield.android.vpn:id/btnVpnConnect').click()
        time.sleep(5)
        d(resourceId='hotspotshield.android.vpn:id/btnVpnConnect').click()
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_pia():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da PiaVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_start("com.privateinternetaccess.android", ".ui.LauncherActivity")
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        d(resourceId='com.privateinternetaccess.android:id/connection_background').click()
        time.sleep(3)
        d(resourceId='com.privateinternetaccess.android:id/connection_background').click()

        abc = False

    def vpn_express():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da ExpressVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_start("com.expressvpn.vpn", ".ui.SplashActivity")
        except:
            pass

        abc = False

    def vpn_nord():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da NordVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop("com.nordvpn.android")
            time.sleep(5)
            d.app_start("com.nordvpn.android", ".MainActivity")
        except:
            pass
        time.sleep(20)

        abc = False

    def vpn_surf():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da SurfShark', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            d.app_start("com.surfshark.vpnclient.android", ".StartActivity")
        except:
            pass
        abc = False

    def vpn_better():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da BetterNet', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        try:
            d.app_start("com.freevpnintouch", "com.anchorfree.betternet.ui.BetternetActivity")
        except:
            pass
        time.sleep(10)
        dialog = driver.find_elements(By.ID, 'com.freevpnintouch:id/dialogCtaPositive')
        connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
        if len(dialog) == 1:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/dialogCtaPositive'))).click()
            time.sleep(3)
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
            # time.sleep(5)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
        while connect == 'CONNECT':
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
            time.sleep(4)
            connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
            # WebDriverWait(driver, 20).until(
            # EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        ip = '127.0.0.1:' + porta

        output = subprocess.check_output(['adb', '-s', ip, 'shell', 'ifconfig'])

        # Verifica se a conexão VPN está ativa
        if not re.search(b"tun0", output):
            window['output'].print("Não conectado na BetterNet.")
            window.Refresh()
            try:
                connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
                driver.start_activity("com.freevpnintouch", "com.anchorfree.betternet.ui.BetternetActivity")
                while connect == 'CONNECT':
                    WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
                    time.sleep(4)
                    connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
            except:
                pass
        abc = False

    def vpn_cyberghost():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da CyberGhost', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            d.app_stop("de.mobileconcepts.cyberghost")
            d.app_start("de.mobileconcepts.cyberghost")
            # d.app_start("de.mobileconcepts.cyberghost", ".view.app.AppActivity filter")
        except:
            pass
        d(resourceId='de.mobileconcepts.cyberghost:id/button').click()
        time.sleep(5)
        abc = False

    def vpn_avg():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da AVG', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)
            d.app_stop("com.avg.android.vpn")
            d.app_start("com.avg.android.vpn", "com.avast.android.vpn.app.wizard.WizardActivity")
        except:
            pass
        time.sleep(10)

    def vpn_windscribe():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da Windscribe', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)
            d.app_stop("com.windscribe.vpn")
            d.app_start("com.windscribe.vpn")
        except:
            pass
        d(resourceId='com.windscribe.vpn:id/on_off_button').click()
        time.sleep(10)

    def vpn_hma():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da HMA', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)

            d.app_stop("com.hidemyass.hidemyassprovpn")
            time.sleep(3)
            d.app_start('com.hidemyass.hidemyassprovpn', 'com.avast.android.vpn.activity.HmaOnboardingActivity')
        except:
            pass
        time.sleep(10)

    def gerar_id():
        chars = string.ascii_lowercase + string.digits
        android_id = ''.join(random.choice(chars) for i in range(16))
        return android_id

    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.page_load_strategy = 'none'
    options.add_experimental_option("prefs", prefs)

    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Senha sendo utilizada: {senha}')
    window.Refresh()

    try:
        comando = f"adb connect 127.0.0.1:{porta}"
        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
    except:
        pass
    try:
        comando = f"adb connect 127.0.0.1:{porta}"
        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global window_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global transition_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global animator_duration_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
    except:
        pass
    gerar_id()
    android_id = gerar_id()
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    time.sleep(2)
    # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True, stdout=subprocess.DEVNULL,
    #               stderr=subprocess.DEVNULL)

    try:
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
    except Exception as e:
        pass

    window.Refresh()
    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando sistema inicializar.')
    window.Refresh()
    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Iniciando criação.\n')
    window.Refresh()
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        client = gspread.authorize(creds)

        spreadsheet_id = config['spreadsheet']
        sheet_name = 'contas'
        # Insert user, password, and timestamp into first empty row
        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
        values = sheet.col_values(1)

        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
        rows = sheet.get_all_values()

        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
        regex = re.compile(r'\S+\s\S+')
        sheet_name = config['2nr']
        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
        num_rows = sum(1 for row in rows if regex.match(row[0]))
        window['total'].update(num_rows)
    except Exception as e:
        print(e)
    first = True
    while parar is False:
        if parar is True:
            print('Parando Thread')
            try:
                chrome.close()
            except:
                pass
            try:
                chrome.quit()
            except:
                pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)


        except:
            pass
        gerar_id()
        android_id = gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        stop = False
        try:
            d.app_start('com.instagram.android')
            window['output'].print(linha_ret)
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Abrindo instagram.')
            window.Refresh()
            time.sleep(20)
            try:
                d.xpath('//android.widget.Button[@content-desc="Criar nova conta"]').click(timeout=200)
            except:
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Página estática.')
                window.Refresh()
                stop = True
                conteudo = config['vpn']
                if conteudo == "AVG":
                    vpn_avg()
                elif conteudo == "SurfShark":
                    vpn_surf()
                elif conteudo == "Avast":
                    vpn_avast()
                elif conteudo == "ExpressVPN":
                    vpn_express()
                elif conteudo == "PiaVPN":
                    vpn_pia()
                elif conteudo == "BetterNet":
                    vpn_better()
                elif conteudo == "WindscribeVPN":
                    vpn_windscribe()
                elif conteudo == "CyberGhost":
                    vpn_cyberghost()
                elif conteudo == "NordVPN":
                    vpn_nord()
                elif conteudo == "HmaVPN":
                    vpn_hma()
                elif conteudo == "HotspotShield":
                    vpn_hotspotshield()
                    break
                else:
                    window['output'].print(
                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                    window.Refresh()
            if stop is True:
                raise Exception("skip.")
            
            ######################################################################
            lista_user = random.choices(range(0, 9), k=2)
            lista_letras = random.choices(letras, k=1)

            with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                nomes = nomes_arquivo.readlines()

            with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                sobrenomes = sobrenomes_arquivo.readlines()

            nomea = fake.first_name_female().replace(" ", "")
            nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
            sobrenomea = fake.last_name().replace(" ", "").lower()
            sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
            nome_completo = nome + ' ' + sobrenome
            nome_completo_s = nome + sobrenome
            numeros_concatenados = ''.join(str(numero) for numero in lista_user)
            user_completo1 = nome_completo_s + '' + str(numeros_concatenados) + ''.join(lista_letras)

            user_completo = random.randint(1, len(user_completo1))
            # Insira o ponto no índice aleatório
            string_with_dot = user_completo1[:user_completo] + '_' + user_completo1[user_completo:]
            user_completo = string_with_dot.lower()
            ######################################################################
            
            cancel = d(resourceId='com.google.android.gms:id/cancel')
            if cancel.exists:
                d.xpath('com.google.android.gms:id/cancel').click()
            senha = config['senha']
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Nome escolhido: {nome_completo}')
            window.Refresh()
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText').click()
            time.sleep(1)
            try:
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText').set_text(
                    nome_completo)
            except:
                time.sleep(5)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText').set_text(
                    nome_completo)

            # time.sleep(1)

            d.xpath('//android.view.View[@content-desc="Avançar"]').click()
            # time.sleep(3)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText').set_text(
                senha)
            # time.sleep(1)
            d.xpath('//android.view.View[@content-desc="Avançar"]').click()
            time.sleep(3)
            new_acc = d(resourceId='android:id/button2')
            if new_acc.exists:
                d(resourceId='android:id/button2').click()
            time.sleep(2)
            salvar_senha = d.xpath('//android.view.View[@content-desc="Agora não"]')
            if salvar_senha.exists:
                d.xpath('//android.view.View[@content-desc="Agora não"]').click()

            time.sleep(4)
            new_acc = d.xpath('android:id/button2')
            if new_acc.exists:
                d(resourceId='android:id/button2').click()
                time.sleep(2)
            d.xpath('//android.view.View[@content-desc="Avançar"]').click()
            time.sleep(2)
            d.xpath('//android.view.View[@content-desc="Avançar"]').click()
            idade_aleatoria = random.randint(18, 35)
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Idade escolhida: {idade_aleatoria}')
            window.Refresh()
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText').set_text(
                str(idade_aleatoria))
            d.xpath('//android.view.View[@content-desc="Avançar"]').click()
            # time.sleep(2)
            d(resourceId='android:id/button2').click()
            try:
                d.xpath('//android.view.View[@content-desc="Alterar nome de usuário"]').click()
            except:
                pass
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: {user_completo}')
            window.Refresh()
            # time.sleep(1)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText').set_text(
                '')
            # time.sleep(1)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText').set_text(
                user_completo)
            time.sleep(3)
            d.xpath('//android.view.View[@content-desc="Avançar"]').click()
            
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Abrindo Free SMS.')
            window.Refresh()
            chromedriver_path = r'chromedriver.exe'
            service = Service(chromedriver_path)
            options = uc.ChromeOptions()
            options.add_argument("--blink-settings=imagesEnabled=false")
            options.add_argument("--disable-gpu")
            # Configurações adicionais para o undetected_chromedriver
            import re
            driver_executable_path = ChromeDriverManager().install()
            version_main = int(re.findall('[0-9]+\.', driver_executable_path)[0][:-1])
            chrome = uc.Chrome(use_subprocess=True, options=options,
                               driver_executable_path=driver_executable_path, version_main=version_main, headless=False)
            ## chrome = uc.Chrome(options=options, service=service)
            #chrome.maximize_window()
            # chrome = uc.Chrome(enable_cdp_events=True, headless=True, options=options, service=service)
            # chrome.implicitly_wait(60)
            
            #import undetected_chromedriver as uc
            #from selenium import webdriver
#
            #options = webdriver.ChromeOptions() 
            #chromedriver_path = r'chromedriver.exe'
            #service = Service(chromedriver_path)
            #options.add_argument("start-maximized")
            #options.add_argument("--blink-settings=imagesEnabled=false")
            #options.add_argument("--disable-gpu")
            #options.add_argument("--headless")
            #chrome = uc.Chrome(options=options, service=service)
            
            stop = False
            try:
                chrome.get('https://temporary-phone-number.com/')
                chrome.set_window_size(800,2000)

                try:
                    WebDriverWait(chrome, 35).until(EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[2]/aside/section/ul/li[2]'))).click()
                    # chrome.find_element(By.XPATH, '/html/body/div[2]/aside/section/ul/li[2]').click()
                    time.sleep(2)
                    if chrome.current_url == "https://temporary-phone-number.com/#google_vignette":
                        chrome.back()
                        # time.sleep(5)
                        WebDriverWait(chrome, 35).until(EC.element_to_be_clickable(
                            (By.XPATH, '/html/body/div[2]/aside/section/ul/li[2]'))).click()
                        # chrome.find_element(By.XPATH, '/html/body/div[2]/aside/section/ul/li[2]').click()
                except:
                    chrome.get('https://temporary-phone-number.com/US-Phone-Number/12673800457')
                time.sleep(7)
                num_33 = True
                tentativa = 0
                while num_33 is True or tentativa == 5:
                    try:
                        tentativa = tentativa + 1
                        print(tentativa)
                        if tentativa == 1:
                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Procurando número.')
                            window.Refresh()
                        elif tentativa == 5:
                            window['output'].print(
                                f'[{datetime.now().strftime("%H:%M:%S")}] Não foi possivel gerar um número.')
                            window.Refresh()
                            chrome.quit()
                            raise Exception("skip.")
                        try:
                            time.sleep(4)
                            #chrome.execute_script("document.body.style.zoom='50%'")
                            chrome.save_screenshot('screenshot.png')
                            WebDriverWait(chrome, 35).until(EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, 'body > div.wrapper:nth-child(2) > div.content-wrapper:nth-child(3) > section.content:nth-child(2) > div.row:nth-child(1) > div.col-xs-12:nth-child(2) > div.box-body.text-center:nth-child(3) > button.btn-primary.btn:nth-child(2) > b'))).click()
                            chrome.save_screenshot('screenshot2.png')
                            time.sleep(7)
                            chrome.save_screenshot('screenshot3.png')
                            num = chrome.find_element(By.XPATH,
                                                      '/html/body/div[2]/div/section[2]/div[1]/div[1]/div/h1').text
                            if num.startswith("+33") or num.startswith("+1") or num.startswith("+31"):
                                chrome.find_element(By.XPATH,
                                                    '/html/body/div[2]/div/section[2]/div[1]/div[2]/div[2]/button[2]').click()
                                time.sleep(7)
                            else:
                                num_33 = False
                        except Exception as e:
                            print(e)
                            try:
                                chrome.close()
                            except:
                                pass
                            try:
                                chrome.quit()
                            except:
                                pass
                    except Exception as e:
                        print(e)
                        try:
                            chrome.close()
                        except:
                            pass
                        try:
                            chrome.quit()
                        except:
                            pass
                        raise Exception("skip.")
            except Exception as e:
                print('_____________________________________')
                try:
                    subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android',
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL, check=True, shell=True)


                except:
                    pass
                try:
                    chrome.close()
                except:
                    pass
                try:
                    chrome.quit()
                except:
                    pass
                print(e)

            try:
                print(num)
            except:
                try:
                    chrome.close()
                except:
                    pass
                try:
                    chrome.quit()
                except:
                    pass
                try:
                    subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android',
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL, check=True, shell=True)


                except:
                    pass
                raise Exception("skip.")
            if not num == '+33756495040':
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Número gerado: {num}')
            else:
                raise Exception("Não foi possivel gerar um número.")
            window.Refresh()

            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText').set_text(
                f'{num}')
            time.sleep(1)
            d.xpath('//android.view.View[@content-desc="Avançar"]').click()

            time.sleep(10)
            restricao = d.xpath('//android.view.View[@content-desc="Cadastrar-se com o email"]')

            if restricao.exists:
                chrome.quit()
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Restrição.')
                window.Refresh()
                try:
                    subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android',
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL, check=True, shell=True)


                except:
                    pass
                conteudo = config['vpn']
                if conteudo == "AVG":
                    vpn_avg()
                elif conteudo == "SurfShark":
                    vpn_surf()
                elif conteudo == "Avast":
                    vpn_avast()
                elif conteudo == "ExpressVPN":
                    vpn_express()
                elif conteudo == "PiaVPN":
                    vpn_pia()
                elif conteudo == "BetterNet":
                    vpn_better()
                elif conteudo == "WindscribeVPN":
                    vpn_windscribe()
                elif conteudo == "CyberGhost":
                    vpn_cyberghost()
                elif conteudo == "NordVPN":
                    vpn_nord()
                elif conteudo == "HmaVPN":
                    vpn_hma()
                elif conteudo == "HotspotShield":
                    vpn_hotspotshield()
                    break
                else:
                    window['output'].print(
                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                    window.Refresh()

            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText').click()

            time.sleep(3)
            novo_layout = d.xpath('//android.view.View[@content-desc="Qual é o seu nome?"]')
            if novo_layout.exists:
                chrome.quit()
                window['output'].print(
                    f'[{datetime.now().strftime("%H:%M:%S")}] Layout novo encontrado, reiniciando app.')
                window.Refresh()
                raise Exception("skip.")
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando código...')
            window.Refresh()
            numeros = ''
            encontrado = False
            tentativa = 0
            while not encontrado and tentativa < 6:
                time.sleep(5)
                # Localize o elemento desejado e obtenha o texto

                elemento = WebDriverWait(chrome, 25).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[2]/div/section[2]/div[1]/div[3]/div/div[1]/div[1]/div[2]'))).text

                time_second = WebDriverWait(chrome, 25).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[2]/div/section[2]/div[1]/div[3]/div/div[1]/div[1]/div[1]/time'))).text

                # Verifique se o texto contém 'instagram'
                # if 'Instagram' in elemento.lower() and 'seconds' in time_second.lower():
                if 'Instagram' in elemento and (
                        'seconds' in time_second or '1 min ago' in time_second or '2 mins ago' in time_second):
                    encontrado = True
                    match = re.search(r'\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+',
                                      elemento)  # Extrai seis grupos de dígitos, permitindo espaços entre eles
                    if match:
                        numeros = ''.join(match.group().split())

                else:
                    # Clique no outro elemento
                    tentativa = tentativa + 1
                    time.sleep(5)
                    botao = WebDriverWait(chrome, 25).until(EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[2]/div/section[2]/div[1]/div[2]/div[2]/button[1]')))
                    botao.click()
            if tentativa == 6:
                chrome.quit()
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Codigo não recebido.')
                window.Refresh()
                conteudo = config['vpn']
                if conteudo == "AVG":
                    vpn_avg()
                elif conteudo == "SurfShark":
                    vpn_surf()
                elif conteudo == "Avast":
                    vpn_avast()
                elif conteudo == "ExpressVPN":
                    vpn_express()
                elif conteudo == "PiaVPN":
                    vpn_pia()
                elif conteudo == "WindscribeVPN":
                    vpn_windscribe()
                elif conteudo == "BetterNet":
                    vpn_better()
                elif conteudo == "CyberGhost":
                    vpn_cyberghost()
                elif conteudo == "HmaVPN":
                    vpn_hma()
                elif conteudo == "NordVPN":
                    vpn_nord()
                elif conteudo == "HotspotShield":
                    vpn_hotspotshield()
                    break
                else:
                    window['output'].print(
                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                    window.Refresh()
                raise Exception("Codigo não recebido.")
            codigo = numeros
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Codigo recebido: {codigo}')
            window.Refresh()
            chrome.quit()
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText').set_text(
                codigo)
            # time.sleep(100)
            d.xpath('//android.view.View[@content-desc="Avançar"]').click()
            time.sleep(2)

            codigo_invalido = d.xpath('//android.view.View[@content-desc="Não recebi o código"]')
            if codigo_invalido.exists:
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Código inválido.')
                window.Refresh()
                conteudo = config['vpn']
                if conteudo == "AVG":
                    vpn_avg()
                elif conteudo == "SurfShark":
                    vpn_surf()
                elif conteudo == "Avast":
                    vpn_avast()
                elif conteudo == "ExpressVPN":
                    vpn_express()
                elif conteudo == "PiaVPN":
                    vpn_pia()
                elif conteudo == "WindscribeVPN":
                    vpn_windscribe()
                elif conteudo == "BetterNet":
                    vpn_better()
                elif conteudo == "HmaVPN":
                    vpn_hma()
                elif conteudo == "CyberGhost":
                    vpn_cyberghost()
                elif conteudo == "NordVPN":
                    vpn_nord()
                elif conteudo == "HotspotShield":
                    vpn_hotspotshield()
                else:
                    window['output'].print(
                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                    window.Refresh()

            
            
            
            
            d.xpath('//android.view.View[@content-desc="Concordo"]').click()
            time.sleep(3)
            errodetec = d.xpath('//android.view.View[@content-desc="Concordo"]')
            if errodetec.exists:
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instagram não deixou avançar.')
                window.Refresh()

            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
            window.Refresh()
            time.sleep(35)
            verificar = d.xpath('//android.view.View[@content-desc="Adicionar foto"]')
            # time.sleep(10)
            try:
                if verificar.exists:
                    try:
                        conteudo = config['vpn']
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                               text_color=('lime'))
                        window.Refresh()
                        contagem = contagem + 1
                        window['criadas'].update(contagem)
                        window.Refresh()
                        now = datetime.now()
                        now_brasilia = tz.localize(now)
                        timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")
                        try:
                            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                            creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                            client = gspread.authorize(creds)

                            spreadsheet_id = config['spreadsheet']
                            sheet_name = 'contas'
                            # Insert user, password, and timestamp into first empty row
                            sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                            values = sheet.col_values(1)
                            last_row = len(values)
                            values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina, conteudo + ' - ' + app]
                            cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                            for i, val in enumerate(values):
                                cell_list[i].value = val
                            sheet.update_cells(cell_list)

                            rows = sheet.get_all_values()

                            # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                            regex = re.compile(r'\S+\s\S+')

                            # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                            num_rows = sum(1 for row in rows if regex.match(row[0]))
                        except Exception as e:
                            print(e)
                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Ocorreu um erro ao salvar a conta na planilha.')
                            tempo_aleatorio = random.randint(10, 40)
                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando {tempo_aleatorio} segundos para tentar novamente.')
                            time.sleep(tempo_aleatorio)
                            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                            creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                            client = gspread.authorize(creds)

                            spreadsheet_id = config['spreadsheet']
                            sheet_name = 'contas'
                            # Insert user, password, and timestamp into first empty row
                            sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                            values = sheet.col_values(1)
                            last_row = len(values)
                            values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina, conteudo + ' - ' + app]
                            cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                            for i, val in enumerate(values):
                                cell_list[i].value = val
                            sheet.update_cells(cell_list)

                            rows = sheet.get_all_values()

                            # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                            regex = re.compile(r'\S+\s\S+')

                            # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                            num_rows = sum(1 for row in rows if regex.match(row[0]))
                        window['total'].update(num_rows)
                        random_number = random.random()

                        # Definir a chance desejada (10%)
                        chance = 0.3

                        # Verificar se o número aleatório está abaixo da chance
                        if random_number < chance and not os.path.exists("wn"):
                            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                            creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                            client = gspread.authorize(creds)

                            spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                            sheet_name = 'relatorio_geral'
                            # Insert user, password, and timestamp into first empty row
                            sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                            values = sheet.col_values(1)
                            last_row = len(values)
                            values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina, conteudo + ' - ' + app]
                            cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                            for i, val in enumerate(values):
                                cell_list[i].value = val
                            sheet.update_cells(cell_list)




                    except Exception as e:
                        print(e)

                    window.Refresh()
                    arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                    # Escreva mais conteúdo no arquivo
                    arquivo.write(user_completo + ' ' + senha + "\n")
                    arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                    # Escreva mais conteúdo no arquivo
                    arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                    try:
                        d.xpath('//android.view.View[@content-desc="Pular"]').click()
                        time.sleep(5)
                        d(resourceId='com.instagram.android:id/skip_button').click()
                        time.sleep(5)
                        d(resourceId='com.instagram.android:id/negative_button').click()
                        time.sleep(5)
                        d(resourceId='com.instagram.android:id/skip_button').click()
                        time.sleep(5)
                        try:
                            d.xpath('//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView').click()
                        except:
                            time.sleep(2)
                            d.xpath('//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView').click()
                        time.sleep(5)
                        try:
                            d(resourceId='com.instagram.android:id/button_text').click()
                        except:
                            pass
                        time.sleep(5)
                        try:
                            d(resourceId='com.instagram.android:id/profile_tab').click()
                        except:
                            time.sleep(5)
                            d(resourceId='com.instagram.android:id/tab_avatar').click()
                        sms = False
                    except Exception as e:
                        d.app_stop("com.instagram.android")
                        time.sleep(1)
                        d.app_start("com.instagram.android")
                        sms = False
                        print(e)
                        pass
                else:

                    try:
                        conteudo = config['vpn']

                        # Executa a função correspondente ao conteúdo do arquivo
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "WindscribeVPN":
                            vpn_windscribe()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "HmaVPN":
                            vpn_hma()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()
                    except:
                        sms = True
                        continue
            except Exception as e:
                print(e)
                if conteudo == "AVG":
                    vpn_avg()
                elif conteudo == "Avast":
                    vpn_avast()
                elif conteudo == "CyberGhost":
                    vpn_cyberghost()
                elif conteudo == "PiaVPN":
                    vpn_pia()
                elif conteudo == "ExpressVPN":
                    vpn_express()
                elif conteudo == "SurfShark":
                    vpn_surf()
                elif conteudo == "WindscribeVPN":
                    vpn_windscribe()
                elif conteudo == "HmaVPN":
                    vpn_hma()
                elif conteudo == "BetterNet":
                    vpn_better()
                elif conteudo == "NordVPN":
                    vpn_nord()
                elif conteudo == "HotspotShield":
                    vpn_hotspotshield()
                else:
                    window['output'].print(
                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                    window.Refresh()
                sms = True
            while sms is False:
                try:
                    time.sleep(3)
                    d(resourceId='com.instagram.android:id/profile_tab').click()

                    window['output'].print(linha_ret)
                    window.Refresh()
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Criação de outro perfil.')
                    window.Refresh()
                    seguido = False
                    # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True)
                    # Clicar no botão de perfil

                    time.sleep(3)
                    d(resourceId='com.instagram.android:id/action_bar_title_chevron').click()
                    time.sleep(2)
                    # Clicar em perfis
                    try:
                        d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[last()]/android.widget.FrameLayout/android.widget.ImageView').click()
                    except Exception as e:
                        print(e)
                        print('Erro aq')
                        time.sleep(200)
                    # Clicar em adicionar conta
                    time.sleep(4)
                    d.xpath('//android.widget.Button[@content-desc="Criar nova conta"]').click()

                    time.sleep(3)
                    # Gerar nome de usuário, digitar no campo e clicar em avançae
                    lista_user = random.choices(range(0, 9), k=2)
                    lista_letras = random.choices(letras, k=1)

                    with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                        nomes = nomes_arquivo.readlines()

                    with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                        sobrenomes = sobrenomes_arquivo.readlines()

                    nomea = fake.first_name_female().replace(" ", "")
                    nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                    sobrenomea = fake.last_name().replace(" ", "").lower()
                    sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                    nome_completo = nome + sobrenome
                    numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                    user_completo1 = nome_completo + '' + str(numeros_concatenados) + ''.join(lista_letras)

                    user_completo = random.randint(1, len(user_completo1))
                    # Insira o ponto no índice aleatório
                    string_with_dot = user_completo1[:user_completo] + '_' + user_completo1[user_completo:]
                    user_completo = string_with_dot.lower()
                    print(user_completo)

                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: ' + user_completo)
                    window.Refresh()
                    d(resourceId='com.instagram.android:id/username').set_text(user_completo)
                    time.sleep(3)
                    d(resourceId='com.instagram.android:id/button_text').click()
                    # Digitar senha e avançar
                    time.sleep(3)
                    try:
                        d(resourceId='com.instagram.android:id/password').set_text(senha)
                    except:
                        try:
                            conteudo = config['vpn']
                            if conteudo == "AVG":
                                vpn_avg()
                            elif conteudo == "SurfShark":
                                vpn_surf()
                            elif conteudo == "Avast":
                                vpn_avast()
                            elif conteudo == "ExpressVPN":
                                vpn_express()
                            elif conteudo == "PiaVPN":
                                vpn_pia()
                            elif conteudo == "WindscribeVPN":
                                vpn_windscribe()
                            elif conteudo == "BetterNet":
                                vpn_better()
                            elif conteudo == "CyberGhost":
                                vpn_cyberghost()
                            elif conteudo == "HmaVPN":
                                vpn_hma()
                            elif conteudo == "NordVPN":
                                vpn_nord()
                            elif conteudo == "HotspotShield":
                                vpn_hotspotshield()
                                break
                            else:
                                window['output'].print(
                                    "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                window.Refresh()

                        except:
                            sms = True
                    d(resourceId='com.instagram.android:id/button_text').click()
                    # Clicar em concluir cadastro
                    time.sleep(3)
                    d(resourceId='com.instagram.android:id/button_text').click()

                    time.sleep(4)
                    feedback = d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.View')
                    if feedback.exists:
                        sms = True

                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
                    window.Refresh()
                    # WebDriverWait(driver, 40).until(EC.visibility_of_element_located)(((By.XPATH,
                    #                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')))
                    time.sleep(30)
                    verificar = d(resourceId='com.instagram.android:id/connect_text')
                    if verificar.exists:
                        try:
                            conteudo = config['vpn']
                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                                   text_color=('lime'))
                            window.Refresh()
                            contagem += 1
                            window['criadas'].update(contagem)
                            window.Refresh()
                            now = datetime.now()
                            now_brasilia = tz.localize(now)
                            timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                            try:
                                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                                client = gspread.authorize(creds)

                                spreadsheet_id = config['spreadsheet']
                                sheet_name = 'contas'
                                # Insert user, password, and timestamp into first empty row
                                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                values = sheet.col_values(1)
                                last_row = len(values)
                                values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina, conteudo + ' - ' + app]
                                cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                for i, val in enumerate(values):
                                    cell_list[i].value = val
                                sheet.update_cells(cell_list)

                                rows = sheet.get_all_values()

                                # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                                regex = re.compile(r'\S+\s\S+')

                                # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                                num_rows = sum(1 for row in rows if regex.match(row[0]))
                            except Exception as e:
                                print(e)
                                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Ocorreu um erro ao salvar a conta na planilha.')
                                tempo_aleatorio = random.randint(10, 40)
                                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando {tempo_aleatorio} segundos para tentar novamente.')
                                time.sleep(tempo_aleatorio)
                                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                                client = gspread.authorize(creds)

                                spreadsheet_id = config['spreadsheet']
                                sheet_name = 'contas'
                                # Insert user, password, and timestamp into first empty row
                                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                values = sheet.col_values(1)
                                last_row = len(values)
                                values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina, conteudo + ' - ' + app]
                                cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                for i, val in enumerate(values):
                                    cell_list[i].value = val
                                sheet.update_cells(cell_list)

                                rows = sheet.get_all_values()

                                # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                                regex = re.compile(r'\S+\s\S+')

                                # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                                num_rows = sum(1 for row in rows if regex.match(row[0]))
                            window['total'].update(num_rows)
                            
                            random_number = random.random()

                            # Definir a chance desejada (10%)
                            chance = 0.3

                            # Verificar se o número aleatório está abaixo da chance
                            if random_number < chance and not os.path.exists("wn"):
                                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                                client = gspread.authorize(creds)

                                spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                                sheet_name = 'relatorio_geral'
                                # Insert user, password, and timestamp into first empty row
                                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                values = sheet.col_values(1)
                                last_row = len(values)
                                values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina, conteudo + ' - ' + app]
                                cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                for i, val in enumerate(values):
                                    cell_list[i].value = val
                                sheet.update_cells(cell_list)




                        except:
                            pass

                        window.Refresh()
                        arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                        # Escreva mais conteúdo no arquivo
                        arquivo.write(user_completo + ' ' + senha + "\n")
                        arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                        # Escreva mais conteúdo no arquivo
                        arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                        window.Refresh()
                        d(resourceId='com.instagram.android:id/skip_button').click()
                        time.sleep(1)
                        d(resourceId='com.instagram.android:id/negative_button').click()
                        time.sleep(3)
                        d(resourceId='com.instagram.android:id/skip_button').click()
                        time.sleep(1)
                        try:
                            d.xpath('//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView').click()
                        except:
                            d(resourceId='com.instagram.android:id/skip_button').click()
                            d.xpath('//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView').click()

                        time.sleep(1)
                        time.sleep(3)
                        try:
                            d(resourceId='com.instagram.android:id/profile_tab').click()
                        except:
                            d(resourceId='com.instagram.android:id/button_text').click()
                            d(resourceId='com.instagram.android:id/profile_tab').click()
                        sms = False

                    else:
                        try:
                            conteudo = config['vpn']
                            if conteudo == "AVG":
                                vpn_avg()
                            elif conteudo == "SurfShark":
                                vpn_surf()
                            elif conteudo == "Avast":
                                vpn_avast()
                            elif conteudo == "ExpressVPN":
                                vpn_express()
                            elif conteudo == "PiaVPN":
                                vpn_pia()
                            elif conteudo == "WindscribeVPN":
                                vpn_windscribe()
                            elif conteudo == "BetterNet":
                                vpn_better()
                            elif conteudo == "CyberGhost":
                                vpn_cyberghost()
                            elif conteudo == "HmaVPN":
                                vpn_hma()
                            elif conteudo == "NordVPN":
                                vpn_nord()
                            elif conteudo == "HotspotShield":
                                vpn_hotspotshield()
                            else:
                                window['output'].print(
                                    "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                window.Refresh()

                        except Exception as e:
                            print(e)
                            sms = True
                            try:
                                chrome.close()
                            except:
                                pass
                            try:
                                chrome.quit()
                            except:
                                pass
                            pass
                except Exception as e:
                    print(e)
                    try:
                        chrome.close()
                    except:
                        pass
                    try:
                        chrome.quit()
                    except:
                        pass
                    sms = True
                    pass
            pass

        except Exception as e:
            logger.error('Ocorreu um erro: %s', e)
            try:
                chrome.close()
            except:
                pass
            try:
                chrome.quit()
            except:
                pass
            print(e)
            pass

def free_sms():
    SPREADSHEET_ID = config['spreadsheet']
    conteudo = config['vpn']
    senha = config['senha']
    maquina = config['maquina']
    email = 'Free SMS'
    tentativa = False
    seguido = False
    app = 'Normal'
    global sms
    global nomes
    global sobrenomes
    global nome
    global contagem
    global sobrenome
    global lista_user
    window['Executar'].update(disabled=True)
    window.Refresh()
    # Código que gera a saída
    import os
    import time
    import requests
    import hashlib
    import subprocess

    # verifica se o arquivo existe na pasta do bot

    try:
        import undetected_chromedriver as uc
    except:
        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        subprocess.run(['pip', 'install', 'undetected_chromedriver'])
        subprocess.run(['deactivate'], shell=True)
        import undetected_chromedriver as uc

    try:
        from rich.console import Console
    except ModuleNotFoundError:
        import subprocess
        import sys

        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instalando dependências...')
        window.Refresh()
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
        subprocess.run(['deactivate'], shell=True)
        from rich.console import Console
    import os
    import time
    import requests
    import hashlib
    import subprocess
    from colorama import init, Fore, Back, Style
    from faker import Faker

    linha_ret = '_________________________________________________\n'
    window.Refresh()
    import random
    from datetime import datetime
    import string
    try:
        import uiautomator2 as u2
    except:
        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        subprocess.run(['pip', 'install', 'uiautomator2'])
        subprocess.run(['deactivate'], shell=True)
        subprocess.run(['pip', 'install', '--upgrade', 'requests'])
        import requests
        time.sleep(10)
        import uiautomator2 as u2
    d = u2.connect(f'127.0.0.1:{porta}')
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.common.exceptions import NoSuchElementException
    from mailtm import Email
    import re
    import logging

    logger = logging.getLogger(__name__)

    handler = logging.FileHandler('log.txt')
    handler.setLevel(logging.ERROR)

    logger.addHandler(handler)

    # RANGE_NAME = 'contas!A:D'
    #
    # SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    def vpn_avast():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da Avast', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop("com.avast.android.vpn")
            d.app_start("com.avast.android.vpn", ".app.wizard.WizardActivity")
            time.sleep(10)
        except Exception as e:
            print(e)
        abc = False

    def nenhuma_vpn():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.facebook.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        time.sleep(10)

    def vpn_hotspotshield():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da HotspotShield',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('hotspotshield.android.vpn')
            d.app_start('hotspotshield.android.vpn')
        except Exception as e:
            print(e)
        d(resourceId='hotspotshield.android.vpn:id/tryAgainButton').click()
        time.sleep(5)
        d(resourceId='hotspotshield.android.vpn:id/btnVpnConnect').click()

        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_pia():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da PiaVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.privateinternetaccess.android')
            d.app_start('com.privateinternetaccess.android')
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        d(resourceId='com.privateinternetaccess.android:id/connection_background').click()
        time.sleep(3)
        d(resourceId='com.privateinternetaccess.android:id/connection_background').click()

        abc = False

    def vpn_express():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da ExpressVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.expressvpn.vpn')
            d.app_start('com.expressvpn.vpn')
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        d(resourceId='com.expressvpn.vpn:id/obiButton').click()
        time.sleep(3)
        d(resourceId='com.expressvpn.vpn:id/obiButton').click()

        abc = False

    def vpn_nord():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da NordVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.nordvpn.android')
            time.sleep(5)
            d.app_start('com.nordvpn.android', use_monkey=True)
        except:
            pass
        time.sleep(10)
        time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_surf():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da SurfShark', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            d.app_stop('com.surfshark.vpnclient.android')
            d.app_start('com.surfshark.vpnclient.android')
        except:
            pass
        time.sleep(15)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_better():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da BetterNet', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        try:
            d.app_stop('com.freevpnintouch')
            d.app_start('com.freevpnintouch')
        except:
            pass
        time.sleep(10)
        dialog = d(resourceId='com.freevpnintouch:id/dialogCtaPositive')
        connect = d(resourceId='com.freevpnintouch:id/buttonConnect').get_text(timeout=80)
        if dialog.exists:
            d(resourceId='com.freevpnintouch:id/dialogCtaPositive').click()
            time.sleep(3)
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
            # time.sleep(5)
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
        while connect == 'CONNECT':
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
            time.sleep(4)
            connect = d(resourceId='com.freevpnintouch:id/buttonConnect').get_text(timeout=80)
            # WebDriverWait(driver, 20).until(
            # EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect').click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        ip = '127.0.0.1:' + porta

        output = subprocess.check_output(['adb', '-s', ip, 'shell', 'ifconfig'])

        # Verifica se a conexão VPN está ativa
        if not re.search(b"tun0", output):
            window['output'].print("Não conectado na BetterNet.")
            window.Refresh()
            try:
                connect = d(resourceId='com.freevpnintouch:id/buttonConnect').get_text(timeout=80)
                d.app_stop('com.freevpnintouch')
                d.app_start('com.freevpnintouch')
                while connect == 'CONNECT':
                    d(resourceId='com.freevpnintouch:id/buttonConnect').click()
                    time.sleep(4)
                    connect = d(resourceId='com.freevpnintouch:id/buttonConnect').get_text(timeout=80)
            except:
                pass
        abc = False

    def vpn_cyberghost():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da CyberGhost', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            d.app_stop('de.mobileconcepts.cyberghost')
            d.app_start('de.mobileconcepts.cyberghost')
        except:
            pass
        # time.sleep(3)
        d(resourceId='de.mobileconcepts.cyberghost:id/button').click()
        rate = d(resourceId='de.mobileconcepts.cyberghost:id/rate_me_text')
        if rate.exists:
            d(resourceId='android:id/button2').click()
        time.sleep(2)
        d(resourceId='de.mobileconcepts.cyberghost:id/button').click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        abc = False

    def vpn_avg():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da AVG', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.avg.android.vpn')
            d.app_start("com.avg.android.vpn", "com.avast.android.vpn.app.wizard.WizardActivity")
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #               stderr=subprocess.DEVNULL, check=True, shell=True)

        time.sleep(30)

    def vpn_windscribe():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da Windscribe', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)
            d.app_stop("com.windscribe.vpn")
            d.app_start("com.windscribe.vpn")
        except:
            pass
        d(resourceId='com.windscribe.vpn:id/on_off_button').click()
        time.sleep(10)

    def vpn_hma():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da HMA', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)

            d.app_stop("com.hidemyass.hidemyassprovpn")
            time.sleep(3)
            d.app_start('com.hidemyass.hidemyassprovpn', 'com.avast.android.vpn.activity.HmaOnboardingActivity')
        except:
            pass
        time.sleep(10)

    def gerar_id():
        chars = string.ascii_lowercase + string.digits
        android_id = ''.join(random.choice(chars) for i in range(16))
        return android_id

    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.page_load_strategy = 'none'
    options.add_experimental_option("prefs", prefs)

    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Senha sendo utilizada: {senha}')
    window.Refresh()

    console = Console()

    device = [
        {'name': 'Bluestacks1', 'port': porta, 'udid': f'127.0.0.1:{porta}'},
    ]
    try:
        comando = f"adb connect 127.0.0.1:{porta}"
        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server.test', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
    except:
        pass
    try:
        comando = f"adb connect 127.0.0.1:{porta}"
        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global window_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global transition_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global animator_duration_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
    except:
        pass
    gerar_id()
    android_id = gerar_id()
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    time.sleep(2)
    # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True, stdout=subprocess.DEVNULL,
    #               stderr=subprocess.DEVNULL)

    try:
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
    except Exception as e:
        pass

    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Efetuando troca de IP.')
    window.Refresh()
    try:
        conteudo = config['vpn']
        if conteudo == "AVG":
            vpn_avg()
        elif conteudo == "SurfShark":
            vpn_surf()
        elif conteudo == "Nenhuma":
            nenhuma_vpn()
        elif conteudo == "Avast":
            vpn_avast()
        elif conteudo == "ExpressVPN":
            vpn_express()
        elif conteudo == "PiaVPN":
            vpn_pia()
        elif conteudo == "BetterNet":
            vpn_better()
        elif conteudo == "CyberGhost":
            vpn_cyberghost()
        elif conteudo == "NordVPN":
            vpn_nord()
        elif conteudo == "HotspotShield":
            vpn_hotspotshield()
        elif conteudo == "WindscribeVPN":
            vpn_windscribe()
        elif conteudo == "HmaVPN":
            vpn_hma()
        else:
            window['output'].print(
                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
            window.Refresh()

    except Exception as e:
        pass

    window.Refresh()
    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando sistema inicializar.')
    window.Refresh()
    
    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Iniciando criação.\n')
    window.Refresh()
    d.implicitly_wait(30.0)
    d.set_fastinput_ime(True)
    while parar is False:
        if parar is True:
           print('Parando Thread')
           break
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)


            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
            client = gspread.authorize(creds)

            spreadsheet_id = config['spreadsheet']
            sheet_name = 'contas'
            # Insert user, password, and timestamp into first empty row
            sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
            values = sheet.col_values(1)

            # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
            rows = sheet.get_all_values()

            # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
            regex = re.compile(r'\S+\s\S+')
            sheet_name = config['2nr']
            # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
            num_rows = sum(1 for row in rows if regex.match(row[0]))
            window['total'].update(num_rows)
        except Exception as e:
            print(e)
            window['output'].print(
                f'[{datetime.now().strftime("%H:%M:%S")}] Ocorreu algum erro ao acessar a planilha.')
            window.Refresh()
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Tentando novamente em 1 minuto.')
            window.Refresh()
            time.sleep(60)
            raise Exception('skip')
        first = True
        while True:
            if first is False:
                try:
                    driver.quit()
                except:
                    pass
                try:
                    comando = f"adb disconnect 127.0.0.1:{porta}"
                    subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                    time.sleep(5)
                    subprocess.run(f"adb connect 127.0.0.1:{porta}", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                check=True, shell=True)

                except:
                    pass
                time.sleep(10)
            first = False
            try:
                subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL, check=True, shell=True)


            except:
                pass
            gerar_id()
            android_id = gerar_id()
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
            try:

                try:

                    d.app_start('com.instagram.android')
                    window['output'].print(linha_ret)
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Abrindo instagram.')
                    window.Refresh()
                    d.xpath('//android.widget.Button[@content-desc="Criar nova conta"]').click(timeout=120)
                
                    time.sleep(6)
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Abrindo Free SMS.')
                    window.Refresh()
                    chromedriver_path = 'storage\\driver\\driver.exe'
                    service = Service(chromedriver_path)
                    options = uc.ChromeOptions()
                    options.add_argument("--start-maximized")
                    options.add_argument("--disable-gpu")
                    # Configurações adicionais para o undetected_chromedriver
                    chrome = uc.Chrome(options=options, service=service)
                    try:
                        chrome.get('https://temporary-phone-number.com/')
                        chrome.set_window_size(800, 2000)
                        time.sleep(10)

                        try:
                            WebDriverWait(chrome, 30).until(
                                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/aside/section/ul/li[2]'))).click()
                            time.sleep(2)
                            print('0')
                            if chrome.current_url == "https://temporary-phone-number.com/#google_vignette":
                                chrome.back()
                                WebDriverWait(chrome, 30).until(EC.element_to_be_clickable(
                                    (By.XPATH, '/html/body/div[2]/aside/section/ul/li[2]'))).click()
                        except:
                            chrome.get('https://temporary-phone-number.com/US-Phone-Number/12673800457')
                        print('0.8')
                        time.sleep(13)
                        num_33 = True
                        while num_33 is True:
                            try:
                                chrome.find_element(By.XPATH,
                                                    '/html/body/div[2]/div/section[2]/div[1]/div[2]/div[2]/button[2]').click()
                                time.sleep(7)
                                num = chrome.find_element(By.XPATH,
                                                        '/html/body/div[2]/div/section[2]/div[1]/div[1]/div/h1').text
                                if num.startswith("+33") or num.startswith("+1"):
                                    chrome.find_element(By.XPATH,
                                                        '/html/body/div[2]/div/section[2]/div[1]/div[2]/div[2]/button[2]').click()
                                    time.sleep(7)
                                else:
                                    num_33 = False
                            except:
                                chrome.quit()
                                driver.quit()
                    except Exception as e:
                        print('_____________________________________')
                        try:
                            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android',
                                        stdout=subprocess.DEVNULL,
                                        stderr=subprocess.DEVNULL, check=True, shell=True)


                        except:
                            pass
                        print(e)
                    print('1')
                    if len(novo_layout) == 1:
                        window['output'].print(
                            f'[{datetime.now().strftime("%H:%M:%S")}] Layout novo encontrado, reiniciando app.')
                        window.Refresh()
                        chrome.quit()
                        raise Exception("skip.")

                    try:
                        print(num)
                    except:
                        chrome.quit()
                        driver.quit()
                        try:
                            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android',
                                        stdout=subprocess.DEVNULL,
                                        stderr=subprocess.DEVNULL, check=True, shell=True)


                        except:
                            pass
                        raise Exception("skip.")
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Número gerado: {num}')
                    window.Refresh()

                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText'))).send_keys(
                        f'{num}')
                    time.sleep(1)
                    WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Avançar"]'))).click()

                    time.sleep(10)
                    restricao = driver.find_elements(By.XPATH,
                                                    '//android.view.View[@content-desc="Cadastrar-se com o email"]')

                    if len(restricao) == 1:
                        chrome.quit()
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Restrição.')
                        window.Refresh()
                        try:
                            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android',
                                        stdout=subprocess.DEVNULL,
                                        stderr=subprocess.DEVNULL, check=True, shell=True)


                        except:
                            pass
                        conteudo = config['vpn']
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                            break
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()
                        driver.quit()

                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText'))).click()
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando código...')
                    window.Refresh()

                    time.sleep(3)
                    numeros = ''
                    encontrado = False
                    tentativa = 0
                    while not encontrado and tentativa < 6:
                        time.sleep(5)
                        # Localize o elemento desejado e obtenha o texto
                        elemento = chrome.find_element(By.XPATH,
                                                    '/html/body/div[2]/div/section[2]/div[1]/div[3]/div/div[1]/div[1]/div[2]').text
                        time_second = chrome.find_element(By.XPATH,
                                                        '/html/body/div[2]/div/section[2]/div[1]/div[3]/div/div[1]/div[1]/div[1]/time').text

                        # Verifique se o texto contém 'instagram'
                        # if 'Instagram' in elemento.lower() and 'seconds' in time_second.lower():
                        if 'Instagram' in elemento and (
                                'seconds' in time_second or '1 min ago' in time_second or '2 mins ago' in time_second):
                            encontrado = True
                            match = re.search(r'\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+',
                                            elemento)  # Extrai seis grupos de dígitos, permitindo espaços entre eles
                            if match:
                                numeros = ''.join(match.group().split())

                        else:
                            # Clique no outro elemento
                            tentativa = tentativa + 1
                            time.sleep(10)
                            botao = chrome.find_element(By.XPATH,
                                                        '/html/body/div[2]/div/section[2]/div[1]/div[2]/div[2]/button[1]')
                            botao.click()
                    if tentativa == 6:
                        chrome.quit()
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Codigo não recebido.')
                        window.Refresh()
                        conteudo = config['vpn']
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                            break
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()
                        driver.quit()
                        raise Exception("Codigo não recebido.")
                    codigo = numeros
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Codigo recebido: {codigo}')
                    window.Refresh()
                    chrome.quit()
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText'))).send_keys(
                        codigo)
                    # time.sleep(100)
                    WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Avançar"]'))).click()
                    time.sleep(4)

                    codigo_invalido = driver.find_elements(By.XPATH,
                                                        '//android.view.View[@content-desc="Não recebi o código"]')
                    if len(codigo_invalido) == 1:
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Código inválido.')
                        window.Refresh()
                        #
                        conteudo = config['vpn']
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()

                    ######################################################################
                    lista_user = random.choices(range(0, 9), k=2)
                    lista_letras = random.choices(letras, k=1)

                    with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                        nomes = nomes_arquivo.readlines()

                    with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                        sobrenomes = sobrenomes_arquivo.readlines()

                    nomea = fake.first_name_female().replace(" ", "")
                    nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                    sobrenomea = fake.last_name().replace(" ", "").lower()
                    sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                    nome_completo = nome + ' ' + sobrenome
                    nome_completo_s = nome + sobrenome
                    numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                    user_completo = nome_completo_s + '' + str(numeros_concatenados) + ''.join(lista_letras)
                    ######################################################################

                    cancel = driver.find_elements(By.ID, 'com.google.android.gms:id/cancel')
                    if len(cancel) == 1:
                        driver.find_element(By.ID, 'com.google.android.gms:id/cancel').click()
                    senha = config['senha']
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText'))).send_keys(
                        nome_completo)
                    time.sleep(1)
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Nome escolhido: {nome_completo}')
                    window.Refresh()
                    WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Avançar"]'))).click()
                    time.sleep(10)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText'))).send_keys(
                        senha)
                    time.sleep(1)
                    WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Avançar"]'))).click()
                    time.sleep(5)
                    new_acc = driver.find_elements(By.ID, 'android:id/button2')
                    if len(new_acc) == 1:
                        driver.find_element(By.ID, 'android:id/button2').click()
                    time.sleep(2)
                    salvar_senha = driver.find_elements(By.XPATH, '//android.view.View[@content-desc="Agora não"]')
                    if len(salvar_senha) == 1:
                        driver.find_element(By.XPATH, '//android.view.View[@content-desc="Agora não"]').click()

                    time.sleep(3)
                    new_acc = driver.find_elements(By.ID, 'android:id/button2')
                    if len(new_acc) == 1:
                        driver.find_element(By.ID, 'android:id/button2').click()
                        time.sleep(2)
                    WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Avançar"]'))).click()
                    time.sleep(2)
                    WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Avançar"]'))).click()
                    idade_aleatoria = random.randint(18, 35)
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Idade escolhida: {idade_aleatoria}')
                    window.Refresh()
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText'))).send_keys(
                        idade_aleatoria)
                    WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Avançar"]'))).click()
                    time.sleep(2)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'android:id/button2'))).click()
                    try:
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                            (By.XPATH, '//android.view.View[@content-desc="Alterar nome de usuário"]'))).click()
                    except:
                        pass
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: {user_completo}')
                    window.Refresh()
                    time.sleep(3)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText'))).clear()
                    time.sleep(2)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText'))).send_keys(
                        user_completo)
                    time.sleep(3)
                    WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Avançar"]'))).click()
                    WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '//android.view.View[@content-desc="Concordo"]'))).click()
                    time.sleep(3)
                    errodetec = driver.find_elements(By.XPATH, '//android.view.View[@content-desc="Concordo"]')
                    if len(errodetec) == 1:
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instagram não deixou avançar.')
                        window.Refresh()

                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
                    window.Refresh()
                    time.sleep(20)
                    verificar = driver.find_elements(By.XPATH, '//android.view.View[@content-desc="Adicionar foto"]')
                    # time.sleep(10)
                    try:
                        if len(verificar) == 1:
                            try:
                                conteudo = config['vpn']
                                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                                    text_color=('lime'))
                                window.Refresh()
                                contagem = contagem + 1
                                window['criadas'].update(contagem)
                                window.Refresh()
                                now = datetime.now()
                                now_brasilia = tz.localize(now)
                                timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                                client = gspread.authorize(creds)

                                spreadsheet_id = config['spreadsheet']
                                sheet_name = 'contas'
                                # Insert user, password, and timestamp into first empty row
                                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                values = sheet.col_values(1)
                                last_row = len(values)
                                values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                        conteudo + ' - ' + app]
                                cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                for i, val in enumerate(values):
                                    cell_list[i].value = val
                                sheet.update_cells(cell_list)

                                rows = sheet.get_all_values()

                                # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                                regex = re.compile(r'\S+\s\S+')

                                # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                                num_rows = sum(1 for row in rows if regex.match(row[0]))
                                window['total'].update(num_rows)
                                time.sleep(4)
                                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                                client = gspread.authorize(creds)

                                spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                                sheet_name = 'relatorio_geral'
                                # Insert user, password, and timestamp into first empty row
                                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                values = sheet.col_values(1)
                                last_row = len(values)
                                values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                        conteudo + ' - ' + app]
                                cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                for i, val in enumerate(values):
                                    cell_list[i].value = val
                                sheet.update_cells(cell_list)




                            except Exception as e:
                                print(e)

                            window.Refresh()
                            arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                            # Escreva mais conteúdo no arquivo
                            arquivo.write(user_completo + ' ' + senha + "\n")
                            arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                            # Escreva mais conteúdo no arquivo
                            arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                            try:
                                WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
                                    (By.XPATH, '//android.view.View[@content-desc="Pular"]'))).click()
                                time.sleep(5)
                                WebDriverWait(driver, 30).until(
                                    EC.element_to_be_clickable((By.ID, 'com.instagram.android:id/skip_button'))).click()
                                time.sleep(5)
                                WebDriverWait(driver, 30).until(
                                    EC.element_to_be_clickable((By.ID, 'com.instagram.android:id/negative_button'))).click()
                                time.sleep(5)
                                WebDriverWait(driver, 30).until(
                                    EC.element_to_be_clickable((By.ID, 'com.instagram.android:id/skip_button'))).click()
                                time.sleep(5)
                                try:
                                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                                '//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView'))).click()
                                except:
                                    time.sleep(2)
                                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                                '//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView'))).click()
                                time.sleep(5)
                                try:
                                    WebDriverWait(driver, 5).until(
                                        EC.element_to_be_clickable((By.ID, 'com.instagram.android:id/button_text'))).click()
                                except:
                                    pass
                                time.sleep(5)
                                try:
                                    WebDriverWait(driver, 30).until(
                                        EC.element_to_be_clickable((By.ID, 'com.instagram.android:id/profile_tab'))).click()
                                except:
                                    time.sleep(5)
                                    WebDriverWait(driver, 30).until(
                                        EC.element_to_be_clickable((By.ID, 'com.instagram.android:id/tab_avatar'))).click()
                                sms = False
                            except:
                                pass
                        else:
                            try:
                                driver.terminate_app('com.instagram.android')
                            except:
                                pass
                            time.sleep(3)
                            driver.activate_app('com.instagram.android')
                            time.sleep(10)
                            verificar = driver.find_elements(By.ID, 'com.instagram.android:id/profile_tab')
                            if len(verificar) == 1:
                                try:
                                    conteudo = config['vpn']
                                    window['output'].print(
                                        f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                        text_color=('lime'))
                                    window.Refresh()
                                    contagem += 1
                                    window['criadas'].update(contagem)
                                    window.Refresh()
                                    now = datetime.now()
                                    now_brasilia = tz.localize(now)
                                    timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                                    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                                    client = gspread.authorize(creds)

                                    spreadsheet_id = config['spreadsheet']
                                    sheet_name = 'contas'
                                    # Insert user, password, and timestamp into first empty row
                                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                    values = sheet.col_values(1)
                                    last_row = len(values)
                                    values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                            conteudo + ' - ' + app]
                                    cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                    for i, val in enumerate(values):
                                        cell_list[i].value = val
                                    sheet.update_cells(cell_list)

                                    rows = sheet.get_all_values()

                                    # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                                    regex = re.compile(r'\S+\s\S+')

                                    # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                                    num_rows = sum(1 for row in rows if regex.match(row[0]))
                                    window['total'].update(num_rows)
                                    time.sleep(4)
                                    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                    creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                                    client = gspread.authorize(creds)

                                    spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                                    sheet_name = 'relatorio_geral'
                                    # Insert user, password, and timestamp into first empty row
                                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                    values = sheet.col_values(1)
                                    last_row = len(values)
                                    values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                            conteudo + ' - ' + app]
                                    cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                    for i, val in enumerate(values):
                                        cell_list[i].value = val
                                    sheet.update_cells(cell_list)




                                except:
                                    pass

                                window.Refresh()
                                arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                                # Escreva mais conteúdo no arquivo
                                arquivo.write(user_completo + ' ' + senha + "\n")
                                arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                                # Escreva mais conteúdo no arquivo
                                arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                                try:
                                    try:
                                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
                                            (By.ID, 'com.instagram.android:id/profile_tab'))).click()
                                    except:
                                        time.sleep(2)
                                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
                                            (By.ID, 'com.instagram.android:id/tab_avatar'))).click()
                                    sms = False
                                except:
                                    pass
                            else:

                                try:
                                    conteudo = config['vpn']

                                    # Executa a função correspondente ao conteúdo do arquivo
                                    if conteudo == "AVG":
                                        vpn_avg()
                                    elif conteudo == "Avast":
                                        vpn_avast()
                                    elif conteudo == "CyberGhost":
                                        vpn_cyberghost()
                                    elif conteudo == "PiaVPN":
                                        vpn_pia()
                                    elif conteudo == "ExpressVPN":
                                        vpn_express()
                                    elif conteudo == "SurfShark":
                                        vpn_surf()
                                    elif conteudo == "BetterNet":
                                        vpn_better()
                                    elif conteudo == "NordVPN":
                                        vpn_nord()
                                    elif conteudo == "HotspotShield":
                                        vpn_hotspotshield()
                                    else:
                                        window['output'].print(
                                            "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                        window.Refresh()
                                    driver.quit()
                                except:
                                    sms = True
                                    driver.quit()
                                    continue
                    except Exception as e:
                        print(e)
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()
                        sms = True
                        driver.quit()
                    while sms is False:
                        try:
                            time.sleep(3)
                            WebDriverWait(driver, 30).until(
                                EC.element_to_be_clickable((By.ID, 'com.instagram.android:id/profile_tab'))).click()

                            window['output'].print(linha_ret)
                            window.Refresh()
                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Criação de outro perfil.')
                            window.Refresh()
                            seguido = False
                            # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True)
                            # Clicar no botão de perfil

                            time.sleep(3)
                            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID,
                                                                                        'com.instagram.android:id/action_bar_title_chevron'))).click()
                            time.sleep(2)
                            # Clicar em perfis
                            try:
                                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[last()]/android.widget.FrameLayout/android.widget.ImageView'))).click()
                            except Exception as e:
                                print(e)
                                print('Erro aq')
                                time.sleep(200)
                            # Clicar em adicionar conta
                            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                            '//android.widget.Button[@content-desc="Criar nova conta"]'))).click()

                            time.sleep(3)
                            # Gerar nome de usuário, digitar no campo e clicar em avançae
                            lista_user = random.choices(range(0, 9), k=2)
                            lista_letras = random.choices(letras, k=1)

                            with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                                nomes = nomes_arquivo.readlines()

                            with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                                sobrenomes = sobrenomes_arquivo.readlines()

                            nomea = fake.first_name_female().replace(" ", "")
                            nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                            sobrenomea = fake.last_name().replace(" ", "").lower()
                            sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                            nome_completo = nome + sobrenome
                            numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                            user_completo = nome_completo + '' + str(numeros_concatenados) + ''.join(lista_letras)

                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: ' + user_completo)
                            window.Refresh()
                            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID,
                                                                                            'com.instagram.android:id/username'))).send_keys(
                                user_completo)
                            time.sleep(3)
                            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID,
                                                                                        'com.instagram.android:id/button_text'))).click()
                            # Digitar senha e avançar
                            time.sleep(3)
                            try:
                                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID,
                                                                                                'com.instagram.android:id/password'))).send_keys(
                                    senha)
                            except:
                                try:
                                    conteudo = config['vpn']
                                    if conteudo == "AVG":
                                        vpn_avg()
                                    elif conteudo == "SurfShark":
                                        vpn_surf()
                                    elif conteudo == "Avast":
                                        vpn_avast()
                                    elif conteudo == "ExpressVPN":
                                        vpn_express()
                                    elif conteudo == "PiaVPN":
                                        vpn_pia()
                                    elif conteudo == "BetterNet":
                                        vpn_better()
                                    elif conteudo == "CyberGhost":
                                        vpn_cyberghost()
                                    elif conteudo == "NordVPN":
                                        vpn_nord()
                                    elif conteudo == "HotspotShield":
                                        vpn_hotspotshield()
                                        break
                                    else:
                                        window['output'].print(
                                            "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                        window.Refresh()

                                except:
                                    sms = True
                            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID,
                                                                                        'com.instagram.android:id/button_text'))).click()
                            # Clicar em concluir cadastro
                            time.sleep(3)
                            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID,
                                                                                            'com.instagram.android:id/button_text'))).click()

                            time.sleep(4)
                            feedback = driver.find_elements(By.XPATH,
                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.View')
                            if len(feedback) == 1:
                                sms = True

                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
                            window.Refresh()
                            # WebDriverWait(driver, 40).until(EC.visibility_of_element_located)(((By.XPATH,
                            #                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')))
                            time.sleep(20)
                            verificar = driver.find_elements(By.ID,
                                                            'com.instagram.android:id/connect_text')
                            if len(verificar) == 1:
                                try:
                                    conteudo = config['vpn']
                                    window['output'].print(
                                        f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                        text_color=('lime'))
                                    window.Refresh()
                                    contagem += 1
                                    window['criadas'].update(contagem)
                                    window.Refresh()
                                    now = datetime.now()
                                    now_brasilia = tz.localize(now)
                                    timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                                    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                                    client = gspread.authorize(creds)

                                    spreadsheet_id = config['spreadsheet']
                                    sheet_name = 'contas'
                                    # Insert user, password, and timestamp into first empty row
                                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                    values = sheet.col_values(1)
                                    last_row = len(values)
                                    values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                            conteudo + ' - ' + app]
                                    cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                    for i, val in enumerate(values):
                                        cell_list[i].value = val
                                    sheet.update_cells(cell_list)

                                    rows = sheet.get_all_values()

                                    # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                                    regex = re.compile(r'\S+\s\S+')

                                    # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                                    num_rows = sum(1 for row in rows if regex.match(row[0]))
                                    window['total'].update(num_rows)
                                    time.sleep(4)
                                    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                    creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                                    client = gspread.authorize(creds)

                                    spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                                    sheet_name = 'relatorio_geral'
                                    # Insert user, password, and timestamp into first empty row
                                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                    values = sheet.col_values(1)
                                    last_row = len(values)
                                    values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                            conteudo + ' - ' + app]
                                    cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                    for i, val in enumerate(values):
                                        cell_list[i].value = val
                                    sheet.update_cells(cell_list)




                                except:
                                    pass

                                window.Refresh()
                                arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                                # Escreva mais conteúdo no arquivo
                                arquivo.write(user_completo + ' ' + senha + "\n")
                                arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                                # Escreva mais conteúdo no arquivo
                                arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                                window.Refresh()
                                WebDriverWait(driver, 30).until(
                                    EC.element_to_be_clickable((By.ID, 'com.instagram.android:id/skip_button'))).click()
                                time.sleep(1)
                                WebDriverWait(driver, 30).until(
                                    EC.element_to_be_clickable((By.ID, 'com.instagram.android:id/negative_button'))).click()
                                time.sleep(3)
                                WebDriverWait(driver, 30).until(
                                    EC.element_to_be_clickable((By.ID, 'com.instagram.android:id/skip_button'))).click()
                                time.sleep(1)
                                try:
                                    WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH,
                                                                                            '//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView'))).click()
                                except:
                                    WebDriverWait(driver, 30).until(
                                        EC.element_to_be_clickable((By.ID, 'com.instagram.android:id/skip_button'))).click()
                                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                                '//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView'))).click()

                                time.sleep(1)
                                time.sleep(3)
                                try:
                                    WebDriverWait(driver, 10).until(
                                        EC.element_to_be_clickable((By.ID, 'com.instagram.android:id/profile_tab'))).click()
                                except:
                                    WebDriverWait(driver, 30).until(
                                        EC.element_to_be_clickable((By.ID, 'com.instagram.android:id/button_text'))).click()
                                    WebDriverWait(driver, 10).until(
                                        EC.element_to_be_clickable((By.ID, 'com.instagram.android:id/profile_tab'))).click()
                                sms = False

                            else:
                                try:
                                    conteudo = config['vpn']
                                    if conteudo == "AVG":
                                        vpn_avg()
                                    elif conteudo == "SurfShark":
                                        vpn_surf()
                                    elif conteudo == "Avast":
                                        vpn_avast()
                                    elif conteudo == "ExpressVPN":
                                        vpn_express()
                                    elif conteudo == "PiaVPN":
                                        vpn_pia()
                                    elif conteudo == "BetterNet":
                                        vpn_better()
                                    elif conteudo == "CyberGhost":
                                        vpn_cyberghost()
                                    elif conteudo == "NordVPN":
                                        vpn_nord()
                                    elif conteudo == "HotspotShield":
                                        vpn_hotspotshield()
                                        break
                                    else:
                                        window['output'].print(
                                            "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                        window.Refresh()

                                except Exception as e:
                                    sms = True
                                    driver.quit()
                                    pass
                        except Exception as e:
                            sms = True
                            driver.quit()
                            pass


                except Exception as e:
                    try:
                        chrome.quit()
                        driver.quit()
                    except:
                        pass
                    print(e)
                    pass

            except Exception as e:
                try:
                    chrome.quit()
                    driver.quit()
                except:
                    pass
                print(e)
                pass


def free_sms_lite():
    SPREADSHEET_ID = config['spreadsheet']
    conteudo = config['vpn']
    senha = config['senha']
    maquina = config['maquina']
    tentativa = False
    email = 'Free SMS'
    seguido = False
    app = 'Lite'
    global sms
    global nomes
    global sobrenomes
    global nome
    global contagem
    global sobrenome
    global lista_user
    window['Executar'].update(disabled=True)
    window.Refresh()
    # Código que gera a saída
    import os
    import time
    from datetime import datetime
    import requests
    import hashlib
    import subprocess

    # verifica se o arquivo existe na pasta do bot
    try:
        import undetected_chromedriver as uc
    except:
        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        subprocess.run(['pip', 'install', 'undetected_chromedriver'])
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instalando dependências...')
        window.Refresh()
        subprocess.run(['deactivate'], shell=True)
        import undetected_chromedriver as uc
    try:
        import uiautomator2 as u2
    except:
        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        subprocess.run(['pip', 'install', 'uiautomator2'])
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instalando dependências...')
        window.Refresh()
        subprocess.run(['deactivate'], shell=True)
        subprocess.run(['pip', 'install', '--upgrade', 'requests'])
        import requests
        time.sleep(10)
        import uiautomator2 as u2
    try:
        from webdriver_manager.chrome import ChromeDriverManager
    except ModuleNotFoundError:
        import subprocess
        import sys

        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instalando dependências...')
        window.Refresh()
        subprocess.run(['pip', 'install', 'webdriver-manager'])
        subprocess.run(['deactivate'], shell=True)
        from webdriver_manager.chrome import ChromeDriverManager
    d = u2.connect(f'127.0.0.1:{porta}')
    import os
    import time
    import requests
    import hashlib
    import subprocess
    from colorama import init, Fore, Back, Style
    from faker import Faker
    # teste

    linha_ret = '_________________________________________________\n'
    window.Refresh()
    import random
    import phonenumbers
    import string
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.common.exceptions import NoSuchElementException
    from mailtm import Email
    import re
    import logging

    logger = logging.getLogger(__name__)

    handler = logging.FileHandler('log.txt')
    handler.setLevel(logging.ERROR)

    logger.addHandler(handler)

    def vpn_hotspotshield():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da HotspotShield',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_start("hotspotshield.android.vpn")
        except Exception as e:
            pass
        d(resourceId='hotspotshield.android.vpn:id/btnVpnConnect').click()
        time.sleep(5)
        d(resourceId='hotspotshield.android.vpn:id/btnVpnConnect').click()
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_pia():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da PiaVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_start("com.privateinternetaccess.android", ".ui.LauncherActivity")
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        d(resourceId='com.privateinternetaccess.android:id/connection_background').click()
        time.sleep(3)
        d(resourceId='com.privateinternetaccess.android:id/connection_background').click()

        abc = False

    def vpn_express():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da ExpressVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_start("com.expressvpn.vpn", ".ui.SplashActivity")
        except:
            pass

        abc = False

    def vpn_nord():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da NordVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop("com.nordvpn.android")
            time.sleep(5)
            d.app_start("com.nordvpn.android", ".MainActivity")
        except:
            pass
        time.sleep(20)

        abc = False

    def vpn_surf():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da SurfShark', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            d.app_start("com.surfshark.vpnclient.android", ".StartActivity")
        except:
            pass
        abc = False

    def vpn_better():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da BetterNet', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        try:
            d.app_start("com.freevpnintouch", "com.anchorfree.betternet.ui.BetternetActivity")
        except:
            pass
        time.sleep(10)
        dialog = driver.find_elements(By.ID, 'com.freevpnintouch:id/dialogCtaPositive')
        connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
        if len(dialog) == 1:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/dialogCtaPositive'))).click()
            time.sleep(3)
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
            # time.sleep(5)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
        while connect == 'CONNECT':
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
            time.sleep(4)
            connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
            # WebDriverWait(driver, 20).until(
            # EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        ip = '127.0.0.1:' + porta

        output = subprocess.check_output(['adb', '-s', ip, 'shell', 'ifconfig'])

        # Verifica se a conexão VPN está ativa
        if not re.search(b"tun0", output):
            window['output'].print("Não conectado na BetterNet.")
            window.Refresh()
            try:
                connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
                driver.start_activity("com.freevpnintouch", "com.anchorfree.betternet.ui.BetternetActivity")
                while connect == 'CONNECT':
                    WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
                    time.sleep(4)
                    connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
            except:
                pass
        abc = False

    def vpn_cyberghost():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da CyberGhost', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            d.app_stop("de.mobileconcepts.cyberghost")
            d.app_start("de.mobileconcepts.cyberghost")
            # d.app_start("de.mobileconcepts.cyberghost", ".view.app.AppActivity filter")
        except:
            pass
        d(resourceId='de.mobileconcepts.cyberghost:id/button').click()
        time.sleep(5)
        abc = False

    def vpn_avg():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da AVG', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)
            d.app_stop("com.avg.android.vpn")
            d.app_start("com.avg.android.vpn", "com.avast.android.vpn.app.wizard.WizardActivity")
        except:
            pass
        time.sleep(10)

    def vpn_windscribe():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da Windscribe', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)
            d.app_stop("com.windscribe.vpn")
            d.app_start("com.windscribe.vpn")
        except:
            pass
        d(resourceId='com.windscribe.vpn:id/on_off_button').click()
        time.sleep(10)

    def vpn_hma():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da HMA', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)

            d.app_stop("com.hidemyass.hidemyassprovpn")
            time.sleep(3)
            d.app_start('com.hidemyass.hidemyassprovpn', 'com.avast.android.vpn.activity.HmaOnboardingActivity')
        except:
            pass
        time.sleep(10)

    def gerar_id():
        chars = string.ascii_lowercase + string.digits
        android_id = ''.join(random.choice(chars) for i in range(16))
        return android_id

    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.page_load_strategy = 'none'
    options.add_experimental_option("prefs", prefs)

    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Senha sendo utilizada: {senha}')
    window.Refresh()

    try:
        comando = f"adb connect 127.0.0.1:{porta}"
    except:
        pass
    try:
        comando = f"adb connect 127.0.0.1:{porta}"
        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global window_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global transition_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global animator_duration_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
    except:
        pass
    gerar_id()
    android_id = gerar_id()
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    time.sleep(2)

    window.Refresh()
    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando sistema inicializar.')
    window.Refresh()
    try:
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Iniciando criação.')
        window.Refresh()
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        client = gspread.authorize(creds)

        spreadsheet_id = config['spreadsheet']
        sheet_name = 'contas'
        # Insert user, password, and timestamp into first empty row
        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
        values = sheet.col_values(1)

        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
        rows = sheet.get_all_values()

        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
        regex = re.compile(r'\S+\s\S+')
        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
        num_rows = sum(1 for row in rows if regex.match(row[0]))
        window['total'].update(num_rows)
    except:
        pass
    first = True
    parar = False
    while parar is False:
        if parar is True:
            print('Parando Thread')
            break
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        gerar_id()
        android_id = gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:

            window['output'].print(linha_ret)
            window.Refresh()
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Abrindo instagram.')
            window.Refresh()
            d.app_start('com.instagram.lite')
            time.sleep(5)
            try:
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()
            except:
                pass

            time.sleep(6)
            # d.xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').set_text('21131231')

            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Abrindo Free SMS.')
            window.Refresh()
            chromedriver_path = 'storage\\driver\\driver.exe'
            service = Service(chromedriver_path)
            options = uc.ChromeOptions()
            options.add_argument("--blink-settings=imagesEnabled=false")
            # Configurações adicionais para o undetected_chromedriver

            driver_executable_path = ChromeDriverManager(path=".\\").install()
            version_main = int(re.findall('[0-9]+\.', driver_executable_path)[0][:-1])
            chrome = uc.Chrome(use_subprocess=True, options=options,
                               driver_executable_path=driver_executable_path, version_main=version_main, headless=True)
            # chrome = uc.Chrome(options=options, service=service)
            chrome.maximize_window()
            # chrome = uc.Chrome(enable_cdp_events=True, headless=True, options=options, service=service)
            # chrome.implicitly_wait(60)
            stop = False
            try:
                chrome.get('https://temporary-phone-number.com/')
                # chrome.set_window_size(800,2000)

                try:
                    WebDriverWait(chrome, 35).until(EC.element_to_be_clickable(
                        (By.XPATH, '/html/body/div[2]/aside/section/ul/li[2]'))).click()
                    # chrome.find_element(By.XPATH, '/html/body/div[2]/aside/section/ul/li[2]').click()
                    time.sleep(2)
                    if chrome.current_url == "https://temporary-phone-number.com/#google_vignette":
                        chrome.back()
                        # time.sleep(5)
                        WebDriverWait(chrome, 35).until(EC.element_to_be_clickable(
                            (By.XPATH, '/html/body/div[2]/aside/section/ul/li[2]'))).click()
                        # chrome.find_element(By.XPATH, '/html/body/div[2]/aside/section/ul/li[2]').click()
                except:
                    chrome.get('https://temporary-phone-number.com/US-Phone-Number/12673800457')
                time.sleep(13)
                num_33 = True
                tentativa = 0
                while num_33 is True or tentativa == 5:
                    try:
                        tentativa = tentativa + 1
                        print(tentativa)
                        if tentativa == 1:
                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Procurando número.')
                            window.Refresh()
                        elif tentativa == 5:
                            window['output'].print(
                                f'[{datetime.now().strftime("%H:%M:%S")}] Não foi possivel gerar um número.')
                            window.Refresh()
                            chrome.quit()
                            raise Exception("skip.")
                        try:
                            chrome.find_element(By.XPATH,
                                                '/html/body/div[2]/div/section[2]/div[1]/div[2]/div[2]/button[2]').click()
                            time.sleep(7)
                            num = chrome.find_element(By.XPATH,
                                                      '/html/body/div[2]/div/section[2]/div[1]/div[1]/div/h1').text
                            if num.startswith("+33") or num.startswith("+1") or num.startswith("+31"):
                                chrome.find_element(By.XPATH,
                                                    '/html/body/div[2]/div/section[2]/div[1]/div[2]/div[2]/button[2]').click()
                                time.sleep(7)
                            else:
                                num_33 = False
                        except Exception as e:
                            print(e)
                            chrome.quit()
                    except Exception as e:
                        print(e)
                        chrome.quit()
                        raise Exception("skip.")
            except Exception as e:
                print('_____________________________________')
                try:
                    subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite',
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL, check=True, shell=True)


                except:
                    pass
                print(e)

            try:
                print(num)
            except:
                chrome.quit()
                try:
                    subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite',
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL, check=True, shell=True)


                except:
                    pass
                raise Exception("skip.")
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Número gerado: {num}')
            window.Refresh()

            def separar_ddi(num):
                try:
                    numero_parseado = phonenumbers.parse(num, None)
                    if phonenumbers.is_valid_number(numero_parseado):
                        ddi = str(numero_parseado.country_code)
                        numero_sem_ddi = str(numero_parseado.national_number)
                        return ddi, numero_sem_ddi
                    else:
                        return None
                except phonenumbers.phonenumberutil.NumberParseException:
                    return None

            numero_completo = num
            resultado = separar_ddi(numero_completo)

            if resultado:
                ddi, numero_sem_ddi = resultado
                print("DDI:", ddi)
                print("Número sem DDI:", numero_sem_ddi)
            else:
                print("O número não possui um formato válido.")
            try:
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]').click()
                time.sleep(5)
                print('a')

            except Exception as e:
                print(e)
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Página estática.')
                window.Refresh()
                conteudo = config['vpn']
                if conteudo == "AVG":
                    vpn_avg()
                elif conteudo == "SurfShark":
                    vpn_surf()
                elif conteudo == "Avast":
                    vpn_avast()
                elif conteudo == "ExpressVPN":
                    vpn_express()
                elif conteudo == "PiaVPN":
                    vpn_pia()
                elif conteudo == "BetterNet":
                    vpn_better()
                elif conteudo == "CyberGhost":
                    vpn_cyberghost()
                elif conteudo == "NordVPN":
                    vpn_nord()
                elif conteudo == "HotspotShield":
                    vpn_hotspotshield()
                else:
                    window['output'].print(
                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                    window.Refresh()
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').set_text(
                ddi)
            print('b')
            time.sleep(6)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup/android.view.View').click()
            time.sleep(1)

            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').set_text(
                numero_sem_ddi)
            time.sleep(1)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]').click()

            time.sleep(7)
            restricao = d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')

            if restricao.exists:
                chrome.quit()
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Restrição.')
                window.Refresh()
                tentativa = True
                try:
                    subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite',
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL, check=True, shell=True)


                except:
                    pass
                try:
                    conteudo = config['vpn']
                    if conteudo == "AVG":
                        vpn_avg()
                    elif conteudo == "SurfShark":
                        vpn_surf()
                    elif conteudo == "Avast":
                        vpn_avast()
                    elif conteudo == "ExpressVPN":
                        vpn_express()
                    elif conteudo == "PiaVPN":
                        vpn_pia()
                    elif conteudo == "BetterNet":
                        vpn_better()
                    elif conteudo == "CyberGhost":
                        vpn_cyberghost()
                    elif conteudo == "NordVPN":
                        vpn_nord()
                    elif conteudo == "HotspotShield":
                        vpn_hotspotshield()
                        break
                    else:
                        window['output'].print(
                            "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                        window.Refresh()
                    continue
                except:
                    continue

            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando código...')
            window.Refresh()
            time.sleep(3)
            numeros = ''
            encontrado = False
            tentativa = 0
            while not encontrado and tentativa < 6:
                time.sleep(5)
                # Localize o elemento desejado e obtenha o texto
                elemento = chrome.find_element(By.XPATH,
                                               '/html/body/div[2]/div/section[2]/div[1]/div[3]/div/div[1]/div[1]/div[2]').text
                time_second = chrome.find_element(By.XPATH,
                                                  '/html/body/div[2]/div/section[2]/div[1]/div[3]/div/div[1]/div[1]/div[1]/time').text

                # Verifique se o texto contém 'instagram'
                # if 'Instagram' in elemento.lower() and 'seconds' in time_second.lower():
                if 'Instagram' in elemento and 'seconds' in time_second:
                    encontrado = True
                    match = re.search(r'\d+\s*\d+\s*\d+\s*\d+\s*\d+\s*\d+',
                                      elemento)  # Extrai seis grupos de dígitos, permitindo espaços entre eles
                    if match:
                        numeros = ''.join(match.group().split())

                else:
                    # Clique no outro elemento
                    tentativa = tentativa + 1
                    time.sleep(10)
                    botao = chrome.find_element(By.XPATH,
                                                '/html/body/div[2]/div/section[2]/div[1]/div[2]/div[2]/button[1]')
                    botao.click()
            if tentativa == 6:
                chrome.quit()
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Codigo não recebido.')
                window.Refresh()
                conteudo = config['vpn']
                if conteudo == "AVG":
                    vpn_avg()
                elif conteudo == "SurfShark":
                    vpn_surf()
                elif conteudo == "Avast":
                    vpn_avast()
                elif conteudo == "ExpressVPN":
                    vpn_express()
                elif conteudo == "PiaVPN":
                    vpn_pia()
                elif conteudo == "BetterNet":
                    vpn_better()
                elif conteudo == "CyberGhost":
                    vpn_cyberghost()
                elif conteudo == "NordVPN":
                    vpn_nord()
                elif conteudo == "HotspotShield":
                    vpn_hotspotshield()
                    break
                else:
                    window['output'].print(
                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                    window.Refresh()
                driver.quit()
                raise Exception("Codigo não recebido.")
            codigo = numeros
            chrome.quit()
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Codigo recebido: {codigo}')
            tentativa = False
            window.Refresh()
            time.sleep(5)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').set_text(
                codigo)
            # time.sleep(100)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]').click()
            time.sleep(2)

            codigo_invalido = driver.find_elements(By.XPATH,
                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[2]')
            if len(codigo_invalido) == 0:
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Código inválido.')
                window.Refresh()

                try:
                    conteudo = config['vpn']
                    if conteudo == "AVG":
                        vpn_avg()
                    elif conteudo == "SurfShark":
                        vpn_surf()
                    elif conteudo == "Avast":
                        vpn_avast()
                    elif conteudo == "ExpressVPN":
                        vpn_express()
                    elif conteudo == "PiaVPN":
                        vpn_pia()
                    elif conteudo == "BetterNet":
                        vpn_better()
                    elif conteudo == "CyberGhost":
                        vpn_cyberghost()
                    elif conteudo == "NordVPN":
                        vpn_nord()
                    elif conteudo == "HotspotShield":
                        vpn_hotspotshield()
                        break
                    else:
                        window['output'].print(
                            "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                        window.Refresh()
                except:
                    pass
            ######################################################################
            lista_user = random.choices(range(0, 9), k=2)
            lista_letras = random.choices(letras, k=1)

            with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                nomes = nomes_arquivo.readlines()

            with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                sobrenomes = sobrenomes_arquivo.readlines()

            nomea = fake.first_name_female().replace(" ", "")
            nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
            sobrenomea = fake.last_name().replace(" ", "").lower()
            sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
            nome_completo = nome + ' ' + sobrenome
            nome_completo_s = nome + sobrenome
            numeros_concatenados = ''.join(str(numero) for numero in lista_user)
            user_completo = nome_completo_s + '' + str(numeros_concatenados) + ''.join(lista_letras)
            ######################################################################

            senha = config['senha']
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[1]'))).send_keys(
                nome_completo)
            time.sleep(1)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[2]'))).send_keys(
                senha)
            time.sleep(1)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[5]/android.view.View'))).click()
            time.sleep(3)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
            time.sleep(1)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'))).click()
            time.sleep(2)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[6]'))).click()
            time.sleep(2)
            idade_aleatoria = random.randint(18, 35)
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Idade escolhida: {idade_aleatoria}')
            window.Refresh()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                idade_aleatoria)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
            op2 = driver.find_elements(By.XPATH,
                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[7]/android.view.View')
            op1 = driver.find_elements(By.XPATH,
                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View')
            time.sleep(5)
            try:
                if len(op1) == 0:
                    try:
                        driver.find_element(By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[7]/android.view.View').click()
                    except:
                        driver.find_element(By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[6]/android.view.View').click()
            except:
                try:
                    driver.find_element(By.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View').click()

                except:
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro ao criar')
                    window.Refresh()
                    sms = True
                    continue
            try:
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).clear()
                time.sleep(3)
                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                    user_completo)
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: {user_completo}')
                window.Refresh()
                time.sleep(3)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                time.sleep(5)
                conta_jacriada = driver.find_elements(By.XPATH,
                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]')
                time.sleep(1)
                if len(conta_jacriada) == 1:
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View'))).click()
                erro_2 = driver.find_elements(By.XPATH,
                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[*]/android.view.View[*]/android.widget.Button')
                erro_1 = driver.find_elements(By.XPATH,
                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
                if len(erro_2) == 1:
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Tentando gerar novamente')
                    window.Refresh()
                    time.sleep(5)
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[1]'))).click()
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]'))).click()
                    time.sleep(3)
                if len(erro_1) == 1:
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
                time.sleep(3)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View'))).click()

            except:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
            time.sleep(20)
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()

            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
            window.Refresh()
            time.sleep(5)
            verificar = driver.find_elements(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')
            # time.sleep(10)

            conta_criada = driver.find_elements(By.XPATH,
                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
            conta_sms = driver.find_elements(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.View[4]')

            try:
                if len(verificar) == 1:

                    try:
                        seguido = False
                        conteudo = config['vpn']
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                               text_color=('lime'))
                        window.Refresh()
                        contagem += 1
                        window['criadas'].update(contagem)
                        window.Refresh()
                        now = datetime.now()
                        now_brasilia = tz.localize(now)
                        timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                        client = gspread.authorize(creds)

                        spreadsheet_id = config['spreadsheet']
                        sheet_name = 'contas'
                        # Insert user, password, and timestamp into first empty row
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                        values = sheet.col_values(1)
                        last_row = len(values)
                        values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                  conteudo + ' - ' + app]
                        cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                        for i, val in enumerate(values):
                            cell_list[i].value = val
                        sheet.update_cells(cell_list)

                        rows = sheet.get_all_values()

                        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                        regex = re.compile(r'\S+\s\S+')

                        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                        num_rows = sum(1 for row in rows if regex.match(row[0]))
                        window['total'].update(num_rows)

                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                        creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                        client = gspread.authorize(creds)

                        spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                        sheet_name = 'relatorio_geral'
                        # Insert user, password, and timestamp into first empty row
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                        values = sheet.col_values(1)
                        last_row = len(values)
                        values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                  conteudo + ' - ' + app]
                        cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                        for i, val in enumerate(values):
                            cell_list[i].value = val
                        sheet.update_cells(cell_list)

                        window.Refresh()
                        arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                        # Escreva mais conteúdo no arquivo
                        arquivo.write(user_completo + ' ' + senha + "\n")
                        arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                        # Escreva mais conteúdo no arquivo
                        arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]'))).click()
                        window.Refresh()
                        sms = False
                    except:
                        pass
                else:
                    if seguido is True:
                        seguido = False
                        window['output'].print(
                            f'[{datetime.now().strftime("%H:%M:%S")}] SMS seguidos, Trocando de número.')
                        window.Refresh()
                        driver.activate_app('pl.rs.sip.softphone.newapp')
                        time.sleep(4)
                        WebDriverWait(driver, 30).until(
                            EC.element_to_be_clickable((By.ID, 'pl.rs.sip.softphone.newapp:id/numbers'))).click()
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/androidx.appcompat.widget.LinearLayoutCompat'))).click()
                        WebDriverWait(driver, 30).until(
                            EC.element_to_be_clickable((By.ID, 'pl.rs.sip.softphone.newapp:id/buttonDelete'))).click()
                        WebDriverWait(driver, 30).until(
                            EC.element_to_be_clickable((By.ID, 'pl.rs.sip.softphone.newapp:id/buttonAgree'))).click()
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Número excluído.')
                        window.Refresh()
                        sms = True
                    elif seguido is False:
                        seguido = True
                    try:
                        conteudo = config['vpn']

                        # Executa a função correspondente ao conteúdo do arquivo
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()
                    except:
                        sms = True
                        continue
            except Exception as e:
                print(e)
                try:
                    if conteudo == "AVG":
                        vpn_avg()
                    elif conteudo == "Avast":
                        vpn_avast()
                    elif conteudo == "CyberGhost":
                        vpn_cyberghost()
                    elif conteudo == "PiaVPN":
                        vpn_pia()
                    elif conteudo == "ExpressVPN":
                        vpn_express()
                    elif conteudo == "SurfShark":
                        vpn_surf()
                    elif conteudo == "BetterNet":
                        vpn_better()
                    elif conteudo == "NordVPN":
                        vpn_nord()
                    elif conteudo == "HotspotShield":
                        vpn_hotspotshield()
                    else:
                        window['output'].print(
                            "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                        window.Refresh()
                except:
                    pass
                sms = True
                continue
            try:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]/android.view.View')))
            except:
                continue
            while sms is False:

                try:
                    pular_erro = driver.find_elements(By.XPATH,
                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
                    if len(pular_erro) == 0:
                        try:
                            driver.find_elements(By.XPATH,
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()
                        except:
                            sms = True
                            continue
                    window['output'].print(linha_ret)
                    window.Refresh()
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Criação de outro perfil.')
                    window.Refresh()
                    # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True)
                    # Clicar no botão de perfil
                    try:
                        time.sleep(3)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]')))
                        time.sleep(2)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]'))).click()

                    except:
                        time.sleep(3)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')))
                        time.sleep(2)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]'))).click()

                        # Clicar em perfis
                    try:
                        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                    except:
                        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]/android.view.View'))).click()
                    # Clicar em adicionar conta
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'))).click()
                    # Clicar em criar nova conta
                    time.sleep(10)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]'))).click()
                    # Gerar nome de usuário, digitar no campo e clicar em avançae
                    lista_user = random.choices(range(0, 9), k=2)
                    lista_letras = random.choices(letras, k=1)

                    with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                        nomes = nomes_arquivo.readlines()

                    with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                        sobrenomes = sobrenomes_arquivo.readlines()

                    nomea = fake.first_name_female().replace(" ", "")
                    nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                    sobrenomea = fake.last_name().replace(" ", "").lower()
                    sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                    nome_completo = nome + sobrenome
                    numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                    user_completo = nome_completo + '' + str(numeros_concatenados) + ''.join(lista_letras)

                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: ' + user_completo)
                    window.Refresh()
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                        user_completo)
                    time.sleep(1)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                    # Digitar senha e avançar
                    time.sleep(3)
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                        senha)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
                    # Clicar em concluir cadastro
                    time.sleep(1)
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]/android.view.View')))
                    time.sleep(2)
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]/android.view.View'))).click()
                    time.sleep(4)
                    feedback = driver.find_elements(By.XPATH,
                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.View')
                    if len(feedback) == 1:
                        sms = True

                    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')))
                    time.sleep(20)
                    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()

                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
                    window.Refresh()
                    # WebDriverWait(driver, 40).until(EC.visibility_of_element_located)(((By.XPATH,
                    #                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')))
                    time.sleep(10)
                    verificar = driver.find_elements(By.XPATH,
                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')

                    conta_criada = driver.find_elements(By.XPATH,
                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
                    conta_sms = driver.find_elements(By.XPATH,
                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.View[4]')
                    if len(verificar) == 1:
                        try:
                            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]'))).click()
                        except:
                            pass
                        try:
                            seguido = False
                            conteudo = config['vpn']
                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                                   text_color=('lime'))
                            window.Refresh()
                            contagem += 1
                            window['criadas'].update(contagem)
                            window.Refresh()
                            now = datetime.now()
                            now_brasilia = tz.localize(now)
                            timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                            creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                            client = gspread.authorize(creds)

                            spreadsheet_id = config['spreadsheet']
                            sheet_name = 'contas'
                            # Insert user, password, and timestamp into first empty row
                            sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                            values = sheet.col_values(1)
                            last_row = len(values)
                            values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                      conteudo + ' - ' + app]
                            cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                            for i, val in enumerate(values):
                                cell_list[i].value = val
                            sheet.update_cells(cell_list)

                            rows = sheet.get_all_values()

                            # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                            regex = re.compile(r'\S+\s\S+')

                            # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                            num_rows = sum(1 for row in rows if regex.match(row[0]))
                            window['total'].update(num_rows)

                            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                            creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                            client = gspread.authorize(creds)

                            spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                            sheet_name = 'relatorio_geral'
                            # Insert user, password, and timestamp into first empty row
                            sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                            values = sheet.col_values(1)
                            last_row = len(values)
                            values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                      conteudo + ' - ' + app]
                            cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                            for i, val in enumerate(values):
                                cell_list[i].value = val
                            sheet.update_cells(cell_list)

                            window.Refresh()
                            arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                            # Escreva mais conteúdo no arquivo
                            arquivo.write(user_completo + ' ' + senha + "\n")
                            arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                            # Escreva mais conteúdo no arquivo
                            arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]'))).click()
                            window.Refresh()
                            sms = False
                        except:
                            pass

                    else:
                        try:
                            conteudo = config['vpn']
                            if conteudo == "AVG":
                                vpn_avg()
                            elif conteudo == "SurfShark":
                                vpn_surf()
                            elif conteudo == "Avast":
                                vpn_avast()
                            elif conteudo == "ExpressVPN":
                                vpn_express()
                            elif conteudo == "PiaVPN":
                                vpn_pia()
                            elif conteudo == "BetterNet":
                                vpn_better()
                            elif conteudo == "CyberGhost":
                                vpn_cyberghost()
                            elif conteudo == "NordVPN":
                                vpn_nord()
                            elif conteudo == "HotspotShield":
                                vpn_hotspotshield()
                                break
                            else:
                                window['output'].print(
                                    "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                window.Refresh()

                        except:
                            sms = True
                            try:
                                chrome.quit()
                            except:
                                pass
                except:
                    sms = True
                    try:
                        chrome.quit()
                    except:
                        pass
                    continue


        except Exception as e:
            print(e)
            chrome.quit()
            print('______________________________________________________')
            # desired_caps = {}
            # desired_caps['udid'] = '127.0.0.1:' + porta
            # desired_caps['newCommandTimeout'] = '500'
            # desired_caps['platformName'] = 'Android'
            # desired_caps['automationName'] = 'UiAutomator2'
            # desired_caps['systemPort'] = random.randint(1024, 65535)
            # desired_caps['uiautomator2ServerInstallTimeout'] = 120000
            # desired_caps['noReset'] = True
            # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            continue


def insta_face_litee():
    SPREADSHEET_ID = config['spreadsheet']
    conteudo = config['vpn']
    senha = config['senha']
    maquina = config['maquina']
    tentativa = False
    email = 'InstaFace'
    seguido = False
    app = 'Lite'
    global sms
    global nomes
    global sobrenomes
    global nome
    global contagem
    global sobrenome
    global lista_user
    window['Executar'].update(disabled=True)
    window.Refresh()
    # Código que gera a saída
    import os
    import time
    from datetime import datetime
    import requests
    import hashlib
    import subprocess

    # verifica se o arquivo existe na pasta do bot
    try:
        import uiautomator2 as u2
    except:
        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        subprocess.run(['pip', 'install', 'uiautomator2'])
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instalando dependências...')
        window.Refresh()
        subprocess.run(['deactivate'], shell=True)
        subprocess.run(['pip', 'install', '--upgrade', 'requests'])
        import requests
        time.sleep(10)
        import uiautomator2 as u2
    d = u2.connect(f'127.0.0.1:{porta}')
    import os
    import time
    import requests
    import hashlib
    import subprocess
    from colorama import init, Fore, Back, Style
    from faker import Faker
    # teste

    linha_ret = '_________________________________________________\n'
    window.Refresh()
    import random
    import phonenumbers
    import string
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.common.exceptions import NoSuchElementException
    from mailtm import Email
    import re
    import logging

    logger = logging.getLogger(__name__)

    handler = logging.FileHandler('log.txt')
    handler.setLevel(logging.ERROR)

    logger.addHandler(handler)

    def vpn_avast():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da Avast', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop("com.avast.android.vpn")
            d.app_start("com.avast.android.vpn", ".app.wizard.WizardActivity")
            time.sleep(10)
        except Exception as e:
            print(e)
        abc = False

    def vpn_hotspotshield():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da HotspotShield',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('hotspotshield.android.vpn')
            d.app_start('hotspotshield.android.vpn')
        except Exception as e:
            print(e)
        d(resourceId='hotspotshield.android.vpn:id/tryAgainButton').click()
        time.sleep(5)
        d(resourceId='hotspotshield.android.vpn:id/btnVpnConnect').click()

        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_pia():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da PiaVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.privateinternetaccess.android')
            d.app_start('com.privateinternetaccess.android')
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        d(resourceId='com.privateinternetaccess.android:id/connection_background').click()
        time.sleep(3)
        d(resourceId='com.privateinternetaccess.android:id/connection_background').click()

        abc = False

    def vpn_express():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da ExpressVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.expressvpn.vpn')
            d.app_start('com.expressvpn.vpn')
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        d(resourceId='com.expressvpn.vpn:id/obiButton').click()
        time.sleep(3)
        d(resourceId='com.expressvpn.vpn:id/obiButton').click()

        abc = False

    def vpn_nord():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da NordVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        sms = True
        try:
            d.app_stop('com.nordvpn.android')
            d.app_start('com.nordvpn.android', '.MainActivity')
        except:
            pass
        time.sleep(10)
        time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_surf():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da SurfShark', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            d.app_stop('com.surfshark.vpnclient.android')
            d.app_start('com.surfshark.vpnclient.android')
        except:
            pass
        time.sleep(15)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_better():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da BetterNet', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        try:
            d.app_stop('com.freevpnintouch')
            d.app_start('com.freevpnintouch')
        except:
            pass
        time.sleep(10)
        dialog = d(resourceId='com.freevpnintouch:id/dialogCtaPositive')
        connect = d(resourceId='com.freevpnintouch:id/buttonConnect').text
        if dialog.exists:
            d(resourceId='com.freevpnintouch:id/dialogCtaPositive').click()
            time.sleep(3)
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
            # time.sleep(5)
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
        while connect == 'CONNECT':
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
            time.sleep(4)
            connect = d(resourceId='com.freevpnintouch:id/buttonConnect').text
            # WebDriverWait(driver, 20).until(
            # EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect').click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        ip = '127.0.0.1:' + porta

        output = subprocess.check_output(['adb', '-s', ip, 'shell', 'ifconfig'])

        # Verifica se a conexão VPN está ativa
        if not re.search(b"tun0", output):
            window['output'].print("Não conectado na BetterNet.")
            window.Refresh()
            try:
                connect = d(resourceId='com.freevpnintouch:id/buttonConnect').text
                d.app_stop('com.freevpnintouch')
                d.app_start('com.freevpnintouch')
                while connect == 'CONNECT':
                    d(resourceId='com.freevpnintouch:id/buttonConnect').click()
                    time.sleep(4)
                    connect = d(resourceId='com.freevpnintouch:id/buttonConnect').text
            except:
                pass
        abc = False

    def vpn_cyberghost():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da CyberGhost', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            d.app_stop('de.mobileconcepts.cyberghost')
            d.app_start('de.mobileconcepts.cyberghost')
        except:
            pass
        # time.sleep(3)
        d(resourceId='de.mobileconcepts.cyberghost:id/button').click()
        rate = d(resourceId='de.mobileconcepts.cyberghost:id/rate_me_text')
        if rate.exists:
            d(resourceId='android:id/button2').click()
        time.sleep(2)
        d(resourceId='de.mobileconcepts.cyberghost:id/button').click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        abc = False

    def vpn_avg():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da AVG', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.avg.android.vpn')
            d.app_start('com.avg.android.vpn')
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #               stderr=subprocess.DEVNULL, check=True, shell=True)

        time.sleep(30)

    def vpn_windscribe():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da Windscribe', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)
            d.app_stop("com.windscribe.vpn")
            d.app_start("com.windscribe.vpn")
        except:
            pass
        d(resourceId='com.windscribe.vpn:id/on_off_button').click()
        time.sleep(10)

    def vpn_hma():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da HMA', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)

            d.app_stop("com.hidemyass.hidemyassprovpn")
            time.sleep(3)
            d.app_start('com.hidemyass.hidemyassprovpn', 'com.avast.android.vpn.activity.HmaOnboardingActivity')
        except:
            pass
        time.sleep(10)

    def nenhuma_vpn():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.facebook.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        time.sleep(10)

    def gerar_id():
        chars = string.ascii_lowercase + string.digits
        android_id = ''.join(random.choice(chars) for i in range(16))
        return android_id

    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.page_load_strategy = 'none'
    options.add_experimental_option("prefs", prefs)

    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Senha sendo utilizada: {senha}')
    window.Refresh()

    num = 'InstaFace'
    try:
        comando = f"adb connect 127.0.0.1:{porta}"
    except:
        pass
    try:
        comando = f"adb connect 127.0.0.1:{porta}"
        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global window_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global transition_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global animator_duration_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
    except:
        pass
    gerar_id()
    android_id = gerar_id()
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    time.sleep(2)
    window.Refresh()
    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando sistema inicializar.')
    window.Refresh()
    d.set_fastinput_ime(True)
    d.settings['operation_delay_methods'] = ['click']
    d.settings['operation_delay'] = (0, 1)
    try:

        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Iniciando criação.')
        window.Refresh()
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        client = gspread.authorize(creds)

        spreadsheet_id = config['spreadsheet']
        sheet_name = 'contas'
        # Insert user, password, and timestamp into first empty row
        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
        values = sheet.col_values(1)

        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
        rows = sheet.get_all_values()

        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
        regex = re.compile(r'\S+\s\S+')
        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
        num_rows = sum(1 for row in rows if regex.match(row[0]))
        window['total'].update(num_rows)
    except:
        pass
    first = True
    parar = False
    while parar is False:
        if parar is True:
            print('Parando Thread')
            break
        codigo = 0
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.facebook.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        gerar_id()
        android_id = gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            # subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm grant com.facebook.lite android.permission.READ_CONTACTS', stdout=subprocess.DEVNULL,
            #        stderr=subprocess.DEVNULL, shell=True)
            window['output'].print(linha_ret)
            window.Refresh()
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Abrindo Facebook Lite')
            window.Refresh()

            d.app_start('com.facebook.lite')
            d(resourceId='com.android.packageinstaller:id/permission_deny_button').click()
            time.sleep(4)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[last()]/android.view.View').click()
            time.sleep(1)

            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[23]/android.view.ViewGroup/android.view.View').click()

            time.sleep(2)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]/android.view.View').click()
            time.sleep(5)
            erro2 = d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[2]')
            if erro2.exists:
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[last()]/android.view.View').click()
                time.sleep(1)

                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[23]/android.view.ViewGroup/android.view.View').click()

                time.sleep(2)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]/android.view.View').click()
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[*]/android.view.View').click()

            lista_user = random.choices(range(0, 9), k=2)
            lista_letras = random.choices(letras, k=1)

            with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                nomes = nomes_arquivo.readlines()

            with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                sobrenomes = sobrenomes_arquivo.readlines()

            nomea = fake.first_name_female().replace(" ", "")
            nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
            sobrenomea = fake.last_name().replace(" ", "").lower()
            sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
            nome_completo = nome + ' ' + sobrenome
            nome_completo_s = nome + sobrenome
            numeros_concatenados = ''.join(str(numero) for numero in lista_user)
            user_completo = nome_completo_s + '' + str(numeros_concatenados) + ''.join(lista_letras)
            ######################################################################

            senha = config['senha']
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[1]').set_text(
                nomea)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[2]').set_text(
                sobrenomea)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]/android.view.View').click()
            time.sleep(5)
            negar = d(resourceId='com.android.packageinstaller:id/permission_deny_button')
            while negar.exists:
                negar.click()
                time.sleep(3)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View').click()
            from mailtm import Email
            def listener(message):
                global nome
                global sobrenome
                global cod
                if 'Facebook' in message['subject']:
                    cod = re.search(r'\d+', message['subject']).group(0)

            test = Email()
            while True:
                try:
                    # Código para registrar o email usando a biblioteca mailtm
                    # ...
                    test.register(username=nome_completo_s, password=senha)
                    break  # Saia do loop se o registro for bem-sucedido

                except requests.exceptions.HTTPError as e:
                    nomea = fake.first_name_female().replace(" ", "")
                    nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                    sobrenomea = fake.last_name().replace(" ", "").lower()
                    sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                    nome_completo = nome + ' ' + sobrenome
                    nome_completo_s = nome + sobrenome
                    if e.response.status_code == 422:
                        print("Erro 422: Unprocessable Entity. Tentando novamente...")
                        time.sleep(1)  # Espere um segundo antes de tentar novamente
                        continue  # Volte ao início do loop
                    else:
                        # Outro código de tratamento de erros, se necessário
                        # ...
                        break  # Saia do loop se ocorrer um erro diferente

                except requests.exceptions.RequestException as e:
                    nomea = fake.first_name_female().replace(" ", "")
                    nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                    sobrenomea = fake.last_name().replace(" ", "").lower()
                    sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                    nome_completo = nome + ' ' + sobrenome
                    nome_completo_s = nome + sobrenome
                    # Tratamento de erros de conexão, se necessário
                    # ...
                    break  # Saia do loop se ocorrer um erro de conexão
            window['output'].print(f"[{datetime.now().strftime('%H:%M:%S')}] Email: " + str(test.address))

            window.Refresh()
            email = str(test.address)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').set_text(
                email)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[*]/android.view.View').click()
            time.sleep(1)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup[2]').click()
            time.sleep(1)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup[2]').click()
            time.sleep(1)
            try:
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup[2]').click(
                    timeout=2)
            except:
                pass
            idade_aleatoria = random.randint(18, 35)
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Idade escolhida: {idade_aleatoria}')
            window.Refresh()
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.MultiAutoCompleteTextView').set_text(
                str(idade_aleatoria))
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View').click()
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]').click()
            time.sleep(1)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]/android.view.View[1]').click()
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').set_text(
                senha)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[*]/android.view.View').click()
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[last()]/android.view.View').click()
            time.sleep(30)
            block = d(text='Wir benötigen noch weitere Informationen')
            if block.exists:
                try:
                    conteudo = config['vpn']

                    # Executa a função correspondente ao conteúdo do arquivo
                    if conteudo == "AVG":
                        vpn_avg()
                    elif conteudo == "Nenhuma":
                        nenhuma_vpn()
                    elif conteudo == "Avast":
                        vpn_avast()
                    elif conteudo == "CyberGhost":
                        vpn_cyberghost()
                    elif conteudo == "PiaVPN":
                        vpn_pia()
                    elif conteudo == "ExpressVPN":
                        vpn_express()
                    elif conteudo == "WindscribeVPN":
                        vpn_windscribe()
                    elif conteudo == "SurfShark":
                        vpn_surf()
                    elif conteudo == "HmaVPN":
                        vpn_hma()
                    elif conteudo == "BetterNet":
                        vpn_better()
                    elif conteudo == "NordVPN":
                        vpn_nord()
                    elif conteudo == "HotspotShield":
                        vpn_hotspotshield()
                    else:
                        window['output'].print(
                            "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                        window.Refresh()
                    raise Exception("SMS.")
                except:
                    sms = True
                    raise Exception("SMS.")
                    continue
            print('passou')
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()
            time.sleep(3)
            negar = d(resourceId='com.android.packageinstaller:id/permission_deny_button')
            while negar.exists:
                negar.click()
                time.sleep(1)
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando codigo...')
            window.Refresh()
            # fetch all emails in the inbox
            codigo = 0
            try:
                test.start(listener, interval=15)
                codigo = 0
                while codigo != 20:
                    time.sleep(2)
                    codigo = codigo + 1
                codigo = cod
            except Exception as e:
                if "Too Many Requests" in str(e):
                    pass
                else:
                    pass
            if codigo == '20':
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Codigo não recebido')
                window.Refresh()
                raise Exception('Codigo não recebido.')
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Codigo recebido: {codigo}')
            window.Refresh()
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').set_text(
                codigo)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]/android.view.View').click()
            time.sleep(10)

            criou = d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[4]')
            if criou.exists:
                criou.click()
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Facebook criado com sucesso.',
                                       text_color=('cyan'))
                window.Refresh()
            else:
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Facebook criado com sucesso.',
                                       text_color=('cyan'))
                window.Refresh()

            try:
                subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, check=True, shell=True)
            except:
                pass

            with open("contas_fbcriadas.txt", "a") as arquivo:
                arquivo.write(email + ' ' + senha + "\n")
            # Escreva mais conteúdo no arquivo

            d.app_start('com.instagram.lite')
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View').click()
            time.sleep(5)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View').click()

            time.sleep(3)
            try:
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View').click(
                    timeout=3)
            except:
                pass
            try:
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[6]/android.view.View').click(
                    timeout=10)
            except:
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]/android.view.View').click()
                time.sleep(3)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[6]/android.view.View').click()

            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: {user_completo}')
            window.Refresh()
            time.sleep(3)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').set_text(
                '')
            campo_de_user = d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView')
            campo_de_user.set_text(user_completo)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View').click()
            time.sleep(20)
            if campo_de_user.exists:
                d.app_stop('com.instagram.lite')
                time.sleep(1)
                d.app_start('com.instagram.lite')
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]/android.view.View').click()
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[1]').set_text(
                    user_completo)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[2]').set_text(
                    senha)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.View').click()

            # time.sleep(200)
            d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()

            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
            window.Refresh()
            time.sleep(5)
            verificar = d.xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')
            # time.sleep(10)

            # conta_criada = driver.find_elements(By.XPATH,
            #                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
            # conta_sms = driver.find_elements(By.XPATH,
            #                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.View[4]')
            #
            try:
                if verificar.exists:

                    try:
                        seguido = False
                        conteudo = config['vpn']
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                               text_color=('lime'))
                        window.Refresh()
                        contagem += 1
                        window['criadas'].update(contagem)
                        window.Refresh()
                        now = datetime.now()
                        now_brasilia = tz.localize(now)
                        timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                        client = gspread.authorize(creds)

                        spreadsheet_id = config['spreadsheet']
                        sheet_name = 'contas'
                        # Insert user, password, and timestamp into first empty row
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                        values = sheet.col_values(1)
                        last_row = len(values)
                        values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                  conteudo + ' - ' + app]
                        cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                        for i, val in enumerate(values):
                            cell_list[i].value = val
                        sheet.update_cells(cell_list)

                        rows = sheet.get_all_values()

                        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                        regex = re.compile(r'\S+\s\S+')

                        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                        num_rows = sum(1 for row in rows if regex.match(row[0]))
                        window['total'].update(num_rows)

                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                        creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                        client = gspread.authorize(creds)

                        spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                        sheet_name = 'relatorio_geral'
                        # Insert user, password, and timestamp into first empty row
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                        values = sheet.col_values(1)
                        last_row = len(values)
                        values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                  conteudo + ' - ' + app]
                        cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                        for i, val in enumerate(values):
                            cell_list[i].value = val
                        sheet.update_cells(cell_list)

                        window.Refresh()
                        arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                        # Escreva mais conteúdo no arquivo
                        arquivo.write(user_completo + ' ' + senha + "\n")
                        arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                        # Escreva mais conteúdo no arquivo
                        arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                        d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]').click()
                        window.Refresh()
                        sms = False
                    except Exception as e:
                        print(e)
                        pass
                else:

                    try:
                        conteudo = config['vpn']

                        # Executa a função correspondente ao conteúdo do arquivo
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "Nenhuma":
                            nenhuma_vpn()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()
                    except:
                        sms = True
                        continue
            except Exception as e:
                print(e)
                try:
                    if conteudo == "AVG":
                        vpn_avg()
                    elif conteudo == "Avast":
                        vpn_avast()
                    elif conteudo == "Nenhuma":
                        nenhuma_vpn()
                    elif conteudo == "CyberGhost":
                        vpn_cyberghost()
                    elif conteudo == "PiaVPN":
                        vpn_pia()
                    elif conteudo == "ExpressVPN":
                        vpn_express()
                    elif conteudo == "SurfShark":
                        vpn_surf()
                    elif conteudo == "BetterNet":
                        vpn_better()
                    elif conteudo == "NordVPN":
                        vpn_nord()
                    elif conteudo == "HotspotShield":
                        vpn_hotspotshield()
                    else:
                        window['output'].print(
                            "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                        window.Refresh()
                except:
                    pass
                sms = True
                continue
            try:
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]/android.view.View')
            except:
                continue
            while sms is False:

                try:
                    pular_erro = d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
                    if not pular_erro.exists:
                        try:
                            d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()
                        except:
                            sms = True
                            continue
                    window['output'].print(linha_ret)
                    window.Refresh()
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Criação de outro perfil.')
                    window.Refresh()
                    # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True)
                    # Clicar no botão de perfil
                    try:
                        time.sleep(3)
                        d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]')
                        time.sleep(2)
                        d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]').click()

                    except:
                        time.sleep(3)
                        d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')
                        time.sleep(2)
                        d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]').click()

                        # Clicar em perfis
                    try:
                        d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()
                    except:
                        d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]/android.view.View').click()
                    # Clicar em adicionar conta
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]').click()
                    # Clicar em criar nova conta
                    time.sleep(10)
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]').click()
                    # Gerar nome de usuário, digitar no campo e clicar em avançae
                    lista_user = random.choices(range(0, 9), k=2)
                    lista_letras = random.choices(letras, k=1)

                    with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                        nomes = nomes_arquivo.readlines()

                    with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                        sobrenomes = sobrenomes_arquivo.readlines()

                    nomea = fake.first_name_female().replace(" ", "")
                    nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                    sobrenomea = fake.last_name().replace(" ", "").lower()
                    sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                    nome_completo = nome + sobrenome
                    numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                    user_completo = nome_completo + '' + str(numeros_concatenados) + ''.join(lista_letras)

                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: ' + user_completo)
                    window.Refresh()
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').set_text(
                        user_completo)
                    time.sleep(1)
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()
                    # Digitar senha e avançar
                    time.sleep(3)
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').set_text(
                        senha)
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]').click()
                    # Clicar em concluir cadastro
                    time.sleep(1)
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]/android.view.View')
                    time.sleep(2)
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]/android.view.View').click()
                    time.sleep(4)
                    feedback = d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.View')
                    if feedback.exists:
                        sms = True

                    time.sleep(20)
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()

                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
                    window.Refresh()
                    # WebDriverWait(driver, 40).until(EC.visibility_of_element_located)(((By.XPATH,
                    #                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')))
                    time.sleep(10)
                    verificar = d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')

                    # conta_criada = driver.find_elements(By.XPATH,
                    #                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
                    # conta_sms = driver.find_elements(By.XPATH,
                    #                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.View[4]')
                    if verificar.exists:
                        try:
                            d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]').click(
                                timeout=5)
                        except:
                            pass
                        try:
                            seguido = False
                            conteudo = config['vpn']
                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                                   text_color=('lime'))
                            window.Refresh()
                            contagem += 1
                            window['criadas'].update(contagem)
                            window.Refresh()
                            now = datetime.now()
                            now_brasilia = tz.localize(now)
                            timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                            creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                            client = gspread.authorize(creds)

                            spreadsheet_id = config['spreadsheet']
                            sheet_name = 'contas'
                            # Insert user, password, and timestamp into first empty row
                            sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                            values = sheet.col_values(1)
                            last_row = len(values)
                            values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                      conteudo + ' - ' + app]
                            cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                            for i, val in enumerate(values):
                                cell_list[i].value = val
                            sheet.update_cells(cell_list)

                            rows = sheet.get_all_values()

                            # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                            regex = re.compile(r'\S+\s\S+')

                            # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                            num_rows = sum(1 for row in rows if regex.match(row[0]))
                            window['total'].update(num_rows)

                            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                            creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                            client = gspread.authorize(creds)

                            spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                            sheet_name = 'relatorio_geral'
                            # Insert user, password, and timestamp into first empty row
                            sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                            values = sheet.col_values(1)
                            last_row = len(values)
                            values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                      conteudo + ' - ' + app]
                            cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                            for i, val in enumerate(values):
                                cell_list[i].value = val
                            sheet.update_cells(cell_list)

                            window.Refresh()
                            arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                            # Escreva mais conteúdo no arquivo
                            arquivo.write(user_completo + ' ' + senha + "\n")
                            arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                            # Escreva mais conteúdo no arquivo
                            arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                            d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]').click()
                            window.Refresh()
                            sms = False
                        except:
                            pass

                    else:
                        try:
                            conteudo = config['vpn']
                            if conteudo == "AVG":
                                vpn_avg()
                            elif conteudo == "SurfShark":
                                vpn_surf()
                            elif conteudo == "Avast":
                                vpn_avast()
                            elif conteudo == "ExpressVPN":
                                vpn_express()
                            elif conteudo == "Nenhuma":
                                nenhuma_vpn()
                            elif conteudo == "PiaVPN":
                                vpn_pia()
                            elif conteudo == "BetterNet":
                                vpn_better()
                            elif conteudo == "CyberGhost":
                                vpn_cyberghost()
                            elif conteudo == "NordVPN":
                                vpn_nord()
                            elif conteudo == "HotspotShield":
                                vpn_hotspotshield()
                                break
                            else:
                                window['output'].print(
                                    "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                window.Refresh()

                        except:
                            sms = True
                except:
                    sms = True
                    continue


        except Exception as e:
            print(e)
            time.sleep(20)
            print('______________________________________________________')
            # desired_caps = {}
            # desired_caps['udid'] = '127.0.0.1:' + porta
            # desired_caps['newCommandTimeout'] = '500'
            # desired_caps['platformName'] = 'Android'
            # desired_caps['automationName'] = 'UiAutomator2'
            # desired_caps['systemPort'] = random.randint(1024, 65535)
            # desired_caps['uiautomator2ServerInstallTimeout'] = 120000
            # desired_caps['noReset'] = True
            # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            continue


def criarporcima():
    global sms
    global nomes
    global sobrenomes
    global nome
    global contagem
    global sobrenome
    global lista_user
    try:
        with open("configuracoes/config2.json", "r") as f:
            config2 = json.load(f)
    except FileNotFoundError:
        config2 = {}
    SPREADSHEET_ID = config2['spreadsheet']
    conteudo = config2['vpn']
    senha = config2['senha']
    maquina = config2['maquina']
    sheet_contas = config2['contas_por_cima']
    tentativa = False
    seguido = False
    window['Executar'].update(disabled=True)
    window.Refresh()
    # Código que gera a saída
    import os
    import time
    import requests
    import hashlib
    import subprocess

    # verifica se o arquivo existe na pasta do bot

    try:
        from rich.console import Console
    except ModuleNotFoundError:
        import subprocess
        import sys

        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instalando dependências...')
        window.Refresh()
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
        subprocess.run(['deactivate'], shell=True)
        from rich.console import Console
    import os
    import time
    import requests
    import hashlib
    import subprocess
    from colorama import init, Fore, Back, Style
    from faker import Faker
    # teste
    init(autoreset=True)
    console = Console()
    from termcolor import colored

    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.rule import Rule

    linha_ret = '_________________________________________________\n'
    window.Refresh()
    import random
    from datetime import datetime
    import string
    from appium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.common.exceptions import NoSuchElementException
    from mailtm import Email
    import re
    import logging

    logger = logging.getLogger(__name__)

    handler = logging.FileHandler('log.txt')
    handler.setLevel(logging.ERROR)

    logger.addHandler(handler)

    def gerar_id():
        chars = string.ascii_lowercase + string.digits
        android_id = ''.join(random.choice(chars) for i in range(16))
        return android_id

    def vpn_avast():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da Avast', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            driver.start_activity("com.avast.android.vpn", ".app.wizard.WizardActivity")
            time.sleep(10)
        except Exception as e:
            print(e)
        abc = False

    def vpn_hotspotshield():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da HotspotShield',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            driver.start_activity("hotspotshield.android.vpn", "com.anchorfree.hotspotshield.ui.HssActivity")
        except Exception as e:
            print(e)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'hotspotshield.android.vpn:id/tryAgainButton'))).click()
        time.sleep(5)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'hotspotshield.android.vpn:id/btnVpnConnect'))).click()

        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_pia():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da PiaVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            driver.start_activity("com.privateinternetaccess.android", ".ui.LauncherActivity")
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'com.privateinternetaccess.android:id/connection_background'))).click()
        time.sleep(3)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'com.privateinternetaccess.android:id/connection_background'))).click()

        abc = False

    def vpn_express():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da ExpressVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            driver.start_activity("com.expressvpn.vpn", ".ui.SplashActivity")
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'com.expressvpn.vpn:id/obiButton'))).click()
        time.sleep(3)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'com.expressvpn.vpn:id/obiButton'))).click()

        abc = False

    def vpn_nord():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da NordVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        sms = True
        try:
            driver.start_activity("com.nordvpn.android", ".MainActivity")
        except:
            pass
        time.sleep(10)
        # try:
        #    WebDriverWait(driver, 10).until(
        #        EC.element_to_be_clickable((By.ID, 'com.nordvpn.android:id/reconnect_button'))).click()
        # except:
        #    pass
        # try:
        #    WebDriverWait(driver, 10).until(
        #        EC.element_to_be_clickable((By.ID, 'com.nordvpn.android:id/secondary_quick_connect_button'))).click()
        # except:
        #    pass
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'com.nordvpn.android:id/primary_quick_connect_button'))).click()
        time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_surf():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da SurfShark', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            driver.start_activity("com.surfshark.vpnclient.android", ".StartActivity")
        except:
            pass
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        time.sleep(5)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_better():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da BetterNet', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        try:
            driver.start_activity("com.freevpnintouch", "com.anchorfree.betternet.ui.BetternetActivity")
        except:
            pass
        time.sleep(10)
        dialog = driver.find_elements(By.ID, 'com.freevpnintouch:id/dialogCtaPositive')
        connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
        if len(dialog) == 1:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/dialogCtaPositive'))).click()
            time.sleep(3)
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
            # time.sleep(5)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
        while connect == 'CONNECT':
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
            time.sleep(4)
            connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
            # WebDriverWait(driver, 20).until(
            # EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        ip = '127.0.0.1:' + porta

        output = subprocess.check_output(['adb', '-s', ip, 'shell', 'ifconfig'])

        # Verifica se a conexão VPN está ativa
        if not re.search(b"tun0", output):
            window['output'].print("Não conectado na BetterNet.")
            window.Refresh()
            try:
                connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
                driver.start_activity("com.freevpnintouch", "com.anchorfree.betternet.ui.BetternetActivity")
                while connect == 'CONNECT':
                    WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
                    time.sleep(4)
                    connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
            except:
                pass
        abc = False

    def vpn_cyberghost():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da CyberGhost', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            driver.start_activity("de.mobileconcepts.cyberghost", ".view.app.AppActivity filter")
        except:
            pass
        # time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'de.mobileconcepts.cyberghost:id/button'))).click()
        rate = driver.find_elements(By.ID, 'de.mobileconcepts.cyberghost:id/rate_me_text')
        if len(rate) == 1:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'android:id/button2'))).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'de.mobileconcepts.cyberghost:id/button'))).click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        abc = False

    def vpn_avg():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da AVG', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            driver.start_activity("com.avg.android.vpn", "com.avast.android.vpn.app.wizard.WizardActivity")
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #               stderr=subprocess.DEVNULL, check=True, shell=True)

        # time.sleep(10)
        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        # time.sleep(10)
        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()

    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.page_load_strategy = 'none'
    options.add_experimental_option("prefs", prefs)

    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Senha sendo utilizada: {senha}')
    window.Refresh()

    console = Console()

    device = [
        {'name': 'Bluestacks1', 'port': porta, 'udid': f'127.0.0.1:{porta}'},
    ]
    try:
        comando = f"adb connect 127.0.0.1:{porta}"
        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server.test', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
    except:
        pass
    try:
        comando = f"adb connect 127.0.0.1:{porta}"
        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global window_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global transition_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global animator_duration_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
    except:
        pass
    gerar_id()
    android_id = gerar_id()
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    time.sleep(2)
    # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True, stdout=subprocess.DEVNULL,
    #               stderr=subprocess.DEVNULL)
    try:
        subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server.test',
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
    except:
        pass

    try:
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
    except Exception as e:
        print(e)
        pass

    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Efetuando troca de IP.')
    window.Refresh()
    try:
        conteudo = config2['vpn']
        if conteudo == "AVG":
            vpn_avg()
        elif conteudo == "SurfShark":
            vpn_surf()
        elif conteudo == "Nenhuma":
            nenhuma_vpn()
        elif conteudo == "Avast":
            vpn_avast()
        elif conteudo == "ExpressVPN":
            vpn_express()
        elif conteudo == "PiaVPN":
            vpn_pia()
        elif conteudo == "BetterNet":
            vpn_better()
        elif conteudo == "CyberGhost":
            vpn_cyberghost()
        elif conteudo == "NordVPN":
            vpn_nord()
        elif conteudo == "HotspotShield":
            vpn_hotspotshield()
        elif conteudo == "WindscribeVPN":
            vpn_windscribe()
        elif conteudo == "HmaVPN":
            vpn_hma()
        else:
            window['output'].print(
                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
            window.Refresh()

    except Exception as e:
        pass

    window.Refresh()
    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando sistema inicializar.')
    window.Refresh()
    desired_caps = {}
    desired_caps['udid'] = '127.0.0.1:' + porta
    desired_caps['newCommandTimeout'] = '500'
    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['systemPort'] = random.randint(1024, 65535)
    desired_caps['uiautomator2ServerInstallTimeout'] = 120000
    desired_caps['noReset'] = True
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Planilha sendo utilizada: {sheet_contas}.\n')
    window.Refresh()
    while True:
        try:
            window['output'].print(linha_ret)
            window.Refresh()

            time.sleep(5)
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
            client = gspread.authorize(creds)

            spreadsheet_id = config['spreadsheet']
            sheet_name = 'contas'
            # Insert user, password, and timestamp into first empty row
            sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
            values = sheet.col_values(1)

            # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
            rows = sheet.get_all_values()

            # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
            regex = re.compile(r'\S+\s\S+')
            # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
            num_rows = sum(1 for row in rows if regex.match(row[0]))
            window['total'].update(num_rows)
            try:
                subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, check=True, shell=True)


            except:
                pass
            try:
                subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, check=True, shell=True)
            except Exception as e:
                print(e)
                pass
            # Insert user, password, and timestamp into first empty row
            sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_contas)
            values = sheet.col_values(1)

            # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
            rows = sheet.get_all_values()

            # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
            regex = re.compile(r'\S+\s\S+')
            # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
            num_rows2 = sum(1 for row in rows if regex.match(row[0]))
            while int(num_rows2) == 0:
                window['output'].print(
                    f'[{datetime.now().strftime("%H:%M:%S")}] Nenhuma conta encontrada. Tentando novamente em 5 min.')
                window.Refresh()
                cope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                client = gspread.authorize(creds)

                spreadsheet_id = config['spreadsheet']
                # Insert user, password, and timestamp into first empty row
                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_contas)
                values = sheet.col_values(1)

                # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                rows = sheet.get_all_values()

                # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                regex = re.compile(r'\S+\s\S+')
                # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                num_rows = sum(1 for row in rows if regex.match(row[0]))
                window['total'].update(num_rows)

                cells = sheet.get_all_values()

                # Armazena as células que correspondem à condição
                matches = [cell for row in cells for cell in row if re.match(r'\S+\s\S+', cell)]

                # Armazena a lista de células correspondentes à condição em uma variável
                num_rows2 = matches
                time.sleep(300)
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] {num_rows2} contas para serem utilizadas.')
            window.Refresh()
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Abrindo Instagram Lite')
            window.Refresh()

            sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_contas)
            values = sheet.col_values(1)
            first_linha = sheet.cell(1, 1).value

            # Divide a string em duas partes separadas por um espaço em branco
            partes = first_linha.split(' ')

            # Atribui a primeira parte (endereço de e-mail) à variável email2nr
            user = partes[0]

            # Atribui a segunda parte (texto) à variável senha2nr
            senha = partes[1]
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta sendo utilizada: {user}')
            window.Refresh()
            driver.activate_app('com.instagram.lite')
            time.sleep(4)
            try:
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
            except:
                desired_caps = {}
                desired_caps['udid'] = '127.0.0.1:' + porta
                desired_caps['newCommandTimeout'] = '500'
                desired_caps['platformName'] = 'Android'
                desired_caps['automationName'] = 'UiAutomator2'
                desired_caps['systemPort'] = random.randint(1024, 65535)
                desired_caps['uiautomator2ServerInstallTimeout'] = 120000
                desired_caps['noReset'] = True
                driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()

            time.sleep(2)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[1]'))).send_keys(
                user)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[2]'))).send_keys(
                senha)
            time.sleep(2)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]/android.view.ViewGroup'))).click()
            time.sleep(5)
            lembrar_login = driver.find_elements(By.XPATH,
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]')
            if len(lembrar_login) == 1:
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'))).click()
            time.sleep(10)
            verificar = driver.find_elements(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')
            # time.sleep(10)

            conta_criada = driver.find_elements(By.XPATH,
                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
            conta_sms = driver.find_elements(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.View[4]')

            try:
                if len(verificar) == 1:
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Logado com sucesso.')
                    window.Refresh()
                    sms = False
            except:
                pass
            while sms is False:
                try:
                    pular_erro = driver.find_elements(By.XPATH,
                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
                    if len(pular_erro) == 0:
                        try:
                            driver.find_elements(By.XPATH,
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()
                        except:
                            sms = True
                            continue
                    window['output'].print(linha_ret)
                    window.Refresh()
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Criação de outro perfil.')
                    window.Refresh()
                    # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True)
                    # Clicar no botão de perfil
                    try:
                        time.sleep(3)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]')))
                        time.sleep(2)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]'))).click()

                    except:
                        time.sleep(3)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')))
                        time.sleep(2)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]'))).click()

                        # Clicar em perfis
                    try:
                        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                    except:
                        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]/android.view.View'))).click()
                    # Clicar em adicionar conta
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'))).click()
                    # Clicar em criar nova conta
                    time.sleep(3)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]'))).click()
                    # Gerar nome de usuário, digitar no campo e clicar em avançae
                    lista_user = random.choices(range(0, 9), k=2)
                    lista_letras = random.choices(letras, k=1)

                    with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                        nomes = nomes_arquivo.readlines()

                    with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                        sobrenomes = sobrenomes_arquivo.readlines()

                    nomea = fake.first_name_female().replace(" ", "")
                    nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                    sobrenomea = fake.last_name_female().replace(" ", "")
                    sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                    nome_completo = nome + sobrenome
                    numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                    user_completo = nome_completo + '' + str(numeros_concatenados) + ''.join(lista_letras)

                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: ' + user_completo)
                    window.Refresh()
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                        user_completo)
                    time.sleep(1)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                    # Digitar senha e avançar
                    time.sleep(3)
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                        senha)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
                    # Clicar em concluir cadastro
                    time.sleep(1)
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]/android.view.View')))
                    time.sleep(2)
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]/android.view.View'))).click()
                    time.sleep(4)
                    feedback = driver.find_elements(By.XPATH,
                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.View')
                    if len(feedback) == 1:
                        sms = True

                    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')))
                    time.sleep(20)
                    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()

                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
                    window.Refresh()
                    # WebDriverWait(driver, 40).until(EC.visibility_of_element_located)(((By.XPATH,
                    #                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')))
                    time.sleep(10)
                    verificar = driver.find_elements(By.XPATH,
                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')

                    conta_criada = driver.find_elements(By.XPATH,
                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
                    conta_sms = driver.find_elements(By.XPATH,
                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.View[4]')
                    if len(verificar) == 1:
                        try:
                            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]'))).click()
                        except:
                            pass
                        seguido = False
                        conteudo = config['vpn']
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                               text_color=('lime'))
                        window.Refresh()
                        contagem += 1
                        window['criadas'].update(contagem)
                        window.Refresh()
                        now = datetime.now()
                        now_brasilia = tz.localize(now)
                        timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                        client = gspread.authorize(creds)

                        spreadsheet_id = config2['spreadsheet']
                        sheet_name = 'contas'
                        # Insert user, password, and timestamp into first empty row
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                        values = sheet.col_values(1)
                        last_row = len(values)
                        email = 'POR CIMA'
                        values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                        cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                        for i, val in enumerate(values):
                            cell_list[i].value = val
                        sheet.update_cells(cell_list)

                        rows = sheet.get_all_values()

                        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                        regex = re.compile(r'\S+\s\S+')

                        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                        num_rows = sum(1 for row in rows if regex.match(row[0]))
                        window['total'].update(num_rows)

                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                        creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                        client = gspread.authorize(creds)

                        spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                        sheet_name = 'relatorio_geral'
                        # Insert user, password, and timestamp into first empty row
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                        values = sheet.col_values(1)
                        last_row = len(values)
                        values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                        cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                        for i, val in enumerate(values):
                            cell_list[i].value = val
                        sheet.update_cells(cell_list)

                        window.Refresh()
                        arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                        # Escreva mais conteúdo no arquivo
                        arquivo.write(user_completo + ' ' + senha + "\n")
                        arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                        # Escreva mais conteúdo no arquivo
                        arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]'))).click()
                        window.Refresh()
                        sms = False

                    else:
                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                        client = gspread.authorize(creds)
                        # Abre a planilha e a planilha de uma determinada aba
                        spreadsheet_id = config2['spreadsheet']
                        sheet_contas = config2['contas_por_cima']
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_contas)

                        # Apaga a primeira célula da coluna A e desloca as células abaixo
                        sheet.delete_rows(1, 1)
                        try:
                            conteudo = config2['vpn']
                            if conteudo == "AVG":
                                vpn_avg()
                            elif conteudo == "SurfShark":
                                vpn_surf()
                            elif conteudo == "Nenhuma":
                                nenhuma_vpn()
                            elif conteudo == "Avast":
                                vpn_avast()
                            elif conteudo == "ExpressVPN":
                                vpn_express()
                            elif conteudo == "PiaVPN":
                                vpn_pia()
                            elif conteudo == "BetterNet":
                                vpn_better()
                            elif conteudo == "CyberGhost":
                                vpn_cyberghost()
                            elif conteudo == "NordVPN":
                                vpn_nord()
                            elif conteudo == "HotspotShield":
                                vpn_hotspotshield()
                            elif conteudo == "WindscribeVPN":
                                vpn_windscribe()
                            elif conteudo == "HmaVPN":
                                vpn_hma()
                            else:
                                window['output'].print(
                                    "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                window.Refresh()
                        except:
                            pass
                except Exception as e:
                    print(e)
                    pass
        except Exception as e:
            print(e)
            pass


def executar_mailtm():
    SPREADSHEET_ID = config['spreadsheet']
    conteudo = config['vpn']
    senha = config['senha']
    maquina = config['maquina']
    global sms
    global nomes
    global sobrenomes
    global nome
    global contagem
    global sobrenome
    global lista_user
    window['Executar'].update(disabled=True)
    window.Refresh()
    # Código que gera a saída
    import os
    import time
    import requests
    import hashlib
    import subprocess

    # verifica se o arquivo existe na pasta do bot

    try:
        from rich.console import Console
    except ModuleNotFoundError:
        import subprocess
        import sys

        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instalando dependências...')
        window.Refresh()
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
        subprocess.run(['deactivate'], shell=True)
        from rich.console import Console
    import os
    import time
    import requests
    import hashlib
    import subprocess
    from colorama import init, Fore, Back, Style
    from faker import Faker
    # teste
    init(autoreset=True)
    console = Console()
    from termcolor import colored

    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.rule import Rule

    linha_ret = '_________________________________________________\n'
    window.Refresh()
    import random
    from datetime import datetime
    import string
    from appium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.common.exceptions import NoSuchElementException
    from mailtm import Email
    import re
    import logging

    logger = logging.getLogger(__name__)

    handler = logging.FileHandler('log.txt')
    handler.setLevel(logging.ERROR)

    logger.addHandler(handler)

    # RANGE_NAME = 'contas!A:D'
    #
    # SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    def vpn_avast():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] SMS\nAlterando IP da Avast', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        sms = True
        try:
            driver.start_activity("com.avast.android.vpn", ".app.wizard.WizardActivity")
            time.sleep(10)
        except Exception as e:
            print(e)

        abc = False

    def vpn_hotspotshield():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] SMS\nAlterando IP da HotspotShield',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        sms = True
        try:
            driver.start_activity("hotspotshield.android.vpn", "com.anchorfree.hotspotshield.ui.HssActivity")
        except Exception as e:
            print(e)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'hotspotshield.android.vpn:id/tryAgainButton'))).click()
        time.sleep(5)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'hotspotshield.android.vpn:id/btnVpnConnect'))).click()

        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_pia():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] SMS\nAlterando IP da PiaVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        sms = True
        try:
            driver.start_activity("com.privateinternetaccess.android", ".ui.LauncherActivity")
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'com.privateinternetaccess.android:id/connection_background'))).click()
        time.sleep(3)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'com.privateinternetaccess.android:id/connection_background'))).click()

        abc = False

    def vpn_express():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] SMS\nAlterando IP da ExpressVPN',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        sms = True
        try:
            driver.start_activity("com.expressvpn.vpn", ".ui.SplashActivity")
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'com.expressvpn.vpn:id/obiButton'))).click()
        time.sleep(3)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'com.expressvpn.vpn:id/obiButton'))).click()

        abc = False

    def vpn_nord():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] SMS\nAlterando IP da NordVPN',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        sms = True
        try:
            driver.start_activity("com.nordvpn.android", ".MainActivity")
        except:
            pass
        time.sleep(10)
        # try:
        #    WebDriverWait(driver, 10).until(
        #        EC.element_to_be_clickable((By.ID, 'com.nordvpn.android:id/reconnect_button'))).click()
        # except:
        #    pass
        # try:
        #    WebDriverWait(driver, 10).until(
        #        EC.element_to_be_clickable((By.ID, 'com.nordvpn.android:id/secondary_quick_connect_button'))).click()
        # except:
        #    pass
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'com.nordvpn.android:id/primary_quick_connect_button'))).click()
        time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_surf():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da SurfShark', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            driver.start_activity("com.surfshark.vpnclient.android", ".StartActivity")
        except:
            pass
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        time.sleep(5)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_better():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] SMS\nAlterando IP da BetterNet',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        try:
            driver.start_activity("com.freevpnintouch", "com.anchorfree.betternet.ui.BetternetActivity")
        except:
            pass
        time.sleep(10)
        dialog = driver.find_elements(By.ID, 'com.freevpnintouch:id/dialogCtaPositive')
        connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
        if len(dialog) == 1:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/dialogCtaPositive'))).click()
            time.sleep(3)
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
            # time.sleep(5)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
        while connect == 'CONNECT':
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
            time.sleep(4)
            connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
            # WebDriverWait(driver, 20).until(
            # EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        ip = '127.0.0.1:' + porta

        output = subprocess.check_output(['adb', '-s', ip, 'shell', 'ifconfig'])

        # Verifica se a conexão VPN está ativa
        if not re.search(b"tun0", output):
            window['output'].print("Não conectado na BetterNet.")
            window.Refresh()
            try:
                connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
                driver.start_activity("com.freevpnintouch", "com.anchorfree.betternet.ui.BetternetActivity")
                while connect == 'CONNECT':
                    WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
                    time.sleep(4)
                    connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
            except:
                pass
        abc = False

    def vpn_cyberghost():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] SMS\nAlterando IP da CyberGhost',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        try:
            driver.start_activity("de.mobileconcepts.cyberghost", ".view.app.AppActivity filter")
        except:
            pass
        # time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'de.mobileconcepts.cyberghost:id/button'))).click()
        rate = driver.find_elements(By.ID, 'de.mobileconcepts.cyberghost:id/rate_me_text')
        if len(rate) == 1:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'android:id/button2'))).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'de.mobileconcepts.cyberghost:id/button'))).click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        abc = False

    def vpn_avg():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] SMS\nAlterando IP da AVG', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        sms = True
        try:
            driver.start_activity("com.avg.android.vpn", "com.avast.android.vpn.app.wizard.WizardActivity")
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        # time.sleep(10)
        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        # time.sleep(10)
        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        # time.sleep(5)
        # WebDriverWait(driver, 30).until(
        #    EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        # time.sleep(5)

        abc = False

    def listener(message):
        global nome
        global sobrenome
        global cod
        if 'code' in message['subject']:
            cod = re.search(r'\d+', message['subject']).group(0)

    def gerar_email():
        global lista_user
        global sms
        global nome
        global sobrenome
        global email
        lista_user = random.choices(range(0, 9), k=2)
        lista_letras = random.choices(letras, k=1)

        with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
            nomes = nomes_arquivo.readlines()

        with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
            sobrenomes = sobrenomes_arquivo.readlines()

        nomea = fake.first_name_female().replace(" ", "")
        nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
        sobrenomea = fake.last_name().replace(" ", "").lower()
        sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
        nome_completo = nome + ' ' + sobrenome
        nome_completo_s = nome + sobrenome
        numeros_concatenados = ''.join(str(numero) for numero in lista_user)
        user_completo = nome_completo_s + '' + str(numeros_concatenados) + ''.join(lista_letras)
        test = Email()

        time.sleep(2)
        num = driver.find_elements(By.XPATH,
                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]/android.view.View')

        while len(num) == 1:
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
            time.sleep(2)
            num = driver.find_elements(By.XPATH,
                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]/android.view.View')
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
            try:
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
                time.sleep(5)
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                time.sleep(3)
            except Exception as e:
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro.')
                window.Refresh()

        test.register(username=user_completo, password=senha)
        window['output'].print("Email: " + str(test.address))

        window.Refresh()
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
            email)
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()
        # driver.find_element(By.XPATH,
        #                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]').click()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando codigo...')
        window.Refresh()
        # fetch all emails in the inbox
        codigo = None
        try:
            test.start(listener, interval=15)
            codigo = 0
            while codigo != 20:
                time.sleep(2)
                codigo = codigo + 1
            codigo = cod
        except Exception as e:
            if "Too Many Requests" in str(e):
                pass
            else:
                pass
        window['output'].print(f"Codigo recebido: {codigo}")
        window.Refresh()
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                codigo)
        except:
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instagram fechou')
            window.Refresh()
        time.sleep(2)
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()
        except:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View')))
        except:
            pass
        ##time.sleep(3)
        # codigo_invalido = driver.find_elements(By.XPATH,
        #                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[5]')
        # continua_na_tela = driver.find_elements(By.XPATH,
        #                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]/android.view.View')
        # continua_na_tela2 = driver.find_elements(By.XPATH,
        #                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]/android.view.View')
        # criou = driver.find_elements(By.XPATH,
        #                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View')
        # time.sleep(25)
        # if len(codigo_invalido) == 1:
        # driver.find_element(By.XPATH,
        #                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH,
        #                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').clear()
        # driver.find_element(By.XPATH,
        #                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]').click()
        # codigo = None
        # try:
        #     test.start(listener, interval=5)
        #     codigo = 0
        #     while codigo != 20:
        #         time.sleep(1.5)
        #         codigo = codigo + 1
        #     codigo = cod
        # except Exception as e:
        #     if "Too Many Requests" in str(e):
        #         pass
        #     else:
        #         window['output'].print(e)
        #         window.Refresh()
        # window['output'].print(f"Codigo recebido: {codigo}")
        # window.Refresh()
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
        #                                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
        #     codigo)
        # try:
        #     WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
        # except:
        #     pass
        # try:
        #     WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()
        #     try:
        #         WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
        #     except:
        #         pass
        # except:
        #     WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
        #     try:
        #         WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
        #     except:
        #         pass
        # test.stop()
        # time.sleep(3)
        # WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
        #                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')))
        # reenv_cod = driver.find_elements(By.XPATH,
        #                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
        # if len(reenv_cod) == 1:
        #    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Enviando um novo codigo.')
        #    window.Refresh()
        #    driver.find_element(By.XPATH,
        #                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
        #    time.sleep(2)
        #    driver.find_element(By.XPATH,
        #                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').clear()
        #    driver.find_element(By.XPATH,
        #                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]').click()

    def gerar_email_firts_reg():
        global cod
        global email
        global lista_user
        global fake
        global nome
        global sobrenome
        global nomes
        global sobrenomes
        global nome_completo
        global nome_completo_s
        global numeros_concatenados
        global user_completo
        lista_user = random.choices(range(0, 9), k=2)
        lista_letras = random.choices(letras, k=1)

        try:
            with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                nomes = nomes_arquivo.readlines()

            with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                sobrenomes = sobrenomes_arquivo.readlines()

            nomea = fake.first_name_female().replace(" ", "")
            nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
            sobrenomea = fake.last_name().replace(" ", "").lower()
            sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')

            nome_completo = nome + ' ' + sobrenome
            nome_completo_s = nome + sobrenome
            numeros_concatenados = ''.join(str(numero) for numero in lista_user)
            user_completo = nome_completo_s + '' + str(numeros_concatenados) + ''.join(lista_letras)

            test = Email()
            arquivo = open('configuracoes/contas/senha_perfis.txt')
            senha = arquivo.read()
            test.register(username=user_completo, password=senha)
            window['output'].print("Email: " + str(test.address))
        except Exception as e:
            print(e)
            window.Refresh()
        time.sleep(2)
        email = str(test.address)
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
            email)
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()

        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando codigo...')
        window.Refresh()
        codigo = None
        try:
            test.start(listener, interval=15)
            codigo = 0
            while codigo != 20:
                time.sleep(2)
                codigo = codigo + 1
            codigo = cod
        except Exception as e:
            if "Too Many Requests" in str(e):
                pass
            else:
                pass
        window['output'].print(f"Codigo recebido: {codigo}")
        window.Refresh()
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                codigo)
            time.sleep(2)
        except:
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro encontrado.')
            window.Refresh()
            time.sleep(5)
        time.sleep(2)
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()
        except:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
        test.stop()
        time.sleep(5)
        codigo_invalido = driver.find_elements(By.XPATH,
                                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[5]')
        continua_na_tela = driver.find_elements(By.XPATH,
                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]/android.view.View')
        if len(codigo_invalido) and len(continua_na_tela) == 1:
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro encontrado.')
            window.Refresh()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]'))).click()
            # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, ''))).click()
            # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, ''))).click()
            # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, ''))).click()

            time.sleep(2)
            codigo = None
            try:
                test.start(listener, interval=5)
                codigo = 0
                while codigo != 20:
                    time.sleep(1.5)
                    codigo = codigo + 1
                codigo = cod
            except Exception as e:
                if "Too Many Requests" in str(e):
                    pass
                else:
                    window['output'].print(e)
                    window.Refresh()
            window['output'].print(f"Código recebido: {codigo}")
            window.Refresh()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                codigo)
            try:
                driver.find_element(By.XPATH,
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]').click()

            except:
                driver.find_element(By.XPATH,
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]').click()

            test.stop()
            time.sleep(3)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[8]')))
        return nome_completo

    def gerar_id():
        chars = string.ascii_lowercase + string.digits
        android_id = ''.join(random.choice(chars) for i in range(16))
        return android_id

    def firts_reg():
        global nome
        global sobrenome
        abc = True
        while abc:
            global sms
            sms = True
            # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True)

            try:
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
                time.sleep(5)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                time.sleep(3)
                error = driver.find_elements(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
                if len(error) == 1:
                    time.sleep(2)
                    driver.find_element(By.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro fechado.')
                    error = driver.find_elements(By.XPATH,
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
                    while len(error) == 1:
                        driver.find_element(By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
                        error = driver.find_elements(By.XPATH,
                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
                    try:
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
                        time.sleep(5)
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                        time.sleep(3)
                    except:
                        pass

                    window.Refresh()
                gerar_email_firts_reg()
            except Exception as e:
                print(e)
                comando = f"adb connect 127.0.0.1:{porta}"
                subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server.test',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, shell=True)

                window.Refresh()

                break
            nome_completo = nome + ' ' + sobrenome
            nome_completo_s = nome + sobrenome
            numeros_concatenados = ''.join(str(numero) for numero in lista_user)
            user_completo = nome_completo_s + '' + str(numeros_concatenados) + ''.join(lista_letras)
            window.Refresh()
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Nome escolhido: ' + nome_completo)
            window.Refresh()
            try:
                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[1]'))).send_keys(
                    nome_completo)
            except:
                cont = False
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro encontrado.')
                window.Refresh()
                pass
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[2]'))).send_keys(
                senha)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[5]/android.view.View'))).click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'))).click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[6]'))).click()
            idade_aleatoria = random.randint(18, 35)
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Idade escolhida: {idade_aleatoria}')
            window.Refresh()
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                idade_aleatoria)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
            op2 = driver.find_elements(By.XPATH,
                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[7]/android.view.View')
            op1 = driver.find_elements(By.XPATH,
                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View')
            time.sleep(5)
            try:
                if len(op1) == 0:
                    try:
                        driver.find_element(By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[7]/android.view.View').click()
                    except:
                        driver.find_element(By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[6]/android.view.View').click()
            except:
                try:
                    driver.find_element(By.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View').click()

                except:
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro ao criar')
                    window.Refresh()
                    sms = True
                    continue

            try:
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]'))).click()
                time.sleep(3)
                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                    user_completo)
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: {user_completo}')
                window.Refresh()
                time.sleep(3)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                time.sleep(5)
                erro_2 = driver.find_elements(By.XPATH,
                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[*]/android.view.View[*]/android.widget.Button')
                erro_1 = driver.find_elements(By.XPATH,
                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
                if len(erro_2) == 1:
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Tentando gerar novamente')
                    window.Refresh()
                    time.sleep(5)
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[1]'))).click()
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]'))).click()
                    time.sleep(3)
                if len(erro_1) == 1:
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
                time.sleep(4)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View'))).click()

            except:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')))
            time.sleep(20)
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
            time.sleep(5)
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
            window.Refresh()
            time.sleep(10)
            verificar = driver.find_elements(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')

            try:
                if len(verificar) == 1:
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                           text_color=('lime'))
                    window.Refresh()
                    contagem += 1
                    window['criadas'].update(contagem)
                    window.Refresh()
                    now = datetime.now()
                    now_brasilia = tz.localize(now)
                    timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                    client = gspread.authorize(creds)

                    spreadsheet_id = config['spreadsheet']
                    sheet_name = 'contas'
                    # Insert user, password, and timestamp into first empty row
                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                    values = sheet.col_values(1)
                    last_row = len(values)
                    values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                    cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                    for i, val in enumerate(values):
                        cell_list[i].value = val
                    sheet.update_cells(cell_list)

                    rows = sheet.get_all_values()

                    # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                    regex = re.compile(r'\S+\s\S+')

                    # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                    num_rows = sum(1 for row in rows if regex.match(row[0]))
                    window['total'].update(num_rows)

                    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                    creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                    client = gspread.authorize(creds)

                    spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                    sheet_name = 'relatorio_geral'
                    # Insert user, password, and timestamp into first empty row
                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                    values = sheet.col_values(1)
                    last_row = len(values)
                    values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                    cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                    for i, val in enumerate(values):
                        cell_list[i].value = val
                    sheet.update_cells(cell_list)

                    window.Refresh()
                    arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                    # Escreva mais conteúdo no arquivo
                    arquivo.write(user_completo + ' ' + senha + "\n")
                    arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                    # Escreva mais conteúdo no arquivo
                    arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]/android.view.View'))).click()

                    sms = False
                    break
                else:
                    conteudo = config['vpn']
                    # Executa a função correspondente ao conteúdo do arquivo
                    if conteudo == "AVG":
                        vpn_avg()
                    elif conteudo == "Avast":
                        vpn_avast()
                    elif conteudo == "CyberGhost":
                        vpn_cyberghost()
                    elif conteudo == "PiaVPN":
                        vpn_pia()
                    elif conteudo == "ExpressVPN":
                        vpn_express()
                    elif conteudo == "SurfShark":
                        vpn_surf()
                    elif conteudo == "BetterNet":
                        vpn_better()
                    elif conteudo == "NordVPN":
                        vpn_nord()
                    elif conteudo == "HotspotShield":
                        vpn_hotspotshield()
                    else:
                        window['output'].print(
                            "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                        window.Refresh()

            except Exception as e:
                print(e)

                sms = True
                conteudo = config['vpn']
                # Executa a função correspondente ao conteúdo do arquivo
                if conteudo == "AVG":
                    vpn_avg()
                elif conteudo == "Avast":
                    vpn_avast()
                elif conteudo == "CyberGhost":
                    vpn_cyberghost()
                elif conteudo == "PiaVPN":
                    vpn_pia()
                elif conteudo == "ExpressVPN":
                    vpn_express()
                elif conteudo == "SurfShark":
                    vpn_surf()
                elif conteudo == "BetterNet":
                    vpn_better()
                elif conteudo == "NordVPN":
                    vpn_nord()
                elif conteudo == "HotspotShield":
                    vpn_hotspotshield()
                else:
                    window['output'].print(
                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                    window.Refresh()
                break

    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.page_load_strategy = 'none'
    options.add_experimental_option("prefs", prefs)

    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Senha sendo utilizada: {senha}')
    window.Refresh()

    console = Console()

    device = [
        {'name': 'Bluestacks1', 'port': porta, 'udid': f'127.0.0.1:{porta}'},
    ]
    comando = f"adb connect 127.0.0.1:{porta}"
    subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
    subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server.test', stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server', stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    try:
        comando = f"adb connect 127.0.0.1:{porta}"
        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global window_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global transition_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global animator_duration_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
    except:
        pass
    gerar_id()
    android_id = gerar_id()
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    time.sleep(2)
    # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True, stdout=subprocess.DEVNULL,
    #               stderr=subprocess.DEVNULL)
    window.Refresh()

    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Iniciando criação.\n')
    window.Refresh()
    cont = True
    while cont is True:
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        window['output'].print(linha_ret)
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Abrindo Instagram')

        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        client = gspread.authorize(creds)

        spreadsheet_id = config['spreadsheet']
        sheet_name = 'contas'
        # Insert user, password, and timestamp into first empty row
        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
        values = sheet.col_values(1)

        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
        rows = sheet.get_all_values()

        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
        regex = re.compile(r'\S+\s\S+')

        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
        num_rows = sum(1 for row in rows if regex.match(row[0]))
        window['total'].update(num_rows)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server.test',
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, shell=True)
        except:
            pass
        window.Refresh()
        # try:
        #    subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
        #                   stderr=subprocess.DEVNULL, check=True, shell=True)
        # except:
        #    pass
        with open("storage/apk/caminho.txt", "r") as arquivo:
            appinsta = arquivo.read().strip()
        try:
            time.sleep(10)
            quantidade = 0
            desired_caps = {}
            desired_caps['udid'] = '127.0.0.1:' + porta
            desired_caps['newCommandTimeout'] = '500'
            desired_caps['platformName'] = 'Android'
            desired_caps['automationName'] = 'UiAutomator2'
            # desired_caps['app'] = appinsta
            # desired_caps['appPackage'] = 'com.instagram.lite'
            # desired_caps['appActivity'] = 'com.facebook.lite.MainActivity'
            desired_caps['systemPort'] = random.randint(1024, 65535)
            desired_caps['noReset'] = True

            driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            driver.activate_app('com.instagram.lite')
            gerar_id()
            android_id = gerar_id()
            # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
            #               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
            time.sleep(5)
            # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True,
            #               stdout=subprocess.DEVNULL,
            #               stderr=subprocess.DEVNULL)
            error = driver.find_elements(By.XPATH,
                                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
            if len(error) == 1:
                time.sleep(2)
                driver.find_element(By.XPATH,
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro fechado.')
                error = driver.find_elements(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
                while len(error) == 1:
                    driver.find_element(By.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
                    error = driver.find_elements(By.XPATH,
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')

                window.Refresh()
            try:
                time.sleep(3)
                cookies = driver.find_elements(By.ID, 'com.android.packageinstaller:id/permission_deny_button')
                if len(cookies) == 1:
                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                        (By.ID, 'com.android.packageinstaller:id/permission_deny_button'))).click()
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Pop-up fechado.')
                    window.Refresh()
                    time.sleep(1)
                firts_reg()

            except Exception as e:
                print(e)
                sms = True
                comando = f"adb connect 127.0.0.1:{porta}"
                subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server.test',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, shell=True)
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro não catalogado.')
                window.Refresh()
                conteudo = config['vpn']

                # Executa a função correspondente ao conteúdo do arquivo
                if conteudo == "AVG":
                    vpn_avg()
                elif conteudo == "SurfShark":
                    vpn_surf()
                elif conteudo == "Avast":
                    vpn_avast()
                elif conteudo == "PiaVPN":
                    vpn_pia()
                elif conteudo == "ExpressVPN":
                    vpn_express()
                elif conteudo == "BetterNet":
                    vpn_better()
                elif conteudo == "NordVPN":
                    vpn_nord()
                elif conteudo == "CyberGhost":
                    vpn_cyberghost()
                elif conteudo == "HotspotShield":
                    vpn_hotspotshield()
                else:
                    window['output'].print(
                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                    window.Refresh()
                continue

            try:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]/android.view.View')))
            except:
                continue

            while sms is False:
                try:
                    pular_erro = driver.find_elements(By.XPATH,
                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
                    if len(pular_erro) == 0:
                        try:
                            driver.find_elements(By.XPATH,
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()
                        except:
                            sms = True
                            continue
                    window['output'].print(linha_ret)
                    window.Refresh()
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Criação de outro perfil.')
                    window.Refresh()
                    # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True)
                    # Clicar no botão de perfil
                    try:
                        time.sleep(3)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]')))
                        time.sleep(2)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]'))).click()

                    except:
                        time.sleep(3)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')))
                        time.sleep(2)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]'))).click()

                        # Clicar em perfis
                    try:
                        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                    except:
                        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View'))).click()
                    # Clicar em adicionar conta
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'))).click()
                    # Clicar em criar nova conta
                    time.sleep(3)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]'))).click()
                    # Gerar nome de usuário, digitar no campo e clicar em avançae
                    lista_user = random.choices(range(0, 9), k=2)
                    lista_letras = random.choices(letras, k=1)

                    with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                        nomes = nomes_arquivo.readlines()

                    with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                        sobrenomes = sobrenomes_arquivo.readlines()

                    nomea = fake.first_name_female().replace(" ", "")
                    nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                    sobrenomea = fake.last_name().replace(" ", "").lower()
                    sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')

                    nome_completo = nome + sobrenome
                    numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                    user_completo = nome_completo + '' + str(numeros_concatenados) + ''.join(lista_letras)

                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: ' + user_completo)
                    window.Refresh()
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                        user_completo)
                    time.sleep(1)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                    # Digitar senha e avançar
                    time.sleep(3)
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                        senha)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
                    # Clicar em adicionar email
                    time.sleep(1)
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View')))
                    time.sleep(2)
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
                    # Clicar em email, gerar e avançar

                    time.sleep(5)
                    gerar_email()
                    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')))
                    time.sleep(10)
                    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()

                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
                    window.Refresh()
                    # WebDriverWait(driver, 40).until(EC.visibility_of_element_located)(((By.XPATH,
                    #                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')))
                    time.sleep(10)
                    verificar = driver.find_elements(By.XPATH,
                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')

                    conta_criada = driver.find_elements(By.XPATH,
                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
                    conta_sms = driver.find_elements(By.XPATH,
                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.View[4]')
                    if len(verificar) == 1:
                        try:
                            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]'))).click()
                        except:
                            pass
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                               text_color=('lime'))
                        contagem += 1
                        window['criadas'].update(contagem)
                        window.Refresh()
                        window.Refresh()
                        now = datetime.now()
                        now_brasilia = tz.localize(now)
                        timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                        client = gspread.authorize(creds)

                        spreadsheet_id = config['spreadsheet']
                        sheet_name = 'contas'
                        # Insert user, password, and timestamp into first empty row
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                        values = sheet.col_values(1)
                        last_row = len(values)
                        values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                        cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                        for i, val in enumerate(values):
                            cell_list[i].value = val
                        sheet.update_cells(cell_list)

                        rows = sheet.get_all_values()

                        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                        regex = re.compile(r'\S+\s\S+')

                        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                        num_rows = sum(1 for row in rows if regex.match(row[0]))
                        window['total'].update(num_rows)

                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                        creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                        client = gspread.authorize(creds)

                        spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                        sheet_name = 'relatorio_geral'
                        # Insert user, password, and timestamp into first empty row
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                        values = sheet.col_values(1)
                        last_row = len(values)
                        values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                        cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                        for i, val in enumerate(values):
                            cell_list[i].value = val
                        sheet.update_cells(cell_list)

                        window.Refresh()
                        arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                        # Escreva mais conteúdo no arquivo
                        arquivo.write(user_completo + ' ' + senha + "\n")
                        arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                        # Escreva mais conteúdo no arquivo
                        arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                        time.sleep(4)
                        arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                        arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]'))).click()
                        window.Refresh()
                        window['output'].print(
                            f'[{datetime.now().strftime("%H:%M:%S")}] Alterando perfil para publico.')
                        window.Refresh()

                        # Clicar nas 3 barras
                        try:
                            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup[5]'))).click()
                        except:
                            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[5]'))).click()

                        time.sleep(0.5)

                        # Clicar em configurações
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.View'))).click()
                        time.sleep(0.5)
                        # Clicar em privacidade
                        try:
                            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[7]/android.view.ViewGroup/android.view.View'))).click()
                        except:
                            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup/android.view.View'))).click()
                        time.sleep(2)
                        # Clicar em privacidade da conta
                        try:
                            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[11]/android.view.ViewGroup/android.view.ViewGroup/android.view.View'))).click()
                        except:
                            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[10]/android.view.ViewGroup/android.view.View'))).click()
                        time.sleep(0.5)
                        # Clicar no botão
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]/android.view.ViewGroup'))).click()
                        time.sleep(0.5)
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterado para publico.')
                        window.Refresh()
                        time.sleep(0.5)
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True, shell=True)
                        time.sleep(0.5)
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True, shell=True)
                        time.sleep(0.5)
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True, shell=True)
                        time.sleep(0.5)

                        sms = False

                    else:
                        try:
                            conteudo = config['vpn']
                            if conteudo == "AVG":
                                vpn_avg()
                            elif conteudo == "SurfShark":
                                vpn_surf()
                            elif conteudo == "Avast":
                                vpn_avast()
                            elif conteudo == "ExpressVPN":
                                vpn_express()
                            elif conteudo == "PiaVPN":
                                vpn_pia()
                            elif conteudo == "BetterNet":
                                vpn_better()
                            elif conteudo == "CyberGhost":
                                vpn_cyberghost()
                            elif conteudo == "NordVPN":
                                vpn_nord()
                            elif conteudo == "HotspotShield":
                                vpn_hotspotshield()
                                break
                            else:
                                window['output'].print(
                                    "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                window.Refresh()

                        except:
                            sms = True
                except:
                    sms = True
        except Exception as e:
            logger.error('Ocorreu um erro: %s', e)
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server.test',
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, shell=True)
            comando = f"adb connect 127.0.0.1:{porta}"
            subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server.test',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, shell=True)
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro não catalogado.')
            print(e)
            # window['output'].print(e)
            window.Refresh()


def executar_minuteinbox():
    SPREADSHEET_ID = config['spreadsheet']
    conteudo = config['vpn']
    senha = config['senha']
    maquina = config['maquina']
    from minuteinbox import Inbox
    global sms
    global nomes
    global sobrenomes
    global nome
    global contagem
    global sobrenome
    global lista_user
    window['Executar'].update(disabled=True)
    window.Refresh()
    # Código que gera a saída
    import os
    import time
    import requests
    import hashlib
    import subprocess

    # verifica se o arquivo existe na pasta do bot

    try:
        from rich.console import Console
    except ModuleNotFoundError:
        import subprocess
        import sys

        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instalando dependências...')
        window.Refresh()
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
        subprocess.run(['deactivate'], shell=True)
        from rich.console import Console
    import os
    import time
    import requests
    import hashlib
    import subprocess
    from colorama import init, Fore, Back, Style
    from faker import Faker
    # teste
    init(autoreset=True)
    console = Console()
    from termcolor import colored

    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.rule import Rule

    linha_ret = '_________________________________________________\n'
    window.Refresh()
    import random
    from datetime import datetime
    import string
    from appium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.common.exceptions import NoSuchElementException
    import re
    import logging

    logger = logging.getLogger(__name__)

    handler = logging.FileHandler('log.txt')
    handler.setLevel(logging.ERROR)

    logger.addHandler(handler)

    # RANGE_NAME = 'contas!A:D'
    #
    # SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    def vpn_avast():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] SMS\nAlterando IP da Avast', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        sms = True
        try:
            driver.start_activity("com.avast.android.vpn", ".app.wizard.WizardActivity")
            time.sleep(10)
        except Exception as e:
            print(e)

        abc = False

    def vpn_hotspotshield():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] SMS\nAlterando IP da HotspotShield',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        sms = True
        try:
            driver.start_activity("hotspotshield.android.vpn", "com.anchorfree.hotspotshield.ui.HssActivity")
        except Exception as e:
            print(e)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'hotspotshield.android.vpn:id/tryAgainButton'))).click()
        time.sleep(5)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'hotspotshield.android.vpn:id/btnVpnConnect'))).click()

        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_pia():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] SMS\nAlterando IP da PiaVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        sms = True
        try:
            driver.start_activity("com.privateinternetaccess.android", ".ui.LauncherActivity")
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'com.privateinternetaccess.android:id/connection_background'))).click()
        time.sleep(3)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'com.privateinternetaccess.android:id/connection_background'))).click()

        abc = False

    def vpn_express():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] SMS\nAlterando IP da ExpressVPN',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        sms = True
        try:
            driver.start_activity("com.expressvpn.vpn", ".ui.SplashActivity")
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'com.expressvpn.vpn:id/obiButton'))).click()
        time.sleep(3)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'com.expressvpn.vpn:id/obiButton'))).click()

        abc = False

    def vpn_nord():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] SMS\nAlterando IP da NordVPN',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        sms = True
        try:
            driver.start_activity("com.nordvpn.android", ".MainActivity")
        except:
            pass
        time.sleep(10)
        # try:
        #    WebDriverWait(driver, 10).until(
        #        EC.element_to_be_clickable((By.ID, 'com.nordvpn.android:id/reconnect_button'))).click()
        # except:
        #    pass
        # try:
        #    WebDriverWait(driver, 10).until(
        #        EC.element_to_be_clickable((By.ID, 'com.nordvpn.android:id/secondary_quick_connect_button'))).click()
        # except:
        #    pass
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'com.nordvpn.android:id/primary_quick_connect_button'))).click()
        time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_surf():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da SurfShark', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            driver.start_activity("com.surfshark.vpnclient.android", ".StartActivity")
        except:
            pass
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        time.sleep(5)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_better():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] SMS\nAlterando IP da BetterNet',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        try:
            driver.start_activity("com.freevpnintouch", "com.anchorfree.betternet.ui.BetternetActivity")
        except:
            pass
        time.sleep(10)
        dialog = driver.find_elements(By.ID, 'com.freevpnintouch:id/dialogCtaPositive')
        connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
        if len(dialog) == 1:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/dialogCtaPositive'))).click()
            time.sleep(3)
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
            # time.sleep(5)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
        while connect == 'CONNECT':
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
            time.sleep(4)
            connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
            # WebDriverWait(driver, 20).until(
            # EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        ip = '127.0.0.1:' + porta

        output = subprocess.check_output(['adb', '-s', ip, 'shell', 'ifconfig'])

        # Verifica se a conexão VPN está ativa
        if not re.search(b"tun0", output):
            window['output'].print("Não conectado na BetterNet.")
            window.Refresh()
            try:
                connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
                driver.start_activity("com.freevpnintouch", "com.anchorfree.betternet.ui.BetternetActivity")
                while connect == 'CONNECT':
                    WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
                    time.sleep(4)
                    connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
            except:
                pass
        abc = False

    def vpn_cyberghost():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] SMS\nAlterando IP da CyberGhost',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        try:
            driver.start_activity("de.mobileconcepts.cyberghost", ".view.app.AppActivity filter")
        except:
            pass
        # time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'de.mobileconcepts.cyberghost:id/button'))).click()
        rate = driver.find_elements(By.ID, 'de.mobileconcepts.cyberghost:id/rate_me_text')
        if len(rate) == 1:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'android:id/button2'))).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'de.mobileconcepts.cyberghost:id/button'))).click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        abc = False

    def vpn_avg():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] SMS\nAlterando IP da AVG', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        sms = True
        try:
            driver.start_activity("com.avg.android.vpn", "com.avast.android.vpn.app.wizard.WizardActivity")
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        # time.sleep(10)
        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        # time.sleep(10)
        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        # time.sleep(5)
        # WebDriverWait(driver, 30).until(
        #    EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        # time.sleep(5)

        abc = False

    def gerar_email():
        global lista_user
        global sms
        global nome
        global sobrenome
        global email
        lista_user = random.choices(range(0, 9), k=2)
        lista_letras = random.choices(letras, k=1)

        with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
            nomes = nomes_arquivo.readlines()

        with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
            sobrenomes = sobrenomes_arquivo.readlines()

        nomea = fake.first_name_female().replace(" ", "")
        nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
        sobrenomea = fake.last_name().replace(" ", "").lower()
        sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')

        nome_completo = nome + ' ' + sobrenome
        nome_completo_s = nome + sobrenome
        numeros_concatenados = ''.join(str(numero) for numero in lista_user)
        user_completo = nome_completo_s + '' + str(numeros_concatenados) + ''.join(lista_letras)

        inbox = Inbox(
            address="",
            token="",
        )

        time.sleep(2)
        num = driver.find_elements(By.XPATH,
                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]/android.view.View')

        while len(num) == 1:
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
            time.sleep(2)
            num = driver.find_elements(By.XPATH,
                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]/android.view.View')
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
            try:
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
                time.sleep(5)
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                time.sleep(3)
            except Exception as e:
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro.')
                window.Refresh()

        email = inbox.address
        window['output'].print("Email: " + email)
        window.Refresh()
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
            email)
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()
        # driver.find_element(By.XPATH,
        #                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]').click()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando codigo...')
        window.Refresh()
        subject = False
        while subject == False:
            for mail in inbox.mails:
                cod = mail.subject
                if 'code' in cod:
                    codigo = re.search(r'\d+', cod).group(0)
                    subject = True
                    time.sleep(1)
        window['output'].print(f"Codigo recebido: {codigo}")
        window.Refresh()
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                codigo)
        except:
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instagram fechou')
            window.Refresh()
        time.sleep(2)
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()
        except:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View')))
        except:
            pass
        ##time.sleep(3)
        # codigo_invalido = driver.find_elements(By.XPATH,
        #                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[5]')
        # continua_na_tela = driver.find_elements(By.XPATH,
        #                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]/android.view.View')
        # continua_na_tela2 = driver.find_elements(By.XPATH,
        #                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]/android.view.View')
        # criou = driver.find_elements(By.XPATH,
        #                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View')
        # time.sleep(25)
        # if len(codigo_invalido) == 1:
        # driver.find_element(By.XPATH,
        #                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
        # time.sleep(2)
        # driver.find_element(By.XPATH,
        #                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').clear()
        # driver.find_element(By.XPATH,
        #                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]').click()
        # codigo = None
        # try:
        #     test.start(listener, interval=5)
        #     codigo = 0
        #     while codigo != 20:
        #         time.sleep(1.5)
        #         codigo = codigo + 1
        #     codigo = cod
        # except Exception as e:
        #     if "Too Many Requests" in str(e):
        #         pass
        #     else:
        #         window['output'].print(e)
        #         window.Refresh()
        # window['output'].print(f"Codigo recebido: {codigo}")
        # window.Refresh()
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
        #                                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
        #     codigo)
        # try:
        #     WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
        # except:
        #     pass
        # try:
        #     WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()
        #     try:
        #         WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
        #     except:
        #         pass
        # except:
        #     WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
        #     try:
        #         WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
        #     except:
        #         pass
        # test.stop()
        # time.sleep(3)
        # WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
        #                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')))
        # reenv_cod = driver.find_elements(By.XPATH,
        #                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
        # if len(reenv_cod) == 1:
        #    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Enviando um novo codigo.')
        #    window.Refresh()
        #    driver.find_element(By.XPATH,
        #                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
        #    time.sleep(2)
        #    driver.find_element(By.XPATH,
        #                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').clear()
        #    driver.find_element(By.XPATH,
        #                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]').click()

    def gerar_email_firts_reg():
        global cod
        global email
        global lista_user
        global fake
        global nome
        global sobrenome
        global nomes
        global sobrenomes
        global nome_completo
        global nome_completo_s
        global numeros_concatenados
        global user_completo
        lista_user = random.choices(range(0, 9), k=2)
        lista_letras = random.choices(letras, k=1)

        with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
            nomes = nomes_arquivo.readlines()

        with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
            sobrenomes = sobrenomes_arquivo.readlines()

        nomea = fake.first_name_female().replace(" ", "")
        nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
        sobrenomea = fake.last_name().replace(" ", "").lower()
        sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
        nome_completo = nome + ' ' + sobrenome
        nome_completo_s = nome + sobrenome
        numeros_concatenados = ''.join(str(numero) for numero in lista_user)
        user_completo = nome_completo_s + '' + str(numeros_concatenados) + ''.join(lista_letras)
        try:
            inbox = Inbox(
                address="",
                token="",
            )
            email = inbox.address
            window['output'].print("Email: " + email)
            window.Refresh()
        except Exception as e:
            print(e)
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
            email)
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()

        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando codigo...')
        window.Refresh()
        subject = False
        while subject == False:
            for mail in inbox.mails:
                cod = mail.subject
                if 'code' in cod:
                    codigo = re.search(r'\d+', cod).group(0)
                    subject = True
                    time.sleep(1)
        window['output'].print(f"Codigo recebido: {codigo}")
        window.Refresh()
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                codigo)
            time.sleep(2)
        except:
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro encontrado.')
            window.Refresh()
            time.sleep(5)
        time.sleep(2)
        try:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()
        except:
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()

        time.sleep(5)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[8]')))
        return nome_completo

    def gerar_id():
        chars = string.ascii_lowercase + string.digits
        android_id = ''.join(random.choice(chars) for i in range(16))
        return android_id

    def firts_reg():
        global nome
        global sobrenome
        abc = True
        while abc:
            global sms
            sms = True
            # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True)

            try:
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
                time.sleep(5)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                time.sleep(3)
                error = driver.find_elements(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
                if len(error) == 1:
                    time.sleep(2)
                    driver.find_element(By.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro fechado.')
                    error = driver.find_elements(By.XPATH,
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
                    while len(error) == 1:
                        driver.find_element(By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
                        error = driver.find_elements(By.XPATH,
                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
                    try:
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
                        time.sleep(5)
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                        time.sleep(3)
                    except:
                        pass

                    window.Refresh()
                gerar_email_firts_reg()
            except Exception as e:
                comando = f"adb connect 127.0.0.1:{porta}"
                subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server.test',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, shell=True)

                window.Refresh()
                break
            nome_completo = nome + ' ' + sobrenome
            nome_completo_s = nome + sobrenome
            numeros_concatenados = ''.join(str(numero) for numero in lista_user)
            user_completo = nome_completo_s + '' + str(numeros_concatenados) + ''.join(lista_letras)
            window.Refresh()
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Nome escolhido: ' + nome_completo)
            window.Refresh()
            try:
                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[1]'))).send_keys(
                    nome_completo)
            except:
                cont = False
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro encontrado.')
                window.Refresh()
                pass
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[2]'))).send_keys(
                senha)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[5]/android.view.View'))).click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'))).click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[6]'))).click()
            idade_aleatoria = random.randint(18, 35)
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Idade escolhida: {idade_aleatoria}')
            window.Refresh()
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                idade_aleatoria)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
            op2 = driver.find_elements(By.XPATH,
                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[7]/android.view.View')
            op1 = driver.find_elements(By.XPATH,
                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View')
            time.sleep(5)
            try:
                if len(op1) == 0:
                    try:
                        driver.find_element(By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[7]/android.view.View').click()
                    except:
                        driver.find_element(By.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[6]/android.view.View').click()
            except:
                try:
                    driver.find_element(By.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View').click()

                except:
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro ao criar')
                    window.Refresh()
                    sms = True
                    continue

            try:
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]'))).click()
                time.sleep(3)
                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                    user_completo)
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: {user_completo}')
                window.Refresh()
                time.sleep(3)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                time.sleep(5)
                erro_2 = driver.find_elements(By.XPATH,
                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[*]/android.view.View[*]/android.widget.Button')
                erro_1 = driver.find_elements(By.XPATH,
                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
                if len(erro_2) == 1:
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Tentando gerar novamente')
                    window.Refresh()
                    time.sleep(5)
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[1]'))).click()
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]'))).click()
                    time.sleep(3)
                if len(erro_1) == 1:
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
                time.sleep(4)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View'))).click()

            except:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')))
            time.sleep(10)
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
            time.sleep(5)
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
            window.Refresh()
            time.sleep(10)
            verificar = driver.find_elements(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')
            # time.sleep(10)

            conta_criada = driver.find_elements(By.XPATH,
                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
            conta_sms = driver.find_elements(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.View[4]')

            try:
                if len(verificar) == 1:
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                           text_color=('lime'))
                    contagem += 1
                    window['criadas'].update(contagem)
                    window.Refresh()
                    window.Refresh()
                    now = datetime.now()
                    now_brasilia = tz.localize(now)
                    timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                    client = gspread.authorize(creds)

                    spreadsheet_id = config['spreadsheet']
                    sheet_name = 'contas'
                    # Insert user, password, and timestamp into first empty row
                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                    values = sheet.col_values(1)
                    last_row = len(values)
                    values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                    cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                    for i, val in enumerate(values):
                        cell_list[i].value = val
                    sheet.update_cells(cell_list)

                    rows = sheet.get_all_values()

                    # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                    regex = re.compile(r'\S+\s\S+')

                    # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                    num_rows = sum(1 for row in rows if regex.match(row[0]))
                    window['total'].update(num_rows)

                    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                    creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                    client = gspread.authorize(creds)

                    spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                    sheet_name = 'relatorio_geral'
                    # Insert user, password, and timestamp into first empty row
                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                    values = sheet.col_values(1)
                    last_row = len(values)
                    values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                    cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                    for i, val in enumerate(values):
                        cell_list[i].value = val
                    sheet.update_cells(cell_list)

                    window.Refresh()
                    arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                    # Escreva mais conteúdo no arquivo
                    arquivo.write(user_completo + ' ' + senha + "\n")
                    arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                    # Escreva mais conteúdo no arquivo
                    arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]/android.view.View'))).click()

                    sms = False
                    break
                else:
                    conteudo = config['vpn']
                    # Executa a função correspondente ao conteúdo do arquivo
                    if conteudo == "AVG":
                        vpn_avg()
                    elif conteudo == "Avast":
                        vpn_avast()
                    elif conteudo == "CyberGhost":
                        vpn_cyberghost()
                    elif conteudo == "PiaVPN":
                        vpn_pia()
                    elif conteudo == "ExpressVPN":
                        vpn_express()
                    elif conteudo == "SurfShark":
                        vpn_surf()
                    elif conteudo == "BetterNet":
                        vpn_better()
                    elif conteudo == "NordVPN":
                        vpn_nord()
                    elif conteudo == "HotspotShield":
                        vpn_hotspotshield()
                    else:
                        window['output'].print(
                            "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                        window.Refresh()

            except:
                sms = True
                break

    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.page_load_strategy = 'none'
    options.add_experimental_option("prefs", prefs)

    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Senha sendo utilizada: {senha}')
    window.Refresh()

    console = Console()

    device = [
        {'name': 'Bluestacks1', 'port': porta, 'udid': f'127.0.0.1:{porta}'},
    ]
    comando = f"adb connect 127.0.0.1:{porta}"
    subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
    subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server.test', stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server', stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    try:
        comando = f"adb connect 127.0.0.1:{porta}"
        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global window_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global transition_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global animator_duration_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
    except:
        pass
    gerar_id()
    android_id = gerar_id()
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    time.sleep(2)
    # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True, stdout=subprocess.DEVNULL,
    #               stderr=subprocess.DEVNULL)
    window.Refresh()
    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Iniciando criação.\n')
    window.Refresh()
    cont = True
    while cont is True:
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        window['output'].print(linha_ret)
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Abrindo Instagram')

        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        client = gspread.authorize(creds)

        spreadsheet_id = config['spreadsheet']
        sheet_name = 'contas'
        # Insert user, password, and timestamp into first empty row
        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
        values = sheet.col_values(1)

        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
        rows = sheet.get_all_values()

        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
        regex = re.compile(r'\S+\s\S+')

        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
        num_rows = sum(1 for row in rows if regex.match(row[0]))
        window['total'].update(num_rows)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server.test',
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        window.Refresh()
        # try:
        #    subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
        #                   stderr=subprocess.DEVNULL, check=True, shell=True)
        # except:
        #    pass
        with open("storage/apk/caminho.txt", "r") as arquivo:
            appinsta = arquivo.read().strip()
        try:
            time.sleep(10)
            quantidade = 0
            desired_caps = {}
            desired_caps['udid'] = '127.0.0.1:' + porta
            desired_caps['newCommandTimeout'] = '500'
            desired_caps['platformName'] = 'Android'
            desired_caps['automationName'] = 'UiAutomator2'
            # desired_caps['appPackage'] = 'com.instagram.lite'
            # desired_caps['appActivity'] = 'com.facebook.lite.MainActivity'
            desired_caps['systemPort'] = random.randint(1024, 65535)
            desired_caps['noReset'] = True
            # desired_caps['app'] = appinsta

            driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            driver.activate_app('com.instagram.lite')
            gerar_id()
            android_id = gerar_id()
            # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
            #               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
            time.sleep(5)
            # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True,
            #               stdout=subprocess.DEVNULL,
            #               stderr=subprocess.DEVNULL)
            error = driver.find_elements(By.XPATH,
                                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
            if len(error) == 1:
                time.sleep(2)
                driver.find_element(By.XPATH,
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro fechado.')
                error = driver.find_elements(By.XPATH,
                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
                while len(error) == 1:
                    driver.find_element(By.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
                    error = driver.find_elements(By.XPATH,
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')

                window.Refresh()
            try:
                time.sleep(3)
                cookies = driver.find_elements(By.ID, 'com.android.packageinstaller:id/permission_deny_button')
                if len(cookies) == 1:
                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                        (By.ID, 'com.android.packageinstaller:id/permission_deny_button'))).click()
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Pop-up fechado.')
                    window.Refresh()
                    time.sleep(1)
                firts_reg()

            except Exception as e:
                print(e)
                sms = True
                comando = f"adb connect 127.0.0.1:{porta}"
                subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server.test',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, shell=True)
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro não catalogado.')
                window.Refresh()
                conteudo = config['vpn']

                # Executa a função correspondente ao conteúdo do arquivo
                if conteudo == "AVG":
                    vpn_avg()
                elif conteudo == "SurfShark":
                    vpn_surf()
                elif conteudo == "Avast":
                    vpn_avast()
                elif conteudo == "PiaVPN":
                    vpn_pia()
                elif conteudo == "ExpressVPN":
                    vpn_express()
                elif conteudo == "BetterNet":
                    vpn_better()
                elif conteudo == "NordVPN":
                    vpn_nord()
                elif conteudo == "CyberGhost":
                    vpn_cyberghost()
                elif conteudo == "HotspotShield":
                    vpn_hotspotshield()
                else:
                    window['output'].print(
                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                    window.Refresh()
                continue

            try:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]/android.view.View')))
            except:
                continue

            while sms is False:
                try:
                    pular_erro = driver.find_elements(By.XPATH,
                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
                    if len(pular_erro) == 0:
                        try:
                            driver.find_elements(By.XPATH,
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()
                        except:
                            sms = True
                            continue
                    window['output'].print(linha_ret)
                    window.Refresh()
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Criação de outro perfil.')
                    window.Refresh()
                    # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True)
                    # Clicar no botão de perfil
                    try:
                        time.sleep(3)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]')))
                        time.sleep(2)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]'))).click()

                    except:
                        time.sleep(3)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')))
                        time.sleep(2)
                        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]'))).click()

                        # Clicar em perfis
                    try:
                        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                    except:
                        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View'))).click()
                    # Clicar em adicionar conta
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'))).click()
                    # Clicar em criar nova conta
                    time.sleep(3)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]'))).click()
                    # Gerar nome de usuário, digitar no campo e clicar em avançae
                    lista_user = random.choices(range(0, 9), k=2)
                    lista_letras = random.choices(letras, k=1)

                    with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                        nomes = nomes_arquivo.readlines()

                    with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                        sobrenomes = sobrenomes_arquivo.readlines()

                    nomea = fake.first_name_female().replace(" ", "")
                    nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                    sobrenomea = fake.last_name().replace(" ", "").lower()
                    sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                    nome_completo = nome + sobrenome
                    numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                    user_completo = nome_completo + '' + str(numeros_concatenados) + ''.join(lista_letras)

                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: ' + user_completo)
                    window.Refresh()
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                        user_completo)
                    time.sleep(1)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                    # Digitar senha e avançar
                    time.sleep(3)
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                        senha)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
                    # Clicar em adicionar email
                    time.sleep(1)
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View')))
                    time.sleep(2)
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
                    # Clicar em email, gerar e avançar

                    time.sleep(5)
                    gerar_email()
                    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')))
                    time.sleep(10)
                    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()

                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
                    window.Refresh()
                    # WebDriverWait(driver, 40).until(EC.visibility_of_element_located)(((By.XPATH,
                    #                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')))
                    time.sleep(10)
                    verificar = driver.find_elements(By.XPATH,
                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')

                    conta_criada = driver.find_elements(By.XPATH,
                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
                    conta_sms = driver.find_elements(By.XPATH,
                                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.View[4]')
                    if len(verificar) == 1:
                        try:
                            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]'))).click()
                        except:
                            pass
                        conteudo = config['vpn']
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                               text_color=('lime'))
                        contagem += 1
                        window['criadas'].update(contagem)
                        window.Refresh()
                        window.Refresh()
                        now = datetime.now()
                        now_brasilia = tz.localize(now)
                        timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                        client = gspread.authorize(creds)

                        spreadsheet_id = config['spreadsheet']
                        sheet_name = 'contas'
                        # Insert user, password, and timestamp into first empty row
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                        values = sheet.col_values(1)
                        last_row = len(values)
                        values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                        cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                        for i, val in enumerate(values):
                            cell_list[i].value = val
                        sheet.update_cells(cell_list)

                        rows = sheet.get_all_values()

                        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                        regex = re.compile(r'\S+\s\S+')

                        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                        num_rows = sum(1 for row in rows if regex.match(row[0]))
                        window['total'].update(num_rows)

                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                        creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                        client = gspread.authorize(creds)

                        spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                        sheet_name = 'relatorio_geral'
                        # Insert user, password, and timestamp into first empty row
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                        values = sheet.col_values(1)
                        last_row = len(values)
                        values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                        cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                        for i, val in enumerate(values):
                            cell_list[i].value = val
                        sheet.update_cells(cell_list)

                        window.Refresh()
                        arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                        # Escreva mais conteúdo no arquivo
                        arquivo.write(user_completo + ' ' + senha + "\n")
                        arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                        # Escreva mais conteúdo no arquivo
                        arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]'))).click()
                        window.Refresh()
                        window['output'].print(
                            f'[{datetime.now().strftime("%H:%M:%S")}] Alterando perfil para publico.')
                        window.Refresh()

                        # Clicar nas 3 barras
                        try:
                            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup[5]'))).click()
                        except:
                            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[5]'))).click()

                        time.sleep(0.5)

                        # Clicar em configurações
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.View'))).click()
                        time.sleep(0.5)
                        # Clicar em privacidade
                        try:
                            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[7]/android.view.ViewGroup/android.view.View'))).click()
                        except:
                            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup/android.view.View'))).click()
                        time.sleep(2)
                        # Clicar em privacidade da conta
                        try:
                            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[11]/android.view.ViewGroup/android.view.ViewGroup/android.view.View'))).click()
                        except:
                            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[10]/android.view.ViewGroup/android.view.View'))).click()
                        time.sleep(0.5)
                        # Clicar no botão
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]/android.view.ViewGroup'))).click()
                        time.sleep(0.5)
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterado para publico.')
                        window.Refresh()
                        time.sleep(0.5)
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True, shell=True)
                        time.sleep(0.5)
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True, shell=True)
                        time.sleep(0.5)
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True, shell=True)
                        time.sleep(0.5)

                        sms = False

                    else:
                        try:
                            conteudo = config['vpn']
                            if conteudo == "AVG":
                                vpn_avg()
                            elif conteudo == "SurfShark":
                                vpn_surf()
                            elif conteudo == "Avast":
                                vpn_avast()
                            elif conteudo == "ExpressVPN":
                                vpn_express()
                            elif conteudo == "PiaVPN":
                                vpn_pia()
                            elif conteudo == "BetterNet":
                                vpn_better()
                            elif conteudo == "CyberGhost":
                                vpn_cyberghost()
                            elif conteudo == "NordVPN":
                                vpn_nord()
                            elif conteudo == "HotspotShield":
                                vpn_hotspotshield()
                                break
                            else:
                                window['output'].print(
                                    "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                window.Refresh()

                        except:
                            sms = True
                except:
                    sms = True
        except Exception as e:
            logger.error('Ocorreu um erro: %s', e)
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server.test',
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, shell=True)
            comando = f"adb connect 127.0.0.1:{porta}"
            subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server.test',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, shell=True)
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro não catalogado.')
            print(e)
            # window['output'].print(e)
            window.Refresh()


def executar_2nr():
    SPREADSHEET_ID = config['spreadsheet']
    conteudo = config['vpn']
    senha = config['senha']
    maquina = config['maquina']
    sheet_name = config['2nr']
    tentativa = False
    seguido = False
    if config['email'] == '-2nr-' and config['app'] == '-instalite-':
        app = 'Lite'
    elif config['email'] == '-2nr-' and config['app'] == '-insta-':
        app = 'Normal'
    global sms
    global nomes
    global sobrenomes
    global nome
    global contagem
    global sobrenome
    global lista_user
    window['Executar'].update(disabled=True)
    window.Refresh()
    # Código que gera a saída
    import os
    import time
    import requests
    import hashlib
    import subprocess

    # verifica se o arquivo existe na pasta do bot

    try:
        from rich.console import Console
    except ModuleNotFoundError:
        import subprocess
        import sys

        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instalando dependências...')
        window.Refresh()
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
        subprocess.run(['deactivate'], shell=True)
        from rich.console import Console
    try:
        import uiautomator2 as u2
    except:
        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        subprocess.run(['pip', 'install', 'uiautomator2'])
        subprocess.run(['deactivate'], shell=True)
        subprocess.run(['pip', 'install', '--upgrade', 'requests'])
        import requests
        time.sleep(10)
        import uiautomator2 as u2
    d = u2.connect(f'127.0.0.1:{porta}')
    import os
    import time
    import requests
    import hashlib
    import subprocess
    from faker import Faker
    # teste

    linha_ret = '_________________________________________________\n'
    window.Refresh()
    import random
    from datetime import datetime
    import string
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.common.exceptions import NoSuchElementException
    from mailtm import Email
    import re
    import logging

    logger = logging.getLogger(__name__)

    handler = logging.FileHandler('log.txt')
    handler.setLevel(logging.ERROR)

    logger.addHandler(handler)

    def vpn_avast():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da Avast', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop("com.avast.android.vpn")
            d.app_start("com.avast.android.vpn", ".app.wizard.WizardActivity")
            time.sleep(10)
        except Exception as e:
            print(e)
        abc = False

    def nenhuma_vpn():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.facebook.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        time.sleep(10)

    def vpn_hotspotshield():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da HotspotShield',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('hotspotshield.android.vpn')
            d.app_start('hotspotshield.android.vpn')
        except Exception as e:
            print(e)
        d(resourceId='hotspotshield.android.vpn:id/tryAgainButton').click()
        time.sleep(5)
        d(resourceId='hotspotshield.android.vpn:id/btnVpnConnect').click()

        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_pia():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da PiaVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.privateinternetaccess.android')
            d.app_start('com.privateinternetaccess.android')
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        d(resourceId='com.privateinternetaccess.android:id/connection_background').click()
        time.sleep(3)
        d(resourceId='com.privateinternetaccess.android:id/connection_background').click()

        abc = False

    def vpn_express():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da ExpressVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.expressvpn.vpn')
            d.app_start('com.expressvpn.vpn')
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        d(resourceId='com.expressvpn.vpn:id/obiButton').click()
        time.sleep(3)
        d(resourceId='com.expressvpn.vpn:id/obiButton').click()

        abc = False

    def vpn_nord():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da NordVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        sms = True
        try:
            d.app_stop('com.nordvpn.android')
            d.app_start("com.nordvpn.android", ".MainActivity")
        except:
            pass
        time.sleep(10)
        time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_surf():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da SurfShark', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            d.app_stop('com.surfshark.vpnclient.android')
            d.app_start('com.surfshark.vpnclient.android')
        except:
            pass
        time.sleep(15)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_better():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da BetterNet', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        try:
            d.app_stop('com.freevpnintouch')
            d.app_start('com.freevpnintouch')
        except:
            pass
        time.sleep(10)
        dialog = d(resourceId='com.freevpnintouch:id/dialogCtaPositive')
        connect = d(resourceId='com.freevpnintouch:id/buttonConnect').text
        if dialog.exists:
            d(resourceId='com.freevpnintouch:id/dialogCtaPositive').click()
            time.sleep(3)
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
            # time.sleep(5)
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
        while connect == 'CONNECT':
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
            time.sleep(4)
            connect = d(resourceId='com.freevpnintouch:id/buttonConnect').text
            # WebDriverWait(driver, 20).until(
            # EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect').click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        ip = '127.0.0.1:' + porta

        output = subprocess.check_output(['adb', '-s', ip, 'shell', 'ifconfig'])

        # Verifica se a conexão VPN está ativa
        if not re.search(b"tun0", output):
            window['output'].print("Não conectado na BetterNet.")
            window.Refresh()
            try:
                connect = d(resourceId='com.freevpnintouch:id/buttonConnect').text
                d.app_stop('com.freevpnintouch')
                d.app_start('com.freevpnintouch')
                while connect == 'CONNECT':
                    d(resourceId='com.freevpnintouch:id/buttonConnect').click()
                    time.sleep(4)
                    connect = d(resourceId='com.freevpnintouch:id/buttonConnect').text
            except:
                pass
        abc = False

    def vpn_cyberghost():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da CyberGhost', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            d.app_stop('de.mobileconcepts.cyberghost')
            d.app_start('de.mobileconcepts.cyberghost')
        except:
            pass
        # time.sleep(3)
        d(resourceId='de.mobileconcepts.cyberghost:id/button').click()
        rate = d(resourceId='de.mobileconcepts.cyberghost:id/rate_me_text')
        if rate.exists:
            d(resourceId='android:id/button2').click()
        time.sleep(2)
        d(resourceId='de.mobileconcepts.cyberghost:id/button').click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        abc = False

    def vpn_avg():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da AVG', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.avg.android.vpn')
            d.app_start("com.avg.android.vpn", "com.avast.android.vpn.app.wizard.WizardActivity")
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #               stderr=subprocess.DEVNULL, check=True, shell=True)

        time.sleep(30)

    def vpn_windscribe():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da Windscribe', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)
            d.app_stop("com.windscribe.vpn")
            d.app_start("com.windscribe.vpn")
        except:
            pass
        d(resourceId='com.windscribe.vpn:id/on_off_button').click()
        time.sleep(10)

    def vpn_hma():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da HMA', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)

            d.app_stop("com.hidemyass.hidemyassprovpn")
            time.sleep(3)
            d.app_start('com.hidemyass.hidemyassprovpn', 'com.avast.android.vpn.activity.HmaOnboardingActivity')
        except:
            pass
        time.sleep(10)

    def gerar_id():
        chars = string.ascii_lowercase + string.digits
        android_id = ''.join(random.choice(chars) for i in range(16))
        return android_id

    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.page_load_strategy = 'none'
    options.add_experimental_option("prefs", prefs)

    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Senha sendo utilizada: {senha}')
    window.Refresh()

    try:
        comando = f"adb connect 127.0.0.1:{porta}"
        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global window_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global transition_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global animator_duration_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
    except:
        pass
    gerar_id()
    android_id = gerar_id()
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    time.sleep(2)

    try:
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
    except Exception as e:
        print(e)
        pass

    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Efetuando troca de IP.')
    window.Refresh()
    try:
        conteudo = config['vpn']
        if conteudo == "AVG":
            vpn_avg()
        elif conteudo == "SurfShark":
            vpn_surf()
        elif conteudo == "Nenhuma":
            nenhuma_vpn()
        elif conteudo == "Avast":
            vpn_avast()
        elif conteudo == "ExpressVPN":
            vpn_express()
        elif conteudo == "PiaVPN":
            vpn_pia()
        elif conteudo == "BetterNet":
            vpn_better()
        elif conteudo == "CyberGhost":
            vpn_cyberghost()
        elif conteudo == "NordVPN":
            vpn_nord()
        elif conteudo == "HotspotShield":
            vpn_hotspotshield()
        elif conteudo == "WindscribeVPN":
            vpn_windscribe()
        elif conteudo == "HmaVPN":
            vpn_hma()
        else:
            window['output'].print(
                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
            window.Refresh()

    except Exception as e:
        pass

    window.Refresh()
    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando sistema inicializar.')
    window.Refresh()

    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Iniciando criação.\n')
    window.Refresh()
    d.implicitly_wait(30.0)
    d.set_fastinput_ime(True)
    while parar is False:

        if parar is True:
            print('Parando Thread')
            break

        try:
            try:
                subprocess.run(f'uiautomator2 -s 127.0.0.1:{porta} uninstall com.instagram.lite',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, check=True, shell=True)
            except Exception as e:
                print(e)
                pass
            try:
                d.app_install('https://www.dropbox.com/s/kbflliyjze5x9bi/InstagramLite.apk?dl=1')
            except Exception as e:
                print(e)
                pass
            window['output'].print(linha_ret)
            window.Refresh()
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Abrindo 2NR')
            time.sleep(5)
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
            client = gspread.authorize(creds)

            spreadsheet_id = config['spreadsheet']
            sheet_name = 'contas'
            # Insert user, password, and timestamp into first empty row
            sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
            values = sheet.col_values(1)

            # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
            rows = sheet.get_all_values()

            # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
            regex = re.compile(r'\S+\s\S+')
            sheet_name = config['2nr']
            # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
            num_rows = sum(1 for row in rows if regex.match(row[0]))
            window['total'].update(num_rows)
            try:
                subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, check=True, shell=True)


            except:
                pass
            try:
                subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, check=True, shell=True)


            except:
                pass
            try:
                subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, check=True, shell=True)
            except Exception as e:
                print(e)
                pass

            window.Refresh()
            try:
                quantidade = 0

                gerar_id()
                android_id = gerar_id()
                subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
                               shell=True)
                d.app_start('pl.rs.sip.softphone.newapp')
                time.sleep(3)
                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                client = gspread.authorize(creds)

                spreadsheet_id = config['spreadsheet']

                sheet_name = config['2nr']
                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                # Obtém todas as células
                cells = sheet.get_all_values()

                # Armazena as células que correspondem à condição
                matches = [cell for row in cells for cell in row if
                           re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', cell)]

                # Armazena a lista de células correspondentes à condição em uma variável
                regex2nr = matches
                while len(regex2nr) == 0:
                    window['output'].print(
                        f'[{datetime.now().strftime("%H:%M:%S")}] Nenhuma conta do 2NR encontrada.\nTentando novamente em 5 min.')
                    window.Refresh()
                    cope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                    client = gspread.authorize(creds)

                    spreadsheet_id = config['spreadsheet']

                    sheet_name = config['2nr']
                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                    # Insert user, password, and timestamp into first empty row
                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                    values = sheet.col_values(1)

                    # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                    rows = sheet.get_all_values()

                    # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                    regex = re.compile(r'\S+\s\S+')
                    sheet_name = config['2nr']
                    # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                    num_rows = sum(1 for row in rows if regex.match(row[0]))
                    window['total'].update(num_rows)

                    time.sleep(300)
                    cells = sheet.get_all_values()

                    # Armazena as células que correspondem à condição
                    matches = [cell for row in cells for cell in row if
                               re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', cell)]

                    # Armazena a lista de células correspondentes à condição em uma variável
                    regex2nr = matches
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] {len(regex2nr)} conta(s) encontrada.')
                window.Refresh()
                time.sleep(3)
                try:
                    d(resourceId='pl.rs.sip.softphone.newapp:id/loginButton').click()
                except:
                    pass
                time.sleep(5)
                spreadsheet_id = config['spreadsheet']
                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                # Obtém todas as células

                # Define a faixa de células para leitura
                first_linha = sheet.cell(1, 1).value

                # Divide a string em duas partes separadas por um espaço em branco
                partes = first_linha.split(' ')

                # Atribui a primeira parte (endereço de e-mail) à variável email2nr
                email2nr = partes[0]

                # Atribui a segunda parte (texto) à variável senha2nr
                senha2nr = partes[1]
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Email 2NR: {email2nr}')
                window.Refresh()
                d(resourceId='pl.rs.sip.softphone.newapp:id/emailEdiText').set_text(email2nr)
                time.sleep(0.5)
                d(resourceId='pl.rs.sip.softphone.newapp:id/passwordEdiText').set_text(senha2nr)
                time.sleep(0.5)
                d(resourceId='pl.rs.sip.softphone.newapp:id/buttonLogin').click()
                time.sleep(7)
                try:
                    d(resourceId='pl.rs.sip.softphone.newapp:id/buttonAgree')
                except:
                    try:
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta não existe.')
                        window.Refresh()
                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                        client = gspread.authorize(creds)
                        # Abre a planilha e a planilha de uma determinada aba
                        spreadsheet_id = config['spreadsheet']
                        sheet_name = config['2nr']
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)

                        # Apaga a primeira célula da coluna A e desloca as células abaixo
                        sheet.delete_rows(1, 1)
                        conteudo = config['vpn']
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "Nenhuma":
                            nenhuma_vpn()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()
                    except Exception as e:
                        print(e)
                    continue
                perm = d(resourceId='pl.rs.sip.softphone.newapp:id/buttonAgree')
                if perm.exists(timeout=30):
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aceitando permissões.')
                    window.Refresh()
                    d(resourceId='pl.rs.sip.softphone.newapp:id/buttonAgree').click()
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/androidx.cardview.widget.CardView[1]/androidx.appcompat.widget.LinearLayoutCompat/android.widget.TextView').click()
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout').click()
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.Switch').click()
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.Switch').click()
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout[2]/android.widget.Switch').click()
                    subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK',
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                    time.sleep(0.5)
                    subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK',
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                    time.sleep(0.5)
                    subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK',
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                else:
                    try:
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta não existe.')
                        window.Refresh()
                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                        client = gspread.authorize(creds)
                        # Abre a planilha e a planilha de uma determinada aba
                        spreadsheet_id = config['spreadsheet']
                        sheet_name = config['2nr']
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)

                        # Apaga a primeira célula da coluna A e desloca as células abaixo
                        sheet.delete_rows(1, 1)
                        conteudo = config['vpn']
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "Nenhuma":
                            nenhuma_vpn()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()
                    except Exception as e:
                        print(e)
                    raise Exception('Erro.')
                qtd_num2 = d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[*]/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.TextView[1]')
                qtd_num = qtd_num2.all()
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] {len(qtd_num)} número(s) encontrado.')
                if len(qtd_num) == 0:
                    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                    client = gspread.authorize(creds)
                    # Abre a planilha e a planilha de uma determinada aba
                    spreadsheet_id = config['spreadsheet']
                    sheet_name = config['2nr']
                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)

                    # Apaga a primeira célula da coluna A e desloca as células abaixo
                    sheet.delete_rows(1, 1)

                    continue
                window.Refresh()
                num = d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.TextView[1]').text
                num = num.replace(' ', '')
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Número: {num}')
                window.Refresh()
                email = num
                d(resourceId='pl.rs.sip.softphone.newapp:id/messages').click()
                d(resourceId='pl.rs.sip.softphone.newapp:id/buttonSettings').click()
                d(resourceId='pl.rs.sip.softphone.newapp:id/buttonDelete').click()
                d(resourceId='pl.rs.sip.softphone.newapp:id/numbers').click()

                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Abrindo instagram.')
                window.Refresh()
                d.app_start('com.instagram.lite')
                time.sleep(5)
                try:
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()
                except:
                    pass

                time.sleep(6)
                try:
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]').click()
                    time.sleep(5)
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.MultiAutoCompleteTextView').set_text(
                        '48')
                    time.sleep(6)
                except:
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Página estática.')
                    window.Refresh()
                    conteudo = config['vpn']
                    if conteudo == "AVG":
                        vpn_avg()
                    elif conteudo == "SurfShark":
                        vpn_surf()
                    elif conteudo == "Avast":
                        vpn_avast()
                    elif conteudo == "Nenhuma":
                        nenhuma_vpn()
                    elif conteudo == "ExpressVPN":
                        vpn_express()
                    elif conteudo == "PiaVPN":
                        vpn_pia()
                    elif conteudo == "BetterNet":
                        vpn_better()
                    elif conteudo == "CyberGhost":
                        vpn_cyberghost()
                    elif conteudo == "NordVPN":
                        vpn_nord()
                    elif conteudo == "HotspotShield":
                        vpn_hotspotshield()
                    else:
                        window['output'].print(
                            "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                        window.Refresh()
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup/android.view.View').click()
                time.sleep(1)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').set_text(
                    num)
                time.sleep(1)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]').click()

                time.sleep(7)
                restricao = d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
                if restricao.exists and tentativa is True:
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Restrição.')
                    window.Refresh()
                    window['output'].print(
                        f'[{datetime.now().strftime("%H:%M:%S")}] Já foi feita uma tentativa. Apagando número.')
                    window.Refresh()
                    tentativa = False

                    d.app_start('pl.rs.sip.softphone.newapp')
                    time.sleep(4)
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/androidx.appcompat.widget.LinearLayoutCompat').click()
                    d(resourceId='pl.rs.sip.softphone.newapp:id/buttonDelete').click()
                    d(resourceId='pl.rs.sip.softphone.newapp:id/buttonAgree').click()
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Número excluído.')
                    window.Refresh()
                    try:
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True, shell=True)


                    except:
                        pass
                    try:
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True, shell=True)
                    except:
                        pass
                    try:
                        conteudo = config['vpn']
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "Nenhuma":
                            nenhuma_vpn()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()
                        raise Exception('skip')
                    except:
                        raise Exception('skip')

                elif restricao.exists and tentativa is False:
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Restrição.')
                    window.Refresh()
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Tentando mais uma vez.')
                    window.Refresh()
                    tentativa = True
                    try:
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True, shell=True)


                    except:
                        pass
                    try:
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True, shell=True)
                    except:
                        pass
                    try:
                        conteudo = config['vpn']
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "Nenhuma":
                            nenhuma_vpn()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                            break
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()
                        raise Exception('skip')
                    except:
                        raise Exception('skip')

                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando código...')
                window.Refresh()
                d.app_start('pl.rs.sip.softphone.newapp')
                time.sleep(3)
                d(resourceId='pl.rs.sip.softphone.newapp:id/messages').click()

                try:
                    cod = d(resourceId='pl.rs.sip.softphone.newapp:id/message').get_text(timeout=80)
                except Exception as e:
                    print(e)
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Reenviando código.')
                    window.Refresh()
                    d.app_start('com.instagram.lite')
                    time.sleep(3)
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup').click()
                    d.app_start('pl.rs.sip.softphone.newapp')
                try:
                    cod = d(resourceId='pl.rs.sip.softphone.newapp:id/message').get_text(timeout=80)
                except Exception as e:
                    print(e)
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Código não recebido.')
                    window.Refresh()
                    seguido = False
                    d.app_start('pl.rs.sip.softphone.newapp')
                    time.sleep(4)
                    d(resourceId='pl.rs.sip.softphone.newapp:id/numbers').click()
                    time.sleep(1)
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/androidx.appcompat.widget.LinearLayoutCompat').click()
                    d(resourceId='pl.rs.sip.softphone.newapp:id/buttonDelete').click()
                    d(resourceId='pl.rs.sip.softphone.newapp:id/buttonAgree').click()
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Número excluído.')
                    window.Refresh()
                    try:
                        conteudo = config['vpn']
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "Nenhuma":
                            nenhuma_vpn()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                            break
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()
                        continue
                        raise Exception('skip')
                    except:
                        raise Exception('skip')
                codigo = re.sub('[^0-9]', '', cod)
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Codigo recebido: {codigo}')
                tentativa = False
                window.Refresh()
                d.app_start('com.instagram.lite')
                time.sleep(5)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').set_text(
                    codigo)
                # time.sleep(100)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]').click()
                time.sleep(5)

                codigo_invalido = d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[2]')
                # if codigo_invalido.exists:
                #    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Código inválido.')
                #    window.Refresh()
                #    d.app_start('pl.rs.sip.softphone.newapp')
                #    time.sleep(4)
                #    d(resourceId='pl.rs.sip.softphone.newapp:id/numbers').click()
                #    time.sleep(1)
                #    d.xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/androidx.appcompat.widget.LinearLayoutCompat').click()
                #    d(resourceId='pl.rs.sip.softphone.newapp:id/buttonDelete').click()
                #    d(resourceId='pl.rs.sip.softphone.newapp:id/buttonAgree').click()
                #    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Número excluído.')
                #    window.Refresh()
                #
                #    try:
                #        conteudo = config['vpn']
                #        if conteudo == "AVG":
                #            vpn_avg()
                #        elif conteudo == "SurfShark":
                #            vpn_surf()
                #        elif conteudo == "Avast":
                #            vpn_avast()
                #        elif conteudo == "ExpressVPN":
                #            vpn_express()
                #        elif conteudo == "PiaVPN":
                #            vpn_pia()
                #        elif conteudo == "BetterNet":
                #            vpn_better()
                #        elif conteudo == "CyberGhost":
                #            vpn_cyberghost()
                #        elif conteudo == "NordVPN":
                #            vpn_nord()
                #        elif conteudo == "HotspotShield":
                #            vpn_hotspotshield()
                #            break
                #        else:
                #            window['output'].print(
                #                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                #            window.Refresh()
                #    except:
                #        pass
                ######################################################################
                lista_user = random.choices(range(0, 9), k=2)
                lista_letras = random.choices(letras, k=1)

                with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                    nomes = nomes_arquivo.readlines()

                with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                    sobrenomes = sobrenomes_arquivo.readlines()

                nomea = fake.first_name_female().replace(" ", "")
                nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                sobrenomea = fake.last_name().replace(" ", "").lower()
                sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                nome_completo = nome + ' ' + sobrenome
                nome_completo_s = nome + sobrenome
                numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                user_completo1 = nome_completo_s + '' + str(numeros_concatenados) + ''.join(lista_letras)

                user_completo = random.randint(1, len(user_completo1))
                # Insira o ponto no índice aleatório
                string_with_dot = user_completo1[:user_completo] + '_' + user_completo1[user_completo:]
                user_completo = string_with_dot.lower()
                print(user_completo)
                ######################################################################

                senha = config['senha']
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[1]').set_text(
                    nome_completo)
                time.sleep(1)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[2]').set_text(
                    senha)
                time.sleep(1)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[5]/android.view.View').click()
                time.sleep(3)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View').click()
                time.sleep(1)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
                time.sleep(2)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[last()]').click()
                time.sleep(2)
                idade_aleatoria = random.randint(18, 35)
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Idade escolhida: {idade_aleatoria}')
                window.Refresh()
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').set_text(
                    str(idade_aleatoria))
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()
                op2 = d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[7]/android.view.View')
                op1 = d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View')
                time.sleep(5)
                try:
                    if not op1.exists:
                        try:

                            d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[last()]/android.view.View').click()
                            print('a1')
                        except:
                            d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[6]/android.view.View').click()
                            print('a2')
                    else:
                        d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[last()]/android.view.View').click()
                        print('aq5')
                except:
                    try:
                        d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[last()]/android.view.View').click()
                        print('aq2')
                    except:
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Erro ao criar')
                        window.Refresh()
                        sms = True
                        continue
                try:
                    time.sleep(1)
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').set_text(
                        '')
                    time.sleep(3)
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').set_text(
                        user_completo)
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: {user_completo}')
                    window.Refresh()
                    time.sleep(3)
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()
                    time.sleep(5)
                    conta_jacriada = d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]')
                    time.sleep(1)
                    if conta_jacriada.exists:
                        d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View').click()
                    erro_2 = d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[*]/android.view.View[*]/android.widget.Button')
                    erro_1 = d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
                    if erro_2.exists:
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Tentando gerar novamente')
                        window.Refresh()
                        time.sleep(5)
                        d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()
                        d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]').click()
                        time.sleep(3)
                    if erro_1.exists:
                        d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')
                    time.sleep(3)
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View').click()

                except Exception as e:
                    print('aq')
                    print(e)

                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View').click()
                time.sleep(20)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()

                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
                window.Refresh()
                time.sleep(5)
                verificar = d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')
                # time.sleep(10)

                conta_criada = d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
                conta_sms = d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.View[4]')

                try:
                    if verificar.exists:
                        try:
                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                                   text_color=('lime'))
                            window.Refresh()
                            seguido = False
                            contagem += 1
                            window['criadas'].update(contagem)
                            window.Refresh()
                            now = datetime.now()
                            now_brasilia = tz.localize(now)
                            timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                            creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                            client = gspread.authorize(creds)

                            spreadsheet_id = config['spreadsheet']
                            sheet_name = 'contas'
                            # Insert user, password, and timestamp into first empty row
                            sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                            values = sheet.col_values(1)
                            last_row = len(values)
                            values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo + ' - ' + app]
                            cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                            for i, val in enumerate(values):
                                cell_list[i].value = val
                            sheet.update_cells(cell_list)

                            rows = sheet.get_all_values()

                            # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                            regex = re.compile(r'\S+\s\S+')

                            # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                            num_rows = sum(1 for row in rows if regex.match(row[0]))
                            window['total'].update(num_rows)

                            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                            creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                            client = gspread.authorize(creds)

                            spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                            sheet_name = 'relatorio_geral'
                            # Insert user, password, and timestamp into first empty row
                            sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                            values = sheet.col_values(1)
                            last_row = len(values)
                            values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo + ' - ' + app]
                            cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                            for i, val in enumerate(values):
                                cell_list[i].value = val
                            sheet.update_cells(cell_list)
                        except Exception as e:
                            print(e)
                            pass
                        window.Refresh()
                        arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                        # Escreva mais conteúdo no arquivo
                        arquivo.write(user_completo + ' ' + senha + "\n")
                        arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                        # Escreva mais conteúdo no arquivo
                        arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                        d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]/android.view.View').click()

                        sms = False
                    else:
                        if seguido is True:
                            seguido = False
                            window['output'].print(
                                f'[{datetime.now().strftime("%H:%M:%S")}] SMS seguidos, Trocando de número.')
                            window.Refresh()
                            d.app_start('pl.rs.sip.softphone.newapp')
                            time.sleep(4)
                            d(resourceId='pl.rs.sip.softphone.newapp:id/numbers').click()
                            d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/androidx.appcompat.widget.LinearLayoutCompat').click()
                            d(resourceId='pl.rs.sip.softphone.newapp:id/buttonDelete').click()
                            d(resourceId='pl.rs.sip.softphone.newapp:id/buttonAgree').click()
                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Número excluído.')
                            window.Refresh()
                            sms = True
                        elif seguido is False:
                            seguido = True
                        try:
                            conteudo = config['vpn']

                            # Executa a função correspondente ao conteúdo do arquivo
                            if conteudo == "AVG":
                                vpn_avg()
                            elif conteudo == "Avast":
                                vpn_avast()
                            elif conteudo == "CyberGhost":
                                vpn_cyberghost()
                            elif conteudo == "PiaVPN":
                                vpn_pia()
                            elif conteudo == "Nenhuma":
                                nenhuma_vpn()
                            elif conteudo == "ExpressVPN":
                                vpn_express()
                            elif conteudo == "SurfShark":
                                vpn_surf()
                            elif conteudo == "BetterNet":
                                vpn_better()
                            elif conteudo == "NordVPN":
                                vpn_nord()
                            elif conteudo == "HotspotShield":
                                vpn_hotspotshield()
                            else:
                                window['output'].print(
                                    "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                window.Refresh()
                        except:
                            sms = True
                            continue
                except Exception as e:
                    print(e)
                    try:
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "Nenhuma":
                            nenhuma_vpn()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()
                    except:
                        pass
                    sms = True
                    continue
                try:
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]/android.view.View')
                except:
                    continue
                if os.path.exists('teste'):
                    try:
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True, shell=True)
                    except:
                        pass
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Utilizando Instagram normal.')
                    window.Refresh()
                    d.set_fastinput_ime(True)
                    d.app_start('com.instagram.android')
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Abrindo instagram.')
                    window.Refresh()
                    time.sleep(10)
                    try:
                        d.xpath(
                            '//android.view.View[@content-desc="Nome de usuário, email ou número de celular"]').wait(
                            timeout=80)
                        d.xpath(
                            '//android.view.View[@content-desc="Nome de usuário, email ou número de celular"]').set_text(
                            user_completo)
                    except Exception as e:
                        print(e)
                        conteudo = config['vpn']
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "WindscribeVPN":
                            vpn_windscribe()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HmaVPN":
                            vpn_hma()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()
                    d.xpath('//android.view.View[@content-desc="Senha"]').set_text(senha)
                    d.xpath('//android.view.View[@content-desc="Entrar"]').click()
                    d.xpath('//android.view.View[@content-desc="Salvar suas informações de login?"]').wait(20)
                    if d.xpath('//android.view.View[@content-desc="Salvar suas informações de login?"]').exists:
                        d.xpath('//android.view.View[@content-desc="Agora não"]').click()
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta logada.')
                        window.Refresh()
                    while sms is False:
                        d(resourceId='com.instagram.android:id/profile_tab').click()
                        time.sleep(3)
                        d(resourceId='com.instagram.android:id/action_bar_title_chevron').click()
                        time.sleep(2)
                        d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[last()]/android.widget.FrameLayout/android.widget.ImageView').click()
                        time.sleep(4)
                        d.xpath('//android.widget.Button[@content-desc="Criar nova conta"]').click()
                        time.sleep(3)
                        # Gerar nome de usuário, digitar no campo e clicar em avançae
                        lista_user = random.choices(range(0, 9), k=2)
                        lista_letras = random.choices(letras, k=1)
                        nomea = fake.first_name_female().replace(" ", "")
                        nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                        sobrenomea = fake.last_name().replace(" ", "").lower()
                        sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                        nome_completo = nome + sobrenome
                        numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                        user_completo1 = nome_completo + '' + str(numeros_concatenados) + ''.join(lista_letras)

                        user_completo = random.randint(1, len(user_completo1))
                        # Insira o ponto no índice aleatório
                        string_with_dot = user_completo1[:user_completo] + '_' + user_completo1[user_completo:]
                        user_completo = string_with_dot.lower()
                        print(user_completo)
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: ' + user_completo)
                        window.Refresh()
                        d(resourceId='com.instagram.android:id/username').set_text(user_completo)
                        time.sleep(3)
                        d(resourceId='com.instagram.android:id/button_text').click()
                        # Digitar senha e avançar
                        time.sleep(3)
                        try:
                            d(resourceId='com.instagram.android:id/password').set_text(senha)
                        except:
                            try:
                                conteudo = config['vpn']
                                if conteudo == "AVG":
                                    vpn_avg()
                                elif conteudo == "SurfShark":
                                    vpn_surf()
                                elif conteudo == "Avast":
                                    vpn_avast()
                                elif conteudo == "ExpressVPN":
                                    vpn_express()
                                elif conteudo == "PiaVPN":
                                    vpn_pia()
                                elif conteudo == "WindscribeVPN":
                                    vpn_windscribe()
                                elif conteudo == "BetterNet":
                                    vpn_better()
                                elif conteudo == "CyberGhost":
                                    vpn_cyberghost()
                                elif conteudo == "HmaVPN":
                                    vpn_hma()
                                elif conteudo == "NordVPN":
                                    vpn_nord()
                                elif conteudo == "HotspotShield":
                                    vpn_hotspotshield()
                                else:
                                    window['output'].print(
                                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                    window.Refresh()

                            except:
                                sms = True
                        d(resourceId='com.instagram.android:id/button_text').click()
                        # Clicar em concluir cadastro
                        time.sleep(3)
                        d(resourceId='com.instagram.android:id/button_text').click()

                        time.sleep(4)
                        feedback = d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.View')
                        if feedback.exists:
                            sms = True

                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
                        window.Refresh()
                        # WebDriverWait(driver, 40).until(EC.visibility_of_element_located)(((By.XPATH,
                        #                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')))
                        # d(resourceId='com.instagram.android:id/connect_text').wait()
                        d(resourceId='com.instagram.android:id/connect_text').wait(timeout=30)
                        time.sleep(3)
                        verificar = d(resourceId='com.instagram.android:id/connect_text')

                        if verificar.exists:
                            try:
                                conteudo = config['vpn']
                                window['output'].print(
                                    f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                    text_color=('lime'))
                                window.Refresh()
                                contagem += 1
                                window['criadas'].update(contagem)
                                window.Refresh()
                                now = datetime.now()
                                now_brasilia = tz.localize(now)
                                timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                                client = gspread.authorize(creds)

                                spreadsheet_id = config['spreadsheet']
                                sheet_name = 'contas'
                                # Insert user, password, and timestamp into first empty row
                                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                values = sheet.col_values(1)
                                last_row = len(values)
                                values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                          conteudo + ' - ' + app]
                                cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                for i, val in enumerate(values):
                                    cell_list[i].value = val
                                sheet.update_cells(cell_list)

                                rows = sheet.get_all_values()

                                # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                                regex = re.compile(r'\S+\s\S+')

                                # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                                num_rows = sum(1 for row in rows if regex.match(row[0]))
                                window['total'].update(num_rows)
                                time.sleep(4)
                                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                                client = gspread.authorize(creds)

                                spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                                sheet_name = 'relatorio_geral'
                                # Insert user, password, and timestamp into first empty row
                                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                values = sheet.col_values(1)
                                last_row = len(values)
                                values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                          conteudo + ' - ' + app]
                                cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                for i, val in enumerate(values):
                                    cell_list[i].value = val
                                sheet.update_cells(cell_list)




                            except:
                                pass

                            window.Refresh()
                            arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                            # Escreva mais conteúdo no arquivo
                            arquivo.write(user_completo + ' ' + senha + "\n")
                            arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                            # Escreva mais conteúdo no arquivo
                            arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                            window.Refresh()
                            d(resourceId='com.instagram.android:id/skip_button').click()
                            time.sleep(1)
                            d(resourceId='com.instagram.android:id/negative_button').click()
                            time.sleep(3)
                            d(resourceId='com.instagram.android:id/skip_button').click()
                            time.sleep(1)
                            try:
                                d.xpath(
                                    '//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView').click()
                            except:
                                d(resourceId='com.instagram.android:id/skip_button').click()
                                d.xpath(
                                    '//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView').click()

                            time.sleep(1)
                            time.sleep(3)
                            try:
                                d(resourceId='com.instagram.android:id/profile_tab').click()
                            except:
                                d(resourceId='com.instagram.android:id/button_text').click()
                                d(resourceId='com.instagram.android:id/profile_tab').click()
                            sms = False
                            window['output'].print(linha_ret)
                            window.Refresh()
                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Criação de outro perfil.')
                            window.Refresh()
                        else:
                            try:
                                conteudo = config['vpn']
                                if conteudo == "AVG":
                                    vpn_avg()
                                elif conteudo == "SurfShark":
                                    vpn_surf()
                                elif conteudo == "Avast":
                                    vpn_avast()
                                elif conteudo == "ExpressVPN":
                                    vpn_express()
                                elif conteudo == "PiaVPN":
                                    vpn_pia()
                                elif conteudo == "WindscribeVPN":
                                    vpn_windscribe()
                                elif conteudo == "BetterNet":
                                    vpn_better()
                                elif conteudo == "CyberGhost":
                                    vpn_cyberghost()
                                elif conteudo == "HmaVPN":
                                    vpn_hma()
                                elif conteudo == "NordVPN":
                                    vpn_nord()
                                elif conteudo == "HotspotShield":
                                    vpn_hotspotshield()
                                else:
                                    window['output'].print(
                                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                    window.Refresh()

                            except Exception as e:
                                sms = True
                                pass
                    else:
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Houve algum erro ao logar.')
                        window.Refresh()
                        sms = True
                else:
                    while sms is False:

                        try:
                            window['output'].print(linha_ret)
                            window.Refresh()
                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Criação de outro perfil.')
                            window.Refresh()
                            # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True)
                            # Clicar no botão de perfil
                            try:
                                time.sleep(3)
                                # d.xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]').click()
                                d.xpath(
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[last()]').click()
                            except Exception as e:
                                print(e)
                                time.sleep(3)
                                d.xpath(
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]').click()

                                # Clicar em perfis
                            time.sleep(8)
                            try:
                                d.xpath(
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()
                            except Exception as e:
                                print(e)
                                d.xpath(
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]/android.view.View').click()
                            # Clicar em adicionar conta
                            time.sleep(2)
                            d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]').click()
                            # Clicar em criar nova conta
                            time.sleep(10)
                            d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]').click()
                            # Gerar nome de usuário, digitar no campo e clicar em avançae
                            lista_user = random.choices(range(0, 9), k=2)
                            lista_letras = random.choices(letras, k=1)

                            with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                                nomes = nomes_arquivo.readlines()

                            with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                                sobrenomes = sobrenomes_arquivo.readlines()

                            nomea = fake.first_name_female().replace(" ", "")
                            nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                            sobrenomea = fake.last_name().replace(" ", "").lower()
                            sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode(
                                'ASCII')
                            nome_completo = nome + sobrenome
                            numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                            user_completo1 = nome_completo_s + '' + str(numeros_concatenados) + ''.join(lista_letras)

                            user_completo = random.randint(1, len(user_completo1))
                            # Insira o ponto no índice aleatório
                            string_with_dot = user_completo1[:user_completo] + '_' + user_completo1[user_completo:]
                            user_completo = string_with_dot
                            print(user_completo)
                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: ' + user_completo)
                            window.Refresh()
                            d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').set_text(
                                user_completo)
                            time.sleep(1)
                            d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()
                            # Digitar senha e avançar
                            time.sleep(3)
                            d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').set_text(
                                senha)
                            d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]').click()
                            # Clicar em concluir cadastro
                            time.sleep(1)
                            d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]/android.view.View')
                            time.sleep(2)
                            d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]/android.view.View').click()
                            time.sleep(4)
                            feedback = d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.View')
                            if feedback.exists:
                                sms = True

                            d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
                            time.sleep(20)
                            d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]').click()

                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
                            window.Refresh()
                            # WebDriverWait(driver, 40).until(EC.visibility_of_element_located)(((By.XPATH,
                            #                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')
                            time.sleep(5)
                            verificar = d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')

                            conta_criada = d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')
                            conta_sms = d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.View[4]')
                            if verificar.exists:
                                try:
                                    d.xpath(
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[11]').click()
                                except:
                                    pass
                                seguido = False
                                conteudo = config['vpn']
                                window['output'].print(
                                    f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                    text_color=('lime'))
                                window.Refresh()
                                contagem += 1
                                window['criadas'].update(contagem)
                                window.Refresh()
                                now = datetime.now()
                                now_brasilia = tz.localize(now)
                                timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                                client = gspread.authorize(creds)

                                spreadsheet_id = config['spreadsheet']
                                sheet_name = 'contas'
                                # Insert user, password, and timestamp into first empty row
                                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                values = sheet.col_values(1)
                                last_row = len(values)
                                values = [user_completo + ' ' + senha, email, timestamp, maquina,
                                          conteudo + ' - ' + app]
                                cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                for i, val in enumerate(values):
                                    cell_list[i].value = val
                                sheet.update_cells(cell_list)

                                rows = sheet.get_all_values()

                                # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                                regex = re.compile(r'\S+\s\S+')

                                # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                                num_rows = sum(1 for row in rows if regex.match(row[0]))
                                window['total'].update(num_rows)

                                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                                client = gspread.authorize(creds)

                                spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                                sheet_name = 'relatorio_geral'
                                # Insert user, password, and timestamp into first empty row
                                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                values = sheet.col_values(1)
                                last_row = len(values)
                                values = [user_completo + ' ' + senha, email, timestamp, maquina,
                                          conteudo + ' - ' + app]
                                cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                for i, val in enumerate(values):
                                    cell_list[i].value = val
                                sheet.update_cells(cell_list)

                                window.Refresh()
                                arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                                # Escreva mais conteúdo no arquivo
                                arquivo.write(user_completo + ' ' + senha + "\n")
                                arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                                # Escreva mais conteúdo no arquivo
                                arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                                d.xpath(
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]').click()
                                window.Refresh()
                                sms = False

                            else:
                                try:
                                    conteudo = config['vpn']
                                    if conteudo == "AVG":
                                        vpn_avg()
                                    elif conteudo == "SurfShark":
                                        vpn_surf()
                                    elif conteudo == "Avast":
                                        vpn_avast()
                                    elif conteudo == "ExpressVPN":
                                        vpn_express()
                                    elif conteudo == "PiaVPN":
                                        vpn_pia()
                                    elif conteudo == "Nenhuma":
                                        nenhuma_vpn()
                                    elif conteudo == "BetterNet":
                                        vpn_better()
                                    elif conteudo == "CyberGhost":
                                        vpn_cyberghost()
                                    elif conteudo == "NordVPN":
                                        vpn_nord()
                                    elif conteudo == "HotspotShield":
                                        vpn_hotspotshield()
                                        break
                                    else:
                                        window['output'].print(
                                            "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                        window.Refresh()

                                except:
                                    sms = True
                        except Exception as e:
                            print(e)
                            sms = True
                            continue


            except Exception as e:
                print(e)
                print('______________________________________________________')
                continue

        except Exception as e:
            print(e)
            window['output'].print(e)
            window.Refresh()
            print('______________________________________________________')
            continue


def executar_2nr_insta():
    SPREADSHEET_ID = config['spreadsheet']
    conteudo = config['vpn']
    senha = config['senha']
    maquina = config['maquina']
    tentativa = False
    seguido = False
    if config['email'] == '-2nr-' and config['app'] == '-instalite-':
        app = 'Lite'
    elif config['email'] == '-2nr-' and config['app'] == '-insta-':
        app = 'Normal'
    global sms
    global nomes
    global sobrenomes
    global nome
    global contagem
    global sobrenome
    global lista_user
    window['Executar'].update(disabled=True)
    window.Refresh()
    # Código que gera a saída
    import os
    import time
    import requests
    import hashlib
    import subprocess

    # verifica se o arquivo existe na pasta do bot

    try:
        from rich.console import Console
    except ModuleNotFoundError:
        import subprocess
        import sys

        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instalando dependências...')
        window.Refresh()
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
        subprocess.run(['deactivate'], shell=True)
        from rich.console import Console
    import os
    import time
    try:
        import uiautomator2 as u2
    except:
        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        subprocess.run(['pip', 'install', 'uiautomator2'])
        subprocess.run(['deactivate'], shell=True)
        subprocess.run(['pip', 'install', '--upgrade', 'requests'])
        import requests
        time.sleep(10)
        import uiautomator2 as u2
    d = u2.connect(f'127.0.0.1:{porta}')
    import requests
    import hashlib
    import subprocess
    from colorama import init, Fore, Back, Style
    from faker import Faker
    # teste
    init(autoreset=True)
    console = Console()
    from termcolor import colored

    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.rule import Rule

    linha_ret = '_________________________________________________\n'
    window.Refresh()
    import random
    from datetime import datetime
    import string
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.common.exceptions import NoSuchElementException
    from mailtm import Email
    import re
    import logging

    logger = logging.getLogger(__name__)

    handler = logging.FileHandler('log.txt')
    handler.setLevel(logging.ERROR)

    logger.addHandler(handler)

    # RANGE_NAME = 'contas!A:D'
    #
    # SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    def vpn_avast():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da Avast', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop("com.avast.android.vpn")
            d.app_start("com.avast.android.vpn", ".app.wizard.WizardActivity")
            time.sleep(10)
        except Exception as e:
            print(e)
        abc = False

    def nenhuma_vpn():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.facebook.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        time.sleep(10)

    def vpn_hotspotshield():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da HotspotShield',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('hotspotshield.android.vpn')
            d.app_start('hotspotshield.android.vpn')
        except Exception as e:
            print(e)
        d(resourceId='hotspotshield.android.vpn:id/tryAgainButton').click()
        time.sleep(5)
        d(resourceId='hotspotshield.android.vpn:id/btnVpnConnect').click()

        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_pia():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da PiaVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.privateinternetaccess.android')
            d.app_start('com.privateinternetaccess.android')
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        d(resourceId='com.privateinternetaccess.android:id/connection_background').click()
        time.sleep(3)
        d(resourceId='com.privateinternetaccess.android:id/connection_background').click()

        abc = False

    def vpn_express():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da ExpressVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.expressvpn.vpn')
            d.app_start('com.expressvpn.vpn')
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        d(resourceId='com.expressvpn.vpn:id/obiButton').click()
        time.sleep(3)
        d(resourceId='com.expressvpn.vpn:id/obiButton').click()

        abc = False

    def vpn_nord():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da NordVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.nordvpn.android')
            time.sleep(5)
            d.app_start('com.nordvpn.android', use_monkey=True)
        except:
            pass
        time.sleep(10)
        time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_surf():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da SurfShark', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            d.app_stop('com.surfshark.vpnclient.android')
            d.app_start('com.surfshark.vpnclient.android')
        except:
            pass
        time.sleep(15)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_better():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da BetterNet', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        try:
            d.app_stop('com.freevpnintouch')
            d.app_start('com.freevpnintouch')
        except:
            pass
        time.sleep(10)
        dialog = d(resourceId='com.freevpnintouch:id/dialogCtaPositive')
        connect = d(resourceId='com.freevpnintouch:id/buttonConnect').get_text(timeout=80)
        if dialog.exists:
            d(resourceId='com.freevpnintouch:id/dialogCtaPositive').click()
            time.sleep(3)
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
            # time.sleep(5)
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
        while connect == 'CONNECT':
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
            time.sleep(4)
            connect = d(resourceId='com.freevpnintouch:id/buttonConnect').get_text(timeout=80)
            # WebDriverWait(driver, 20).until(
            # EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect').click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        ip = '127.0.0.1:' + porta

        output = subprocess.check_output(['adb', '-s', ip, 'shell', 'ifconfig'])

        # Verifica se a conexão VPN está ativa
        if not re.search(b"tun0", output):
            window['output'].print("Não conectado na BetterNet.")
            window.Refresh()
            try:
                connect = d(resourceId='com.freevpnintouch:id/buttonConnect').get_text(timeout=80)
                d.app_stop('com.freevpnintouch')
                d.app_start('com.freevpnintouch')
                while connect == 'CONNECT':
                    d(resourceId='com.freevpnintouch:id/buttonConnect').click()
                    time.sleep(4)
                    connect = d(resourceId='com.freevpnintouch:id/buttonConnect').get_text(timeout=80)
            except:
                pass
        abc = False

    def vpn_cyberghost():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da CyberGhost', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            d.app_stop('de.mobileconcepts.cyberghost')
            d.app_start('de.mobileconcepts.cyberghost')
        except:
            pass
        # time.sleep(3)
        d(resourceId='de.mobileconcepts.cyberghost:id/button').click()
        rate = d(resourceId='de.mobileconcepts.cyberghost:id/rate_me_text')
        if rate.exists:
            d(resourceId='android:id/button2').click()
        time.sleep(2)
        d(resourceId='de.mobileconcepts.cyberghost:id/button').click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        abc = False

    def vpn_avg():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da AVG', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.avg.android.vpn')
            d.app_start("com.avg.android.vpn", "com.avast.android.vpn.app.wizard.WizardActivity")
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #               stderr=subprocess.DEVNULL, check=True, shell=True)

        time.sleep(30)

    def vpn_windscribe():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da Windscribe', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)
            d.app_stop("com.windscribe.vpn")
            d.app_start("com.windscribe.vpn")
        except:
            pass
        d(resourceId='com.windscribe.vpn:id/on_off_button').click()
        time.sleep(10)

    def vpn_hma():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da HMA', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)

            d.app_stop("com.hidemyass.hidemyassprovpn")
            time.sleep(3)
            d.app_start('com.hidemyass.hidemyassprovpn', 'com.avast.android.vpn.activity.HmaOnboardingActivity')
        except:
            pass
        time.sleep(10)

    def gerar_id():
        chars = string.ascii_lowercase + string.digits
        android_id = ''.join(random.choice(chars) for i in range(16))
        return android_id

    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.page_load_strategy = 'none'
    options.add_experimental_option("prefs", prefs)

    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Senha sendo utilizada: {senha}')
    window.Refresh()

    try:
        comando = f"adb connect 127.0.0.1:{porta}"
        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global window_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global transition_animation_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global animator_duration_scale 0',
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
    except:
        pass
    gerar_id()
    android_id = gerar_id()
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    time.sleep(2)
    # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True, stdout=subprocess.DEVNULL,
    #               stderr=subprocess.DEVNULL)

    try:
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
    except Exception as e:
        pass

    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Efetuando troca de IP.')
    window.Refresh()
    try:
        conteudo = config['vpn']
        if conteudo == "AVG":
            vpn_avg()
        elif conteudo == "SurfShark":
            vpn_surf()
        elif conteudo == "Nenhuma":
            nenhuma_vpn()
        elif conteudo == "Avast":
            vpn_avast()
        elif conteudo == "ExpressVPN":
            vpn_express()
        elif conteudo == "PiaVPN":
            vpn_pia()
        elif conteudo == "BetterNet":
            vpn_better()
        elif conteudo == "CyberGhost":
            vpn_cyberghost()
        elif conteudo == "NordVPN":
            vpn_nord()
        elif conteudo == "HotspotShield":
            vpn_hotspotshield()
        elif conteudo == "WindscribeVPN":
            vpn_windscribe()
        elif conteudo == "HmaVPN":
            vpn_hma()
        else:
            window['output'].print(
                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
            window.Refresh()

    except Exception as e:
        print(e)
        pass

    window.Refresh()
    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando sistema inicializar.')
    window.Refresh()

    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Iniciando criação.\n')
    window.Refresh()
    d.implicitly_wait(30.0)
    d.set_fastinput_ime(True)
    while parar is False:
        if parar is True:
            print('Parando Thread')
            break
        try:
            try:
                subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, check=True, shell=True)


            except:
                pass
            gerar_id()
            android_id = gerar_id()
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
            window['output'].print(linha_ret)
            window.Refresh()
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Abrindo 2NR')
            window.Refresh()
            try:
                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                client = gspread.authorize(creds)
#
                spreadsheet_id = config['spreadsheet']
                sheet_name = 'contas'
                # Insert user, password, and timestamp into first empty row
                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                values = sheet.col_values(1)
#
                # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                rows = sheet.get_all_values()
#
                # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                regex = re.compile(r'\S+\s\S+')
#
                # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                num_rows = sum(1 for row in rows if regex.match(row[0]))
                window['total'].update(num_rows)
            except Exception as e:
                print(e)
                window['output'].print(
                    f'[{datetime.now().strftime("%H:%M:%S")}] Ocorreu algum erro ao acessar a planilha.')
                window.Refresh()
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Tentando novamente em 1 minuto.')
                window.Refresh()
                time.sleep(60)
                raise Exception('skip')

            try:
                subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, check=True, shell=True)


            except Expception as e:
                print(e)
                pass
            try:
                subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, check=True, shell=True)
            except Exception as e:
                print(e)
                pass
            try:
                subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server.test',
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} clear io.appium.uiautomator2.server',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, shell=True)
            except:
                pass
            window.Refresh()

            try:
                # time.sleep(10)

                gerar_id()
                android_id = gerar_id()
                subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
                               shell=True)
                try:
                    subprocess.run(
                        f'adb -s 127.0.0.1:{porta} shell pm grant pl.rs.sip.softphone.newapp android.permission.READ_CONTACTS',
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                    subprocess.run(
                        f'adb -s 127.0.0.1:{porta} shell pm grant pl.rs.sip.softphone.newapp android.permission.CAMERA',
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                    subprocess.run(
                        f'adb -s 127.0.0.1:{porta} shell pm grant pl.rs.sip.softphone.newapp android.permission.RECORD_AUDIO',
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                    try:
                        subprocess.run(
                            f'adb -s {porta} shell pm grant pl.rs.sip.softphone.newapp android.permission.ACCESS_NOTIFICATION_POLICY',
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                    except:
                        pass

                    subprocess.run(
                        f'adb -s {porta} shell pm grant pl.rs.sip.softphone.newapp android.permission.POST_NOTIFICATIONS',
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                except:
                    pass
                try:
                    d.app_start('pl.rs.sip.softphone.newapp')
                except:
                    window['output'].print(
                        f'[{datetime.now().strftime("%H:%M:%S")}] Ocorreu algum erro ao abrir o 2NR, tentando novamente.')
                    window.Refresh()
                time.sleep(3)
                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                client = gspread.authorize(creds)

                spreadsheet_id = config['spreadsheet']
                sheet_name = config['2nr']

                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                # Obtém todas as células
                cells = sheet.get_all_values()

                # Armazena as células que correspondem à condição
                matches = [cell for row in cells for cell in row if
                           re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', cell)]

                # Armazena a lista de células correspondentes à condição em uma variável
                regex2nr = matches
                while len(regex2nr) == 0:
                    window['output'].print(
                        f'[{datetime.now().strftime("%H:%M:%S")}] Nenhuma conta do 2NR encontrada.\nTentando novamente em 5 min.')
                    window.Refresh()
                    cope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                    client = gspread.authorize(creds)

                    spreadsheet_id = config['spreadsheet']

                    sheet_name = config['2nr']
                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                    # Insert user, password, and timestamp into first empty row
                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                    values = sheet.col_values(1)

                    # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                    rows = sheet.get_all_values()

                    # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                    regex = re.compile(r'\S+\s\S+')
                    sheet_name = config['2nr']
                    # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                    num_rows = sum(1 for row in rows if regex.match(row[0]))
                    window['total'].update(num_rows)

                    time.sleep(300)
                    cells = sheet.get_all_values()

                    # Armazena as células que correspondem à condição
                    matches = [cell for row in cells for cell in row if
                               re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', cell)]

                    # Armazena a lista de células correspondentes à condição em uma variável
                    regex2nr = matches
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] {len(regex2nr)} conta(s) encontrada.')
                window.Refresh()
                time.sleep(3)
                try:
                    d(resourceId='pl.rs.sip.softphone.newapp:id/loginButton').click(timeout=60)
                except:
                    window['output'].print(
                        f'[{datetime.now().strftime("%H:%M:%S")}] Ocorreu um erro ao clicar em login. Tentando novamente.')
                    window.Refresh()
                    subprocess.run(
                        f'uiautomator2 -s 127.0.0.1:{porta} uninstall com.github.uiautomator',
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                    raise Exception('Ocorreu um erro ao clicar em login.')
                time.sleep(5)
                spreadsheet_id = config['spreadsheet']
                sheet_name = config['2nr']
                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                # Obtém todas as células

                # Define a faixa de células para leitura
                first_linha = sheet.cell(1, 1).value

                # Divide a string em duas partes separadas por um espaço em branco
                partes = first_linha.split(' ')

                # Atribui a primeira parte (endereço de e-mail) à variável email2nr
                email2nr = partes[0]

                # Atribui a segunda parte (texto) à variável senha2nr
                senha2nr = partes[1]
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Email 2NR: {email2nr}')
                window.Refresh()
                d(resourceId='pl.rs.sip.softphone.newapp:id/emailEdiText').set_text(email2nr)
                time.sleep(0.5)
                d(resourceId='pl.rs.sip.softphone.newapp:id/passwordEdiText').set_text(senha2nr)
                time.sleep(0.5)
                d(resourceId='pl.rs.sip.softphone.newapp:id/buttonLogin').click()
                time.sleep(3)
                perm = d(resourceId='pl.rs.sip.softphone.newapp:id/messages')
                if perm.exists(timeout=30):
                    time.sleep(10)
                    pass
                else:
                    try:
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta não existe.')
                        window.Refresh()
                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                        client = gspread.authorize(creds)
                        # Abre a planilha e a planilha de uma determinada aba
                        spreadsheet_id = config['spreadsheet']
                        sheet_name = config['2nr']
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)

                        # Apaga a primeira célula da coluna A e desloca as células abaixo
                        sheet.delete_rows(1, 1)
                        conteudo = config['vpn']
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "Nenhuma":
                            nenhuma_vpn()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                        elif conteudo == "WindscribeVPN":
                            vpn_windscribe()
                        elif conteudo == "HmaVPN":
                            vpn_hma()
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()
                        raise Exception('skip')
                    except Exception as e:
                        print(e)
                    raise Exception('Erro.')
                try:
                    qtd_num2 = d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[*]/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.TextView[1]')
                    qtd_num = qtd_num2.all()
                    window['output'].print(
                        f'[{datetime.now().strftime("%H:%M:%S")}] {len(qtd_num)} número(s) encontrado.')
                except Exception as e:
                    print(e)
                if len(qtd_num) == 0:
                    try:
                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                        client = gspread.authorize(creds)
                        # Abre a planilha e a planilha de uma determinada aba
                        spreadsheet_id = config['spreadsheet']
                        sheet_name = config['2nr']
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)

                        # Apaga a primeira célula da coluna A e desloca as células abaixo
                        sheet.delete_rows(1, 1)
                    except Exception as e:
                        print(e)
                    continue
                window.Refresh()
                try:
                    num = d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.TextView[1]').get_text()
                    num = num.replace(' ', '')
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Número: +48{num}')
                    window.Refresh()
                    email = num
                except Exception as e:
                    print(e)
                d(resourceId='pl.rs.sip.softphone.newapp:id/messages').click()
                d(resourceId='pl.rs.sip.softphone.newapp:id/buttonSettings').click()
                d(resourceId='pl.rs.sip.softphone.newapp:id/buttonDelete').click()
                d(resourceId='pl.rs.sip.softphone.newapp:id/numbers').click()

                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Abrindo instagram.')
                window.Refresh()
                d.app_start('com.instagram.android')
                try:
                    d.xpath('//android.widget.Button[@content-desc="Criar nova conta"]').click(timeout=120)
                except:
                    conteudo = config['vpn']
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Pagina Estática.')
                    window.Refresh()
                    if conteudo == "AVG":
                        vpn_avg()
                    elif conteudo == "SurfShark":
                        vpn_surf()
                    elif conteudo == "Nenhuma":
                        nenhuma_vpn()
                    elif conteudo == "Avast":
                        vpn_avast()
                    elif conteudo == "ExpressVPN":
                        vpn_express()
                    elif conteudo == "PiaVPN":
                        vpn_pia()
                    elif conteudo == "BetterNet":
                        vpn_better()
                    elif conteudo == "CyberGhost":
                        vpn_cyberghost()
                    elif conteudo == "NordVPN":
                        vpn_nord()
                    elif conteudo == "HotspotShield":
                        vpn_hotspotshield()
                    elif conteudo == "WindscribeVPN":
                        vpn_windscribe()
                    elif conteudo == "HmaVPN":
                        vpn_hma()
                    else:
                        window['output'].print(
                            "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                        window.Refresh()
                    raise Exception('skip')
                # time.sleep(6)
                # novo_layout = d.xpath('//android.view.View[@content-desc="Qual é o seu nome?"]')
                # if len(novo_layout) == 1:
                #    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Layout novo encontrado, reiniciando app.')
                #    window.Refresh()
                #    raise Exception("skip.")

                ######################################################################
                lista_user = random.choices(range(0, 9), k=2)
                lista_letras = random.choices(letras, k=1)

                with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                    nomes = nomes_arquivo.readlines()

                with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                    sobrenomes = sobrenomes_arquivo.readlines()

                nomea = fake.first_name_female().replace(" ", "")
                nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                sobrenomea = fake.last_name().replace(" ", "").lower()
                sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                nome_completo = nome + ' ' + sobrenome
                nome_completo_s = nome + sobrenome
                numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                user_completo1 = nome_completo_s + '' + str(numeros_concatenados) + ''.join(lista_letras)

                user_completo = random.randint(1, len(user_completo1))
                # Insira o ponto no índice aleatório
                string_with_dot = user_completo1[:user_completo] + '_' + user_completo1[user_completo:]
                user_completo = string_with_dot.lower()
                ######################################################################

                cancel = d(resourceId='com.google.android.gms:id/cancel')
                if cancel.exists(timeout=10):
                    d(resourceId='com.google.android.gms:id/cancel').click()
                senha = config['senha']
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText').set_text(
                    nome_completo)
                time.sleep(1)
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Nome escolhido: {nome_completo}')
                window.Refresh()
                d.xpath('//android.view.View[@content-desc="Avançar"]').click()
                time.sleep(4)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText').set_text(
                    senha)
                time.sleep(1)
                d.xpath('//android.view.View[@content-desc="Avançar"]').click()
                new_acc = d(resourceId='android:id/button2')
                if new_acc.exists:
                    d(resourceId='android:id/button2').click()
                time.sleep(2)
                try:
                    d.xpath('//android.view.View[@content-desc="Agora não"]').click_exists(timeout=20.0)
                except Exception as e:
                    print(e)
                #salvar_senha = d.xpath('//android.view.View[@content-desc="Agora não"]')
                #if salvar_senha.exists:
                #    d.xpath('//android.view.View[@content-desc="Agora não"]').click()

                time.sleep(3)
                new_acc = d(resourceId='android:id/button2')
                if new_acc.exists(timeout=20):
                    d(resourceId='android:id/button2').click()
                    time.sleep(2)
                d.xpath('//android.view.View[@content-desc="Avançar"]').click()
                time.sleep(2)
                d.xpath('//android.view.View[@content-desc="Avançar"]').click()
                idade_aleatoria = random.randint(18, 35)
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Idade escolhida: {idade_aleatoria}')
                window.Refresh()
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText').set_text(
                    str(idade_aleatoria))
                d.xpath('//android.view.View[@content-desc="Avançar"]').click()
                time.sleep(2)
                new_acc = d(resourceId='android:id/button2')
                if new_acc.exists(timeout=10):
                    d(resourceId='android:id/button2').click()
                    time.sleep(2)
                try:
                    d.xpath('//android.view.View[@content-desc="Alterar nome de usuário"]').click(timeout=5)
                except:
                    pass
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: {user_completo}')
                window.Refresh()
                time.sleep(3)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText').set_text(
                    '')
                time.sleep(1)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText').set_text(
                    user_completo)
                time.sleep(3)
                d.xpath('//android.view.View[@content-desc="Avançar"]').click()
                time.sleep(3)
                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText').set_text(
                    f'+48{num}')
                time.sleep(1)
                d.xpath('//android.view.View[@content-desc="Avançar"]').click()
                new_acc = d(resourceId='android:id/button2')
                if new_acc.exists(timeout=10):
                    d(resourceId='android:id/button2').click()
                    time.sleep(2)
                restricao = d.xpath('//android.view.View[@content-desc="Cadastrar-se com o email"]')
                if restricao.exists and tentativa is True:
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Restrição.')
                    window.Refresh()
                    window['output'].print(
                        f'[{datetime.now().strftime("%H:%M:%S")}] Já foi feita uma tentativa. Apagando número.')
                    window.Refresh()
                    tentativa = False

                    d.app_start('pl.rs.sip.softphone.newapp')
                    time.sleep(4)
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/androidx.appcompat.widget.LinearLayoutCompat').click()
                    d(resourceId='pl.rs.sip.softphone.newapp:id/buttonDelete').click()
                    d(resourceId='pl.rs.sip.softphone.newapp:id/buttonAgree').click()
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Número excluído.')
                    window.Refresh()
                    try:
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True, shell=True)


                    except:
                        pass
                    try:
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True, shell=True)
                    except:
                        pass

                    conteudo = config['vpn']
                    if conteudo == "AVG":
                        vpn_avg()
                    elif conteudo == "SurfShark":
                        vpn_surf()
                    elif conteudo == "Nenhuma":
                        nenhuma_vpn()
                    elif conteudo == "Avast":
                        vpn_avast()
                    elif conteudo == "ExpressVPN":
                        vpn_express()
                    elif conteudo == "PiaVPN":
                        vpn_pia()
                    elif conteudo == "BetterNet":
                        vpn_better()
                    elif conteudo == "CyberGhost":
                        vpn_cyberghost()
                    elif conteudo == "NordVPN":
                        vpn_nord()
                    elif conteudo == "HotspotShield":
                        vpn_hotspotshield()
                    elif conteudo == "WindscribeVPN":
                        vpn_windscribe()
                    elif conteudo == "HmaVPN":
                        vpn_hma()
                    else:
                        window['output'].print(
                            "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                        window.Refresh()
                    raise Exception('skip')

                elif restricao.exists and tentativa is False:
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Restrição.')
                    window.Refresh()
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Tentando mais uma vez.')
                    window.Refresh()
                    tentativa = True
                    try:
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True, shell=True)


                    except:
                        pass
                    try:
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True, shell=True)
                    except:
                        pass
                    try:
                        conteudo = config['vpn']
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "Nenhuma":
                            nenhuma_vpn()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                        elif conteudo == "WindscribeVPN":
                            vpn_windscribe()
                        elif conteudo == "HmaVPN":
                            vpn_hma()
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()
                        raise Exception('skip')
                    except:
                        raise Exception('skip')

                d.app_start('pl.rs.sip.softphone.newapp')
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando código...')
                window.Refresh()

                time.sleep(20)
                d(resourceId='pl.rs.sip.softphone.newapp:id/messages').click()
                window.Refresh()
                try:
                    cod = d(resourceId='pl.rs.sip.softphone.newapp:id/message').get_text(timeout=80)

                except:
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Código não recebido.')
                    window.Refresh()
                    d.app_start('pl.rs.sip.softphone.newapp')
                    time.sleep(4)
                    d(resourceId='pl.rs.sip.softphone.newapp:id/numbers').click()
                    time.sleep(1)
                    d.xpath(
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/androidx.appcompat.widget.LinearLayoutCompat').click()
                    d(resourceId='pl.rs.sip.softphone.newapp:id/buttonDelete').click()
                    d(resourceId='pl.rs.sip.softphone.newapp:id/buttonAgree').click()
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Número excluído.')
                    window.Refresh()
                    try:
                        conteudo = config['vpn']
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "Nenhuma":
                            nenhuma_vpn()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                        elif conteudo == "WindscribeVPN":
                            vpn_windscribe()
                        elif conteudo == "HmaVPN":
                            vpn_hma()
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()
                        continue
                    except:
                        pass
                codigo = re.sub('[^0-9]', '', cod)[:6]
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Codigo recebido: {codigo}')
                window.Refresh()
                d.app_start('com.instagram.android')
                time.sleep(1)

                d.xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText').set_text(
                    codigo)
                # time.sleep(100)
                d.xpath('//android.view.View[@content-desc="Avançar"]').click()
                time.sleep(4)

                codigo_invalido = d.xpath('//android.view.View[@content-desc="Não recebi o código"]')
                d.xpath('//android.view.View[@content-desc="Concordo"]').click()
                time.sleep(3)
                errodetec = d.xpath('//android.view.View[@content-desc="Concordo"]')
                if errodetec.exists:
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instagram não deixou avançar.')
                    window.Refresh()

                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
                window.Refresh()
                time.sleep(30)
                verificar = d.xpath('//android.view.View[@content-desc="Adicionar foto"]')
                # time.sleep(10)
                try:
                    if verificar.exists:
                        try:
                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                                   text_color=('lime'))
                            window.Refresh()
                            seguido = False
                            contagem += 1
                            window['criadas'].update(contagem)
                            window.Refresh()
                            now = datetime.now()
                            now_brasilia = tz.localize(now)
                            timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")
                            try:
                                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                                client = gspread.authorize(creds)

                                spreadsheet_id = config['spreadsheet']
                                sheet_name = 'contas'
                                # Insert user, password, and timestamp into first empty row
                                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                values = sheet.col_values(1)
                                last_row = len(values)
                                values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo + ' - ' + app]
                                cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                for i, val in enumerate(values):
                                    cell_list[i].value = val
                                sheet.update_cells(cell_list)

                                rows = sheet.get_all_values()

                                # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                                regex = re.compile(r'\S+\s\S+')

                                # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                                num_rows = sum(1 for row in rows if regex.match(row[0]))
                            except Exception as e:
                                print(e)
                                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Ocorreu um erro ao salvar a conta na planilha.')
                                tempo_aleatorio = random.randint(10, 40)
                                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando {tempo_aleatorio} segundos para tentar novamente.')
                                time.sleep(tempo_aleatorio)
                                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                                client = gspread.authorize(creds)

                                spreadsheet_id = config['spreadsheet']
                                sheet_name = 'contas'
                                # Insert user, password, and timestamp into first empty row
                                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                values = sheet.col_values(1)
                                last_row = len(values)
                                values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo + ' - ' + app]
                                cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                for i, val in enumerate(values):
                                    cell_list[i].value = val
                                sheet.update_cells(cell_list)

                                rows = sheet.get_all_values()

                                # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                                regex = re.compile(r'\S+\s\S+')

                                # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                                num_rows = sum(1 for row in rows if regex.match(row[0]))
                            window['total'].update(num_rows)
                            random_number = random.random()

                            # Definir a chance desejada (10%)
                            chance = 0.3

                            # Verificar se o número aleatório está abaixo da chance
                            if random_number < chance and not os.path.exists("wn"):
                                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                                client = gspread.authorize(creds)

                                spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                                sheet_name = 'relatorio_geral'
                                # Insert user, password, and timestamp into first empty row
                                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                values = sheet.col_values(1)
                                last_row = len(values)
                                values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo + ' - ' + app]
                                cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                for i, val in enumerate(values):
                                    cell_list[i].value = val
                                sheet.update_cells(cell_list)
                        except Exception as e:
                            print(e)
                            pass
                        window.Refresh()
                        arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                        # Escreva mais conteúdo no arquivo
                        arquivo.write(user_completo + ' ' + senha + "\n")
                        arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                        # Escreva mais conteúdo no arquivo
                        arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                        try:
                            d.xpath('//android.view.View[@content-desc="Pular"]').click()
                            time.sleep(2)
                            d(resourceId='com.instagram.android:id/skip_button').click()
                            time.sleep(2)
                            d(resourceId='com.instagram.android:id/negative_button').click()
                            time.sleep(2)
                            d(resourceId='com.instagram.android:id/skip_button').click()
                            time.sleep(4)
                            try:
                                element_id = "com.instagram.android:id/row_recommended_user_follow_button"
                                target_text = "Seguir"

                                # Encontre todos os elementos que correspondem ao ID fornecido
                                elements = d(resourceId=element_id)
                                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Seguindo sugeridos...')
                                window.Refresh()
                                time.sleep(5)
                                for element in elements:
                                    if element.get_text() == target_text:
                                        element.click()
                                        time.sleep(1)
                                d.xpath(
                                    '//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView').click()
                            except Exception as e:
                                print(e)
                                time.sleep(2)
                                element_id = "com.instagram.android:id/row_recommended_user_follow_button"
                                target_text = "Seguir"

                                # Encontre todos os elementos que correspondem ao ID fornecido
                                elements = d(resourceId=element_id)
                                window['output'].print("Seguindo sugeridos...")
                                window.Refresh()
                                for element in elements:
                                    if element.get_text() == target_text:
                                        element.click()
                                        time.sleep(1)
                                d.xpath(
                                    '//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView').click()
                            time.sleep(1)
                            try:
                                d(resourceId='com.instagram.android:id/button_text').click()
                            except:
                                pass
                            time.sleep(3)
                            try:
                                d(resourceId='com.instagram.android:id/profile_tab').click()
                            except:
                                time.sleep(2)
                                d(resourceId='com.instagram.android:id/tab_avatar').click()
                            sms = False
                        except Exception as e:
                            print(e)
                            pass
                    else:
                        verificar = d(resourceId='com.instagram.android:id/profile_tab')
                        if verificar.exists:
                            try:
                                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                                    text_color=('lime'))
                                window.Refresh()
                                seguido = False
                                contagem += 1
                                window['criadas'].update(contagem)
                                window.Refresh()
                                now = datetime.now()
                                now_brasilia = tz.localize(now)
                                timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")
                                try:
                                    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                                    client = gspread.authorize(creds)

                                    spreadsheet_id = config['spreadsheet']
                                    sheet_name = 'contas'
                                    # Insert user, password, and timestamp into first empty row
                                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                    values = sheet.col_values(1)
                                    last_row = len(values)
                                    values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo + ' - ' + app]
                                    cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                    for i, val in enumerate(values):
                                        cell_list[i].value = val
                                    sheet.update_cells(cell_list)

                                    rows = sheet.get_all_values()

                                    # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                                    regex = re.compile(r'\S+\s\S+')

                                    # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                                    num_rows = sum(1 for row in rows if regex.match(row[0]))
                                except Exception as e:
                                    print(e)
                                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Ocorreu um erro ao salvar a conta na planilha.')
                                    tempo_aleatorio = random.randint(10, 40)
                                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando {tempo_aleatorio} segundos para tentar novamente.')
                                    time.sleep(tempo_aleatorio)
                                    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                                    client = gspread.authorize(creds)

                                    spreadsheet_id = config['spreadsheet']
                                    sheet_name = 'contas'
                                    # Insert user, password, and timestamp into first empty row
                                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                    values = sheet.col_values(1)
                                    last_row = len(values)
                                    values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo + ' - ' + app]
                                    cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                    for i, val in enumerate(values):
                                        cell_list[i].value = val
                                    sheet.update_cells(cell_list)

                                    rows = sheet.get_all_values()

                                    # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                                    regex = re.compile(r'\S+\s\S+')

                                    # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                                    num_rows = sum(1 for row in rows if regex.match(row[0]))
                                window['total'].update(num_rows)
                                random_number = random.random()

                                # Definir a chance desejada (10%)
                                chance = 0.3

                                # Verificar se o número aleatório está abaixo da chance
                                if random_number < chance and not os.path.exists("wn"):
                                    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                    creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                                    client = gspread.authorize(creds)

                                    spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                                    sheet_name = 'relatorio_geral'
                                    # Insert user, password, and timestamp into first empty row
                                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                    values = sheet.col_values(1)
                                    last_row = len(values)
                                    values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo + ' - ' + app]
                                    cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                    for i, val in enumerate(values):
                                        cell_list[i].value = val
                                    sheet.update_cells(cell_list)
                            except Exception as e:
                                print(e)
                                pass
                            window.Refresh()
                            arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                            # Escreva mais conteúdo no arquivo
                            arquivo.write(user_completo + ' ' + senha + "\n")
                            arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                            # Escreva mais conteúdo no arquivo
                            arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                            try:
                                d.xpath('//android.view.View[@content-desc="Pular"]').click()
                                time.sleep(2)
                                d(resourceId='com.instagram.android:id/skip_button').click()
                                time.sleep(2)
                                d(resourceId='com.instagram.android:id/negative_button').click()
                                time.sleep(2)
                                d(resourceId='com.instagram.android:id/skip_button').click()
                                time.sleep(4)
                                try:
                                    element_id = "com.instagram.android:id/row_recommended_user_follow_button"
                                    target_text = "Seguir"

                                    # Encontre todos os elementos que correspondem ao ID fornecido
                                    elements = d(resourceId=element_id)
                                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Seguindo sugeridos...')
                                    window.Refresh()
                                    time.sleep(5)
                                    for element in elements:
                                        if element.get_text() == target_text:
                                            element.click()
                                            time.sleep(1)
                                    d.xpath(
                                        '//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView').click()
                                except Exception as e:
                                    print(e)
                                    time.sleep(2)
                                    element_id = "com.instagram.android:id/row_recommended_user_follow_button"
                                    target_text = "Seguir"

                                    # Encontre todos os elementos que correspondem ao ID fornecido
                                    elements = d(resourceId=element_id)
                                    window['output'].print("Seguindo sugeridos...")
                                    window.Refresh()
                                    for element in elements:
                                        if element.get_text() == target_text:
                                            element.click()
                                            time.sleep(1)
                                    d.xpath(
                                        '//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView').click()
                                time.sleep(1)
                                try:
                                    d(resourceId='com.instagram.android:id/button_text').click()
                                except:
                                    pass
                                time.sleep(3)
                                try:
                                    d(resourceId='com.instagram.android:id/profile_tab').click()
                                except:
                                    time.sleep(2)
                                    d(resourceId='com.instagram.android:id/tab_avatar').click()
                                sms = False
                            except Exception as e:
                                print(e)
                                window['output'].print(
                                    f'[{datetime.now().strftime("%H:%M:%S")}] Reabrindo Instagram.')
                                window.Refresh()
                                d.app_stop('com.instagram.android')
                                d.app_start('com.instagram.android')
                                pass
                        else:
                            if seguido is True:
                                seguido = False
                                window['output'].print(
                                    f'[{datetime.now().strftime("%H:%M:%S")}] SMS seguidos, Trocando de número.')
                                window.Refresh()
                                d.app_start('pl.rs.sip.softphone.newapp')
                                time.sleep(4)
                                d(resourceId='pl.rs.sip.softphone.newapp:id/numbers').click()
                                d.xpath(
                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/androidx.appcompat.widget.LinearLayoutCompat').click()
                                d(resourceId='pl.rs.sip.softphone.newapp:id/buttonDelete').click()
                                d(resourceId='pl.rs.sip.softphone.newapp:id/buttonAgree').click()
                                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Número excluído.')
                                window.Refresh()
                                sms = True
                            elif seguido is False:
                                seguido = True
                            try:
                                conteudo = config['vpn']

                                # Executa a função correspondente ao conteúdo do arquivo
                                if conteudo == "AVG":
                                    vpn_avg()
                                elif conteudo == "SurfShark":
                                    vpn_surf()
                                elif conteudo == "Nenhuma":
                                    nenhuma_vpn()
                                elif conteudo == "Avast":
                                    vpn_avast()
                                elif conteudo == "ExpressVPN":
                                    vpn_express()
                                elif conteudo == "PiaVPN":
                                    vpn_pia()
                                elif conteudo == "BetterNet":
                                    vpn_better()
                                elif conteudo == "CyberGhost":
                                    vpn_cyberghost()
                                elif conteudo == "NordVPN":
                                    vpn_nord()
                                elif conteudo == "HotspotShield":
                                    vpn_hotspotshield()
                                elif conteudo == "WindscribeVPN":
                                    vpn_windscribe()
                                elif conteudo == "HmaVPN":
                                    vpn_hma()
                                else:
                                    window['output'].print(
                                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                    window.Refresh()
                            except:
                                sms = True
                                continue
                except Exception as e:
                    print(e)
                    if conteudo == "AVG":
                        vpn_avg()
                    elif conteudo == "SurfShark":
                        vpn_surf()
                    elif conteudo == "Nenhuma":
                        nenhuma_vpn()
                    elif conteudo == "Avast":
                        vpn_avast()
                    elif conteudo == "ExpressVPN":
                        vpn_express()
                    elif conteudo == "PiaVPN":
                        vpn_pia()
                    elif conteudo == "BetterNet":
                        vpn_better()
                    elif conteudo == "CyberGhost":
                        vpn_cyberghost()
                    elif conteudo == "NordVPN":
                        vpn_nord()
                    elif conteudo == "HotspotShield":
                        vpn_hotspotshield()
                    elif conteudo == "WindscribeVPN":
                        vpn_windscribe()
                    elif conteudo == "HmaVPN":
                        vpn_hma()
                    else:
                        window['output'].print(
                            "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                        window.Refresh()
                    sms = True
                while sms is False:
                    try:
                        time.sleep(3)
                        try:
                            d(resourceId='com.instagram.android:id/profile_tab').click(timeout=120)
                        except:
                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Ocorreu algum erro nesta conta.')
                            window.Refresh()
                            raise Exception('Erro na conta')
                        window['output'].print(linha_ret)
                        window.Refresh()
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Criação de outro perfil.')
                        window.Refresh()
                        seguido = False
                        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True)
                        # Clicar no botão de perfil

                        time.sleep(3)
                        d(resourceId='com.instagram.android:id/action_bar_title_chevron').click()
                        time.sleep(2)
                        # Clicar em perfis
                        try:
                            d.xpath(
                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[last()]/android.widget.FrameLayout/android.widget.ImageView').click()
                        except Exception as e:
                            print(e)
                            print('Erro aq')
                            time.sleep(200)
                        # Clicar em adicionar conta
                        d.xpath('//android.widget.Button[@content-desc="Criar nova conta"]').click()

                        time.sleep(3)
                        # Gerar nome de usuário, digitar no campo e clicar em avançae
                        lista_user = random.choices(range(0, 9), k=2)
                        lista_letras = random.choices(letras, k=1)

                        with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                            nomes = nomes_arquivo.readlines()

                        with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                            sobrenomes = sobrenomes_arquivo.readlines()

                        nomea = fake.first_name_female().replace(" ", "")
                        nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                        sobrenomea = fake.last_name().replace(" ", "").lower()
                        sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                        nome_completo = nome + sobrenome
                        numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                        user_completo1 = nome_completo + '' + str(numeros_concatenados) + ''.join(lista_letras)

                        user_completo = random.randint(1, len(user_completo1))
                        # Insira o ponto no índice aleatório
                        string_with_dot = user_completo1[:user_completo] + '_' + user_completo1[user_completo:]
                        user_completo = string_with_dot.lower()
                        print(user_completo)
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: ' + user_completo)
                        window.Refresh()
                        d(resourceId='com.instagram.android:id/username').set_text(
                            user_completo)
                        time.sleep(3)
                        d(resourceId='com.instagram.android:id/button_text').click()
                        # Digitar senha e avançar
                        time.sleep(3)
                        try:
                            d(resourceId='com.instagram.android:id/password').set_text(
                                senha)
                        except:
                            try:
                                conteudo = config['vpn']
                                if conteudo == "AVG":
                                    vpn_avg()
                                elif conteudo == "SurfShark":
                                    vpn_surf()
                                elif conteudo == "Nenhuma":
                                    nenhuma_vpn()
                                elif conteudo == "Avast":
                                    vpn_avast()
                                elif conteudo == "ExpressVPN":
                                    vpn_express()
                                elif conteudo == "PiaVPN":
                                    vpn_pia()
                                elif conteudo == "BetterNet":
                                    vpn_better()
                                elif conteudo == "CyberGhost":
                                    vpn_cyberghost()
                                elif conteudo == "NordVPN":
                                    vpn_nord()
                                elif conteudo == "HotspotShield":
                                    vpn_hotspotshield()
                                elif conteudo == "WindscribeVPN":
                                    vpn_windscribe()
                                elif conteudo == "HmaVPN":
                                    vpn_hma()
                                else:
                                    window['output'].print(
                                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                    window.Refresh()

                            except:
                                sms = True
                        d(resourceId='com.instagram.android:id/button_text').click()
                        # Clicar em concluir cadastro
                        time.sleep(3)
                        d(resourceId='com.instagram.android:id/button_text').click()

                        time.sleep(4)
                        feedback = d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.View')
                        if feedback.exists:
                            sms = True

                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
                        window.Refresh()
                        # WebDriverWait(driver, 40).until(EC.visibility_of_element_located)(((By.XPATH,
                        #                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')

                        verificar = d(resourceId='com.instagram.android:id/connect_text')
                        if verificar.exists(timeout=60):
                            time.sleep(20)
                            verificar = d(resourceId='com.instagram.android:id/connect_text')
                        if verificar.exists:
                            try:
                                conteudo = config['vpn']
                                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                                    text_color=('lime'))
                                window.Refresh()
                                contagem += 1
                                window['criadas'].update(contagem)
                                window.Refresh()
                                now = datetime.now()
                                now_brasilia = tz.localize(now)
                                timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                                try:
                                    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                                    client = gspread.authorize(creds)

                                    spreadsheet_id = config['spreadsheet']
                                    sheet_name = 'contas'
                                    # Insert user, password, and timestamp into first empty row
                                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                    values = sheet.col_values(1)
                                    last_row = len(values)
                                    values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo + ' - ' + app]
                                    cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                    for i, val in enumerate(values):
                                        cell_list[i].value = val
                                    sheet.update_cells(cell_list)

                                    rows = sheet.get_all_values()

                                    # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                                    regex = re.compile(r'\S+\s\S+')

                                    # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                                    num_rows = sum(1 for row in rows if regex.match(row[0]))
                                except Exception as e:
                                    print(e)
                                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Ocorreu um erro ao salvar a conta na planilha.')
                                    tempo_aleatorio = random.randint(10, 40)
                                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando {tempo_aleatorio} segundos para tentar novamente.')
                                    time.sleep(tempo_aleatorio)
                                    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                                    client = gspread.authorize(creds)

                                    spreadsheet_id = config['spreadsheet']
                                    sheet_name = 'contas'
                                    # Insert user, password, and timestamp into first empty row
                                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                    values = sheet.col_values(1)
                                    last_row = len(values)
                                    values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo + ' - ' + app]
                                    cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                    for i, val in enumerate(values):
                                        cell_list[i].value = val
                                    sheet.update_cells(cell_list)

                                    rows = sheet.get_all_values()

                                    # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                                    regex = re.compile(r'\S+\s\S+')

                                    # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                                    num_rows = sum(1 for row in rows if regex.match(row[0]))
                                    
                                window['total'].update(num_rows)
                                try:
                                    random_number = random.random()

                                    # Definir a chance desejada (10%)
                                    chance = 0.3

                                    # Verificar se o número aleatório está abaixo da chance
                                    if random_number < chance and not os.path.exists("wn"):
                                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                        creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                                        client = gspread.authorize(creds)

                                        spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                                        sheet_name = 'relatorio_geral'
                                        # Insert user, password, and timestamp into first empty row
                                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                        values = sheet.col_values(1)
                                        last_row = len(values)
                                        values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo + ' - ' + app]
                                        cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                        for i, val in enumerate(values):
                                            cell_list[i].value = val
                                        sheet.update_cells(cell_list)
                                except:
                                    pass

                                window.Refresh()
                                arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                                # Escreva mais conteúdo no arquivo
                                arquivo.write(user_completo + ' ' + senha + "\n")
                                arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                                # Escreva mais conteúdo no arquivo
                                arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                                window.Refresh()
                                d(resourceId='com.instagram.android:id/skip_button').click()
                                time.sleep(1)
                                d(resourceId='com.instagram.android:id/negative_button').click()
                                time.sleep(3)
                                d(resourceId='com.instagram.android:id/skip_button').click()
                                time.sleep(1)
                                try:
                                    element_id = "com.instagram.android:id/row_recommended_user_follow_button"
                                    target_text = "Seguir"

                                    # Encontre todos os elementos que correspondem ao ID fornecido
                                    elements = d(resourceId=element_id)
                                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Seguindo sugeridos...')
                                    window.Refresh()
                                    for element in elements:
                                        if element.get_text() == target_text:
                                            element.click()
                                            time.sleep(1)
                                    d.xpath(
                                        '//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView').click()
                                except Exception as e:
                                    print(e)
                                    d(resourceId='com.instagram.android:id/skip_button').click()
                                    element_id = "com.instagram.android:id/row_recommended_user_follow_button"
                                    target_text = "Seguir"

                                    # Encontre todos os elementos que correspondem ao ID fornecido
                                    elements = d(resourceId=element_id)
                                    window.Refresh()
                                    for element in elements:
                                        if element.text == target_text:
                                            element.click()
                                            time.sleep(1)
                                    d.xpath(
                                        '//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView').click()

                                time.sleep(1)
                                time.sleep(3)
                                try:
                                    d(resourceId='com.instagram.android:id/profile_tab').click()
                                except Exception as e:
                                    print(e)
                                    d(resourceId='com.instagram.android:id/button_text').click()
                                    d(resourceId='com.instagram.android:id/profile_tab').click()
                                sms = False
                            except Exception as e:
                                print(e)

                        else:
                            try:
                                conteudo = config['vpn']
                                if conteudo == "AVG":
                                    vpn_avg()
                                elif conteudo == "SurfShark":
                                    vpn_surf()
                                elif conteudo == "Nenhuma":
                                    nenhuma_vpn()
                                elif conteudo == "Avast":
                                    vpn_avast()
                                elif conteudo == "ExpressVPN":
                                    vpn_express()
                                elif conteudo == "PiaVPN":
                                    vpn_pia()
                                elif conteudo == "BetterNet":
                                    vpn_better()
                                elif conteudo == "CyberGhost":
                                    vpn_cyberghost()
                                elif conteudo == "NordVPN":
                                    vpn_nord()
                                elif conteudo == "HotspotShield":
                                    vpn_hotspotshield()
                                elif conteudo == "WindscribeVPN":
                                    vpn_windscribe()
                                elif conteudo == "HmaVPN":
                                    vpn_hma()
                                else:
                                    window['output'].print(
                                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                    window.Refresh()

                            except:
                                sms = True
                    except Exception as e:
                        print(e)
                        sms = True


            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
            pass


def insta_face_lite():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {}
    SPREADSHEET_ID = config['spreadsheet']
    conteudo = config['vpn']
    senha = config['senha']
    maquina = config['maquina']
    tentativa = False
    email = 'InstaFace'
    seguido = False
    app = 'Lite'
    global recebido
    global sms
    global nomes
    global sobrenomes
    global nome
    global contagem
    global sobrenome
    global lista_user
    window['Executar'].update(disabled=True)
    window.Refresh()
    # Código que gera a saída
    import os
    import time
    from datetime import datetime
    import requests
    import hashlib
    import subprocess

    # verifica se o arquivo existe na pasta do bo
    try:
        from py_random_useragent import UserAgent
    except:
        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instalando dependências...')
        window.Refresh()
        subprocess.run(['pip', 'install', 'py_random_useragent'])
        from py_random_useragent import UserAgent

    try:
        import uiautomator2 as u2
    except:
        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        subprocess.run(['pip', 'install', 'uiautomator2'])
        subprocess.run(['deactivate'], shell=True)
        subprocess.run(['pip', 'install', '--upgrade', 'requests'])
        import requests
        time.sleep(10)
        import uiautomator2 as u2

    try:

        import psutil
    except:
        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instalando dependências...')
        window.Refresh()
        subprocess.run(['pip', 'install', 'psutil'])
        import psutil
    try:
        from gologin import GoLogin
    except:
        pass
    import os
    import time
    import requests
    import hashlib
    import subprocess
    from colorama import init, Fore, Back, Style
    from faker import Faker
    # teste

    linha_ret = '_________________________________________________\n'
    window.Refresh()
    import random
    try:
        import undetected_chromedriver as uc
    except:
        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        subprocess.run(['pip', 'install', 'undetected_chromedriver'])
        subprocess.run(['deactivate'], shell=True)
        import undetected_chromedriver as uc
    try:
        import phonenumbers
    except:
        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        subprocess.run(['pip', 'install', 'phonenumbers'])
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instalando dependências...')
        window.Refresh()
        import phonenumbers
    import string

    from minuteinbox import Inbox
    try:
        from selenium_profiles.webdriver import Chrome
        from selenium_profiles.profiles import profiles
    except:
        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        subprocess.run(['pip', 'install', 'selenium-profiles'])
        subprocess.run(['deactivate'], shell=True)
        from selenium_profiles.webdriver import Chrome
        from selenium_profiles.profiles import profiles
    # import seleniumwire.undetected_chromedriver as uc
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver import ChromeOptions

    from selenium.webdriver.chrome.options import Options
    from selenium.common.exceptions import NoSuchElementException
    from mailtm import Email
    import re
    import logging
    from phonenumbers import PhoneNumberFormat, geocoder
    logger = logging.getLogger(__name__)

    handler = logging.FileHandler('log.txt')
    handler.setLevel(logging.ERROR)

    logger.addHandler(handler)

    def vpn_avast():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da Avast', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop("com.avast.android.vpn")
            d.app_start("com.avast.android.vpn", ".app.wizard.WizardActivity")
            time.sleep(10)
        except Exception as e:
            print(e)
        abc = False

    def nenhuma_vpn():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.facebook.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        time.sleep(10)

    def vpn_hotspotshield():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da HotspotShield',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('hotspotshield.android.vpn')
            d.app_start('hotspotshield.android.vpn')
        except Exception as e:
            print(e)
        d(resourceId='hotspotshield.android.vpn:id/tryAgainButton').click()
        time.sleep(5)
        d(resourceId='hotspotshield.android.vpn:id/btnVpnConnect').click()

        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_pia():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da PiaVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.privateinternetaccess.android')
            d.app_start('com.privateinternetaccess.android')
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        d(resourceId='com.privateinternetaccess.android:id/connection_background').click()
        time.sleep(3)
        d(resourceId='com.privateinternetaccess.android:id/connection_background').click()

        abc = False

    def vpn_express():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da ExpressVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.expressvpn.vpn')
            d.app_start('com.expressvpn.vpn')
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        d(resourceId='com.expressvpn.vpn:id/obiButton').click()
        time.sleep(3)
        d(resourceId='com.expressvpn.vpn:id/obiButton').click()

        abc = False

    def vpn_nord():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da NordVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        sms = True
        try:
            d.app_stop('com.nordvpn.android')
            d.app_start('com.nordvpn.android', '.MainActivity')

        except:
            pass
        time.sleep(10)
        time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_surf():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da SurfShark', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            d.app_stop('com.surfshark.vpnclient.android')
            d.app_start('com.surfshark.vpnclient.android')
        except:
            pass
        time.sleep(15)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_better():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da BetterNet', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        try:
            d.app_stop('com.freevpnintouch')
            d.app_start('com.freevpnintouch')
        except:
            pass
        time.sleep(10)
        dialog = d(resourceId='com.freevpnintouch:id/dialogCtaPositive')
        connect = d(resourceId='com.freevpnintouch:id/buttonConnect').text
        if dialog.exists:
            d(resourceId='com.freevpnintouch:id/dialogCtaPositive').click()
            time.sleep(3)
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
            # time.sleep(5)
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
        while connect == 'CONNECT':
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
            time.sleep(4)
            connect = d(resourceId='com.freevpnintouch:id/buttonConnect').text
            # WebDriverWait(driver, 20).until(
            # EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect').click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        ip = '127.0.0.1:' + porta

        output = subprocess.check_output(['adb', '-s', ip, 'shell', 'ifconfig'])

        # Verifica se a conexão VPN está ativa
        if not re.search(b"tun0", output):
            window['output'].print("Não conectado na BetterNet.")
            window.Refresh()
            try:
                connect = d(resourceId='com.freevpnintouch:id/buttonConnect').text
                d.app_stop('com.freevpnintouch')
                d.app_start('com.freevpnintouch')
                while connect == 'CONNECT':
                    d(resourceId='com.freevpnintouch:id/buttonConnect').click()
                    time.sleep(4)
                    connect = d(resourceId='com.freevpnintouch:id/buttonConnect').text
            except:
                pass
        abc = False

    def vpn_cyberghost():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da CyberGhost', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            d.app_stop('de.mobileconcepts.cyberghost')
            d.app_start('de.mobileconcepts.cyberghost')
        except:
            pass
        # time.sleep(3)
        d(resourceId='de.mobileconcepts.cyberghost:id/button').click()
        rate = d(resourceId='de.mobileconcepts.cyberghost:id/rate_me_text')
        if rate.exists:
            d(resourceId='android:id/button2').click()
        time.sleep(2)
        d(resourceId='de.mobileconcepts.cyberghost:id/button').click()
        # time.sleep(5)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        abc = False

    def vpn_avg():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da AVG', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.avg.android.vpn')
            d.app_start("com.avg.android.vpn", "com.avast.android.vpn.app.wizard.WizardActivity")
        except:
            pass
        # subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #               stderr=subprocess.DEVNULL, check=True, shell=True)

        time.sleep(30)

    def vpn_windscribe():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da Windscribe', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)
            d.app_stop("com.windscribe.vpn")
            d.app_start("com.windscribe.vpn")
        except:
            pass
        d(resourceId='com.windscribe.vpn:id/on_off_button').click()
        time.sleep(10)

    def vpn_hma():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da HMA', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)
        try:
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)

            d.app_stop("com.hidemyass.hidemyassprovpn")
            time.sleep(3)
            d.app_start('com.hidemyass.hidemyassprovpn', 'com.avast.android.vpn.activity.HmaOnboardingActivity')
        except:
            pass
        time.sleep(10)

    def gerar_id():
        chars = string.ascii_lowercase + string.digits
        android_id = ''.join(random.choice(chars) for i in range(16))
        return android_id

    def trocar_email():
        global nomea
        global nome
        global sobrenomea
        global sobrenome
        global nome_completo
        global nome_completo_s
        try:
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Trocando e-mail.')
            window.Refresh()

            chrome.get('https://accountscenter.instagram.com/personal_info/')
            try:
                WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/main/div/div/div[3]/div/div[1]/div/div/a[2]/div[1]/div/div[1]/div/div/span[2]'))).click()
            except:
                WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/html/body/div/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/main/div/div/div[3]/div/div[1]/div/div/a[2]'))).click()
            time.sleep(10)

            chrome.get('https://accountscenter.instagram.com/accounts/')
            WebDriverWait(chrome, 35).until(EC.element_to_be_clickable((By.XPATH,
                                                                        "/html/body/div/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/main/main/div[3]/div/div/div/div[1]/div/div[2]/div/a/div/div[1]/div/span/span"))).click()
            try:
                WebDriverWait(chrome, 35).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[4]/div[3]/div/div/div/div/div/div/div/div/div[1]/div/span/span"))).click()

            except:
                WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                           "/html/body/div/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[6]/div[3]/div/div/div/div/div/div/div/div/div[1]/div/span/span"))).click()

            try:
                WebDriverWait(chrome, 35).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[4]/div[3]/div/div/div/div/div[1]/div[1]/div/div/div[1]/div/span/span"))).click()

            except:
                WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                           "/html/body/div/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[6]/div[3]/div/div/div/div/div[1]/div[1]/div/div/div[1]/div/span/span"))).click()

            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Facebook desvinculado à conta.')
            window.Refresh()
            chrome.get('https://accountscenter.instagram.com/personal_info/contact_points/')
            try:
                WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "/html/body/div/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div[4]/div/div/div[2]/div/div/div/div/div[1]/div[1]/div/div[2]/div/div/span[1]"))).click()

            except:
                WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[5]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[1]/div[1]/div/div[2]/div/div/span[1]"))).click()

            try:
                WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "/html/body/div/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div[4]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/span"))).click()

            except:
                WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[5]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/span"))).click()

            try:
                WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "/html/body/div[2]/div[1]/div/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[1]/div/span/span"))).click()

            except:
                WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[1]/div/span/span"))).click()

            try:
                WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "/html/body/div/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[3]/div[2]/div[4]/div/div/div[1]/div[2]/span[2]/div"))).click()

            except:
                WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[5]/div[2]/div[1]/div/div/div[1]/div[2]/span[2]/div"))).click()

            test = Email()
            while True:
                try:
                    nomea = fake.first_name_female().replace(" ", "")
                    nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                    sobrenomea = fake.last_name().replace(" ", "").lower()
                    sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                    nome_completo = nome + ' ' + sobrenome
                    nome_completo_s = nome + sobrenome
                    test.register(username=nome_completo_s + str(random.randint(000, 999)), password=senha)
                    break  # Saia do loop se o registro for bem-sucedido

                except requests.exceptions.HTTPError as e:
                    nomea = fake.first_name_female().replace(" ", "")
                    nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                    sobrenomea = fake.last_name().replace(" ", "").lower()
                    sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                    nome_completo = nome + ' ' + sobrenome
                    nome_completo_s = nome + sobrenome
                    if e.response.status_code == 422:
                        print("Erro 422: Unprocessable Entity. Tentando novamente...")
                        time.sleep(1)  # Espere um segundo antes de tentar novamente
                        continue  # Volte ao início do loop
                    else:
                        # Outro código de tratamento de erros, se necessário
                        # ...
                        break  # Saia do loop se ocorrer um erro diferente

                except requests.exceptions.RequestException as e:
                    nomea = fake.first_name_female().replace(" ", "")
                    nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                    sobrenomea = fake.last_name().replace(" ", "").lower()
                    sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                    nome_completo = nome + ' ' + sobrenome
                    nome_completo_s = nome + sobrenome
                    # Tratamento de erros de conexão, se necessário
                    # ...
                    break  # Saia do loop se ocorrer um erro de conexão
            email = str(test.address)

            try:
                WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "/html/body/div/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div[4]/div[2]/div/div/div/div/input"))).send_keys(
                    email)
            except:
                WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[5]/div[2]/div[1]/div[2]/div/div/div/div/input"))).send_keys(
                    email)

            try:
                WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "/html/body/div/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[4]/div[3]/div/div/div/div/div/div/div/div/div[1]/div/span/span"))).click()

            except:
                WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[6]/div[3]/div/div/div/div/div/div/div/div/div[1]/div/span/span"))).click()

            codigo = 0
        except Exception as e:
            print(e)
            pass

        def listener(message):
            global nome
            global sobrenome
            global cod
            time.sleep(10)
            if 'Instagram' in message['text']:
                cod = re.search(r'\d{6}', message['text']).group(0)
                global recebido
                recebido = True

        try:
            test.start(listener, interval=15)
            codigo = 0
            while codigo != 20:
                time.sleep(2)
                codigo = codigo + 1
            codigo = cod
        except Exception as e:
            if "Too Many Requests" in str(e):
                pass
            else:
                pass
        test.stop()
        if recebido is False:
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Codigo não recebido')
            window.Refresh()
            raise Exception('Codigo não recebido.')
        try:
            WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                        "/html/body/div/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[3]/div[2]/div[4]/div[2]/div/div/div/div/input"))).send_keys(
                codigo)

        except:
            WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[5]/div[2]/div[1]/div[2]/div/div/div/div/input"))).send_keys(
                codigo)

        try:
            WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                        "/html/body/div/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[4]/div[3]/div/div/div/div/div/div/div/div/div[1]/div/span/span"))).click()

        except:
            WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[6]/div[3]/div/div/div/div/div/div/div/div/div[1]/div/span/span"))).click()

        time.sleep(10)
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Email alterado com sucesso.')
        window.Refresh()
        chrome.get('https://instagram.com/accounts/logout')

    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Senha sendo utilizada: {senha}')
    window.Refresh()

    num = 'InstaFace'
    try:
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Iniciando criação.')
        window.Refresh()
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        client = gspread.authorize(creds)

        spreadsheet_id = config['spreadsheet']
        sheet_name = 'contas'
        # Insert user, password, and timestamp into first empty row
        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
        values = sheet.col_values(1)

        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
        rows = sheet.get_all_values()

        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
        regex = re.compile(r'\S+\s\S+')
        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
        num_rows = sum(1 for row in rows if regex.match(row[0]))
        window['total'].update(num_rows)
    except:
        pass
    first = True
    parar = False
    while parar is False:
        if parar is True:
            print('Parando Thread')
            break
        try:
            try:
                chrome.quit()
            except:
                pass
            try:
                gl.stop()
                gl.delete(profile_id)
            except:
                pass
        except:
            pass

        try:
            random_port = str(random.randint(1000, 9999))
            # gl = GoLogin({
            #    "token": apigologin,
            #    'extra_params': ['--window-position=0,0'],
            #    "port": random_port
            #    })
            # profile_id = gl.create({
            #    "name": 'Creator-FB',
            #    "os": 'win',
            #    "navigator": {
            #        "language": 'pt-BR',
            #        "userAgent": 'random', # Your userAgent (if you don't want to change, leave it at 'random')
            #        "resolution": '800x1800', # Your resolution (if you want a random resolution - set it to 'random')
            #        "platform": 'Win32',
            #    },
            #    'proxyEnabled': True, # Specify 'false' if not using proxy
            #    'proxy': {
            #        'mode': 'http',
            #        #'autoProxyRegion': 'br'
            #        'host': ip,
            #        'port': porta2,
            #        'username': usuario,
            #        'password': senha2,
            #    },
            #    "webRTC": {
            #        "mode": "alerted",
            #        "enabled": True,
            #    },
            # })
            #
            # gl = GoLogin({
            #    "token": apigologin,
            #    "port": random_port,
            #    'extra_params': ['--window-position=0,0', ],
            #    "profile_id": profile_id
            #    })

            UA = UserAgent()

            random_user_agent = UA.get_ua()

            chrome_driver_path = "chromedriver.exe"
            profile = profiles.Windows()  # or .Android()
            # debugger_address = gl.start()
            chrome_options = ChromeOptions()
            chrome_options.page_load_strategy = 'eager'
            if senha2 == '':
                chrome_options.add_argument(f'--proxy-server=http://{ip}:{porta2}')
                options = {
                    'request_storage_base_dir': 'storage\\'
                    # 'ca_cert': 'C:\\Users\\welli\\Desktop\\Outros\\Creator 2.0.1\\ca.crt'
                }
            else:
                # options = {
                # 'request_storage_base_dir': 'storage\\'
                # 'ca_cert': 'C:\\Users\\welli\\Desktop\\Outros\\Creator 2.0.1\\ca.crt'  # Use own root certificate
                # 'proxy': {
                #    'http': f'http://{usuario}:{senha2}@{ip}:{porta2}'
                # }
                profile["proxy"] = {
                    "proxy": f"http://{usuario}:{senha2}@{ip}:{porta2}"
                }
            chrome_options.add_argument(f'user-agent={random_user_agent}')
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--ignore-ssl-errors')

            chrome_options.add_argument("--headless=new")
            # chrome_options.add_experimental_option("debuggerAddress", debugger_address)
            service = Service(executable_path=chrome_driver_path)
            # chrome = uc.Chrome(service=service, options=chrome_options)
            chrome = Chrome(service=service, options=chrome_options, profile=profile)
            chrome.set_window_size(700, 2000)
            chrome.implicitly_wait(30)
            window['output'].print(linha_ret)
            window.Refresh()
            window['output'].print(f"[{datetime.now().strftime('%H:%M:%S')}] Abrindo site do Facebook")
            window.Refresh()
            chrome.get("https://www.facebook.com/signup/")
            ddi = random.choice(["2199", "1199", "2198", "1198"])
            final_number = ddi + str(random.randint(0, 9999999)).zfill(7)
            lista_user = random.choices(range(0, 9), k=2)
            lista_letras = random.choices(letras, k=1)
            nomea = fake.first_name_female().replace(" ", "")
            nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
            sobrenomea = fake.last_name().replace(" ", "").lower()
            sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
            nome_completo = nome + ' ' + sobrenome
            nome_completo_s = nome + sobrenome
            numeros_concatenados = ''.join(str(numero) for numero in lista_user)
            user_completo = nome_completo_s + '' + str(numeros_concatenados) + ''.join(lista_letras)
            # chrome.get("https://www.facebook.com/signup/")
            chrome.find_element(By.NAME, "firstname").send_keys(nomea)
            chrome.find_element(By.NAME, "lastname").send_keys(sobrenomea)

            chrome.find_element(By.NAME, "reg_email__").send_keys(f'+55 {final_number}')
            chrome.find_element(By.NAME, "reg_passwd__").send_keys(senha)
            chrome.find_element(By.NAME, "birthday_day").send_keys(random.randint(10, 27))
            chrome.find_element(By.NAME, "birthday_year").send_keys(random.randint(1970, 2003))
            url = chrome.current_url
            chrome.find_element(By.NAME, "sex").click()
            # /html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[1]/input

            time.sleep(5)
            chrome.find_element(By.NAME, "websubmit").click()
            substrings = ["confirmemail", "checkpoint"]
            cont = 1
            while True:
                # Aguardar um intervalo de tempo (opcional)
                # Coloque aqui qualquer espera necessária antes de capturar a URL novamente

                # Capturar a URL atual novamente
                nova_url = chrome.current_url

                # Verificar se a URL mudou e contém uma das substrings
                if nova_url != url and any(substring in nova_url for substring in substrings):
                    # Realizar ação quando a condição for atendida
                    print("A URL mudou.")
                    break
                else:
                    print("A URL não mudou.")
                    cont += 1
                    if cont >= 10:
                        window['output'].print(
                            f"[{datetime.now().strftime('%H:%M:%S')}] Algum erro no navegador, reiniciando.")
                        window.Refresh()
                        raise Exception("SMS.")
                    time.sleep(5)
                # Atualizar a URL anterior
                url = nova_url
            if "checkpoint" in nova_url:
                window['output'].print(f"[{datetime.now().strftime('%H:%M:%S')}] SMS", text_color=('red'))
                window.Refresh()
                raise Exception("SMS.")
            chrome.find_element(By.XPATH,
                                "/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[2]/div/a").click()

            def listener(message):
                global nome
                global sobrenome
                global cod
                if 'Facebook' in message['subject']:
                    cod = re.search(r'\d+', message['subject']).group(0)

            test = Email()
            while True:
                try:
                    nomea = fake.first_name_female().replace(" ", "")
                    nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                    sobrenomea = fake.last_name().replace(" ", "").lower()
                    sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                    nome_completo = nome + ' ' + sobrenome
                    nome_completo_s = nome + sobrenome
                    test.register(username=nome_completo_s + str(random.randint(000, 999)), password=senha)
                    break  # Saia do loop se o registro for bem-sucedido

                except requests.exceptions.HTTPError as e:
                    nomea = fake.first_name_female().replace(" ", "")
                    nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                    sobrenomea = fake.last_name().replace(" ", "").lower()
                    sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                    nome_completo = nome + ' ' + sobrenome
                    nome_completo_s = nome + sobrenome
                    if e.response.status_code == 422:
                        print("Erro 422: Unprocessable Entity. Tentando novamente...")
                        time.sleep(1)  # Espere um segundo antes de tentar novamente
                        continue  # Volte ao início do loop
                    else:
                        # Outro código de tratamento de erros, se necessário
                        # ...
                        break  # Saia do loop se ocorrer um erro diferente

                except requests.exceptions.RequestException as e:
                    nomea = fake.first_name_female().replace(" ", "")
                    nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                    sobrenomea = fake.last_name().replace(" ", "").lower()
                    sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                    nome_completo = nome + ' ' + sobrenome
                    nome_completo_s = nome + sobrenome
                    # Tratamento de erros de conexão, se necessário
                    # ...
                    break  # Saia do loop se ocorrer um erro de conexão
            #

            email = str(test.address)
            window['output'].print(f"[{datetime.now().strftime('%H:%M:%S')}] Email: " + email)
            #
            window.Refresh()
            time.sleep(5)
            chrome.find_element(By.NAME, "contactpoint").send_keys(email)
            chrome.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/form/div[3]/button").click()
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando codigo...')
            window.Refresh()
            # fetch all emails in the inbox
            codigo = 0
            print(codigo)
            recebido = False

            def listener(message):
                global nome
                global sobrenome
                global cod
                if 'Facebook' in message['subject']:
                    global recebido
                    recebido = True
                    cod = re.search(r'\d+', message['subject']).group(0)

            try:
                test.start(listener, interval=5)
                codigo = 0
                while codigo != 20:
                    time.sleep(2)
                    codigo = codigo + 1
                codigo = cod
            except Exception as e:
                if "Too Many Requests" in str(e):
                    pass
                else:
                    pass
            print(codigo)
            if recebido is False:
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Codigo não recebido')
                window.Refresh()
                raise Exception('Codigo não recebido.')
            #
            test.stop()
            ##chrome.execute_script("window.open('about:blank', '_blank');")
            ##chrome.switch_to.window(chrome.window_handles[1])  # Mude para a nova guia
            ##chrome.get('https://moakt.com/pt')
            ##WebDriverWait(chrome, 35).until(EC.element_to_be_clickable((By.NAME, "random"))).click()
            ##email = WebDriverWait(chrome, 35).until(EC.element_to_be_clickable((By.ID, "email-address"))).text
            ##window['output'].print(f"[{datetime.now().strftime('%H:%M:%S')}] Email: " + email)
            ##window.Refresh()
            ##chrome.switch_to.window(chrome.window_handles[0])
            ##chrome.find_element(By.NAME, "contactpoint").send_keys(email)
            ##chrome.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/form/div[3]/button").click()
            ##window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Aguardando codigo...')
            ##window.Refresh()
            ##chrome.switch_to.window(chrome.window_handles[1])
            ##
            ##cod = chrome.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[2]/td[1]/a')
            ##while True:
            ##    chrome.refresh()
            ##    time.sleep(5)
            ##    cod = chrome.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[2]/td[1]/a')
            ##    if len(cod) == 1:
            ##        cod = chrome.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr[2]/td[1]/a').text
            ##        codigo = re.search(r'\d+', cod).group(0)
            ##        print(cod)
            ##        chrome.close()
            ##        chrome.switch_to.window(chrome.window_handles[0])
            ##        break
            ##    else:
            ##        pass
            ###WebDriverWait(chrome, 35).until(EC.element_to_be_clickable((By.XPATH, ""))).click()
            ###WebDriverWait(chrome, 35).until(EC.element_to_be_clickable((By.XPATH, ""))).click()
            ###WebDriverWait(chrome, 35).until(EC.element_to_be_clickable((By.XPATH, ""))).click()
            ###WebDriverWait(chrome, 35).until(EC.element_to_be_clickable((By.XPATH, ""))).click()
            ###WebDriverWait(chrome, 35).until(EC.element_to_be_clickable((By.XPATH, ""))).click()

            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Codigo recebido: {codigo}')
            window.Refresh()
            # test.stop()
            chrome.find_element(By.NAME, "code").send_keys(codigo)
            chrome.find_element(By.NAME, "confirm").click()
            WebDriverWait(chrome, 35).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div/div/div[3]/div/a"))).click()
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
            window.Refresh()
            time.sleep(10)
            if chrome.current_url == 'https://web.facebook.com/' or chrome.current_url == 'https://www.facebook.com/':
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Facebook criado com sucesso',
                                       text_color='cyan')
                window.Refresh()
            else:
                window['output'].print(f"[{datetime.now().strftime('%H:%M:%S')}] SMS", text_color=('red'))
                window.Refresh()
                raise Exception('SMS')
            chrome.get("https://www.instagram.com/")
            try:
                WebDriverWait(chrome, 15).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[last()]/button"))).click()
            except:
                chrome.refresh()
                WebDriverWait(chrome, 15).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[last()]/button"))).click()
            try:
                confirm = chrome.find_element(By.NAME, "__CONFIRM__")
                confirm.click()
            except:
                chrome.refresh()
                confirm = chrome.find_element(By.NAME, "__CONFIRM__")
                confirm.click()
            while len(chrome.find_elements(By.NAME, "__CONFIRM__")) == 1:
                confirm = chrome.find_element(By.NAME, "__CONFIRM__")
                confirm.click()
                time.sleep(5)
            time.sleep(5)
            while not 'disclosure' in chrome.current_url:
                chrome.get("https://www.instagram.com/")
                WebDriverWait(chrome, 35).until(EC.element_to_be_clickable((By.XPATH,
                                                                            "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[last()]/button"))).click()
                time.sleep(5)
                if len(chrome.find_elements(By.NAME, "__CONFIRM__")) == 1:
                    chrome.find_element(By.NAME, "__CONFIRM__").click()
                time.sleep(10)

            chrome.find_element(By.XPATH,
                                "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div/div/div/div[3]/button").click()
            time.sleep(2)
            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: {user_completo}')
            chrome.find_element(By.NAME, "username").send_keys(user_completo)
            chrome.find_element(By.NAME, "password").send_keys(senha)
            url = chrome.current_url
            chrome.find_element(By.XPATH,
                                "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[3]/form/div[4]/div/button").click()

            substrings = ["checkpoint"]
            while True:
                time.sleep(10)
                # Coloque aqui qualquer espera necessária antes de capturar a URL novamente

                # Capturar a URL atual novamente
                nova_url = chrome.current_url

                # Verificar se a URL mudou e contém uma das substrings
                if nova_url != url:
                    # Realizar ação quando a condição for atendida
                    print("A URL mudou.")
                    break
                elif len(chrome.find_elements(By.ID, 'ssfErrorAlert')) == 1:
                    chrome.get("https://www.instagram.com/")
                    time.sleep(5)
                    if len(chrome.find_elements(By.NAME, 'username')) == 1:
                        chrome.find_element(By.NAME, "username").send_keys(user_completo)
                        chrome.find_element(By.NAME, "password").send_keys(senha)
                        url_antiga = chrome.current_url
                        chrome.find_element(By.XPATH,
                                            "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button").click()
                        # while url_antiga ==
                        time.sleep(15)
                    else:
                        chrome.find_element(By.XPATH,
                                            "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div/div[2]/div[2]/button").click()
                        WebDriverWait(chrome, 35).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]")))
                        time.sleep(10)

                else:
                    print("A URL não mudou.")
                    time.sleep(5)
                # Atualizar a URL anterior
                url = nova_url
            if chrome.current_url == 'https://www.instagram.com/':
                conteudo = config['vpn']
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                       text_color=('lime'))
                window.Refresh()
                contagem += 1

                window['criadas'].update(contagem)
                window.Refresh()
                try:
                    now = datetime.now()
                    now_brasilia = tz.localize(now)
                    timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                    client = gspread.authorize(creds)

                    spreadsheet_id = config['spreadsheet']
                    sheet_name = 'contas'
                    # Insert user, password, and timestamp into first empty row
                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                    values = sheet.col_values(1)
                    last_row = len(values)
                    values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo + ' - ' + app]
                    cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                    for i, val in enumerate(values):
                        cell_list[i].value = val
                    sheet.update_cells(cell_list)

                    rows = sheet.get_all_values()

                    # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                    regex = re.compile(r'\S+\s\S+')

                    # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                    num_rows = sum(1 for row in rows if regex.match(row[0]))
                    window['total'].update(num_rows)

                    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                    creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                    client = gspread.authorize(creds)

                    spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                    sheet_name = 'relatorio_geral'
                    # Insert user, password, and timestamp into first empty row
                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                    values = sheet.col_values(1)
                    last_row = len(values)
                    values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo + ' - ' + app]
                    cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                    for i, val in enumerate(values):
                        cell_list[i].value = val
                    sheet.update_cells(cell_list)

                    window.Refresh()
                    arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                    # Escreva mais conteúdo no arquivo
                    arquivo.write(user_completo + ' ' + senha + "\n")
                    arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                    # Escreva mais conteúdo no arquivo
                    arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                    window.Refresh()
                except:
                    pass
                try:
                    trocar_email()
                except:
                    pass
                sms = False

            else:
                window['output'].print(f"[{datetime.now().strftime('%H:%M:%S')}] SMS", text_color=('red'))
                window.Refresh()
                try:
                    chrome.quit()
                except:
                    pass
                gl.delete(profile_id)
                raise Exception('SMS')

            try:
                window['output'].print(linha_ret)
                window.Refresh()
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Criação de outro perfil.')
                window.Refresh()
                try:
                    with open("config.json", "r") as f:
                        config = json.load(f)
                except FileNotFoundError:
                    config = {}
                if config['app'] == '-instalite-':
                    pass
                elif config['app'] == '-insta-':
                    chrome.quit()
                    try:
                        gl.stop()
                    except:
                        pass
                    try:
                        comando = f"adb connect 127.0.0.1:{porta}"
                        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True,
                                       shell=True)
                    except:
                        pass
                    try:
                        comando = f"adb connect 127.0.0.1:{porta}"
                        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True,
                                       shell=True)
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global window_animation_scale 0',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, shell=True)
                        subprocess.run(
                            f'adb -s 127.0.0.1:{porta} shell settings put global transition_animation_scale 0',
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL, shell=True)
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put global animator_duration_scale 0',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, shell=True)
                    except:
                        pass

                    def gerar_id():
                        chars = string.ascii_lowercase + string.digits
                        android_id = ''.join(random.choice(chars) for i in range(16))
                        return android_id

                    gerar_id()
                    android_id = gerar_id()
                    subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL, shell=True)
                    try:
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.android',
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True, shell=True)
                    except:
                        pass
                    d = u2.connect(f'127.0.0.1:{porta}')

                    d.set_fastinput_ime(True)
                    d.app_start('com.instagram.android')
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Abrindo instagram.')
                    window.Refresh()
                    time.sleep(10)
                    try:
                        d.xpath(
                            '//android.view.View[@content-desc="Nome de usuário, email ou número de celular"]').wait(
                            timeout=80)
                        d.xpath(
                            '//android.view.View[@content-desc="Nome de usuário, email ou número de celular"]').set_text(
                            user_completo)
                    except Exception as e:
                        print(e)
                        conteudo = config['vpn']
                        if conteudo == "AVG":
                            vpn_avg()
                        elif conteudo == "SurfShark":
                            vpn_surf()
                        elif conteudo == "Avast":
                            vpn_avast()
                        elif conteudo == "ExpressVPN":
                            vpn_express()
                        elif conteudo == "PiaVPN":
                            vpn_pia()
                        elif conteudo == "BetterNet":
                            vpn_better()
                        elif conteudo == "WindscribeVPN":
                            vpn_windscribe()
                        elif conteudo == "CyberGhost":
                            vpn_cyberghost()
                        elif conteudo == "NordVPN":
                            vpn_nord()
                        elif conteudo == "HmaVPN":
                            vpn_hma()
                        elif conteudo == "HotspotShield":
                            vpn_hotspotshield()
                        else:
                            window['output'].print(
                                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                            window.Refresh()
                    d.xpath('//android.view.View[@content-desc="Senha"]').set_text(senha)
                    d.xpath('//android.view.View[@content-desc="Entrar"]').click()
                    d.xpath('//android.view.View[@content-desc="Salvar suas informações de login?"]').wait(20)
                    if d.xpath('//android.view.View[@content-desc="Salvar suas informações de login?"]').exists:
                        d.xpath('//android.view.View[@content-desc="Agora não"]').click()
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta logada.')
                        window.Refresh()
                    while sms is False:
                        d(resourceId='com.instagram.android:id/profile_tab').click()
                        time.sleep(3)
                        d(resourceId='com.instagram.android:id/action_bar_title_chevron').click(timeout=50)
                        time.sleep(2)
                        d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[last()]/android.widget.FrameLayout/android.widget.ImageView').click()
                        time.sleep(4)
                        d.xpath('//android.widget.Button[@content-desc="Criar nova conta"]').click()
                        time.sleep(3)
                        # Gerar nome de usuário, digitar no campo e clicar em avançae
                        lista_user = random.choices(range(0, 9), k=2)
                        lista_letras = random.choices(letras, k=1)
                        nomea = fake.first_name_female().replace(" ", "")
                        nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                        sobrenomea = fake.last_name().replace(" ", "").lower()
                        sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                        nome_completo = nome + sobrenome
                        numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                        user_completo = nome_completo + '' + str(numeros_concatenados) + ''.join(lista_letras)

                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: ' + user_completo)
                        window.Refresh()
                        d(resourceId='com.instagram.android:id/username').set_text(user_completo)
                        time.sleep(3)
                        d(resourceId='com.instagram.android:id/button_text').click()
                        # Digitar senha e avançar
                        time.sleep(3)
                        try:
                            d(resourceId='com.instagram.android:id/password').set_text(senha)
                        except:
                            try:
                                conteudo = config['vpn']
                                if conteudo == "AVG":
                                    vpn_avg()
                                elif conteudo == "SurfShark":
                                    vpn_surf()
                                elif conteudo == "Avast":
                                    vpn_avast()
                                elif conteudo == "ExpressVPN":
                                    vpn_express()
                                elif conteudo == "PiaVPN":
                                    vpn_pia()
                                elif conteudo == "WindscribeVPN":
                                    vpn_windscribe()
                                elif conteudo == "BetterNet":
                                    vpn_better()
                                elif conteudo == "CyberGhost":
                                    vpn_cyberghost()
                                elif conteudo == "HmaVPN":
                                    vpn_hma()
                                elif conteudo == "NordVPN":
                                    vpn_nord()
                                elif conteudo == "HotspotShield":
                                    vpn_hotspotshield()
                                else:
                                    window['output'].print(
                                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                    window.Refresh()

                            except:
                                sms = True
                        d(resourceId='com.instagram.android:id/button_text').click()
                        # Clicar em concluir cadastro
                        time.sleep(3)
                        d(resourceId='com.instagram.android:id/button_text').click()

                        time.sleep(4)
                        feedback = d.xpath(
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.View')
                        if feedback.exists:
                            sms = True

                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Verificando...')
                        window.Refresh()
                        # WebDriverWait(driver, 40).until(EC.visibility_of_element_located)(((By.XPATH,
                        #                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[10]')))
                        # d(resourceId='com.instagram.android:id/connect_text').wait()
                        verificar = d(resourceId='com.instagram.android:id/connect_text')
                        if verificar.exists(timeout=30):
                            try:
                                conteudo = config['vpn']
                                window['output'].print(
                                    f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                    text_color=('lime'))
                                window.Refresh()
                                contagem += 1
                                window['criadas'].update(contagem)
                                window.Refresh()
                                now = datetime.now()
                                now_brasilia = tz.localize(now)
                                timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                                client = gspread.authorize(creds)

                                spreadsheet_id = config['spreadsheet']
                                sheet_name = 'contas'
                                # Insert user, password, and timestamp into first empty row
                                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                values = sheet.col_values(1)
                                last_row = len(values)
                                values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                          conteudo + ' - ' + app]
                                cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                for i, val in enumerate(values):
                                    cell_list[i].value = val
                                sheet.update_cells(cell_list)

                                rows = sheet.get_all_values()

                                # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                                regex = re.compile(r'\S+\s\S+')

                                # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                                num_rows = sum(1 for row in rows if regex.match(row[0]))
                                window['total'].update(num_rows)
                                time.sleep(4)
                                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                                creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                                client = gspread.authorize(creds)

                                spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                                sheet_name = 'relatorio_geral'
                                # Insert user, password, and timestamp into first empty row
                                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                                values = sheet.col_values(1)
                                last_row = len(values)
                                values = [user_completo + ' ' + senha, num + ' - ' + email, timestamp, maquina,
                                          conteudo + ' - ' + app]
                                cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                                for i, val in enumerate(values):
                                    cell_list[i].value = val
                                sheet.update_cells(cell_list)




                            except:
                                pass

                            window.Refresh()
                            arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                            # Escreva mais conteúdo no arquivo
                            arquivo.write(user_completo + ' ' + senha + "\n")
                            arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                            # Escreva mais conteúdo no arquivo
                            arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                            window.Refresh()
                            d(resourceId='com.instagram.android:id/skip_button').click()
                            time.sleep(1)
                            d(resourceId='com.instagram.android:id/negative_button').click()
                            time.sleep(3)
                            d(resourceId='com.instagram.android:id/skip_button').click()
                            time.sleep(1)
                            try:
                                d.xpath(
                                    '//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView').click()
                            except:
                                d(resourceId='com.instagram.android:id/skip_button').click()
                                d.xpath(
                                    '//android.widget.Button[@content-desc="Avançar"]/android.widget.ImageView').click()

                            time.sleep(1)
                            time.sleep(3)
                            try:
                                d(resourceId='com.instagram.android:id/profile_tab').click()
                            except:
                                d(resourceId='com.instagram.android:id/button_text').click()
                                d(resourceId='com.instagram.android:id/profile_tab').click()
                            sms = False
                            window['output'].print(linha_ret)
                            window.Refresh()
                            window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Criação de outro perfil.')
                            window.Refresh()
                        else:
                            try:
                                conteudo = config['vpn']
                                if conteudo == "AVG":
                                    vpn_avg()
                                elif conteudo == "SurfShark":
                                    vpn_surf()
                                elif conteudo == "Avast":
                                    vpn_avast()
                                elif conteudo == "ExpressVPN":
                                    vpn_express()
                                elif conteudo == "PiaVPN":
                                    vpn_pia()
                                elif conteudo == "WindscribeVPN":
                                    vpn_windscribe()
                                elif conteudo == "BetterNet":
                                    vpn_better()
                                elif conteudo == "CyberGhost":
                                    vpn_cyberghost()
                                elif conteudo == "HmaVPN":
                                    vpn_hma()
                                elif conteudo == "NordVPN":
                                    vpn_nord()
                                elif conteudo == "HotspotShield":
                                    vpn_hotspotshield()
                                else:
                                    window['output'].print(
                                        "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                                    window.Refresh()

                            except Exception as e:
                                sms = True
                                pass
                    else:
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Houve algum erro ao logar.')
                        window.Refresh()
                        sms = True
                else:
                    try:
                        WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[last()]/button"))).click()
                    except:
                        WebDriverWait(chrome, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div[2]/form/div/div[5]/button"))).click()
                    while not 'disclosure' in chrome.current_url:
                        chrome.get("https://www.instagram.com/")
                        WebDriverWait(chrome, 35).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[last()]/button"))).click()
                        time.sleep(10)
                    chrome.find_element(By.XPATH,
                                        "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div/div/div/div[3]/button").click()
                    time.sleep(2)
                    lista_user = random.choices(range(0, 9), k=2)
                    lista_letras = random.choices(letras, k=1)
                    nomea = fake.first_name_female().replace(" ", "")
                    nome = unicodedata.normalize('NFKD', nomea).encode('ASCII', 'ignore').decode('ASCII')
                    sobrenomea = fake.last_name().replace(" ", "").lower()
                    sobrenome = unicodedata.normalize('NFKD', sobrenomea).encode('ASCII', 'ignore').decode('ASCII')
                    nome_completo = nome + ' ' + sobrenome
                    nome_completo_s = nome + sobrenome
                    numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                    user_completo = nome_completo_s + '' + str(numeros_concatenados) + ''.join(lista_letras)
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Usuário: {user_completo}')
                    chrome.find_element(By.NAME, "username").send_keys(user_completo)
                    chrome.find_element(By.NAME, "password").send_keys(senha)
                    url = chrome.current_url
                    chrome.find_element(By.XPATH,
                                        "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[3]/form/div[4]/div/button").click()

                    substrings = ["checkpoint"]
                    while True:
                        # Aguardar um intervalo de tempo (opcional)
                        # Coloque aqui qualquer espera necessária antes de capturar a URL novamente

                        # Capturar a URL atual novamente
                        nova_url = chrome.current_url

                        # Verificar se a URL mudou e contém uma das substrings
                        if nova_url != url:
                            # Realizar ação quando a condição for atendida
                            print("A URL mudou.")
                            break
                        elif len(chrome.find_elements(By.ID, 'ssfErrorAlert')) == 1:
                            chrome.get("https://www.instagram.com/")
                            time.sleep(5)
                            if len(chrome.find_elements(By.NAME, 'username')) == 1:
                                chrome.find_element(By.NAME, "username").send_keys(user_completo)
                                chrome.find_element(By.NAME, "password").send_keys(senha)
                                chrome.find_element(By.XPATH,
                                                    "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button").click()
                                time.sleep(10)
                            else:
                                chrome.find_element(By.XPATH,
                                                    "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div/div[2]/div[2]/button").click()
                                WebDriverWait(chrome, 35).until(EC.element_to_be_clickable((By.XPATH,
                                                                                            "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]")))
                                time.sleep(10)

                        else:
                            print("A URL não mudou.")
                            time.sleep(5)
                        # Atualizar a URL anterior
                        url = nova_url
                    if chrome.current_url == 'https://www.instagram.com/':
                        conteudo = config['vpn']
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Conta criada com sucesso.',
                                               text_color=('lime'))
                        window.Refresh()
                        contagem += 1

                        trocar_email()

                        window['criadas'].update(contagem)
                        window.Refresh()
                        now = datetime.now()
                        now_brasilia = tz.localize(now)
                        timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")

                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                        client = gspread.authorize(creds)

                        spreadsheet_id = config['spreadsheet']
                        sheet_name = 'contas'
                        # Insert user, password, and timestamp into first empty row
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                        values = sheet.col_values(1)
                        last_row = len(values)
                        values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo + ' - ' + app]
                        cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                        for i, val in enumerate(values):
                            cell_list[i].value = val
                        sheet.update_cells(cell_list)

                        rows = sheet.get_all_values()

                        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                        regex = re.compile(r'\S+\s\S+')

                        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                        num_rows = sum(1 for row in rows if regex.match(row[0]))
                        window['total'].update(num_rows)

                        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                        creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                        client = gspread.authorize(creds)
                        try:
                            spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                            sheet_name = 'relatorio_geral'
                            # Insert user, password, and timestamp into first empty row
                            sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                            values = sheet.col_values(1)
                            last_row = len(values)
                            values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo + ' - ' + app]
                            cell_list = sheet.range(f'A{last_row + 1}:E{last_row + 1}')
                            for i, val in enumerate(values):
                                cell_list[i].value = val
                            sheet.update_cells(cell_list)

                            window.Refresh()
                            arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')
                            # Escreva mais conteúdo no arquivo
                            arquivo.write(user_completo + ' ' + senha + "\n")
                            arquivo = open('configuracoes/contas/contas_criadas_email_incluso.txt', 'a')
                            # Escreva mais conteúdo no arquivo
                            arquivo.write(email + '\n' + user_completo + '\n' + senha + "\n\n")
                            window.Refresh()
                            sms = False
                        except:
                            pass

                    else:
                        window['output'].print(f"[{datetime.now().strftime('%H:%M:%S')}] SMS", text_color=('red'))
                        window.Refresh()
                        try:
                            chrome.quit()
                        except:
                            pass
                        gl.delete(profile_id)
                        raise Exception('SMS')
            except Exception as e:
                print(e)
                try:
                    if not os.path.exists('error_log'):
                        os.makedirs('error_log')
                    now = datetime.now()
                    timestamp = now.strftime('%Y%m%d_%H%M%S')

                    # Tirar o print da página
                    screenshot_path = os.path.join('error_log', f'screenshot_{timestamp}.png')
                    chrome.save_screenshot(screenshot_path)
                except:
                    pass
                try:
                    chrome.quit()
                except:
                    pass
                gl.delete(profile_id)
                sms = True
                continue


        except Exception as e:
            print(e)
            if not 'SMS.' in str(e):
                try:
                    if not os.path.exists('error_log'):
                        os.makedirs('error_log')
                    now = datetime.now()
                    timestamp = now.strftime('%Y%m%d_%H%M%S')

                    # Tirar o print da página
                    screenshot_path = os.path.join('error_log', f'screenshot_{timestamp}.png')
                    chrome.save_screenshot(screenshot_path)
                except:
                    pass
            try:
                chrome.quit()
            except:
                pass
            try:
                gl.stop()
                gl.delete(profile_id)
            except:
                pass
            sms = True
            continue


def executar_creator_2nr():
    import time
    import re
    import requests
    import random
    import PySimpleGUI as sg
    import json
    from datetime import datetime
    import threading
    import subprocess
    import string
    from appium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.common.exceptions import NoSuchElementException
    try:
        from minuteinbox import Inbox
    except:
        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        subprocess.run(['pip', 'install', 'minuteinbox'])
        subprocess.run(['deactivate'], shell=True)
        from minuteinbox import Inbox
    from faker import Faker
    linha_ret = '_________________________________________________\n'
    fake = Faker('pt_BR')
    try:
        import uiautomator2 as u2
    except:
        subprocess.run(['venv/scripts/activate.bat'], shell=True)
        subprocess.run(['pip', 'install', 'uiautomator2'])
        subprocess.run(['deactivate'], shell=True)
        subprocess.run(['pip', 'install', '--upgrade', 'requests'])
        import requests
        time.sleep(10)
        import uiautomator2 as u2

    # use without parameters to create a new inbox
    # inbox = Inbox()

    try:
        with open("config2nr.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {}
    d = u2.connect(f'{porta}')
    subprocess.run(f'adb -s {porta} uninstall io.appium.uiautomator2.server.test',
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    subprocess.run(f'adb -s {porta} uninstall io.appium.uiautomator2.server',
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)

    # test = Email()

    def listener(message):
        global nome
        global sobrenome
        global cod
        if '2nr' in message['subject']:

            urls = re.findall("(?P<url>https?://[^\s]+)", message['text'] if message['text'] else message['html'])

            # Acessar cada URL
            for url in urls:
                if url.startswith('https://api.2nr.xyz/register/?'):
                    response = requests.get(url)

                    # Verificar o código de status
                    if response.status_code == 200:
                        pass
                    else:
                        print(f"Erro ao acessar o link: {response.status_code}")

    contagem = 0
    troca_ip = 0

    def gerar_id():
        chars = string.ascii_lowercase + string.digits
        android_id = ''.join(random.choice(chars) for i in range(16))
        return android_id

    def vpn_avast():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da Avast', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s {porta} shell pm clear pl.rs.sip.softphone.newapp', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            subprocess.run(f'adb -s {porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop("com.avast.android.vpn")
            d.app_start("com.avast.android.vpn", ".app.wizard.WizardActivity")
            time.sleep(10)
        except Exception as e:
            print(e)
        abc = False

    def nenhuma_vpn():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()

        try:
            subprocess.run(f'adb -s {porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s {porta} shell pm clear com.facebook.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        time.sleep(10)

    def vpn_hotspotshield():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da HotspotShield',
                               text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s {porta} shell pm clear pl.rs.sip.softphone.newapp', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            subprocess.run(f'adb -s {porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('hotspotshield.android.vpn')
            d.app_start('hotspotshield.android.vpn')
        except Exception as e:
            print(e)
        d(resourceId='hotspotshield.android.vpn:id/tryAgainButton').click()
        time.sleep(5)
        d(resourceId='hotspotshield.android.vpn:id/btnVpnConnect').click()

        # subprocess.run(f'adb -s {porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_pia():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da PiaVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()

        try:
            subprocess.run(f'adb -s {porta} shell pm clear pl.rs.sip.softphone.newapp', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s {porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.privateinternetaccess.android')
            d.app_start('com.privateinternetaccess.android')
        except:
            pass
        # subprocess.run(f'adb -s {porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        d(resourceId='com.privateinternetaccess.android:id/connection_background').click()
        time.sleep(3)
        d(resourceId='com.privateinternetaccess.android:id/connection_background').click()

        abc = False

    def vpn_express():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da ExpressVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()

        try:
            subprocess.run(f'adb -s {porta} shell pm clear pl.rs.sip.softphone.newapp', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        try:
            subprocess.run(f'adb -s {porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.expressvpn.vpn')
            d.app_start('com.expressvpn.vpn')
        except:
            pass
        # subprocess.run(f'adb -s {porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #            stderr=subprocess.DEVNULL, check=True, shell=True)

        d(resourceId='com.expressvpn.vpn:id/obiButton').click()
        time.sleep(3)
        d(resourceId='com.expressvpn.vpn:id/obiButton').click()

        abc = False

    def vpn_nord():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da NordVPN', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s {porta} shell pm clear pl.rs.sip.softphone.newapp', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        subprocess.run(f'adb -s {porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        sms = True
        try:
            d.app_stop('com.nordvpn.android')
            d.app_start('com.nordvpn.android', '.MainActivity')
        except:
            pass
        time.sleep(10)
        time.sleep(5)
        subprocess.run(f'adb -s {porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_surf():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da SurfShark', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s {porta} shell pm clear pl.rs.sip.softphone.newapp', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            subprocess.run(f'adb -s {porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            d.app_stop('com.surfshark.vpnclient.android')
            d.app_start('com.surfshark.vpnclient.android')
        except:
            pass
        time.sleep(15)
        subprocess.run(f'adb -s {porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        abc = False

    def vpn_better():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da BetterNet', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s {porta} shell pm clear pl.rs.sip.softphone.newapp', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        subprocess.run(f'adb -s {porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

        try:
            d.app_stop('com.freevpnintouch')
            d.app_start('com.freevpnintouch')
        except:
            pass
        time.sleep(10)
        dialog = d(resourceId='com.freevpnintouch:id/dialogCtaPositive')
        connect = d(resourceId='com.freevpnintouch:id/buttonConnect').get_text(timeout=80)
        if dialog.exists:
            d(resourceId='com.freevpnintouch:id/dialogCtaPositive').click()
            time.sleep(3)
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
            # time.sleep(5)
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
        while connect == 'CONNECT':
            d(resourceId='com.freevpnintouch:id/buttonConnect').click()
            time.sleep(4)
            connect = d(resourceId='com.freevpnintouch:id/buttonConnect').get_text(timeout=80)
            # WebDriverWait(driver, 20).until(
            # EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect').click()
        # time.sleep(5)
        subprocess.run(f'adb -s {porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        ip = '' + porta

        output = subprocess.check_output(['adb', '-s', ip, 'shell', 'ifconfig'])

        # Verifica se a conexão VPN está ativa
        if not re.search(b"tun0", output):
            window['output'].print("Não conectado na BetterNet.")
            window.Refresh()
            try:
                connect = d(resourceId='com.freevpnintouch:id/buttonConnect').get_text(timeout=80)
                d.app_stop('com.freevpnintouch')
                d.app_start('com.freevpnintouch')
                while connect == 'CONNECT':
                    d(resourceId='com.freevpnintouch:id/buttonConnect').click()
                    time.sleep(4)
                    connect = d(resourceId='com.freevpnintouch:id/buttonConnect').get_text(timeout=80)
            except:
                pass
        abc = False

    def vpn_cyberghost():
        global nome
        global sobrenome
        global sms
        sms = True
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da CyberGhost', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s {porta} shell pm clear pl.rs.sip.softphone.newapp', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            subprocess.run(f'adb -s {porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            d.app_stop('de.mobileconcepts.cyberghost')
            d.app_start('de.mobileconcepts.cyberghost')
        except:
            pass
        # time.sleep(3)
        d(resourceId='de.mobileconcepts.cyberghost:id/button').click()
        rate = d(resourceId='de.mobileconcepts.cyberghost:id/rate_me_text')
        if rate.exists:
            d(resourceId='android:id/button2').click()
        time.sleep(2)
        d(resourceId='de.mobileconcepts.cyberghost:id/button').click()
        # time.sleep(5)
        subprocess.run(f'adb -s {porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        abc = False

    def vpn_avg():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da AVG', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()
        try:
            subprocess.run(f'adb -s {porta} shell pm clear pl.rs.sip.softphone.newapp', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass

        try:
            subprocess.run(f'adb -s {porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            d.app_stop('com.avg.android.vpn')
            d.app_start("com.avg.android.vpn", "com.avast.android.vpn.app.wizard.WizardActivity")
        except:
            pass
        # subprocess.run(f'adb -s {porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #               stderr=subprocess.DEVNULL, check=True, shell=True)

        time.sleep(30)

    def vpn_windscribe():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da Windscribe', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()

        try:
            subprocess.run(f'adb -s {porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)
            d.app_stop("com.windscribe.vpn")
            d.app_start("com.windscribe.vpn")
        except:
            pass
        d(resourceId='com.windscribe.vpn:id/on_off_button').click()
        time.sleep(10)

    def vpn_hma():
        global nome
        global sobrenome
        global sms
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Alterando IP da HMA', text_color='red')
        window.Refresh()
        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Limpando dados.')
        window.Refresh()
        gerar_id()

        try:
            subprocess.run(f'adb -s {porta} shell pm clear com.instagram.android', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
        except:
            pass
        sms = True
        try:
            # subprocess.run(f'adb shell am start -n com.avg.android.vpn/com.avast.android.vpn.app.wizard.WizardActivity', shell=True)

            d.app_stop("com.hidemyass.hidemyassprovpn")
            time.sleep(3)
            d.app_start('com.hidemyass.hidemyassprovpn', 'com.avast.android.vpn.activity.HmaOnboardingActivity')
        except:
            pass
        time.sleep(10)

    while True:
        window['output'].print(linha_ret)
        window.Refresh()
        try:
            if troca_ip == 5:
                try:
                    troca_ip = 0
                    conteudo = config['vpn']
                    if conteudo == "AVG":
                        vpn_avg()
                    elif conteudo == "SurfShark":
                        vpn_surf()
                    elif conteudo == "Nenhuma":
                        nenhuma_vpn()
                    elif conteudo == "Avast":
                        vpn_avast()
                    elif conteudo == "ExpressVPN":
                        vpn_express()
                    elif conteudo == "PiaVPN":
                        vpn_pia()
                    elif conteudo == "BetterNet":
                        vpn_better()
                    elif conteudo == "CyberGhost":
                        vpn_cyberghost()
                    elif conteudo == "NordVPN":
                        vpn_nord()
                    elif conteudo == "HotspotShield":
                        vpn_hotspotshield()
                    elif conteudo == "WindscribeVPN":
                        vpn_windscribe()
                    elif conteudo == "HmaVPN":
                        vpn_hma()
                    else:
                        window['output'].print(
                            "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
                        window.Refresh()

                except Exception as e:
                    print(e)
                    troca_ip = 0
            nome = fake.first_name()
            sobrenome = fake.last_name()
            if event == sg.WINDOW_CLOSED:
                break
            try:
                # if thread_parar:
                #    break
                try:
                    subprocess.run(f'adb -s {porta} shell pm clear pl.rs.sip.softphone.newapp',
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL, check=True, shell=True)
                except:
                    pass

                senha = config['senha2nr']

                quantidade = 0

                d.app_start('pl.rs.sip.softphone.newapp')
                d.set_fastinput_ime(True)
                try:
                    d(resourceId='pl.rs.sip.softphone.newapp:id/registerButton').click()
                except:
                    d(resourceId='pl.rs.sip.softphone.newapp:id/registerButton').click()
                try:
                    subprocess.run(
                        f'adb -s {porta} shell pm grant pl.rs.sip.softphone.newapp android.permission.READ_CONTACTS',
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                    subprocess.run(
                        f'adb -s {porta} shell pm grant pl.rs.sip.softphone.newapp android.permission.CAMERA',
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                    subprocess.run(
                        f'adb -s {porta} shell pm grant pl.rs.sip.softphone.newapp android.permission.RECORD_AUDIO',
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                    try:
                        subprocess.run(
                            f'adb -s {porta} shell pm grant pl.rs.sip.softphone.newapp android.permission.ACCESS_NOTIFICATION_POLICY',
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                    except:
                        pass

                    subprocess.run(
                        f'adb -s {porta} shell pm grant pl.rs.sip.softphone.newapp android.permission.POST_NOTIFICATIONS',
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                except:
                    pass
                # inbox = Inbox(
                #    address="",
                #    token="",
                # )

                # address = inbox.address
                # token = inbox.token

                # extend the expiration of the inbox by 10 minutes
                # inbox.extend_10m()
                lista_user = random.choices(range(1, 9), k=3)
                nome_completo_s = nome + sobrenome
                numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                user_completo = nome_completo_s + '.' + str(numeros_concatenados)
                # test.register(username=user_completo, password=senha)
                try:
                    inbox = Inbox(
                        address="",
                        token="",
                    )
                    email = inbox.address
                    # window['output'].print("Email: " + email)
                    # window.Refresh()
                except Exception as e:
                    print(e)
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Email: {email}')
                window.Refresh()
                d(resourceId='pl.rs.sip.softphone.newapp:id/inputEmailEditText').set_text(email)
                d(resourceId='pl.rs.sip.softphone.newapp:id/inputPasswordEditText').set_text(senha)
                d(resourceId='pl.rs.sip.softphone.newapp:id/repeat_password_edit_text').set_text(senha)
                d(resourceId='pl.rs.sip.softphone.newapp:id/checkPrivacyPolicy').click()
                d(resourceId='pl.rs.sip.softphone.newapp:id/buttonRegister').click()

                # use with address and token to reuse an existing inbox

                time.sleep(2)

                codigo = None

                # try:
                #    test.start(listener, interval=5)
                #    codigo = 0
                #    while codigo != 5:
                #        time.sleep(2)
                #        codigo = codigo + 1
                # except Exception as e:
                #    if "Too Many Requests" in str(e):
                #        pass
                #    else:
                #        pass

                def listener(message):
                    global nome
                    global sobrenome
                    global cod
                    if '2nr' in message['subject']:

                        urls = re.findall("(?P<url>https?://[^\s]+)",
                                          message['text'] if message['text'] else message['html'])

                        # Acessar cada URL
                        for url in urls:
                            if url.startswith('https://api.2nr.xyz/register/?'):
                                response = requests.get(url)

                                # Verificar o código de status
                                if response.status_code == 200:
                                    pass
                                else:
                                    print(f"Erro ao acessar o link: {response.status_code}")

                subject = False

                def make_request(url):
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            pass
                        else:
                            print(f"Falha na requisição. Código de status: {response.status_code}")
                    except requests.exceptions.RequestException as e:
                        print(f"Erro na requisição: {e}")
                    
                while subject == False:
                    for mail in inbox.mails:
                        time.sleep(10)
                        cod = mail.content
                        if '2nr' in mail.subject:
                            urls = re.findall(r'href=["\']?([^"\'>]+)', mail.content)
                            # Acessar cada URL
                            for url in urls:
                                make_request(url)
                                time.sleep(0.5)
                                # if url.startswith('https://api.2nr.xyz/register/?email'):
                                #    try:
                                #        new_url = url.replace('</p></div>', '')
                                #        print(new_url)
                                #    except:
                                #        pass
                                #    #response = requests.get(new_url)
                                #    d.open_url(new_url)
                                #    # Verificar o código de status
                                #    #if response.status_code == 200:
                                #    #    print('clicou')
                                #    #    d.open_url(new_url)
                                #    #    pass
                                #    #else:
                                #    #    print(f"Erro ao acessar o link: {response.status_code}")
                                #    print('d')
                            subject = True

                troca_ip += 1
                print(f"Email confirmado.")
                d(resourceId='pl.rs.sip.softphone.newapp:id/buttonOk').click()
                d.xpath('//android.widget.LinearLayout[@content-desc="Log in"]/android.widget.TextView').click()
                d(resourceId='pl.rs.sip.softphone.newapp:id/emailEdiText').set_text(email)
                d(resourceId='pl.rs.sip.softphone.newapp:id/passwordEdiText').set_text(senha)
                d(resourceId='pl.rs.sip.softphone.newapp:id/buttonLogin').click()

                d(resourceId='pl.rs.sip.softphone.newapp:id/addNumber').click()
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] 2NR criado com sucesso.',
                                       text_color=('cyan'))
                
                contagem = contagem + 1
                print(f'Contas criadas: {contagem}')
                try:
                    arquivo = open('configuracoes/contas/contas2nr.txt', 'x')
                except FileExistsError:
                    arquivo = open('configuracoes/contas/contas2nr.txt', 'a')

                arquivo.write(email + ' ' + senha + "\n")
                arquivo.close()
                window['quantidade'].update(contagem)
                window.Refresh()
                d(resourceId='pl.rs.sip.softphone.newapp:id/inputNumberName').set_text(
                    random.choice(list(range(1, 100))))
                d(resourceId='pl.rs.sip.softphone.newapp:id/save').click()

                d(resourceId='pl.rs.sip.softphone.newapp:id/buttonAgree').click()
                time.sleep(1)
                d(resourceId='pl.rs.sip.softphone.newapp:id/buttonAgree').click()
                d(resourceId='pl.rs.sip.softphone.newapp:id/save').click()
                success = d(resourceId='pl.rs.sip.softphone.newapp:id/captchaCode').get_text()
                tries = 0
                success = 'Null'
                while success != 'Successful verification' or tries != '30':
                    success = d(resourceId='pl.rs.sip.softphone.newapp:id/captchaCode').get_text()
                    if success == 'Successful verification':
                        break
                    elif success == 'Verification failed':
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Falha no verificação.')
                        window.Refresh()
                        raise Exception('Falha na verificação.')
                    tries += 1
                d(resourceId='pl.rs.sip.softphone.newapp:id/save').click()
                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Número criado com sucesso.',
                                       text_color=('lime'))
                window.Refresh()
                sms = False
                while sms is False:
                    try:
                        try:
                            d(resourceId='pl.rs.sip.softphone.newapp:id/settings').click()
                        except:
                            raise Exception(' ')
                        d(resourceId='pl.rs.sip.softphone.newapp:id/numbers').click()
                        time.sleep(2)
                        d(resourceId='pl.rs.sip.softphone.newapp:id/save').click()
                        try:
                            d(resourceId='pl.rs.sip.softphone.newapp:id/buttonAgree').click()
                        except:
                            raise Exception(' ')
                        time.sleep(1)
                        d(resourceId='pl.rs.sip.softphone.newapp:id/buttonAgree').click()
                        d(resourceId='pl.rs.sip.softphone.newapp:id/save').click()
                        success = d(resourceId='pl.rs.sip.softphone.newapp:id/captchaCode').get_text()
                        tries = 0
                        success = 'Null'
                        while success != 'Successful verification' or tries != '30':
                            success = d(resourceId='pl.rs.sip.softphone.newapp:id/captchaCode').get_text()
                            if success == 'Successful verification':
                                break
                            tries += 1
                        d(resourceId='pl.rs.sip.softphone.newapp:id/save').click()
                        window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Número criado com sucesso.',
                                               text_color=('lime'))
                        window.Refresh()
                        # d(resourceId='pl.rs.sip.softphone.newapp:id/settings').click()
                        # d(resourceId='pl.rs.sip.softphone.newapp:id/settings').click()
                        # d(resourceId='pl.rs.sip.softphone.newapp:id/settings').click()
                        # d(resourceId='pl.rs.sip.softphone.newapp:id/settings').click()
                    except Exception as e:
                        print(e)
                        sms = True


            except Exception as e:
                print(e)
        except Exception as e:
            print(e)


pool = concurrent.futures.ThreadPoolExecutor()
while True:
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {}
    event, values = inicio.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'CREATOR':
        dialog_layout = [
            [sg.Text('Digite a porta:', font=('Open Sans', 10))],
            [sg.Input(key='port', font=('Open Sans', 10))],
            [sg.Button('Avançar', font=('Open Sans', 10), button_color='#1c2024')]
        ]
        try:
            state = config['fixtop']
            if state:
                dialog_window = sg.Window('Digite a porta do emulador.', dialog_layout, keep_on_top=True)
            else:
                dialog_window = sg.Window('Digite a porta do emulador.', dialog_layout, keep_on_top=False)
        except:
            dialog_window = sg.Window('Digite a porta do emulador.', dialog_layout, keep_on_top=False)

        # Loop principal da janela de diálogo
        while True:
            dialog_event, dialog_values = dialog_window.read()

            # Finaliza a janela de diálogo se o usuário fechar a janela
            if dialog_event == sg.WINDOW_CLOSED:
                break

            # Avança para a janela principal se o usuário clicar no botão
            if dialog_event == 'Avançar':
                porta = dialog_values['port']
                break

        dialog_window.close()
        port = porta
        time_img = 'storage\\img\\time.png'
        url = "https://i.ibb.co/5vJ5sQz/time.png"
        filename = 'time.png'
        diretorio = 'storage/img/'  # Diretório onde você deseja verificar a existência do arquivo

        caminho_arquivo = os.path.join(diretorio, filename)

        if not os.path.exists(caminho_arquivo):
            response = requests.get(url)

            if response.status_code == 200:
                image_content = response.content

                with open(caminho_arquivo, 'wb') as image_file:
                    image_file.write(image_content)
                print("Imagem baixada com sucesso.")
            else:
                print("Falha ao baixar a imagem.")
        else:
            pass

        layout = [
            [
                sg.Frame('WNx3 CREATOR', [
                    [sg.Multiline(font=('Open Sans', 10), key='output', size=(50, 15), disabled=True)]
                ], border_width=5, title_location='n')
            ],
            [
                sg.Button('Executar', button_color='#1c2024'),
                sg.Button('Configurações', key='-config-', button_color='#1c2024'),
                sg.Image(filename=check_img, pad=((40, 0), 0)), sg.Text('0', key='total'),
                sg.Image(filename=criada_img, pad=((0, 0), 0)), sg.Text('0', key='criadas'),
                sg.Image(filename=time_img, pad=((0, 0), 0)), sg.Text("00:00:00", key="-TIME-", pad=((0, 0), 0))
            ]
        ]
        try:
            state = config['fixtop']
            if state:
                window = sg.Window(f'CREATOR WNx3 | Porta: {porta}', layout, keep_on_top=True)
            else:
                window = sg.Window(f'CREATOR WNx3 | Porta: {porta}', layout, keep_on_top=False)
        except:
            window = sg.Window(f'CREATOR WNx3 | Porta: {porta}', layout, keep_on_top=False)

        inicio.close()
        while True:
            global parar
            minha_thread = None
            parar = False
            event, values = window.read()

            # Finaliza a janela se o usuário fechar a janela
            if event == sg.WINDOW_CLOSED:

                parar = True
                time_thread.join()
                try:
                    chrome.quit()
                except:
                    pass
                break

            # Executa o código e atualiza a saída na Multiline em tempo real
            if event == 'Executar':
                contagem = 0
                running = True


                def format_time(seconds):
                    hours = seconds // 3600
                    minutes = (seconds % 3600) // 60
                    seconds = seconds % 60
                    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


                #
                def update_time(window):
                    start_time = time.time()  # Armazena o tempo inicial
                    while running:
                        current_time = time.time() - start_time
                        window["-TIME-"].update(format_time(int(current_time)))
                        window['criadas'].update(contagem)
                        window.refresh()  # Atualiza a interface do usuário


                time_thread = threading.Thread(target=update_time, args=(window,))
                time_thread.start()
                # tentativa = False
                if not os.path.exists("credentials.json"):
                    # se o arquivo não existe, pede o nome do arquivo ao usuário e armazena em uma variável global
                    window['output'].print(
                        f'[{datetime.now().strftime("%H:%M:%S")}] Nenhum credentials.json encontrado.')
                    window.Refresh()
                    time.sleep(200)
                else:
                    pass
                try:
                    with open("config.json", "r") as f:
                        config = json.load(f)
                except FileNotFoundError:
                    config = {}

                if 'senha' not in config or config['maquina'] == '':
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Configure o bot primeiro.')
                    window.Refresh()
                    time.sleep(200)
                if '2nr' not in config or config['maquina'] == '':
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Configure o bot primeiro.')
                    window.Refresh()
                    time.sleep(200)
                if config['email'] == '-mailtm-':
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Email selecionado: Mail.TM')
                    window.Refresh()
                    minha_thread = threading.Thread(target=executar_mailtm)
                    minha_thread.start()
                elif config['email'] == '-minuteinbox-':
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Email selecionado: MinuteInBox')
                    window.Refresh()
                    minha_thread = threading.Thread(target=executar_minuteinbox)
                    minha_thread.start()
                elif config['email'] == '-2nr-' and config['app'] == '-instalite-':
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] 2NR selecionado.')
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instagram Lite selecionado.')
                    window.Refresh()
                    minha_thread = threading.Thread(target=executar_2nr)
                    minha_thread.start()
                elif config['email'] == '-2nr-' and config['app'] == '-insta-':
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] 2NR selecionado.')
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instagram selecionado.')
                    window.Refresh()
                    minha_thread = threading.Thread(target=executar_2nr_insta)
                    minha_thread.start()
                elif config['email'] == '-instaface-':
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] InstaFace selecionado.')
                    window.Refresh()

                    try:
                        with open('configuracoes\\config3.json', 'r') as file:
                            config2 = json.load(file)
                    except FileNotFoundError:
                        config2 = {}

                    # Define o layout da janela de diálogo
                    dialog_layout = [
                        [sg.Text('API GoLogin:'), sg.Input(key='-API-', default_text=config2.get('api', ''))],
                        [sg.Text('IP:'), sg.Input(key='-IP-', default_text=config2.get('ip', ''))],
                        [sg.Text('Porta:'), sg.Input(key='-Porta-', default_text=config2.get('porta', ''))],
                        [sg.Text('Usuário:'), sg.Input(key='-Usuario-', default_text=config2.get('usuario', ''))],
                        [sg.Text('Senha:'),
                         sg.Input(key='-Senha-', password_char='*', default_text=config2.get('senha', ''))],
                        [sg.Button('Executar')]
                    ]
                    try:
                        state = config['fixtop']
                        if state:
                            dialog_window = sg.Window('Configurações do iProxy.', dialog_layout, keep_on_top=True)
                        else:
                            dialog_window = sg.Window('Configurações do iProxy.', dialog_layout, keep_on_top=False)
                    except:
                        dialog_window = sg.Window('Configurações do iProxy.', dialog_layout, keep_on_top=False)

                    # Loop principal da janela de diálogo
                    while True:
                        dialog_event, dialog_values = dialog_window.read()

                        # Finaliza a janela de diálogo se o usuário fechar a janela
                        if dialog_event == sg.WINDOW_CLOSED:
                            break

                        # Avança para a janela principal se o usuário clicar no botão
                        if dialog_event == 'Executar':
                            apigologin = dialog_values['-API-']
                            ip = dialog_values['-IP-']
                            porta2 = dialog_values['-Porta-']
                            usuario = dialog_values['-Usuario-']
                            senha2 = dialog_values['-Senha-']
                            config2 = {'api': apigologin, 'ip': ip, 'porta': porta2, 'usuario': usuario,
                                       'senha': senha2}

                            # Salva os valores no arquivo JSON
                            with open('configuracoes\\config3.json', 'w') as file:
                                json.dump(config2, file)

                            break

                            break

                    dialog_window.close()
                    minha_thread = threading.Thread(target=insta_face_lite)
                    minha_thread.start()
                elif config['email'] == '-freesms-' and config['app'] == '-insta-':
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Free SMS selecionado.')
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instagram selecionado.')
                    window.Refresh()
                    minha_thread = threading.Thread(target=free_sms)
                    minha_thread.start()
                elif config['email'] == '-freesmsbeta-' and config['app'] == '-instalite-':
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Free SMS BETA selecionado.')
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instagram Lite selecionado.')
                    window.Refresh()
                    minha_thread = threading.Thread(target=free_sms_lite)
                    minha_thread.start()
                elif config['email'] == '-freesmsbeta-' and config['app'] == '-insta-':
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Free SMS BETA selecionado.')
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Instagram selecionado.')
                    window.Refresh()
                    minha_thread = threading.Thread(target=free_sms_beta)
                    minha_thread.start()
            if event == 'clear':
                window['output'].update('')
                if not os.path.exists("credentials.json"):
                    # se o arquivo não existe, pede o nome do arquivo ao usuário e armazena em uma variável global
                    window['output'].print(
                        f'[{datetime.now().strftime("%H:%M:%S")}] Nenhum credentials.json encontrado.')
                    window.Refresh()
                    time.sleep(200)
                else:
                    pass
                if 'senha' not in config or config['maquina'] == '':
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Configure o bot primeiro.')
                    window.Refresh()
                    time.sleep(200)
            if event == '-config-':
                if os.path.exists('beta'):
                    beta_folder_exists = True
                else:
                    beta_folder_exists = False
                if os.path.exists('wn3'):
                    wn3_folder_exists = True
                else:
                    wn3_folder_exists = False
                layout_configuracoes = [
                    [sg.Text("Senha dos perfis: ", font=('Open Sans', 12)),
                     sg.InputText(key="-senha-", default_text=config.get("senha", ""))],
                    [sg.Text('VPN: ', font=('Open Sans', 12)),
                     sg.Combo(vpn_list, default_value=config.get("vpn", ""), readonly=True, key='-vpn-')],
                    # sg.OptionMenu(vpn_list, size=(7, 19), key="-vpn-", default_value=config.get("vpn", ""))],
                    [sg.Text('Email ou número: ', font=('Open Sans', 12)),
                     sg.Radio('Mail.TM', 'RADIO1', key='-mailtm-', default=config.get("email", "") == "-mailtm-"),
                     sg.Radio('MinuteInBox', 'RADIO1', key='-minuteinbox-',
                              default=config.get("email", "") == "-minuteinbox-"),
                     sg.Radio('2NR', 'RADIO1', key='-2nr-', default=config.get("email", "") == "-2nr-"),
                     sg.Radio('InstaFace Lite', 'RADIO1', key='-instaface-',
                              default=config.get("email", "") == "-instaface-"),
                     sg.Radio('Free SMS', 'RADIO1', visible=beta_folder_exists, key='-freesms-',
                              default=config.get("email", "") == "-freesms-"),
                     sg.Radio('Free SMS BETA', 'RADIO1', visible=beta_folder_exists, key='-freesmsbeta-',
                              default=config.get("email", "") == "-freesmsbeta-")],
                    [sg.Radio('Instagram Lite', 'RADIO2', key='-instalite-',
                              default=config.get("app", "") == "-instalite-"),
                     sg.Radio('Instagram', 'RADIO2', key='-insta-', default=config.get("app", "") == "-insta-")],
                    [sg.HorizontalSeparator()],
                    [sg.Text("Nome da maquina: "), sg.InputText(key="maquina", default_text=config.get("maquina", ""))],
                    [sg.Text("SpreadsheetID: "),
                     sg.InputText(key="spreadsheet", default_text=config.get("spreadsheet", ""))],
                    [sg.Text("Planilha 2NR: "), sg.InputText(key="2nr", default_text=config.get("2nr", ""))],
                    [sg.Button("Salvar", button_color='#1c2024'),
                     sg.Checkbox("Sempre no topo", key="-FIXED_TOP-", enable_events=True,
                                 default=config.get("fixtop", ""))]
                ]

                # Criar a janela da GUI de configuração
                try:
                    state = config['fixtop']
                    if state:
                        janela_configuracoes = sg.Window("Configurações", layout_configuracoes, keep_on_top=True)
                    else:
                        janela_configuracoes = sg.Window("Configurações", layout_configuracoes, keep_on_top=False)
                except:
                    janela_configuracoes = sg.Window("Configurações", layout_configuracoes, keep_on_top=False)
                while True:
                    # janela_configuracoes = sg.Window('Configurações', layout_configuracoes)
                    evento, valores = janela_configuracoes.read()

                    if evento == sg.WINDOW_CLOSED:
                        break

                    if evento == "Salvar":
                        janela_configuracoes.close()
                        if valores["-instalite-"]:
                            app = '-instalite-'
                        elif valores["-insta-"]:
                            app = '-insta-'
                        if valores["-mailtm-"]:
                            email = '-mailtm-'
                        elif valores['-minuteinbox-']:
                            email = '-minuteinbox-'
                        elif valores['-2nr-']:
                            email = '-2nr-'
                        elif valores['-instaface-']:
                            email = '-instaface-'
                        elif valores['-freesms-']:
                            email = '-freesms-'
                        elif valores['-freesmsbeta-']:
                            email = '-freesmsbeta-'

                        # Salvar as configurações em um arquivo JSON
                        config = {
                            "senha": valores["-senha-"],
                            "vpn": valores["-vpn-"],
                            "email": email,
                            "app": app,
                            "maquina": valores['maquina'],
                            "spreadsheet": valores['spreadsheet'],
                            "2nr": valores['2nr'],
                            "fixtop": valores['-FIXED_TOP-']

                        }
                        with open("config.json", "w") as f:
                            json.dump(config, f)
                        # Atualizar os valores padrão dos campos na GUI de configuração
                        layout_configuracoes[1][0].update(value=config.get("senha", ""))
                        layout_configuracoes[2][0].update(value=config.get("vpn", ""))
                        layout_configuracoes[3][0].update(value=config.get("email", ""))
                        layout_configuracoes[4][0].update(value=config.get("app", ""))
                        layout_configuracoes[5][0].update(value=config.get("maquina", ""))
                        layout_configuracoes[6][0].update(value=config.get("spreadsheet", ""))
                        layout_configuracoes[7][0].update(value=config.get("2nr", ""))

    if event == 'CREATOR 2NR':
        contagem = 0
        dialog_layout = [
            [sg.Text('Digite a porta:', font=('Open Sans', 10))],
            [sg.Input(key='port', font=('Open Sans', 10))],
            [sg.Button('Avançar', font=('Open Sans', 10), button_color='#1c2024')]
        ]
        try:
            state = config['fixtop']
            if state:
                dialog_window = sg.Window('Digite a porta do celular.', dialog_layout, keep_on_top=True)
            else:
                dialog_window = sg.Window('Digite a porta do celular.', dialog_layout, keep_on_top=False)
        except:
            dialog_window = sg.Window('Digite a porta do celular.', dialog_layout, keep_on_top=False)

        # Loop principal da janela de diálogo
        while True:
            dialog_event, dialog_values = dialog_window.read()

            # Finaliza a janela de diálogo se o usuário fechar a janela
            if dialog_event == sg.WINDOW_CLOSED:
                break

            # Avança para a janela principal se o usuário clicar no botão
            if dialog_event == 'Avançar':
                porta = dialog_values['port']
                break

        dialog_window.close()
        port = porta
        time_img = 'storage\\img\\time.png'
        url = "https://i.ibb.co/5vJ5sQz/time.png"
        filename = 'time.png'
        diretorio = 'storage/img/'  # Diretório onde você deseja verificar a existência do arquivo

        caminho_arquivo = os.path.join(diretorio, filename)

        if not os.path.exists(caminho_arquivo):
            response = requests.get(url)

            if response.status_code == 200:
                image_content = response.content

                with open(caminho_arquivo, 'wb') as image_file:
                    image_file.write(image_content)
                print("Imagem baixada com sucesso.")
            else:
                print("Falha ao baixar a imagem.")
        else:
            pass

        layout = [
            [
                sg.Frame('WNx3 CREATOR', [
                    [sg.Multiline(font=('Open Sans', 10), key='output', size=(50, 15), disabled=True)]
                ], border_width=5, title_location='n')
            ],
            [
                sg.Button('Executar', button_color='#1c2024'),
                sg.Button('Configurações', key='-config-', button_color='#1c2024'),
                sg.Image(filename=criada_img, pad=((90, 0), 0)), sg.Text('0', key='quantidade'),
                sg.Image(filename=time_img, pad=((0, 0), 0)), sg.Text("00:00:00", key="-TIME-", pad=((0, 0), 0))
            ]
        ]
        window = sg.Window(f'CREATOR 2NR WNx3 | Porta: {porta}', layout, keep_on_top=False)

        inicio.close()
        while True:
            global thread_parar
            minha_thread = None
            parar = False
            event, values = window.read()

            # Finaliza a janela se o usuário fechar a janela
            if event == sg.WINDOW_CLOSED:
                parar = True
                time_thread.join()
                break

            # Executa o código e atualiza a saída na Multiline em tempo real
            if event == 'Executar':
                contagem = 0
                running = True


                def format_time(seconds):
                    hours = seconds // 3600
                    minutes = (seconds % 3600) // 60
                    seconds = seconds % 60
                    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


                #
                def update_time(window):
                    start_time = time.time()  # Armazena o tempo inicial
                    while running:
                        current_time = time.time() - start_time
                        window["-TIME-"].update(format_time(int(current_time)))
                        #window['criadas'].update(contagem)
                        window.refresh()  # Atualiza a interface do usuário


                time_thread = threading.Thread(target=update_time, args=(window,))
                time_thread.start()
                # tentativa = False
                if not os.path.exists("credentials.json"):
                    # se o arquivo não existe, pede o nome do arquivo ao usuário e armazena em uma variável global
                    window['output'].print(
                        f'[{datetime.now().strftime("%H:%M:%S")}] Nenhum credentials.json encontrado.')
                    window.Refresh()
                    time.sleep(200)
                else:
                    pass

                contagem = 0
                thread_parar = False
                window['Executar'].update(disabled=True)
                window['output'].print(f'Bot iniciado.')
                window.Refresh()
                try:
                    with open("config2nr.json", "r") as f:
                        config = json.load(f)
                except FileNotFoundError:
                    config = {}

                minha_thread = threading.Thread(target=executar_creator_2nr)
                minha_thread.start()
            if event == 'clear':
                window['output'].update('')
                if not os.path.exists("credentials.json"):
                    # se o arquivo não existe, pede o nome do arquivo ao usuário e armazena em uma variável global
                    window['output'].print(
                        f'[{datetime.now().strftime("%H:%M:%S")}] Nenhum credentials.json encontrado.')
                    window.Refresh()
                    time.sleep(200)
                else:
                    pass
                if 'senha' not in config or config['maquina'] == '':
                    window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Configure o bot primeiro.')
                    window.Refresh()
                    time.sleep(200)
            if event == '-config-':
                layout_configuracoes = [
                    [sg.Text("Senha dos perfis: ", font=('Open Sans', 12)),
                     sg.InputText(key="-senha2nr-", default_text=config.get("senha2nr", "@SenhaPadrao2023"))],
                    [sg.Text('VPN: ', font=('Open Sans', 12)),
                     sg.Combo(vpn_list, default_value=config.get("vpn", ""), readonly=True, key='-vpn-')],
                    [sg.Button("Salvar")]
                ]

                # Criar a janela da GUI de configuração
                janela_configuracoes = sg.Window("Configurações", layout_configuracoes)

                while True:
                    # janela_configuracoes = sg.Window('Configurações', layout_configuracoes)
                    evento, valores = janela_configuracoes.read()

                    if evento == sg.WINDOW_CLOSED:
                        thread_parar = True
                        break

                    if evento == "Salvar":
                        # Salvar as configurações em um arquivo JSON
                        config = {
                            "senha2nr": valores['-senha2nr-'],
                            "vpn": valores["-vpn-"]
                        }
                        with open("config2nr.json", "w") as f:
                            json.dump(config, f)

                        # Atualizar os valores padrão dos campos na GUI de configuração
                    janela_configuracoes.close()
    if event == 'DIVISOR':
        inicio.close()
        import PySimpleGUI as sg

        try:
            import pyperclip
        except ModuleNotFoundError:
            import subprocess
            import sys

            subprocess.run(['venv/scripts/activate.bat'], shell=True)
            subprocess.run(['pip', 'install', 'pyperclip'])
            subprocess.run(['deactivate'], shell=True)
            from google.oauth2.credentials import Credentials
            from googleapiclient.discovery import build
            from googleapiclient.errors import HttpError
            import pyperclip


        def dividir_lista(lista, num_partes):
            tam_parte = len(lista) // num_partes
            resto = len(lista) % num_partes
            partes = []
            inicio = 0
            for i in range(num_partes):
                tam = tam_parte + 1 if i < resto else tam_parte
                partes.append(lista[inicio:inicio + tam])
                inicio += tam
            return partes


        sg.theme("DarkGrey14")

        layout = [
            [sg.Text("Insira as contas:")],
            [sg.Multiline(size=(50, 10), key="-CONTA_INPUT-")],
            [sg.Radio('SC', 'RADIO1', key='-sc-'), sg.Radio('NextGen', 'RADIO1', key='-next-')],
            [sg.Text("Insira quantas abas:")],
            [sg.Slider(range=(1, 10), orientation="h", size=(40, 15), default_value=1, key="-NUM_PARTES-")],
            [sg.Button("Dividir", button_color='#1c2024')],
        ]

        janela = sg.Window("Divisor", layout)

        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == "Dividir" and valores['-sc-'] is True:
                lista_contas = valores["-CONTA_INPUT-"].strip().split("\n")
                num_partes = int(valores["-NUM_PARTES-"])
                partes = dividir_lista(lista_contas, num_partes)
                for i in range(num_partes):
                    partes[i] = "\n".join(partes[i]).replace(" ", "\n")
                layout_resultado = []
                for i in range(num_partes):
                    layout_resultado.append([
                        sg.Multiline(size=(50, 5), key=f"-CONTA_OUTPUT{i + 1}-", disabled=True),
                        sg.Button("Copiar", key=f"-COPY{i + 1}-", button_color='#1c2024')
                    ])
                window_resultado = sg.Window("Resultado", layout_resultado)
                window_resultado.finalize()
                for i in range(num_partes):
                    window_resultado[f"-CONTA_OUTPUT{i + 1}-"].update(value=partes[i])
                while True:
                    evento_resultado, valores_resultado = window_resultado.read()
                    if evento_resultado == sg.WINDOW_CLOSED:
                        break
                    for i in range(num_partes):
                        if evento_resultado == f"-COPY{i + 1}-":
                            pyperclip.copy(partes[i])
                window_resultado.close()
            elif evento == "Dividir" and valores['-next-'] is True:
                lista_contas = valores["-CONTA_INPUT-"].strip().split("\n")
                num_partes = int(valores["-NUM_PARTES-"])
                partes = dividir_lista(lista_contas, num_partes)
                for i in range(num_partes):
                    partes[i] = "\n".join(partes[i])
                layout_resultado = []
                for i in range(num_partes):
                    layout_resultado.append([
                        sg.Multiline(size=(50, 5), key=f"-CONTA_OUTPUT{i + 1}-", disabled=True),
                        sg.Button("Copiar", key=f"-COPY{i + 1}-", button_color='#1c2024')
                    ])
                window_resultado = sg.Window("Resultado", layout_resultado)
                window_resultado.finalize()
                for i in range(num_partes):
                    window_resultado[f"-CONTA_OUTPUT{i + 1}-"].update(value=partes[i])
                while True:
                    evento_resultado, valores_resultado = window_resultado.read()
                    if evento_resultado == sg.WINDOW_CLOSED:
                        break
                    for i in range(num_partes):
                        if evento_resultado == f"-COPY{i + 1}-":
                            pyperclip.copy(partes[i])
                window_resultado.close()
    if event == 'CRIAR POR CIMA':
        dialog_layout = [
            [sg.Text('Digite a porta:', font=('Open Sans', 10))],
            [sg.Input(key='port', font=('Open Sans', 10))],
            [sg.Button('Avançar', font=('Open Sans', 10), button_color='#1c2024')]
        ]

        dialog_window = sg.Window('Digite a porta do emulador.', dialog_layout)

        # Loop principal da janela de diálogo
        while True:
            dialog_event, dialog_values = dialog_window.read()

            # Finaliza a janela de diálogo se o usuário fechar a janela
            if dialog_event == sg.WINDOW_CLOSED:
                break

            # Avança para a janela principal se o usuário clicar no botão
            if dialog_event == 'Avançar':
                porta = dialog_values['port']
                break

        dialog_window.close()
        port = porta
        layoutporcima = [
            [
                sg.Frame('WNx3 CREATOR', [
                    [sg.Multiline(font=('Open Sans', 10), key='output', size=(50, 15), disabled=True)]
                ], border_width=5, title_location='n')
            ],
            [
                sg.Button('Executar', button_color='#1c2024'),
                sg.Button('Reiniciar', key='clear', disabled=True, button_color='#1c2024'),
                sg.Button('Configurações', key='-config-', button_color='#1c2024'),
                sg.Image(filename=check_img, pad=((0, 0), 0)), sg.Text('0', key='total'),
                sg.Image(filename=criada_img, pad=((0, 0), 0)), sg.Text('0', key='criadas')
            ]
        ]
        window = sg.Window(f'CREATOR WNx3 | Porta: {porta}', layoutporcima)
        inicio.close()
        while True:
            event, values = window.read()

            # Finaliza a janela se o usuário fechar a janela
            if event == sg.WINDOW_CLOSED:
                minha_thread.stop()
                break

            # Executa o código e atualiza a saída na Multiline em tempo real
            if event == 'Executar':
                contagem = 0
                # tentativa = False
                if not os.path.exists("credentials.json"):
                    # se o arquivo não existe, pede o nome do arquivo ao usuário e armazena em uma variável global
                    window['output'].print(
                        f'[{datetime.now().strftime("%H:%M:%S")}] Nenhum credentials.json encontrado.')
                    window.Refresh()
                    time.sleep(200)
                else:
                    pass
                try:
                    with open("configuracoes/config2.json", "r") as f:
                        config2 = json.load(f)
                except FileNotFoundError:
                    config2 = {}

                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Iniciando criação.')
                window.Refresh()
                minha_thread = threading.Thread(target=criarporcima)
                minha_thread.start()

            if event == '-config-':
                try:
                    with open("configuracoes/config2.json", "r") as f:
                        config2 = json.load(f)
                except FileNotFoundError:
                    config2 = {}
                layout_configuracoes = [
                    [sg.Text("Senha dos perfis: ", font=('Open Sans', 12)),
                     sg.InputText(key="-senha-", default_text=config2.get("senha", ""))],
                    [sg.Text('VPN: ', font=('Open Sans', 12)),
                     sg.Combo(vpn_list, default_value=config2.get("vpn", ""), readonly=True, key='-vpn-')],
                    [sg.HorizontalSeparator()],
                    [sg.Text("Nome da maquina: "),
                     sg.InputText(key="maquina", default_text=config2.get("maquina", ""))],
                    [sg.Text("SpreadsheetID: "),
                     sg.InputText(key="spreadsheet", default_text=config2.get("spreadsheet", ""))],
                    [sg.Text("Planilha com as contas: "),
                     sg.InputText(key="contas_por_cima", default_text=config2.get("contas_por_cima", ""))],
                    [sg.Button("Salvar", button_color='#1c2024')]
                ]

                # Criar a janela da GUI de configuração
                janela_configuracoes = sg.Window("Configurações", layout_configuracoes)

                while True:
                    # janela_configuracoes = sg.Window('Configurações', layout_configuracoes)
                    evento, valores = janela_configuracoes.read()

                    if evento == sg.WINDOW_CLOSED:
                        break

                    if evento == "Salvar":
                        # Salvar as configurações em um arquivo JSON
                        config2 = {
                            "senha": valores["-senha-"],
                            "vpn": valores["-vpn-"],
                            "maquina": valores['maquina'],
                            "spreadsheet": valores['spreadsheet'],
                            "contas_por_cima": valores['contas_por_cima']
                        }

                        # Salvar a lista de dicionários em um arquivo JSON
                        with open("configuracoes/config2.json", "w") as f:
                            json.dump(config2, f)

                        # Atualizar os valores padrão dos campos na GUI de configuração
                        layout_configuracoes[1][0].update(value=config2.get("senha", ""))
                        layout_configuracoes[2][0].update(value=config2.get("vpn", ""))
                        layout_configuracoes[3][0].update(value=config2.get("maquina", ""))
                        layout_configuracoes[4][0].update(value=config2.get("spreadsheet", ""))
                        layout_configuracoes[5][0].update(value=config2.get("contas_por_cima", ""))

                    janela_configuracoes.close()

    if event == 'MONTADOR':

        layoutporcima = [
            [
                sg.Frame('WNx3 CREATOR', [
                    [sg.Multiline(font=('Open Sans', 10), key='output', size=(50, 15), disabled=True)]
                ], border_width=5, title_location='n')
            ],
            [
                sg.Button('Executar', button_color='#1c2024'),
                sg.Button('Configurações', key='-config-', button_color='#1c2024'),
                sg.Image(filename=check_img, pad=((0, 0), 0)), sg.Text('0', key='total'),
                sg.Image(filename=criada_img, pad=((0, 0), 0)), sg.Text('0', key='criadas')
            ]
        ]
        window = sg.Window(f'CREATOR WNx3 | MONTADOR', layoutporcima)
        inicio.close()
        while True:
            event, values = window.read()

            # Finaliza a janela se o usuário fechar a janela
            if event == sg.WINDOW_CLOSED:
                minha_thread.stop()
                break

            # Executa o código e atualiza a saída na Multiline em tempo real
            if event == 'Executar':
                contagem = 0
                # tentativa = False
                if not os.path.exists("credentials.json"):
                    # se o arquivo não existe, pede o nome do arquivo ao usuário e armazena em uma variável global
                    window['output'].print(
                        f'[{datetime.now().strftime("%H:%M:%S")}] Nenhum credentials.json encontrado.')
                    window.Refresh()
                    time.sleep(200)
                else:
                    pass
                try:
                    with open("configuracoes/config2.json", "r") as f:
                        config2 = json.load(f)
                except FileNotFoundError:
                    config2 = {}

                try:
                    with open('configuracoes\\config5.json', 'r') as file:
                        config5 = json.load(file)
                except FileNotFoundError:
                    config5 = {}

                # Define o layout da janela de diálogo
                dialog_layout = [
                    [sg.Text('Tema das fotos:'), sg.Input(key='tema', default_text=config5.get('tema', ''))],
                    [sg.Text("Quantidade de fotos: "),
                     sg.Slider(range=(1, 12), orientation='h', default_value=config5.get("qtdfotos", ""),
                               key='qtdfotos')],
                    [sg.Multiline(size=(30, 10), key='contas', autoscroll=True)],
                    [sg.Button('Executar')]
                ]
                try:
                    state = config['fixtop']
                    if state:
                        dialog_window = sg.Window('Configurações do iProxy.', dialog_layout, keep_on_top=True)
                    else:
                        dialog_window = sg.Window('Configurações do iProxy.', dialog_layout, keep_on_top=False)
                except:
                    dialog_window = sg.Window('Configurações do iProxy.', dialog_layout, keep_on_top=False)

                # Loop principal da janela de diálogo
                lines = []  # Lista para armazenar as linhas digitadas
                line_index = 0
                while True:
                    dialog_event, dialog_values = dialog_window.read()

                    # Finaliza a janela de diálogo se o usuário fechar a janela
                    if dialog_event == sg.WINDOW_CLOSED:
                        break

                    # Avança para a janela principal se o usuário clicar no botão
                    if dialog_event == 'Executar':
                        lines.extend(dialog_values['contas'].splitlines(keepends=True))
                        tema = dialog_values['tema']
                        qtdfotos = dialog_values['qtdfotos']
                        contas = dialog_values['contas']
                        config4 = {'tema': tema, 'qtdfotos': qtdfotos}

                        # Salva os valores no arquivo JSON
                        config5 = {
                            "tema": dialog_values["tema"],
                            "qtdfotos": dialog_values['qtdfotos']

                        }
                        with open('configuracoes\\config5.json', 'w') as file:
                            json.dump(config5, file)

                        break

                dialog_window.close()

                window['output'].print(f'[{datetime.now().strftime("%H:%M:%S")}] Iniciando montagem.')
                window.Refresh()
                for username in lines:
                    print(username)
                    time.sleep(5)
                minha_thread = threading.Thread(target=montador)
                minha_thread.start()

            if event == '-config-':
                try:
                    with open("configuracoes/config4.json", "r") as f:
                        config4 = json.load(f)
                except FileNotFoundError:
                    config4 = {}
                layout_configuracoes = [
                    [sg.Text("Tempo entre ações:", font=('Open Sans', 12))],
                    [sg.Text("MIN: "),
                     sg.Slider(range=(0, 50), orientation='h', default_value=config4.get("min", ""), key='min')],
                    [sg.Text("MAX: "),
                     sg.Slider(range=(1, 60), orientation='h', default_value=config4.get("max", ""), key='max')],

                    [sg.HorizontalSeparator()],
                    [sg.Text("Nome da maquina: "),
                     sg.InputText(key="maquina", default_text=config4.get("maquina", ""))],
                    [sg.Text("SpreadsheetID: "),
                     sg.InputText(key="spreadsheet", default_text=config4.get("spreadsheet", ""))],
                    [sg.Text("Planilha com as contas: "),
                     sg.InputText(key="contas_vazias", default_text=config4.get("planilha_contas", ""))],
                    [sg.Text("Planilha onde será salvo: "),
                     sg.InputText(key="contas_montadas", default_text=config4.get("planilha_montadas", ""))],

                    [sg.Button("Salvar", button_color='#1c2024')]
                ]

                windowconfig = sg.Window('Configurações', layout_configuracoes)

                while True:
                    event, values = windowconfig.read()
                    if event == sg.WINDOW_CLOSED:
                        break
                    if event == 'Salvar':
                        config4 = {
                            "min": values.get("min", 0),
                            "max": values.get("max", 1),
                            "maquina": values.get('maquina', ''),
                            "spreadsheet": values.get('spreadsheet', ''),
                            "planilha_contas": values.get('contas_vazias', ''),
                            "planilha_montadas": values.get('contas_montadas', '')
                        }
                        # Exemplo de como acessar os valores selecionados:
                        tempo_entre_acoes_min = values.get("min", 0)
                        tempo_entre_acoes_max = values.get("max", 1)
                        nome_maquina = values.get('maquina', '')
                        spreadsheet_id = values.get('spreadsheet', '')
                        planilha_contas = values.get('contas_vazias', '')
                        planilha_montadas = values.get('contas_montadas', '')

                        print('Tempo entre ações min:', tempo_entre_acoes_min)
                        print('Tempo entre ações max:', tempo_entre_acoes_max)
                        print('Nome da máquina:', nome_maquina)
                        print('SpreadsheetID:', spreadsheet_id)
                        print('Planilha com as contas:', planilha_contas)
                        print('Planilha com as contas montadas:', planilha_montadas)

                        # Salvar as configurações em um arquivo JSON
                        with open("configuracoes/config4.json", "w") as f:
                            json.dump(config4, f)

                        windowconfig.close()

inicio.close()