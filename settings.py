from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options

import os

import time
import winsound
import win32gui
import sys

print("Aguarde...")

matricula = sys.argv[1]
email = sys.argv[2]
senha_usuario = sys.argv[3]
professor = sys.argv[4]
materia = sys.argv[5]
data = sys.argv[6]
horario = sys.argv[7]
cpf = sys.argv[8]

global_time = time.time()

print({ matricula, email, senha_usuario, professor, materia, data, horario })
driver = webdriver.Edge()

def alarm():
    duration = 2000  # milliseconds
    freq = 1500  # Hz
    winsound.Beep(freq, duration)

navegador = driver

url = "https://autenticacao.unb.br/sso-server/login?service=https%3A%2F%2Fsig.unb.br%2Fsigaa%2Flogin%2Fcas"
navegador.get(url)

def login():
    input_username = navegador.find_element(By.NAME, "username")
    input_username.send_keys(matricula)
    input_password = navegador.find_element(By.NAME, "password")
    input_password.send_keys(senha_usuario)
    button_login = navegador.find_element(By.NAME, "submit")
    button_login.click()

def path_extraordinaria():
    ensino = navegador.find_element(By.CLASS_NAME, "ThemeOfficeMainFolderText")
    ensino.click()
    matricula_online = navegador.find_element(By.XPATH, '//td[text()="{}"]'.format("Matrícula On-Line"))
    matricula_online.click()
    realizar_matricula = navegador.find_element(By.XPATH, '//td[text()="{}"]'.format("Realizar Matrícula Extraordinária"))
    realizar_matricula.click()

def search():
    search = navegador.find_element(By.ID, "form:buscar")
    input_horario = navegador.find_element(By.NAME, "form:txtHorario")
    input_horario.clear()
    input_horario.send_keys(horario)
    input_materia = navegador.find_element(By.NAME, "form:txtCodigo")
    input_materia.clear()
    input_materia.send_keys(materia)
    input_professor = navegador.find_element(By.NAME, "form:txtNomeDocente")
    input_professor.clear()
    input_professor.send_keys(professor)
    search.click()

def found():
    if(navegador.find_element(By.XPATH, '//td[text()="{}"]'.format(professor))):
        content = navegador.find_element(By.XPATH, '//td[text()="{}"]'.format(professor))
        contentFather = content.find_element(By.XPATH, "..")
        selecionar_turma = contentFather.find_element(By.XPATH, ".//img[@title='Selecionar turma']")
        selecionar_turma.click()
        alarm()
        return True
    return False

def confirm():
    confirmar = navegador.find_element(By.XPATH, ".//input[@value='Confirmar Matrícula']")
    confirmar.click()
    alert = Alert(navegador)
    alert.accept()

def logout():
    sair = navegador.find_element(By.CLASS_NAME, "sair-sistema")
    sair.click()

def check_time(minutes):
    current_time = time.time()
    minutes_remaining = (current_time - global_time) / 60
    return minutes_remaining >= minutes

while True:
    try:
        if check_time(5):
            navegador.get(url)
            logout()
            global_time = time.time()

        if 'autenticacao' in navegador.current_url:
            login()

        if ('extraordinaria' in navegador.current_url) == False:
            path_extraordinaria()

        search()

        if found():
            break

    except:
        print("Nenhum resultado encontrado!")

    time.sleep(5)

def preenche_credenciais():
    senha = navegador.find_element(By.NAME, "j_id_jsp_334536566_1:senha")
    senha.clear()
    senha.send_keys(senha_usuario)

    dataNascimento = navegador.find_element(By.NAME, "j_id_jsp_334536566_1:Data")
    dataNascimento.clear()
    dataNascimento.send_keys(data)

    input_cpf = navegador.find_element(By.NAME, "j_id_jsp_334536566_1:cpf")
    input_cpf.clear()
    input_cpf.send_keys(cpf)

while True:
    try:
        # dataNascimento = navegador.find_element(By.NAME, "j_id_jsp_334536566_1:Data")
        # input_cpf = navegador.find_element(By.NAME, "j_id_jsp_334536566_1:cpf")
        obrigatorio = navegador.find_elements(By.CLASS_NAME, "obrigatorio")
        if len(obrigatorio) == 1:
            senha = navegador.find_element(By.NAME, "j_id_jsp_334536566_1:senha")
            senha.click()
            senha.clear()
            # preencher senha
            senha.send_keys(senha_usuario)
            break
        else:
            navegador.refresh()
    except:
        navegador.refresh()   
    time.sleep(2)

# preenche_credenciais()

while True:
    try:
        confirm()
        navegador.quit()
    except:
        print("erro")