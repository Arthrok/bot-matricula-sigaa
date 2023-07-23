from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import winsound
import win32gui
import json


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

url = "https://aprender3.unb.br/mod/quiz/review.php?attempt=1871426&cmid=1042339"
navegador.get(url)


while True:
    try:
        if navegador.current_url == url:
            questions = navegador.find_elements(By.XPATH, "//div[contains(@class, 'multichoice')]")

            data = {}  # Initialize an empty dictionary to store the data

            for question in questions:
                title_element = question.find_element(By.XPATH, ".//div[contains(@class, 'qtext')]")
                title = title_element.text.strip()  # Extract the title text and remove leading/trailing spaces

                options_elements = question.find_elements(By.XPATH, ".//div[contains(@class, 'flex-fill')]")
                options = [option.text.strip() for option in options_elements]  # Extract options text and remove leading/trailing spaces

                right_answer_elements = question.find_element(By.XPATH, ".//div[contains(@class, 'rightanswer')]")
                right_answers = right_answer_elements.find_elements(By.TAG_NAME, "p")
                rightAnswers = [right_answer.text.strip() for right_answer in right_answers]

                data[title] = {
                    "options": options,
                    "right_answers": rightAnswers
                }  # Store title, options, and right answers in the dictionary

            with open("prova_4.json", "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)
            break
    except:
        print("...")

    time.sleep(5)

navegador.quit()