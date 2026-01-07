import os
import pyautogui
from time import sleep
import pandas as pd
import pyperclip
import openpyxl

os.system("open -a 'Google Chrome'")
sleep(2)
pyautogui.write("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
sleep(2)
pyautogui.press("enter")
sleep(7)
pyautogui.click(x = 260,y = 230)

caminho_rota = ("/Users/lucaspaguettipereira/Downloads/Vendas.xlsx") #atente-se em mudar o caminho do seu arquivo
tabela_faturamento_empresa = pd.read_excel(caminho_rota)
faturamento_empresa = tabela_faturamento_empresa["Valor Final"].sum()
quantidade_empresa_produtos = tabela_faturamento_empresa["Quantidade"].sum()

assunto = "Relatório de Vendas – Janeiro"
corpo = f"""Prezados,

Encaminho, abaixo, o relatório de vendas referente ao mês de janeiro 👇📊

Resumo dos resultados:
• Faturamento total: R$ {faturamento_empresa:,.2f} .
• Quantidade de produtos vendidos: {quantidade_empresa_produtos:.2f} .
Fico disposto para quaisquer esclarecimentos adicionais.

Atenciosamente,
Lucas Paguetti Pereira
"""
pyautogui.hotkey("command", "t")
sleep(1)
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")
sleep(10)
pyautogui.click(x=100, y=230)  
sleep(2)
pyautogui.press("tab")
sleep(0.5)
pyautogui.write(assunto)
pyautogui.press("tab")
sleep(0.5)
pyautogui.write(corpo)