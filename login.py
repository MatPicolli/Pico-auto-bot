import PySimpleGUI as sg
import os


def verifica_login(user, password):
    # verifica se existe um arquivo chamado authpass.keys
    if os.path.exists('authpass.keys'):
        pass
    else:
        with open('authpass.keys', 'w') as file:
            file.close()
    if user == 'admin' and password == 'admin':
        return True
    else:
        return False
        

def login():
    # define o tema para a janela
    sg.theme('DarkAmber')

    # define o layout da janela
    layout = [
        # Input do usuário
        [sg.Text('Usuário', size=(7, 1)), sg.Input(key='-USER-', size=(20, 1))],
        # passord input com caracter de escondimento
        [sg.Text('Password', size=(7, 1)), sg.Input(key='-PASSWORD-', size=(20, 1), password_char='*')],
        # botão de login centralizado
        [sg.Button('Login', key='-LOGIN-', size=(8, 1), pad=((0, 0), (10, 0)))]
    ]

    # cria a janela
    window = sg.Window('Login', layout, finalize=True)
    # caso o enter seja pressionado, o botão de login é clicado
    window.bind('<Return>', '-LOGIN-')

    # loop de eventos
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        # caso o botão de login seja clicado ou a tecla enter seja pressionada
        if event == '-LOGIN-' or event == '<Return>':
            # verifica se o usuário e senha estão corretos
            if verifica_login(values['-USER-'], values['-PASSWORD-']):
                window.close()
                return True
            else:
                # se não, mostra uma mensagem de erro
                sg.popup('Usuário ou senha incorretos', title='Erro')

    # fecha a janela
    window.close()
    return False