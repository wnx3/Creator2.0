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

import time

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

# Lista de arquivos que você deseja verificar e atualizar
#file_list = ['relatorio.json', 'requirements.txt']
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

import multiprocessing
import os
import PySimpleGUI as sg
import time
from datetime import datetime

import threading
import asyncio
import concurrent.futures
import re

with open("configuracoes\outros\SPREADSHEET_ID.txt", "r") as arquivo:
    SPREADSHEET_ID = arquivo.read().strip()

import PySimpleGUI as sg

# Tenta abrir o arquivo token.json
try:
    with open("token.json", "r") as f:
        # Se o arquivo existir, lê o conteúdo
        content = f.read()
except FileNotFoundError:
    # Se o arquivo não existir, abre uma GUI para informar o usuário
    sg.theme('Dark')
    layout = [[sg.Text("Arquivo token.json não encontrado.", font=('Open Sans', 10))],
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
layout = [
    [sg.Multiline(font=('Open Sans', 10), key='output', size=(50, 15), disabled=True)],
    [sg.Button('Executar'),sg.Button('Reiniciar', key='clear', pad=((5, 190), 0), disabled=True),sg.Image(filename=check_img, pad=((0, 0), 0)), sg.Text('0', key='total')]
]

window = sg.Window(f'CREATOR WNx3 | Porta: {porta}', layout)




def contagem():
    global nome
    global sobrenome
    contagem += 1
    window['contagem'].update(contagem)
    window.Refresh()

def executar():
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
    from mailtm import Email
    import re
    import logging

     #verifica se o arquivo existe na pasta do bot
    if not os.path.exists("configuracoes/outros/nome_maquina.txt"):
        # se o arquivo não existe, pede o nome do arquivo ao usuário e armazena em uma variável global
        global nome_arquivo
        with open("configuracoes/outros/nome_maquina.txt", "w") as f:
            f.write('Configure o nome da maquina.')
            pass
        
    else:
        # se o arquivo existe, lê o nome do arquivo a partir do arquivo de configuração ou da variável global
        with open("configuracoes/outros/nome_maquina.txt") as f:
            maquina = f.readline().strip()


    
    logger = logging.getLogger(__name__)
    
    handler = logging.FileHandler('log.txt')
    handler.setLevel(logging.ERROR)
    
    logger.addHandler(handler)


    with open("configuracoes\outros\SPREADSHEET_ID.txt", "r") as arquivo:
        SPREADSHEET_ID = arquivo.read().strip()
    #RANGE_NAME = 'contas!A:D'
#
    #SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


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
        #try:
        #    WebDriverWait(driver, 10).until(
        #        EC.element_to_be_clickable((By.ID, 'com.nordvpn.android:id/reconnect_button'))).click()
        #except:
        #    pass
        #try:
        #    WebDriverWait(driver, 10).until(
        #        EC.element_to_be_clickable((By.ID, 'com.nordvpn.android:id/secondary_quick_connect_button'))).click()
        #except:
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
            #time.sleep(5)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
        while connect == 'CONNECT':
            WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
            time.sleep(4)
            connect = driver.find_element(By.ID, 'com.freevpnintouch:id/buttonConnect').text
            #WebDriverWait(driver, 20).until(
            #EC.element_to_be_clickable((By.ID, 'com.freevpnintouch:id/buttonConnect'))).click()
        #time.sleep(5)
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
        #time.sleep(3)
        #WebDriverWait(driver, 10).until(
        #    EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        #time.sleep(3)
        #WebDriverWait(driver, 10).until(
        #    EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        #time.sleep(5)
        #WebDriverWait(driver, 10).until(
        #    EC.element_to_be_clickable((By.ID, 'com.avg.android.vpn:id/view_switch'))).click()
        #time.sleep(5)
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
        arquivo = open('configuracoes/contas/senha_perfis.txt')
        senha = arquivo.read()
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()

        test.register(username=user_completo, password=senha)
        window['output'].print("Email: " + str(test.address))
        window.Refresh()
        email = str(test.address)
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
        test.stop()
        ##time.sleep(3)
        #codigo_invalido = driver.find_elements(By.XPATH,
        #                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[5]')
        #continua_na_tela = driver.find_elements(By.XPATH,
        #                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]/android.view.View')
        #continua_na_tela2 = driver.find_elements(By.XPATH,
        #                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]/android.view.View')
        #criou = driver.find_elements(By.XPATH,
        #                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View')
        #time.sleep(25)
        #if len(codigo_invalido) == 1:
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
        #WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
        #                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')))
        #reenv_cod = driver.find_elements(By.XPATH,
        #                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
        #if len(reenv_cod) == 1:
        #    window['output'].print('Enviando um novo codigo.')
        #    window.Refresh()
        #    driver.find_element(By.XPATH,
        #                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
        #    time.sleep(2)
        #    driver.find_element(By.XPATH,
        #                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').clear()
        #    driver.find_element(By.XPATH,
        #                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]').click()
#
        #    codigo = None
#
        #    codigo = 0
        #    try:
        #        while codigo != 20:
        #            test.start(listener, interval=5)
        #            time.sleep(1.5)
        #            codigo = codigo + 1
        #        codigo = cod
        #    except Exception as e:
        #        if "Too Many Requests" in str(e):
        #            pass
        #        else:
        #            window['output'].print(e)
        #            window.Refresh()
        #    window['output'].print(f"Codigo recebido: {codigo}")
        #    window.Refresh()
        #    # time.sleep(3)
        #    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
        #                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
        #        codigo)
        #    # try:
        #    #    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
        #    #                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
        #    # except:
        #    #    pass
        #    try:
        #        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()
        #        try:
        #            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
        #        except:
        #            pass
        #    except:
        #        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
        #        try:
        #            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
        #        except:
        #            pass
        #    test.stop()
        #    time.sleep(3)
        #    codigo_invalido = driver.find_elements(By.XPATH,
        #                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.View[5]')
        #    continua_na_tela = driver.find_elements(By.XPATH,
        #                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.View[5]')
        #    if len(codigo_invalido) == 1:
        #        driver.find_element(By.XPATH,
        #                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
        #        time.sleep(2)
        #        driver.find_element(By.XPATH,
        #                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView').clear()
        #        driver.find_element(By.XPATH,
        #                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[1]').click()
        #        codigo = None
        #        try:
        #            test.start(listener, interval=5)
        #            codigo = 0
        #            while codigo != 20:
        #                time.sleep(2)
        #                codigo = codigo + 1
        #            codigo = cod
        #        except Exception as e:
        #            if "Too Many Requests" in str(e):
        #                pass
        #            else:
        #                window['output'].print(e)
        #                window.Refresh()
        #        window['output'].print(f"Codigo recebido: {codigo}")
        #        window.Refresh()
        #        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
        #                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
        #            codigo)
        #        try:
        #            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[4]'))).click()
        #            try:
        #                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
        #            except:
        #                pass
        #        except:
        #            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
        #            try:
        #                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View')))
        #            except:
        #                pass
#
        #        test.stop()
        #        time.sleep(5)
        #elif reenv_cod == 0:
        #    window['output'].print('Codigo aceito.')
        #    window.Refresh()
#
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
            #subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True)

            try:
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
                time.sleep(5)
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                time.sleep(3)
                gerar_email_firts_reg()
            except Exception as e:
                logger.error('Ocorreu um erro: %s', e)
                subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL, check=True, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL, check=True, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test',
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
                subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server', stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL, shell=True)
                window['output'].print('Algum erro não catalogado encontrado.')
                window['output'].print(e)
                #window['output'].print(e)
                window.Refresh()
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
                    window['output'].print('Conta criada com sucesso.', text_color='green')
                    with open("configuracoes/vpn/vpn.txt", "r") as arquivo:
                        conteudo = arquivo.read().strip()
                    window.Refresh()
                    now = datetime.now()
                    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
                    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
                    service = build('sheets', 'v4', credentials=creds)
                    # Get values of columns A and B
                    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
                    values = result.get('values', [])
                    # Find first empty row
                    first_empty_row_index = len(values) + 1
                    # Insert user, password, and timestamp into first empty row
                    range_to_update = f'contas!A{first_empty_row_index}:E{first_empty_row_index}'
                    value_input_option = 'USER_ENTERED'
                    value_range_body = {'values': [[user_completo + ' ' + senha, email, timestamp, maquina, conteudo]]}
                    result = service.spreadsheets().values().update(
                        spreadsheetId=SPREADSHEET_ID,
                        range=range_to_update,
                        valueInputOption=value_input_option,
                        body=value_range_body).execute()
                    
                    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
                    values = result.get('values', [])

                    # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                    regex = re.compile(r'^.*\.\d{3}\s.*$')

                    # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                    num_rows = sum(1 for row in values if regex.match(row[0]))
                    window['total'].update(num_rows)


                    creds = Credentials.from_authorized_user_file('relatorio.json', SCOPES)
                    service = build('sheets', 'v4', credentials=creds)
                    # Get values of columns A and B
                    result = service.spreadsheets().values().get(spreadsheetId='1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4', range='relatorio_geral!A:D').execute()
                    values = result.get('values', [])
                    # Find first empty row
                    first_empty_row_index = len(values) + 1
                    # Insert user, password, and timestamp into first empty row
                    range_to_update = f'relatorio_geral!A{first_empty_row_index}:E{first_empty_row_index}'
                    value_input_option = 'USER_ENTERED'
                    value_range_body = {'values': [[user_completo + ' ' + senha, email, timestamp, maquina, conteudo]]}
                    result = service.spreadsheets().values().update(
                        spreadsheetId='1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4',
                        range=range_to_update,
                        valueInputOption=value_input_option,
                        body=value_range_body).execute()
                    
                    
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
                    with open("configuracoes/vpn/vpn.txt", "r") as arquivo:
                        conteudo = arquivo.read().strip()
                    # Executa a função correspondente ao conteúdo do arquivo
                    if conteudo == "avg":
                        vpn_avg()
                    elif conteudo == "cyberghost":
                        vpn_cyberghost()
                    elif conteudo == "surf":
                        vpn_surf()
                    elif conteudo == "betternet":
                        vpn_better()
                    elif conteudo == "nord":
                        vpn_nord()
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

    arquivo = open('configuracoes/contas/senha_perfis.txt')
    senha = arquivo.read()
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
    subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}', stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL, shell=True)
    time.sleep(2)
    #subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True, stdout=subprocess.DEVNULL,
    #               stderr=subprocess.DEVNULL)
    window.Refresh()
    window['output'].print('Iniciando criação.\n')
    window.Refresh()
    cont = True
    while cont is True:

        window['output'].print(linha_ret)
        window.Refresh()
        window['output'].print('Abrindo Instagram')

        RANGE_NAME = 'contas!A:E'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        service = build('sheets', 'v4', credentials=creds)
        
        # Obter os valores da página 'teste' da planilha
        result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        values = result.get('values', [])
        
        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
        regex = re.compile(r'^.*\.\d{3}\s.*$')
        
        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
        num_rows = sum(1 for row in values if regex.match(row[0]))
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
        #try:
        #    subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
        #                   stderr=subprocess.DEVNULL, check=True, shell=True)
        #except:
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
            #subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings put secure android_id {android_id}',
            #               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
            time.sleep(5)
            #subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True,
            #               stdout=subprocess.DEVNULL,
            #               stderr=subprocess.DEVNULL)
            error = driver.find_elements(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
            if len(error) == 1:
                driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup').click()
                window['output'].print('Erro fechado.')
                window.Refresh()
            try:
                time.sleep(3)
                cookies = driver.find_elements(By.ID, 'com.android.packageinstaller:id/permission_deny_button')
                if len(cookies) == 1:
                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_deny_button'))).click()
                    window['output'].print('Pop-up fechado.')
                    window.Refresh()
                    time.sleep(1)
                firts_reg()

            except Exception as e:
                if driver.current_activity() is 'com.facebook.lite.MainActivity':
                    logger.error('Ocorreu um erro: %s', e)
                    subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_HOME', stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL, check=True, shell=True)
                    subprocess.run(f'adb -s 127.0.0.1:{porta} shell pm uninstall com.instagram.lite', stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL, check=True, shell=True)
                    subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server.test',
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
                    subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server', stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL, shell=True)
                    window['output'].print('Algum erro não catalogado encontrado.')
                    window['output'].print(e)
                    #window['output'].print(e)
                    window.Refresh()
                else:
                    window['output'].print('Instagram fechou.')
                    window.Refresh()
                    with open("configuracoes/vpn/vpn.txt", "r") as arquivo:
                        conteudo = arquivo.read().strip()

                    # Executa a função correspondente ao conteúdo do arquivo
                    if conteudo == "avg":
                        vpn_avg()
                    elif conteudo == "surf":
                        vpn_surf()
                    elif conteudo == "betternet":
                        vpn_better()
                    elif conteudo == "nord":
                        vpn_nord()
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
                    #subprocess.run(f'adb -s 127.0.0.1:{porta} shell settings get secure android_id', shell=True)
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
                    window['output'].print('User: ' + user_completo)
                    window.Refresh()
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                        user_completo)
                    time.sleep(1)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()
                    # Digitar senha e avançar
                    arquivo = open('configuracoes/contas/senha_perfis.txt')
                    senha = arquivo.read()
                    time.sleep(3)
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.widget.MultiAutoCompleteTextView'))).send_keys(
                        senha)
                    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]'))).click()
                    # Clicar em adicionar email
                    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]/android.view.View'))).click()
                    # Clicar em email, gerar e avançar

                    time.sleep(5)
                    gerar_email()
                    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[2]'))).click()

                    window['output'].print('Verificando...')
                    window.Refresh()
                    #WebDriverWait(driver, 40).until(EC.visibility_of_element_located)(((By.XPATH,
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
                        window['output'].print('Conta criada com sucesso.', text_color='green')
                        with open("configuracoes/vpn/vpn.txt", "r") as arquivo:
                            conteudo = arquivo.read().strip()
                        window.Refresh()
                        now = datetime.now()
                        timestamp = now.strftime("%d/%m/%Y %H:%M:%S")

                        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
                        service = build('sheets', 'v4', credentials=creds)
                        # Get values of columns A and B
                        result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                                    range=RANGE_NAME).execute()
                        values = result.get('values', [])
                        # Find first empty row
                        first_empty_row_index = len(values) + 1
                        # Insert user, password, and timestamp into first empty row
                        range_to_update = f'contas!A{first_empty_row_index}:E{first_empty_row_index}'
                        value_input_option = 'USER_ENTERED'
                        value_range_body = {'values': [[user_completo + ' ' + senha, email, timestamp, maquina, conteudo]]}
                        result = service.spreadsheets().values().update(
                            spreadsheetId=SPREADSHEET_ID,
                            range=range_to_update,
                            valueInputOption=value_input_option,
                            body=value_range_body).execute()
                        

                        result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
                        values = result.get('values', [])

                        # Definir uma expressão regular para filtrar as linhas que atendem ao formato especificado
                        regex = re.compile(r'^.*\.\d{3}\s.*$')

                        # Filtrar as linhas que atendem à expressão regular e contar o número de linhas
                        num_rows = sum(1 for row in values if regex.match(row[0]))
                        window['total'].update(num_rows)

                        creds = Credentials.from_authorized_user_file('relatorio.json', SCOPES)
                        service = build('sheets', 'v4', credentials=creds)
                        # Get values of columns A and B
                        result = service.spreadsheets().values().get(spreadsheetId='1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4', range='relatorio_geral!A:D').execute()
                        values = result.get('values', [])
                        # Find first empty row
                        first_empty_row_index = len(values) + 1
                        # Insert user, password, and timestamp into first empty row
                        range_to_update = f'relatorio_geral!A{first_empty_row_index}:E{first_empty_row_index}'
                        value_input_option = 'USER_ENTERED'
                        value_range_body = {'values': [[user_completo + ' ' + senha, email, timestamp, maquina, conteudo]]}
                        result = service.spreadsheets().values().update(
                            spreadsheetId='1dA96HvQ8_i5Ybn8daBrffmhwwAjBmsTbrivGMxlJMa4',
                            range=range_to_update,
                            valueInputOption=value_input_option,
                            body=value_range_body).execute()
                        window.Refresh()
                        arquivo = open('configuracoes/contas/contas_criadas.txt', 'a')  # Escreva mais conteúdo no arquivo
                        arquivo.write(user_completo + ' ' + senha + "\n")
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
                            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup[5]'))).click()
                        except:
                            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[5]'))).click()

                        time.sleep(0.5)

                        # Clicar em configurações
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.View'))).click()
                        time.sleep(0.5)
                        # Clicar em privacidade
                        try:
                            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[7]/android.view.ViewGroup/android.view.View'))).click()
                        except:
                            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup/android.view.View'))).click()
                        time.sleep(2)
                        # Clicar em privacidade da conta
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[11]/android.view.ViewGroup/android.view.ViewGroup/android.view.View'))).click()
                        time.sleep(0.5)
                        # Clicar no botão
                        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[*]/android.view.ViewGroup[3]/android.view.ViewGroup'))).click()
                        time.sleep(0.5)
                        window['output'].print('Alterado para publico.')
                        window.Refresh()
                        time.sleep(0.5)
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK', stdout=subprocess.DEVNULL,
                                                stderr=subprocess.DEVNULL, check=True, shell=True)
                        time.sleep(0.5)
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK', stdout=subprocess.DEVNULL,
                                                stderr=subprocess.DEVNULL, check=True, shell=True)
                        time.sleep(0.5)
                        subprocess.run(f'adb -s 127.0.0.1:{porta} shell input keyevent KEYCODE_BACK', stdout=subprocess.DEVNULL,
                                                stderr=subprocess.DEVNULL, check=True, shell=True)
                        time.sleep(0.5)
                            
                        sms = False

                    else:
                        try:
                            with open("configuracoes/vpn/vpn.txt", "r") as arquivo:
                                conteudo = arquivo.read().strip()
                            if conteudo == "avg":
                                vpn_avg()
                            elif conteudo == "surf":
                                vpn_surf()
                            elif conteudo == "betternet":
                                vpn_better()
                            elif conteudo == "cyberghost":
                                vpn_cyberghost()
                            elif conteudo == "nord":
                                vpn_nord()
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
            subprocess.run(f'adb -s 127.0.0.1:{porta} uninstall io.appium.uiautomator2.server', stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL, shell=True)
            window['output'].print('Algum erro não catalogado encontrado.')
            window['output'].print(e)
            #window['output'].print(e)
            window.Refresh()
                

