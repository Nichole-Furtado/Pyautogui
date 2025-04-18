# PyAutoGUI Automation Scripts

Este repositório contém uma coleção de scripts em Python que utilizam a biblioteca `PyAutoGUI` para automação de tarefas no ambiente Windows, como abertura de programas, interação com o Bloco de Notas, e consulta de informações via navegador.

## - Tecnologias utilizadas

- **Python 3**
- **PyAutoGUI** – Automação da interface gráfica do usuário
- **Time** – Controle de tempo e delays
- **Webbrowser** – Abertura de links no navegador

## 📁 Estrutura dos Scripts

### 1. `Abertura Excel, Word ou Bloco de Notas.py`

Este script permite ao usuário escolher entre abrir o **Excel**, **Word** ou **Bloco de Notas**, digitando o nome do aplicativo no console. O PyAutoGUI simula o pressionamento da tecla `Win`, digita o nome do aplicativo e o executa automaticamente.

### 2. `Abertura e escrevendo no bloco de notas.py`

Este script automatiza a abertura do Bloco de Notas e escreve uma frase personalizada dentro dele. Após abrir o aplicativo, ele aguarda alguns segundos e digita a frase desejada diretamente na janela.

### 3. `Acessando a Calculadora.py`

Script que abre a **Calculadora do Windows** utilizando automação via PyAutoGUI. Simula o processo de abrir o menu Iniciar, digitar "Calculadora" e pressionar Enter para executá-la.

### 4. `Consultando_Dolar.py`

Script que abre o navegador padrão e acessa o Google para realizar uma busca automática pela cotação do dólar. Ele utiliza a biblioteca `webbrowser` para abrir a URL da busca e simula ações de teclado para interagir com a página, se necessário.

## - Requisitos

- Python 3.x
- Instalação da biblioteca PyAutoGUI:
  ```bash
  pip install pyautogui
