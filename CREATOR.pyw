import json

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

    sg.theme('Dark')
    layout = [[sg.Text("Bot atualizado com sucesso.", font=('Open Sans', 10))],
              [sg.Text("Abra novamente.", font=('Open Sans', 10))],
              [sg.Button("OK")]]
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

    sg.theme('Dark')
    layout = [[sg.Text("Bot atualizado com sucesso.", font=('Open Sans', 10))],
              [sg.Text("Abra novamente.", font=('Open Sans', 10))],
              [sg.Button("OK")]]
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

    sg.theme('Dark')
    layout = [[sg.Text("Bot atualizado com sucesso.", font=('Open Sans', 10))],
              [sg.Text("Abra novamente.", font=('Open Sans', 10))],
              [sg.Button("OK")]]
    window = sg.Window("Atualização", layout)
    event, values = window.read()
    window.close()

from datetime import datetime
import time

now = datetime.now()
hora = now.strftime("[%H:%M:%S] ")

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

    sg.theme('Dark')
    layout = [[sg.Text("Bot atualizado com sucesso.", font=('Open Sans', 10))],
              [sg.Text("Abra novamente.", font=('Open Sans', 10))],
              [sg.Button("OK")]]
    window = sg.Window("Atualização", layout)
    event, values = window.read()
    window.close()

base_url = 'https://raw.githubusercontent.com/wnx3/Creator2.0/main/'

#Lista de arquivos que você deseja verificar e atualizar
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
        sg.theme('Dark')
        layout = [[sg.Text("Bot atualizado com sucesso.", font=('Open Sans', 10))],
                  [sg.Text("Abra novamente.", font=('Open Sans', 10))],
                  [sg.Button("OK")]]
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

    sg.theme('Dark')
    layout = [[sg.Text("Bot atualizado com sucesso.", font=('Open Sans', 10))],
              [sg.Text("Abra novamente.", font=('Open Sans', 10))],
              [sg.Button("OK")]]
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
    sg.theme('Dark')
    layout = [[sg.Text("Arquivo credentials.json não encontrado.", font=('Open Sans', 10))],
              [sg.Button("OK")]]
    window = sg.Window("Erro", layout)
    event, values = window.read()
    window.close()

