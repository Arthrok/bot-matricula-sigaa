import tkinter as tk
from threading import Thread
import subprocess
import sys
import time

matricula = {}

verify = False

def verify_key():
    global verify
    verify = True
    update_layout()

def update_layout():
    if verify:
        botao.grid(row=2, columnspan=2, pady=20)
    else:
        botao.grid_forget()

def iniciar_bot():
    email = email_entry.get()
    senha = senha_entry.get()
    professor = professor_entry.get().upper()
    materia = materia_entry.get().upper()
    matricula = matricula_entry.get()
    data = data_entry.get()
    horario = horario_entry.get().upper()
    if verify:
        root.destroy()
        print("Aguarde...")
        subprocess.run(["python", "settings.py", matricula, email, senha, professor, materia, data, horario])

root = tk.Tk()
root.title("MatriculArth 2.0")
root.minsize(600, 300)  # Largura x Altura

# Criando coluna da esquerda
left_frame = tk.Frame(root)
left_frame.grid(row=0, column=0, padx=20)

matricula_label = tk.Label(left_frame, text="Matrícula:")
matricula_label.pack()
matricula_entry = tk.Entry(left_frame, width=40)
matricula_entry.pack()

email_label = tk.Label(left_frame, text="Email:")
email_label.pack()
email_entry = tk.Entry(left_frame, width=40)
email_entry.pack()

senha_label = tk.Label(left_frame, text="Senha:")
senha_label.pack()
senha_entry = tk.Entry(left_frame, width=40)
senha_entry.pack()

data_label = tk.Label(left_frame, text="Data de nascimento:")
data_label.pack()
data_entry = tk.Entry(left_frame, width=40)
data_entry.pack()

cpf_label = tk.Label(left_frame, text="CPF")
cpf_label.pack()
cpf_entry = tk.Entry(left_frame, width=40)
cpf_entry.pack()

# Criando coluna da direita
right_frame = tk.Frame(root)
right_frame.grid(row=0, column=1, padx=20)

professor_label = tk.Label(right_frame, text="Nome do professor:")
professor_label.pack()
professor_entry = tk.Entry(right_frame, width=40)
professor_entry.pack()

materia_label = tk.Label(right_frame, text="Código da matéria:")
materia_label.pack()
materia_entry = tk.Entry(right_frame, width=40)
materia_entry.pack()

horario_label = tk.Label(right_frame, text="Horário:")
horario_label.pack()
horario_entry = tk.Entry(right_frame, width=40)
horario_entry.pack()

key_label = tk.Label(right_frame, text="Access Key:")
key_label.pack()
key_entry = tk.Entry(right_frame, width=40)
key_entry.pack()

verificar = tk.Button(right_frame, text="Verificar Key", command=verify_key)
verificar.pack(pady=7)

botao = tk.Button(root, text="Executar", command=iniciar_bot, width=30)
update_layout()

root.mainloop()