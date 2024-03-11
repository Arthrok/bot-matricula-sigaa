import tkinter as tk
from threading import Thread
import subprocess
import sys
import time
from tkinter import ttk
import json

matricula = {}
verify = False


def salvar_usuario():
    usuario = {
        "matricula": matricula_entry.get(),
        "email": email_entry.get(),
        "senha": senha_entry.get(),
        "data de nascimento": data_entry.get(),
        "CPF": cpf_entry.get()
    }
    try:
        with open("usuarios.json", "r") as file:
            usuarios = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        usuarios = {}

    usuarios[matricula_entry.get()] = usuario


    with open("usuarios.json", "w") as file:
        json.dump(usuarios, file, indent=4)

    preencher_dropdowns()


# Função para salvar matérias em arquivo JSON
def salvar_materia():
    materia = {
        "professor": professor_entry.get(),
        "codigo materia": materia_entry.get(),
        "horario": horario_entry.get()
    }
    try:
        with open("materias.json", "r") as file:
            materias = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        materias = {}

    materias[materia_entry.get()] = materia

    with open("materias.json", "w") as file:
        json.dump(materias, file, indent=4)

    preencher_dropdowns()


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
    cpf = cpf_entry.get()
    if verify:
        root.destroy()
        print("Aguarde...")
        subprocess.run(["python", "settings.py", matricula, email, senha, professor, materia, data, horario, cpf])

def carregar_dados():
    usuarios = {}
    materias = {}
    try: 
        with open("usuarios.json", "r") as file:
            usuarios = json.load(file)
        with open("materias.json", "r") as file:
            materias = json.load(file)
    except:
        pass
    return usuarios, materias


def preencher_dropdowns():
    usuarios, materias = carregar_dados()
    usuarios_dropdown['values'] = list(usuarios.keys())
    materia_dropdown['values'] = list(materias.keys())

def selecionar_usuario(event):
    usuario_selecionado = usuarios_dropdown.get()
    if usuario_selecionado:
        with open("usuarios.json", "r") as file:
            usuarios = json.load(file)
        usuario = usuarios.get(usuario_selecionado)
        if usuario:
            matricula_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            data_entry.delete(0, tk.END)
            cpf_entry.delete(0, tk.END)
            senha_entry.delete(0, tk.END)
            matricula_entry.insert(0, usuario.get("matricula", ""))
            email_entry.insert(0, usuario.get("email", ""))
            senha_entry.insert(0, usuario.get("senha", ""))
            data_entry.insert(0, usuario.get("data de nascimento", ""))
            cpf_entry.insert(0, usuario.get("CPF", ""))

# Função para selecionar uma matéria e preencher automaticamente os campos correspondentes
def selecionar_materia(event):
    materia_selecionada = materia_dropdown.get()
    if materia_selecionada:
        with open("materias.json", "r") as file:
            materias = json.load(file)
        materia = materias.get(materia_selecionada)
        if materia:
            professor_entry.delete(0, tk.END)
            horario_entry.delete(0, tk.END)
            materia_entry.delete(0, tk.END)
            professor_entry.insert(0, materia.get("professor", ""))
            materia_entry.insert(0, materia.get("codigo materia", ""))
            horario_entry.insert(0, materia.get("horario", ""))

root = tk.Tk()
root.title("MatriculArth 3.0")
root.minsize(600, 300)  # Largura x Altura

# Criando coluna da esquerda

left_frame = tk.Frame(root)
left_frame.grid(row=0, column=0, padx=20)

usuarios_dropdown_label = tk.Label(left_frame, text="Selecione o usuário:")
usuarios_dropdown_label.pack()
usuarios_dropdown = ttk.Combobox(left_frame, width=37, state="readonly")
usuarios_dropdown.pack()

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

salvar_usuario_btn = tk.Button(left_frame, text="Salvar Usuário", command=salvar_usuario)
salvar_usuario_btn.pack(pady=10)

# Criando coluna da direita
right_frame = tk.Frame(root)
right_frame.grid(row=0, column=1, padx=20)
materia_label_dropdown = tk.Label(right_frame, text="Selecione a matéria:")
materia_label_dropdown.pack()
materia_dropdown = ttk.Combobox(right_frame, width=37, state="readonly")
materia_dropdown.pack()

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

salvar_materia_btn = tk.Button(right_frame, text="Salvar Matéria", command=salvar_materia)
salvar_materia_btn.pack(pady=10)

key_label = tk.Label(right_frame, text="Access Key:")
key_label.pack()
key_entry = tk.Entry(right_frame, width=40)
key_entry.pack()

preencher_dropdowns()

verificar = tk.Button(right_frame, text="Verificar Key", command=verify_key)
verificar.pack(pady=7)

botao = tk.Button(root, text="Executar", command=iniciar_bot, width=30)
update_layout()

# Bind para selecionar usuário e matéria
usuarios_dropdown.bind("<<ComboboxSelected>>", selecionar_usuario)
materia_dropdown.bind("<<ComboboxSelected>>", selecionar_materia)

root.mainloop()