sg.theme('Dark')
# Define a janela de diálogo com um input e um botão
dialog_layout = [
    [sg.Text('Digite a porta:', font=('Open Sans', 10))],
    [sg.Input(key='port', font=('Open Sans', 10))],
    [sg.Button('Avançar', font=('Open Sans', 10))]
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
sg.theme('Dark')
sg.SetOptions(font=('Open Sans', 10))
# Define a janela com uma Multiline e um botão
check_img = 'storage\\img\\total.png'
criada_img = 'storage\\img\\check.png'
#config_img = 'storage/img/config.png'
layout = [
    [
        sg.Frame('WNx3 CREATOR', [
            [sg.Multiline(font=('Open Sans', 10), key='output', size=(50, 15), disabled=True)]
        ], border_width=10, title_location='n')
    ],
    [
        sg.Button('Executar'), sg.Button('Reiniciar', key='clear', disabled=True),
        sg.Button('Configurações', key='-config-'),
        sg.Image(filename=check_img, pad=((0, 0), 0)), sg.Text('0', key='total'),
        sg.Image(filename=criada_img, pad=((0, 0), 0)), sg.Text('0', key='criadas')
    ]
]

window = sg.Window(f'CREATOR WNx3 | Porta: {porta}', layout)

vpn_list = ["AVG", "Avast", "SurfShark", "ExpressVPN", "PiaVPN", "BetterNet", "NordVPN", "CyberGhost", "HotspotShield"]
# Definir o layout da GUI de configuração
layout_configuracoes = [
    [sg.Text("Senha dos perfis: ", font=('Open Sans', 12)),
     sg.InputText(key="-senha-", default_text=config.get("senha", ""))],
    [sg.Text('VPN: ', font=('Open Sans', 12)),
     sg.OptionMenu(vpn_list, size=(7, 19), key="-vpn-", default_value=config.get("vpn", ""))],
    [sg.Text('Email ou número: ', font=('Open Sans', 12)),
     sg.Radio('Mail.TM', 'RADIO1', key='-mailtm-', default=config.get("email", "") == "-mailtm-"),
     sg.Radio('MinuteInBox', 'RADIO1', key='-minuteinbox-', default=config.get("email", "") == "-minuteinbox-"),
     sg.Radio('2NR', 'RADIO1', key='-2nr-', default=config.get("email", "") == "-2nr-")],
    [sg.Radio('Instagram Lite', 'RADIO2', key='-instalite-', default=config.get("app", "") == "-instalite-"),
     sg.Radio('Instagram', 'RADIO2', key='-insta-', default=config.get("app", "") == "-insta-")],
    [sg.HorizontalSeparator()],
    [sg.Text("Nome da maquina: "), sg.InputText(key="maquina", default_text=config.get("maquina", ""))],
    [sg.Text("SpreadsheetID: "), sg.InputText(key="spreadsheet", default_text=config.get("spreadsheet", ""))],
    [sg.Text("Planilha 2NR: "), sg.InputText(key="2nr", default_text=config.get("2nr", ""))],
    [sg.Button("Salvar")]
]

# Criar a janela da GUI de configuração
janela_configuracoes = sg.Window("Configurações", layout_configuracoes)

contagem = 0
def contagem():
    global nome
    global sobrenome
    contagem += 1
    window['contagem'].update(contagem)
    window.Refresh()




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
        window['output'].print('Instalando dependências...')
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
    # SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    def vpn_avast():
        global nome
        global sobrenome
        global sms
        window['output'].print('SMS\nAlterando IP da Avast', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
        window['output'].print('SMS\nAlterando IP da HotspotShield', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
        window['output'].print('SMS\nAlterando IP da PiaVPN', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
        window['output'].print('SMS\nAlterando IP da ExpressVPN', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
        window['output'].print('SMS\nAlterando IP da NordVPN', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
        window['output'].print('SMS\nAlterando IP da SurfShark', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

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
        window['output'].print('SMS\nAlterando IP da BetterNet', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
        window['output'].print('SMS\nAlterando IP da CyberGhost', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
        window['output'].print('SMS\nAlterando IP da AVG', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
        lista_user = random.choices(range(1, 9), k=3)
        with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
            nomes = nomes_arquivo.readlines()

        with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
            sobrenomes = sobrenomes_arquivo.readlines()

        nome = random.choice(nomes).strip()
        sobrenome = random.choice(sobrenomes).strip()
        nome_completo = nome + ' ' + sobrenome
        nome_completo_s = nome + sobrenome
        numeros_concatenados = ''.join(str(numero) for numero in lista_user)
        user_completo = nome_completo_s + '.' + str(numeros_concatenados)
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
                window['output'].print('Erro.')
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
        window['output'].print('Aguardando codigo...')
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
            window['output'].print('Instagram fechou')
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
        #    window['output'].print('Enviando um novo codigo.')
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
        lista_user = random.choices(range(1, 9), k=3)
        with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
            nomes = nomes_arquivo.readlines()

        with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
            sobrenomes = sobrenomes_arquivo.readlines()

        nome = random.choice(nomes).strip()
        sobrenome = random.choice(sobrenomes).strip()
        nome_completo = nome + ' ' + sobrenome
        nome_completo_s = nome + sobrenome
        numeros_concatenados = ''.join(str(numero) for numero in lista_user)
        user_completo = nome_completo_s + '.' + str(numeros_concatenados)

        test = Email()
        arquivo = open('configuracoes/contas/senha_perfis.txt')
        senha = arquivo.read()
        test.register(username=user_completo, password=senha)
        window['output'].print("Email: " + str(test.address))
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

        window['output'].print('Aguardando codigo...')
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
            window['output'].print('Erro encontrado.')
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
            window['output'].print('Erro encontrado.')
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
                    window['output'].print('Erro fechado.')
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
                subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, shell=True)

                window.Refresh()
                break
            nome_completo = nome + ' ' + sobrenome
            nome_completo_s = nome + sobrenome
            numeros_concatenados = ''.join(str(numero) for numero in lista_user)
            user_completo = nome_completo_s + '.' + str(numeros_concatenados)
            window.Refresh()
            window['output'].print('Nome escolhido: ' + nome_completo)
            window.Refresh()
            try:
                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[1]'))).send_keys(
                    nome_completo)
            except:
                cont = False
                window['output'].print('Erro encontrado.')
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
            window['output'].print(f'Idade escolhida: {idade_aleatoria}')
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
                    window['output'].print('Erro ao criar')
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
                window['output'].print(f'Usuário: {user_completo}')
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
                    window['output'].print('Tentando gerar novamente')
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
            window['output'].print('Verificando...')
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
                    window['output'].print('Conta criada com sucesso.', text_color=('lime'))
                    window.Refresh()
                    contagem += 1
                    window['criadas'].update(contagem)
                    window.Refresh()
                    now = datetime.now()
                    now_brasilia = tz.localize(now)
                    timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")
                    
                    scope = ['https://www.googleapis.com/auth/spreadsheets']
                    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                    client = gspread.authorize(creds)

                    spreadsheet_id = config['spreadsheet']
                    sheet_name = 'contas'
                    # Insert user, password, and timestamp into first empty row
                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                    values = sheet.col_values(1)
                    last_row = len(values)
                    values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                    cell_list = sheet.range(f'A{last_row+1}:E{last_row+1}')
                    for i, val in enumerate(values):
                        cell_list[i].value = val
                    sheet.update_cells(cell_list)
                    

                    rows = sheet.get_all_values()

                    # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                    regex = re.compile(r'^.*\.\d{3}\s.*$')

                    # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                    num_rows = sum(1 for row in rows if regex.match(row[0]))
                    window['total'].update(num_rows)

                    scope = ['https://www.googleapis.com/auth/spreadsheets']
                    creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                    client = gspread.authorize(creds)

                    spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                    sheet_name = 'relatorio_geral'
                    # Insert user, password, and timestamp into first empty row
                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                    values = sheet.col_values(1)
                    last_row = len(values)
                    values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                    cell_list = sheet.range(f'A{last_row+1}:E{last_row+1}')
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

    window['output'].print(f'Senha sendo utilizada: {senha}')
    window.Refresh()

    console = Console()

    device = [
        {'name': 'Bluestacks1', 'port': porta, 'udid': f'127.0.0.1:{porta}'},
    ]
    comando = f"adb connect 127.0.0.1:{porta}"
    subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
    subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test', stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server', stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)

    gerar_id()
    android_id = gerar_id()
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    time.sleep(2)
    # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True, stdout=subprocess.DEVNULL,
    #               stderr=subprocess.DEVNULL)
    window.Refresh()
    window['output'].print('Iniciando criação.\n')
    window.Refresh()
    cont = True
    while cont is True:

        window['output'].print(linha_ret)
        window.Refresh()
        window['output'].print('Abrindo Instagram')

        scope = ['https://www.googleapis.com/auth/spreadsheets']
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
        regex = re.compile(r'^.*\.\d{3}\s.*$')

        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
        num_rows = sum(1 for row in rows if regex.match(row[0]))
        window['total'].update(num_rows)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test',
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        window.Refresh()
        # try:
        #    subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
            desired_caps['appPackage'] = 'com.instagram.lite'
            desired_caps['appActivity'] = 'com.facebook.lite.MainActivity'
            desired_caps['systemPort'] = random.randint(6000, 8299)
            desired_caps['noReset'] = True
            desired_caps['app'] = appinsta

            driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

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
                window['output'].print('Erro fechado.')
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
                    window['output'].print('Pop-up fechado.')
                    window.Refresh()
                    time.sleep(1)
                firts_reg()

            except Exception as e:
                print(e)
                sms = True
                comando = f"adb connect 127.0.0.1:{porta}"
                subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, shell=True)
                window['output'].print('Erro não catalogado.')
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
                    window['output'].print('Criação de outro perfil.')
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
                    lista_user = random.choices(range(1, 9), k=3)
                    with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                        nomes = nomes_arquivo.readlines()

                    with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                        sobrenomes = sobrenomes_arquivo.readlines()

                    nome = random.choice(nomes).strip()
                    sobrenome = random.choice(sobrenomes).strip()
                    nome_completo = nome + sobrenome
                    numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                    user_completo = nome_completo + '.' + str(numeros_concatenados)
                    window['output'].print('Usuário: ' + user_completo)
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

                    window['output'].print('Verificando...')
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
                        window['output'].print('Conta criada com sucesso.', text_color=('lime'))
                        contagem += 1
                        window['criadas'].update(contagem)
                        window.Refresh()
                        window.Refresh()
                        now = datetime.now()
                        now_brasilia = tz.localize(now)
                        timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")
                        
                        scope = ['https://www.googleapis.com/auth/spreadsheets']
                        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                        client = gspread.authorize(creds)

                        spreadsheet_id = config['spreadsheet']
                        sheet_name = 'contas'
                        # Insert user, password, and timestamp into first empty row
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                        values = sheet.col_values(1)
                        last_row = len(values)
                        values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                        cell_list = sheet.range(f'A{last_row+1}:E{last_row+1}')
                        for i, val in enumerate(values):
                            cell_list[i].value = val
                        sheet.update_cells(cell_list)
                        

                        rows = sheet.get_all_values()

                        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                        regex = re.compile(r'^.*\.\d{3}\s.*$')

                        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                        num_rows = sum(1 for row in rows if regex.match(row[0]))
                        window['total'].update(num_rows)

                        scope = ['https://www.googleapis.com/auth/spreadsheets']
                        creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                        client = gspread.authorize(creds)

                        spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                        sheet_name = 'relatorio_geral'
                        # Insert user, password, and timestamp into first empty row
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                        values = sheet.col_values(1)
                        last_row = len(values)
                        values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                        cell_list = sheet.range(f'A{last_row+1}:E{last_row+1}')
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
                        window['output'].print('Alterando perfil para publico.')
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
                        window['output'].print('Alterado para publico.')
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
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test',
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, shell=True)
            comando = f"adb connect 127.0.0.1:{porta}"
            subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, shell=True)
            window['output'].print('Erro não catalogado.')
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
        window['output'].print('Instalando dependências...')
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
    # SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    def vpn_avast():
        global nome
        global sobrenome
        global sms
        window['output'].print('SMS\nAlterando IP da Avast', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
        window['output'].print('SMS\nAlterando IP da HotspotShield', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
        window['output'].print('SMS\nAlterando IP da PiaVPN', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
        window['output'].print('SMS\nAlterando IP da ExpressVPN', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
        window['output'].print('SMS\nAlterando IP da NordVPN', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
        window['output'].print('SMS\nAlterando IP da SurfShark', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)

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
        window['output'].print('SMS\nAlterando IP da BetterNet', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
        window['output'].print('SMS\nAlterando IP da CyberGhost', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
        window['output'].print('SMS\nAlterando IP da AVG', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
        lista_user = random.choices(range(1, 9), k=3)
        with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
            nomes = nomes_arquivo.readlines()

        with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
            sobrenomes = sobrenomes_arquivo.readlines()

        nome = random.choice(nomes).strip()
        sobrenome = random.choice(sobrenomes).strip()
        nome_completo = nome + ' ' + sobrenome
        nome_completo_s = nome + sobrenome
        numeros_concatenados = ''.join(str(numero) for numero in lista_user)
        user_completo = nome_completo_s + '.' + str(numeros_concatenados)

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
                window['output'].print('Erro.')
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
        window['output'].print('Aguardando codigo...')
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
            window['output'].print('Instagram fechou')
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
        #    window['output'].print('Enviando um novo codigo.')
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
        lista_user = random.choices(range(1, 9), k=3)
        with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
            nomes = nomes_arquivo.readlines()

        with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
            sobrenomes = sobrenomes_arquivo.readlines()

        nome = random.choice(nomes).strip()
        sobrenome = random.choice(sobrenomes).strip()
        nome_completo = nome + ' ' + sobrenome
        nome_completo_s = nome + sobrenome
        numeros_concatenados = ''.join(str(numero) for numero in lista_user)
        user_completo = nome_completo_s + '.' + str(numeros_concatenados)

        inbox = Inbox(
            address="",
            token="",
        )
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

        window['output'].print('Aguardando codigo...')
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
            window['output'].print('Erro encontrado.')
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
                    window['output'].print('Erro fechado.')
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
                subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, shell=True)

                window.Refresh()
                break
            nome_completo = nome + ' ' + sobrenome
            nome_completo_s = nome + sobrenome
            numeros_concatenados = ''.join(str(numero) for numero in lista_user)
            user_completo = nome_completo_s + '.' + str(numeros_concatenados)
            window.Refresh()
            window['output'].print('Nome escolhido: ' + nome_completo)
            window.Refresh()
            try:
                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[1]'))).send_keys(
                    nome_completo)
            except:
                cont = False
                window['output'].print('Erro encontrado.')
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
            window['output'].print(f'Idade escolhida: {idade_aleatoria}')
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
                    window['output'].print('Erro ao criar')
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
                window['output'].print(f'Usuário: {user_completo}')
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
                    window['output'].print('Tentando gerar novamente')
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
            window['output'].print('Verificando...')
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
                    window['output'].print('Conta criada com sucesso.', text_color=('lime'))
                    contagem += 1
                    window['criadas'].update(contagem)
                    window.Refresh()
                    window.Refresh()
                    now = datetime.now()
                    now_brasilia = tz.localize(now)
                    timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")
                    
                    scope = ['https://www.googleapis.com/auth/spreadsheets']
                    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                    client = gspread.authorize(creds)

                    spreadsheet_id = config['spreadsheet']
                    sheet_name = 'contas'
                    # Insert user, password, and timestamp into first empty row
                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                    values = sheet.col_values(1)
                    last_row = len(values)
                    values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                    cell_list = sheet.range(f'A{last_row+1}:E{last_row+1}')
                    for i, val in enumerate(values):
                        cell_list[i].value = val
                    sheet.update_cells(cell_list)
                    

                    rows = sheet.get_all_values()

                    # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                    regex = re.compile(r'^.*\.\d{3}\s.*$')

                    # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                    num_rows = sum(1 for row in rows if regex.match(row[0]))
                    window['total'].update(num_rows)

                    scope = ['https://www.googleapis.com/auth/spreadsheets']
                    creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                    client = gspread.authorize(creds)

                    spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                    sheet_name = 'relatorio_geral'
                    # Insert user, password, and timestamp into first empty row
                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                    values = sheet.col_values(1)
                    last_row = len(values)
                    values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                    cell_list = sheet.range(f'A{last_row+1}:E{last_row+1}')
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

    window['output'].print(f'Senha sendo utilizada: {senha}')
    window.Refresh()

    console = Console()

    device = [
        {'name': 'Bluestacks1', 'port': porta, 'udid': f'127.0.0.1:{porta}'},
    ]
    comando = f"adb connect 127.0.0.1:{porta}"
    subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
    subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test', stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server', stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)

    gerar_id()
    android_id = gerar_id()
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    time.sleep(2)
    # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True, stdout=subprocess.DEVNULL,
    #               stderr=subprocess.DEVNULL)
    window.Refresh()
    window['output'].print('Iniciando criação.\n')
    window.Refresh()
    cont = True
    while cont is True:

        window['output'].print(linha_ret)
        window.Refresh()
        window['output'].print('Abrindo Instagram')

        scope = ['https://www.googleapis.com/auth/spreadsheets']
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
        regex = re.compile(r'^.*\.\d{3}\s.*$')

        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
        num_rows = sum(1 for row in rows if regex.match(row[0]))
        window['total'].update(num_rows)

        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, check=True, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test',
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
        subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server', stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, shell=True)
        window.Refresh()
        # try:
        #    subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
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
            desired_caps['appPackage'] = 'com.instagram.lite'
            desired_caps['appActivity'] = 'com.facebook.lite.MainActivity'
            desired_caps['systemPort'] = random.randint(6000, 8299)
            desired_caps['noReset'] = True
            desired_caps['app'] = appinsta

            driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

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
                window['output'].print('Erro fechado.')
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
                    window['output'].print('Pop-up fechado.')
                    window.Refresh()
                    time.sleep(1)
                firts_reg()

            except Exception as e:
                print(e)
                sms = True
                comando = f"adb connect 127.0.0.1:{porta}"
                subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server',
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, shell=True)
                window['output'].print('Erro não catalogado.')
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
                    window['output'].print('Criação de outro perfil.')
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
                    lista_user = random.choices(range(1, 9), k=3)
                    with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                        nomes = nomes_arquivo.readlines()

                    with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                        sobrenomes = sobrenomes_arquivo.readlines()

                    nome = random.choice(nomes).strip()
                    sobrenome = random.choice(sobrenomes).strip()
                    nome_completo = nome + sobrenome
                    numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                    user_completo = nome_completo + '.' + str(numeros_concatenados)
                    window['output'].print('Usuário: ' + user_completo)
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

                    window['output'].print('Verificando...')
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
                        window['output'].print('Conta criada com sucesso.', text_color=('lime'))
                        contagem += 1
                        window['criadas'].update(contagem)
                        window.Refresh()
                        window.Refresh()
                        now = datetime.now()
                        now_brasilia = tz.localize(now)
                        timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")
                        
                        scope = ['https://www.googleapis.com/auth/spreadsheets']
                        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                        client = gspread.authorize(creds)

                        spreadsheet_id = config['spreadsheet']
                        sheet_name = 'contas'
                        # Insert user, password, and timestamp into first empty row
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                        values = sheet.col_values(1)
                        last_row = len(values)
                        values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                        cell_list = sheet.range(f'A{last_row+1}:E{last_row+1}')
                        for i, val in enumerate(values):
                            cell_list[i].value = val
                        sheet.update_cells(cell_list)
                        

                        rows = sheet.get_all_values()

                        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                        regex = re.compile(r'^.*\.\d{3}\s.*$')

                        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                        num_rows = sum(1 for row in rows if regex.match(row[0]))
                        window['total'].update(num_rows)

                        scope = ['https://www.googleapis.com/auth/spreadsheets']
                        creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                        client = gspread.authorize(creds)

                        spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                        sheet_name = 'relatorio_geral'
                        # Insert user, password, and timestamp into first empty row
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                        values = sheet.col_values(1)
                        last_row = len(values)
                        values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                        cell_list = sheet.range(f'A{last_row+1}:E{last_row+1}')
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
                        window['output'].print('Alterando perfil para publico.')
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
                        window['output'].print('Alterado para publico.')
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
            subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, check=True, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test',
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, shell=True)
            comando = f"adb connect 127.0.0.1:{porta}"
            subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server',
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, shell=True)
            window['output'].print('Erro não catalogado.')
            print(e)
            # window['output'].print(e)
            window.Refresh()

def executar_2nr():
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
        window['output'].print('Instalando dependências...')
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
    # SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    def vpn_avast():
        global nome
        global sobrenome
        global sms
        window['output'].print('Alterando IP da Avast', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
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
        window['output'].print('Alterando IP da HotspotShield', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
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
        window['output'].print('Alterando IP da PiaVPN', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

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
        window['output'].print('Alterando IP da ExpressVPN', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', shell=True)

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
        window['output'].print('Alterando IP da NordVPN', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
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
        window['output'].print('Alterando IP da SurfShark', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
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
        window['output'].print('Alterando IP da BetterNet', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
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
        window['output'].print('Alterando IP da CyberGhost', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
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
        window['output'].print('Alterando IP da AVG', text_color='red')
        window.Refresh()
        window['output'].print('Limpando dados.')
        window.Refresh()
        gerar_id()
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
        #subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
        #               stderr=subprocess.DEVNULL, check=True, shell=True)

        # time.sleep(10)
        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        # time.sleep(10)
        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        
    def gerar_id():
        chars = string.ascii_lowercase + string.digits
        android_id = ''.join(random.choice(chars) for i in range(16))
        return android_id
    
    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.page_load_strategy = 'none'
    options.add_experimental_option("prefs", prefs)

    window['output'].print(f'Senha sendo utilizada: {senha}')
    window.Refresh()

    console = Console()

    device = [
        {'name': 'Bluestacks1', 'port': porta, 'udid': f'127.0.0.1:{porta}'},
    ]
    comando = f"adb connect 127.0.0.1:{porta}"
    subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
    subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test', stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server', stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)

    gerar_id()
    android_id = gerar_id()
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, shell=True)
    time.sleep(2)
    # subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True, stdout=subprocess.DEVNULL,
    #               stderr=subprocess.DEVNULL)
    
    desired_caps = {}
    desired_caps['udid'] = '127.0.0.1:' + porta
    desired_caps['newCommandTimeout'] = '500'
    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['systemPort'] = random.randint(6000, 8299)
    desired_caps['noReset'] = True
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    try:
        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp', stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL, check=True, shell=True)
    except:
        pass
    
    window['output'].print('Efetuando troca de IP.')
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
        else:
            window['output'].print(
                "Verifique se escreveu certo a VPN que deseja.\nOBS: Não pode conter espaços e o conteúdo tem que ser todo minúsculo")
            window.Refresh()

    except Exception as e:
        print(e)
        pass

    window.Refresh()
    window['output'].print('Iniciando criação.\n')
    window.Refresh()
    while True:
        try:

            window['output'].print(linha_ret)
            window.Refresh()
            window['output'].print('Abrindo 2NR')

            scope = ['https://www.googleapis.com/auth/spreadsheets']
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
            regex = re.compile(r'^.*\.\d{3}\s.*$')

            # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
            num_rows = sum(1 for row in rows if regex.match(row[0]))
            window['total'].update(num_rows)
            try:
                subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL, check=True, shell=True)
                
                
            except:
                pass
            try:
                subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp', stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL, check=True, shell=True)
            except:
                pass
                
            subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test',
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
            subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server', stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL, shell=True)
            window.Refresh()
            
            with open("storage/apk/caminho.txt", "r") as arquivo:
                app = arquivo.read().strip()
            try:
                time.sleep(10)
                quantidade = 0
                desired_caps = {}
                desired_caps['udid'] = '127.0.0.1:' + porta
                desired_caps['newCommandTimeout'] = '500'
                desired_caps['platformName'] = 'Android'
                desired_caps['automationName'] = 'UiAutomator2'
                desired_caps['systemPort'] = random.randint(6000, 8299)
                desired_caps['noReset'] = True
            
                driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
                
                gerar_id()
                android_id = gerar_id()
                driver.activate_app('pl.rs.sip.softphone.newapp')
                time.sleep(10)
                scope = ['https://www.googleapis.com/auth/spreadsheets']
                creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                client = gspread.authorize(creds)

                spreadsheet_id = config['spreadsheet']
                sheet_name = config['2nr']

                sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                # Obtém todas as células
                cells = sheet.get_all_values()

                # Armazena as células que correspondem à condição
                matches = [cell for row in cells for cell in row if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', cell)]

                # Armazena a lista de células correspondentes à condição em uma variável
                regex2nr = matches
                while len(regex2nr) == 0:
                    window['output'].print('Nenhuma conta do 2NR encontrada.\nTentando novamente em 5 min.')
                    window.Refresh()
                    time.sleep(300)
                    cells = sheet.get_all_values()

                    # Armazena as células que correspondem à condição
                    matches = [cell for row in cells for cell in row if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', cell)]

                    # Armazena a lista de células correspondentes à condição em uma variável
                    regex2nr = matches
                window['output'].print(f'{len(regex2nr)} conta(s) encontrada.')
                window.Refresh()
                time.sleep(3)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'pl.rs.sip.softphone.newapp:id/loginButton'))).click()
                

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
                window['output'].print(f'Email sendo usado: {email2nr}')
                window.Refresh()
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'pl.rs.sip.softphone.newapp:id/emailEdiText'))).send_keys(email2nr)
                time.sleep(0.5)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'pl.rs.sip.softphone.newapp:id/passwordEdiText'))).send_keys(senha2nr)
                time.sleep(0.5)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'pl.rs.sip.softphone.newapp:id/buttonLogin'))).click()
                time.sleep(3)
                try:
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'pl.rs.sip.softphone.newapp:id/buttonAgree')))
                except:
                    pass
                perm = driver.find_elements(By.ID, 'pl.rs.sip.softphone.newapp:id/buttonAgree')
                if len(perm) == 1:
                    window['output'].print(f'Aceitando permissões.')
                    window.Refresh()
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'pl.rs.sip.softphone.newapp:id/buttonAgree'))).click()
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/androidx.cardview.widget.CardView[1]/androidx.appcompat.widget.LinearLayoutCompat/android.widget.TextView'))).click()
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout'))).click()
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.Switch'))).click()
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.Switch'))).click()
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout[2]/android.widget.Switch'))).click()
                    subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                    time.sleep(0.5)
                    subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                    time.sleep(0.5)
                    subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, shell=True)
                
                qtd_num = driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[*]/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.TextView[1]')
                window['output'].print(f'{len(qtd_num)} número(s) encontrado.')
                if len(qtd_num) == 0:
                    SHEET_NAME = config['2nr']

                    scope = ['https://www.googleapis.com/auth/spreadsheets']
                    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                    client = gspread.authorize(creds)
                    # Abre a planilha e a planilha de uma determinada aba
                    spreadsheet_id = config['spreadsheet']
                    sheet_name = SHEET_NAME
                    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)

                    # Apaga a primeira célula da coluna A e desloca as células abaixo
                    sheet.delete_rows(1, 1)
                    
                    continue
                window.Refresh()
                num = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.TextView[1]'))).text
                num = num.replace(' ', '')
                window['output'].print(f'Número: {num}')
                window.Refresh()
                email = num
                window['output'].print(f'Abrindo instagram.')
                window.Refresh()
                driver.activate_app('com.instagram.lite')
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                time.sleep(6)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
                time.sleep(5)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.MultiAutoCompleteTextView'))).send_keys('48')
                time.sleep(3)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup/android.view.View'))).click()
                time.sleep(1)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(num)
                time.sleep(1)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()
                time.sleep(4)
                restricao = driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
                if len(restricao) == 1:
                    window['output'].print(f'Restrição.')
                    window.Refresh()
                    
                    
                    driver.activate_app('pl.rs.sip.softphone.newapp')
                    time.sleep(4)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/androidx.appcompat.widget.LinearLayoutCompat'))).click()
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'pl.rs.sip.softphone.newapp:id/buttonDelete'))).click()
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'pl.rs.sip.softphone.newapp:id/buttonAgree'))).click()
                    window['output'].print(f'Número excluído.')
                    window.Refresh()
                    try:
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear com.instagram.lite', stdout=subprocess.DEVNULL,
                                    stderr=subprocess.DEVNULL, check=True, shell=True)
                        
                        
                    except:
                        pass
                    try:
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm clear pl.rs.sip.softphone.newapp', stdout=subprocess.DEVNULL,
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
                driver.activate_app('pl.rs.sip.softphone.newapp')
                time.sleep(3)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'pl.rs.sip.softphone.newapp:id/messages'))).click()
                time.sleep(15)
                cod = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'pl.rs.sip.softphone.newapp:id/message'))).text
                codigo = re.sub('[^0-9]', '', cod)
                window['output'].print(f'Codigo recebido: {codigo}')
                window.Refresh()
                driver.activate_app('com.instagram.lite')
                time.sleep(5)
                WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(codigo)
                #time.sleep(100)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
                time.sleep(2)

                codigo_invalido = driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[2]')
                if len(codigo_invalido) == 0:
                    window['output'].print(f'Código inválido.')
                    window.Refresh()
                    driver.activate_app('pl.rs.sip.softphone.newapp')
                    time.sleep(4)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'pl.rs.sip.softphone.newapp:id/numbers'))).click()
                    time.sleep(1)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/androidx.appcompat.widget.LinearLayoutCompat'))).click()
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'pl.rs.sip.softphone.newapp:id/buttonDelete'))).click()
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'pl.rs.sip.softphone.newapp:id/buttonAgree'))).click()
                    window['output'].print(f'Número excluído.')
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
                ######################################################################
                lista_user = random.choices(range(1, 9), k=3)
                with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                    nomes = nomes_arquivo.readlines()

                with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                    sobrenomes = sobrenomes_arquivo.readlines()

                nome = random.choice(nomes).strip()
                sobrenome = random.choice(sobrenomes).strip()
                nome_completo = nome + ' ' + sobrenome
                nome_completo_s = nome + sobrenome
                numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                user_completo = nome_completo_s + '.' + str(numeros_concatenados)
                ######################################################################

                senha = config['senha']
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[1]'))).send_keys(nome_completo)
                time.sleep(1)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView[2]'))).send_keys(senha)
                time.sleep(1)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[5]/android.view.View'))).click()
                time.sleep(3)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
                time.sleep(1)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'))).click()
                time.sleep(2)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[6]'))).click()
                time.sleep(2)
                idade_aleatoria = random.randint(18, 35)
                window['output'].print(f'Idade escolhida: {idade_aleatoria}')
                window.Refresh()
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(idade_aleatoria)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
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
                        window['output'].print('Erro ao criar')
                        window.Refresh()
                        sms = True
                        continue
                try:
                    time.sleep(1)
                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).clear()
                    time.sleep(3)
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                        user_completo)
                    window['output'].print(f'Usuário: {user_completo}')
                    window.Refresh()
                    time.sleep(3)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                    time.sleep(5)
                    conta_jacriada = driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]')
                    time.sleep(1)
                    if len(conta_jacriada) == 1:
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View'))).click()
                    erro_2 = driver.find_elements(By.XPATH,
                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[*]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[*]/android.view.View[*]/android.widget.Button')
                    erro_1 = driver.find_elements(By.XPATH,
                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
                    if len(erro_2) == 1:
                        window['output'].print('Tentando gerar novamente')
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
                window['output'].print('Verificando...')
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
                        
                        window['output'].print('Conta criada com sucesso.', text_color=('lime'))
                        window.Refresh()
                        contagem += 1
                        window['criadas'].update(contagem)
                        window.Refresh()
                        now = datetime.now()
                        now_brasilia = tz.localize(now)
                        timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")
                        
                        scope = ['https://www.googleapis.com/auth/spreadsheets']
                        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                        client = gspread.authorize(creds)

                        spreadsheet_id = config['spreadsheet']
                        sheet_name = 'contas'
                        # Insert user, password, and timestamp into first empty row
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                        values = sheet.col_values(1)
                        last_row = len(values)
                        values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                        cell_list = sheet.range(f'A{last_row+1}:E{last_row+1}')
                        for i, val in enumerate(values):
                            cell_list[i].value = val
                        sheet.update_cells(cell_list)
                        

                        rows = sheet.get_all_values()

                        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                        regex = re.compile(r'^.*\.\d{3}\s.*$')

                        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                        num_rows = sum(1 for row in rows if regex.match(row[0]))
                        window['total'].update(num_rows)

                        scope = ['https://www.googleapis.com/auth/spreadsheets']
                        creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                        client = gspread.authorize(creds)

                        spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                        sheet_name = 'relatorio_geral'
                        # Insert user, password, and timestamp into first empty row
                        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                        values = sheet.col_values(1)
                        last_row = len(values)
                        values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                        cell_list = sheet.range(f'A{last_row+1}:E{last_row+1}')
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
                    else:
                        try:
                            conteudo = config['vpn']

                            SHEET_NAME = config['2nr']
                            SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
                            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
                            # Conecta à API
                            service = build('sheets', 'v4', credentials=creds)
                            # Obtém o ID da aba
                            sheet_metadata = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
                            sheet_id = None
                            for sheet in sheet_metadata['sheets']:
                                if sheet['properties']['title'] == SHEET_NAME:
                                    sheet_id = sheet['properties']['sheetId']
                                    break
                            if sheet_id is None:
                                raise Exception(f"Aba '{SHEET_NAME}' não encontrada na planilha")
                            # Define a faixa de células para leitura
                            RANGE_NAME2nr = f'{SHEET_NAME}!A1:A1'
                            # Lê o valor da célula A1
                            result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME2nr).execute()
                            values = result.get('values', [])
                            # Apaga a primeira linha
                            request = service.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID, body={
                                'requests': [
                                    {
                                        'deleteDimension': {
                                            'range': {
                                                'sheetId': sheet_id,
                                                'dimension': 'ROWS',
                                                'startIndex': 0,
                                                'endIndex': 1
                                            }
                                        }
                                    }
                                ]
                            })
                            # Adicione o objeto updateSheetPropertiesRequest envolvendo o objeto deleteDimension
                            request = service.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID, body={
                                'requests': [
                                    {
                                        'updateSheetProperties': {
                                            'properties': {
                                                'sheetId': sheet_id,
                                            },
                                            'fields': 'gridProperties(frozenRowCount)',
                                        }
                                    },
                                    {
                                        'deleteDimension': {
                                            'range': {
                                                'sheetId': sheet_id,
                                                'dimension': 'ROWS',
                                                'startIndex': 0,
                                                'endIndex': 1
                                            }
                                        }
                                    },
                                ]
                            })


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
                except Exception as e:
                    print(e)
                    sms = True
                    break
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
                        window['output'].print('Criação de outro perfil.')
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
                        lista_user = random.choices(range(1, 9), k=3)
                        with open("storage\\txt\\nomes.txt", "r") as nomes_arquivo:
                            nomes = nomes_arquivo.readlines()

                        with open("storage\\txt\\sobrenomes.txt", "r") as sobrenomes_arquivo:
                            sobrenomes = sobrenomes_arquivo.readlines()

                        nome = random.choice(nomes).strip()
                        sobrenome = random.choice(sobrenomes).strip()
                        nome_completo = nome + sobrenome
                        numeros_concatenados = ''.join(str(numero) for numero in lista_user)
                        user_completo = nome_completo + '.' + str(numeros_concatenados)
                        window['output'].print('Usuário: ' + user_completo)
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
                        feedback = driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.View')
                        if len(feedback) == 1:
                            sms = True

                        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]')))
                        time.sleep(10)
                        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()

                        window['output'].print('Verificando...')
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
                            window['output'].print('Conta criada com sucesso.', text_color=('lime'))
                            window.Refresh()
                            contagem += 1
                            window['criadas'].update(contagem)
                            window.Refresh()
                            now = datetime.now()
                            now_brasilia = tz.localize(now)
                            timestamp = now_brasilia.strftime("%d/%m/%Y %H:%M:%S")
                            
                            scope = ['https://www.googleapis.com/auth/spreadsheets']
                            creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
                            client = gspread.authorize(creds)

                            spreadsheet_id = config['spreadsheet']
                            sheet_name = 'contas'
                            # Insert user, password, and timestamp into first empty row
                            sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                            values = sheet.col_values(1)
                            last_row = len(values)
                            values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                            cell_list = sheet.range(f'A{last_row+1}:E{last_row+1}')
                            for i, val in enumerate(values):
                                cell_list[i].value = val
                            sheet.update_cells(cell_list)
                            

                            rows = sheet.get_all_values()

                            # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                            regex = re.compile(r'^.*\.\d{3}\s.*$')

                            # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                            num_rows = sum(1 for row in rows if regex.match(row[0]))
                            window['total'].update(num_rows)

                            scope = ['https://www.googleapis.com/auth/spreadsheets']
                            creds = ServiceAccountCredentials.from_json_keyfile_name('relatorio.json', scope)
                            client = gspread.authorize(creds)

                            spreadsheet_id = '1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4'
                            sheet_name = 'relatorio_geral'
                            # Insert user, password, and timestamp into first empty row
                            sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
                            values = sheet.col_values(1)
                            last_row = len(values)
                            values = [user_completo + ' ' + senha, email, timestamp, maquina, conteudo]
                            cell_list = sheet.range(f'A{last_row+1}:E{last_row+1}')
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
                            ################################################################
                            #window['output'].print('Alterando perfil para publico.')
                            #window.Refresh()

                            ## Clicar nas 3 barras
                            #try:
                            #    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                            #                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup[5]'))).click()
                            #except:
                            #    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                            #                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[5]'))).click()

                            #time.sleep(0.5)

                            ## Clicar em configurações
                            #WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                            #                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.View'))).click()
                            #time.sleep(0.5)
                            ## Clicar em privacidade
                            #try:
                            #    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                            #                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[7]/android.view.ViewGroup/android.view.View'))).click()
                            #except:
                            #    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                            #                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup/android.view.View'))).click()
                            #time.sleep(2)
                            ## Clicar em privacidade da conta
                            #try:
                            #    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                            #                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[11]/android.view.ViewGroup/android.view.ViewGroup/android.view.View'))).click()
                            #except:
                            #    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                            #                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[10]/android.view.ViewGroup/android.view.View'))).click()
                            #time.sleep(0.5)
                            ## Clicar no botão
                            #WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                            #                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]/android.view.ViewGroup'))).click()
                            #time.sleep(0.5)
                            #window['output'].print('Alterado para publico.')
                            #window.Refresh()
                            #time.sleep(0.5)
                            #subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK',
                            #            stdout=subprocess.DEVNULL,
                            #            stderr=subprocess.DEVNULL, check=True, shell=True)
                            #time.sleep(0.5)
                            #subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK',
                            #            stdout=subprocess.DEVNULL,
                            #            stderr=subprocess.DEVNULL, check=True, shell=True)
                            #time.sleep(0.5)
                            #subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK',
                            #            stdout=subprocess.DEVNULL,
                            #            stderr=subprocess.DEVNULL, check=True, shell=True)
                            #time.sleep(0.5)
                            ################################################################
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
                print(e)
                print('finalizado')
                pass
                
        except Exception as e:
            print(e)
            print('Erro')
            