pool = concurrent.futures.ThreadPoolExecutor()
while True:
    event, values = window.read()
    
    # Finaliza a janela se o usuário fechar a janela
    if event == sg.WINDOW_CLOSED:
        break
    
    # Executa o código e atualiza a saída na Multiline em tempo real
    if event == 'Executar':
        if not os.path.exists("token.json"):
        # se o arquivo não existe, pede o nome do arquivo ao usuário e armazena em uma variável global
            window['output'].print('Nenhum token.json encontrado.')
            window.Refresh()
            time.sleep(200)
        else:
            pass
        with open("configuracoes\\contas\\senha_perfis.txt", "r") as arquivo:
            config = arquivo.read().strip()
        if config == 'digite_a_senha_que_sera_usada_nos_perfis':
            window['output'].print('Configure a senha das contas primeiro.')
            window.Refresh()
            time.sleep(200)
        with open("configuracoes\\outros\\SPREADSHEET_ID.txt", "r") as arquivo:
            config_sheets = arquivo.read().strip()
        if config_sheets == 'digite aqui sua SPREADSHEET_ID':
            window['output'].print('Configure a sua SPREADSHEET primeiro.')
            window.Refresh()
            time.sleep(200)
        with open("configuracoes\\outros\\nome_maquina.txt", "r") as arquivo:
            config_maquina = arquivo.read().strip()
        if config_maquina == 'Configure o nome da maquina.':
            window['output'].print('Configure o nome da maquina primeiro.')
            window.Refresh()
            time.sleep(200)
        with open("configuracoes\\vpn\\vpn.txt", "r") as arquivo:
            config_vpn = arquivo.read().strip()
        if config_vpn == 'avg, surf, nord, cyberghost ou betternet':
            window['output'].print('Configure a vpn que você deseja primeiro.')
            window.Refresh()
            time.sleep(200)
        pool.submit(executar)
    if event == 'clear':
        window['output'].update('')
        if not os.path.exists("token.json"):
        # se o arquivo não existe, pede o nome do arquivo ao usuário e armazena em uma variável global
            window['output'].print('Nenhum token.json encontrado.')
            window.Refresh()
            time.sleep(200)
        else:
            pass
        with open("configuracoes\\contas\\senha_perfis.txt", "r") as arquivo:
            config = arquivo.read().strip()
        if config == 'digite_a_senha_que_sera_usada_nos_perfis':
            window['output'].print('Configure a senha das contas primeiro.')
            window.Refresh()
            time.sleep(200)
        with open("configuracoes\\outros\\SPREADSHEET_ID.txt", "r") as arquivo:
            config_sheets = arquivo.read().strip()
        if config_sheets == 'digite aqui sua SPREADSHEET_ID':
            window['output'].print('Configure a sua SPREADSHEET primeiro.')
            window.Refresh()
            time.sleep(200)
        with open("configuracoes\\outros\\nome_maquina.txt", "r") as arquivo:
            config_maquina = arquivo.read().strip()
        if config_maquina == 'Configure o nome da maquina.':
            window['output'].print('Configure o nome da maquina primeiro.')
            window.Refresh()
            time.sleep(200)
        with open("configuracoes\\vpn\\vpn.txt", "r") as arquivo:
            config_vpn = arquivo.read().strip()
        if config_vpn == 'avg, surf, nord, cyberghost ou betternet':
            window['output'].print('Configure a vpn que você deseja primeiro.')
            window.Refresh()
            time.sleep(200)
        pool.submit(executar)

window.close()
