from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import winsound
import win32gui

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

url = "https://sigaa.unb.br/sigaa/graduacao/matricula/extraordinaria/matricula_extraordinaria.jsf"
navegador.get(url)


while True:
    try:
        button = navegador.find_element(By.ID, "form:buscar")
        input1 = navegador.find_element(By.NAME, "form:txtNome")
        input1.clear()
        # nome da matéria
        input1.send_keys("DISCRETA 2")
        button.click()
        #inserir nome do professor 
        if(navegador.find_element(By.XPATH, '//td[text()="VINICIUS DE CARVALHO RISPOLI"]')):
            chrome_hwnd = win32gui.FindWindow(None, "SIGAA - Sistema Integrado de Gestão de Atividades Acadêmicas - Google Chrome")
            win32gui.SetForegroundWindow(chrome_hwnd)
            winsound.PlaySound("SOM_DE_ALERTA.wav", winsound.SND_ASYNC)
            winsound.PlaySound("SOM_DE_ALERTA.wav", winsound.SND_ASYNC)
            winsound.PlaySound("SOM_DE_ALERTA.wav", winsound.SND_ASYNC)
            cont = navegador.find_element(By.XPATH, '//td[text()="VINICIUS DE CARVALHO RISPOLI"]')
            contPai = cont.find_element(By.XPATH, "..")
            imgSelecionar = contPai.find_element(By.XPATH, ".//img[@title='Selecionar turma']")
            if(imgSelecionar):
               imgSelecionar.click()
               break   
    except:
        print("...")

    time.sleep(5)



while True:
    try:
        janelas = navegador.window_handles
        # alterna o foco do driver para a nova janela
        navegador.switch_to.window(janelas[-1])
        dataNascimento = navegador.find_element(By.NAME, "j_id_jsp_334536566_1:Data")
        senha = navegador.find_element(By.NAME, "j_id_jsp_334536566_1:senha")
        if(dataNascimento):
            dataNascimento.click()
            dataNascimento.clear()
            # preencher data de nascimento
            dataNascimento.send_keys("xx/xx/xxxx")
        if(senha):
            senha.click()
            senha.clear()
            # preencher senha
            senha.send_keys("xxxxxx")
            break
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