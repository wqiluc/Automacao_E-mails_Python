from cores import(Negrito,Reset,Verde,Amarelo,MagentaClaro)
import os
import pyautogui
from time import sleep
import pandas as pandas
import pyperclip
import openpyxl

os.system("open -a 'Google Chrome'")
sleep(2)

drive_dados = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga"

webhook_url = "https://api.pushcut.io/ZOlNMRPS825y5dde6LLpV/notifications/Email%20Enviado"

pyautogui.write(drive_dados)

pyautogui.press("enter")
sleep(2)
pyautogui.click(x=150, y=230)
sleep(3)
pyautogui.click(x=300, y=300)
sleep(4)
pyautogui.press("enter")
sleep(4)
pyautogui.press("enter")

caminho_rota = ("projeto/Vendas.xlsx")

tabela_faturamento_empresa = pandas.read_excel(caminho_rota)
faturamento_empresa = tabela_faturamento_empresa["Valor Final"].sum()
quantidade_empresa_produtos = tabela_faturamento_empresa["Quantidade"].sum()

print(f"\n {Negrito}Faturamento da Empresa:{Reset} {Verde}R${faturamento_empresa:.2f}{Reset}", end=" \n ")

print(f"\n {Negrito}Produtos da empresa (em quantidade): {Reset}{Amarelo}{quantidade_empresa_produtos}{Reset} Produtos 📦", end=" \n ")

remetente = f"lucaspaguetti2@gmail.com"

assunto = f"Relatório de Vendas – Julho 💸📊"
corpo = f"""Prezados,

Encaminho, abaixo, o relatório de vendas referente ao mês de julho

Resumo dos resultados:
• Faturamento total: R$ {faturamento_empresa:,.2f} .
• Quantidade de produtos vendidos: {quantidade_empresa_produtos:.2f} .
Fico à disposição para quaisquer esclarecimentos adicionais.

- Se quiserem se aprofundar dos dados, acessem:\n
{drive_dados}

Atenciosamente,
Lucas Paguetti Pereira.
"""

emails = [remetente] * 10

for indice_email, email in enumerate(emails, 1):
    print(f"\n {Negrito}Enviando e-mail {indice_email}/10 para {email}{Reset}")

    pyautogui.hotkey("command", "t")
    sleep(1)

    acessar_gmail = "https://mail.google.com/mail/u/0/#inbox"

    pyautogui.write(acessar_gmail)
    pyautogui.press("enter")
    sleep(20)
    pyautogui.click(x=100, y=230)
    sleep(2)

    pyperclip.copy(email)
    pyautogui.hotkey("command", "v")
    sleep(1)
    pyautogui.press("tab")
    sleep(0.5)

    pyperclip.copy(assunto)
    pyautogui.hotkey("command", "v")
    pyautogui.press("tab")

    sleep(0.5)
    pyperclip.copy(corpo)
    pyautogui.hotkey("command", "v")

    sleep(2)

    pyautogui.hotkey("command", "enter")

    print(f"\n {Negrito}E-mail {indice_email}/5{Reset} {Verde}enviado com sucesso! ✅📧🤖 {Reset}\n", end=" ")

    pyautogui.hotkey("command", "t")
    sleep(1)
    pyperclip.copy(webhook_url)
    pyautogui.hotkey("command", "v")
    pyautogui.press("enter")
    sleep(2)

    print(f"\n {Negrito}Notificação{Reset} {Verde}disparada no celular via Pushcut! 📲{Reset}\n", end=" ")

print(f"""\n {Negrito}Drive com os dados: {Reset}
{Negrito}Pasta dados/{Reset}
{Amarelo}├── Exportar{Reset}
│{Amarelo}└── Vendas.xlsx{Reset}
{MagentaClaro}├── Apostila - Aula1.pdf
├── Arquivo Inicial - Aula 1.ipynb
└── Arquivo Inicial - Aula 1.py \n\n{Reset}""")