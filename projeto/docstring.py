from cores import (Reset, Azul, AmareloClaro, Magenta)

print(f"""{Azul}🚀 Projeto 1 da Hashtag Treinamentos - Automação de Tarefas com Python 💉💻
{Reset}

{AmareloClaro}🎯 Objetivo:
Automatizar o processo de coleta, análise e envio de indicadores
utilizando Python, simulando um fluxo comum em ambientes corporativos.
{Reset}

{Magenta}📚 Bibliotecas utilizadas e suas funções:

- 🐍 Python: Linguagem principal do projeto.
- 🐼 Pandas: Manipulação de dados e cálculo de indicadores como faturamento e quantidade de produtos vendidos.
- 🧭 PyAutoGUI: Automatiza ações no sistema operacional (abrir navegador, clicar, digitar, navegar).
- 📎 PyperClip: Função dentro do PyAutoGUI que permite o copiar e colar de textos, 
     que funciona melhor que o .write() do próprio PyAutoGUI.
- ⏰ from time import sleep: Controla pausas entre ações automatizadas.
- 💻 OS: Interage com o sistema operacional, abre aplicativos e manipula arquivos.
- 📧 SMTPLib / Yagmail: Envio automático de e-mails com os indicadores calculados.
{Reset}

{AmareloClaro}📝 Passo a passo do desafio:

1️⃣ Acessar o sistema da empresa(no nosso caso, drive - simulador):
- 🌐 Abrir o navegador;
- 🔗 Digitar ou colar o link do sistema:
- 🔑 Realizar login, se necessário.

2️⃣ Navegar até a área de relatórios:
- 🗂️ Localizar a seção de relatórios;
- 📄 Selecionar o relatório desejado.

3️⃣ Realizar o download da base de dados/
- ⬇️ Baixar o arquivo Excel:
- 💾 Salvar em um local acessível.

4️⃣ Calcular os principais indicadores;
- 📊 Manipular dados com Pandas;
- 💰 Calcular faturamento total;
- 📦 Calcular quantidade de produtos vendidos.

5️⃣ Enviar e-mail com os indicadores ==>:
- ✉️ Formatar o e-mail;
- 📝 Inserir assunto e corpo;
- 📤 Enviar para a diretoria.
{Reset}
""")
# Fim do docstring