pool = concurrent.futures.ThreadPoolExecutor()
while True:
    event, values = window.read()

    # Finaliza a janela se o usuário fechar a janela
    if event == sg.WINDOW_CLOSED:
        break

    # Executa o código e atualiza a saída na Multiline em tempo real
    if event == 'Executar':
        contagem = 0
        if not os.path.exists("credentials.json"):
            # se o arquivo não existe, pede o nome do arquivo ao usuário e armazena em uma variável global
            window['output'].print('Nenhum credentials.json encontrado.')
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
            window['output'].print('Configure o bot primeiro.')
            window.Refresh()
            time.sleep(200)
        if '2nr' not in config or config['maquina'] == '':
            window['output'].print('Configure o bot primeiro.')
            window.Refresh()
            time.sleep(200)
        if config['email'] == '-mailtm-':
            window['output'].print('Email selecionado: Mail.TM')
            window.Refresh()
            minha_thread = threading.Thread(target=executar_mailtm)
            minha_thread.start()
        elif config['email'] == '-minuteinbox-':
            window['output'].print('Email selecionado: MinuteInBox')
            window.Refresh()
            minha_thread = threading.Thread(target=executar_minuteinbox)
            minha_thread.start()
        elif config['email'] == '-2nr-':
            window['output'].print('2NR selecionado.')
            window.Refresh()
            minha_thread = threading.Thread(target=executar_2nr)
            minha_thread.start()
    if event == 'clear':
        window['output'].update('')
        if not os.path.exists("credentials.json"):
            # se o arquivo não existe, pede o nome do arquivo ao usuário e armazena em uma variável global
            window['output'].print('Nenhum credentials.json encontrado.')
            window.Refresh()
            time.sleep(200)
        else:
            pass
        if 'senha' not in config or config['maquina'] == '':
            window['output'].print('Configure o bot primeiro.')
            window.Refresh()
            time.sleep(200)
    if event == '-config-':

        layout_configuracoes = [
        [sg.Text("Senha dos perfis: ", font=('Open Sans', 12)),
        sg.InputText(key="-senha-", default_text=config.get("senha", ""))],
        [sg.Text('VPN: ', font=('Open Sans', 12)),
        sg.Combo(vpn_list, default_value=config.get("vpn", ""), readonly=True, key='-vpn-')],
        #sg.OptionMenu(vpn_list, size=(7, 19), key="-vpn-", default_value=config.get("vpn", ""))],
        [sg.Text('Email ou número: ', font=('Open Sans', 12)),
        sg.Radio('Mail.TM', 'RADIO1', key='-mailtm-', default=config.get("email", "") == "-mailtm-"),
        sg.Radio('MinuteInBox', 'RADIO1', key='-minuteinbox-', default=config.get("email", "") == "-minuteinbox-"),
        sg.Radio('2NR', 'RADIO1', key='-2nr-', default=config.get("email", "") == "-2nr-")],
        [sg.Radio('Instagram Lite', 'RADIO2', key='-instalite-', default=config.get("app", "") == "-instalite-"),
        sg.Radio('Instagram', 'RADIO2', key='-insta-', default=config.get("app", "") == "-insta-")],
        [sg.HorizontalSeparator()],
        [sg.Text("Nome da maquina: "), sg.InputText(key="maquina", default_text=config.get("maquina", ""))],
        [sg.Text("SpreadsheetID: "), sg.InputText(key="spreadsheet", default_text=config.get("spreadsheet", ""))],
        [sg.Text("Planilha 2NR: "), sg.InputText(key="2nr", default_text=config.get("2nr", ""))],
        [sg.Button("Salvar")]
        ]

        # Criar a janela da GUI de configuração
        janela_configuracoes = sg.Window("Configurações", layout_configuracoes)

        while True:
            #janela_configuracoes = sg.Window('Configurações', layout_configuracoes)
            evento, valores = janela_configuracoes.read()

            if evento == sg.WINDOW_CLOSED:
                break

            if evento == "Salvar":
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
                # Salvar as configurações em um arquivo JSON
                config = {
                    "senha": valores["-senha-"],
                    "vpn": valores["-vpn-"],
                    "email": email,
                    "app": app,
                    "maquina": valores['maquina'],
                    "spreadsheet": valores['spreadsheet'],
                    "2nr": valores['2nr']
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

            janela_configuracoes.close()
window.close()
