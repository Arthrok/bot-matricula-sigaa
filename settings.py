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


print({ matricula, email, senha_usuario, professor, materia, data, horario })
driver = webdriver.Edge()

def alarm():
    duration = 2000  # milliseconds
    freq = 1500  # Hz
    winsound.Beep(freq, duration)

servico = Service()
chrome_options = Options()
chrome_options.binary_location = r"C:\Users\Arth\Downloads\chrome-win64\chrome.exe"

# chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})

current_directory = os.path.dirname(os.path.abspath(__file__))
chromedriver_path = os.path.join(current_directory, "chromedriver.exe")


servico = Service(ChromeDriverManager(version="114.0.5735.90").install())
navegador = driver

url = "https://sigaa.unb.br/sigaa/graduacao/matricula/extraordinaria/matricula_extraordinaria.jsf"
navegador.get(url)

while True:
    try:
        if 'autenticacao' in navegador.current_url:
            input_username = navegador.find_element(By.NAME, "username")
            input_username.send_keys(matricula)
            input_password = navegador.find_element(By.NAME, "password")
            input_password.send_keys(senha_usuario)
            button_login = navegador.find_element(By.NAME, "submit")
            button_login.click()
            navegador.get(url)

        if ('extraordinaria' in navegador.current_url) == False:
            navegador.get(url)

        buscar = navegador.find_element(By.ID, "form:buscar")
        input_horario = navegador.find_element(By.NAME, "form:txtHorario")
        input_horario.clear()
        input_horario.send_keys(horario)
        input_materia = navegador.find_element(By.NAME, "form:txtCodigo")
        input_materia.clear()
        input_materia.send_keys(materia)
        input_professor = navegador.find_element(By.NAME, "form:txtNomeDocente")
        input_professor.clear()
        input_professor.send_keys(professor)
        buscar.click()

        #inserir nome do professor 
        if(navegador.find_element(By.XPATH, '//td[text()="{}"]'.format(professor))):
            cont = navegador.find_element(By.XPATH, '//td[text()="{}"]'.format(professor))
            contPai = cont.find_element(By.XPATH, "..")
            imgSelecionar = contPai.find_element(By.XPATH, ".//img[@title='Selecionar turma']")
            if(imgSelecionar):
               imgSelecionar.click()
               alarm()
               break   
        
    except:
        print("...")

    time.sleep(5)



while True:
    try:
        janelas = navegador.window_handles
        navegador.switch_to.window(janelas[-1])
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

while True:
    try:
        confirmar = navegador.find_element(By.XPATH, ".//input[@value='Confirmar Matrícula']")
        confirmar.click()
        alert = Alert(navegador)
        alert.accept()
        navegador.quit()
    except:
        print("erro")

navegador.quit()