import PySimpleGUI as sg
from pyautogui import position, pixel


def rgb_para_hexdecimal(rgb=(0, 0, 0)):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])


def adicionar_area():
    
    # tema da janela
    sg.theme('DarkAmber')

    # layout da janela
    layout = [
        [sg.Text('Coordenadas ❓', tooltip='Pressione M para obter as coordenadas')],
        [sg.Text('X:', size=(2, 1)), sg.Input(key='-X-', size=(10, 1), disabled=True, text_color='black')],
        [sg.Text('Y:', size=(2, 1)), sg.Input(key='-Y-', size=(10, 1), disabled=True, text_color='black')],
        [sg.Text('Pixel:', size=(4, 1)), sg.Button(size=(2, 1), key='-PIXEL-', disabled=True)],
        [sg.Button('Salvar', key='-SAVE-'), sg.Button('Cancelar', key='-CANCEL-')],
    ]

    # cria a janela
    window = sg.Window('Coordenadas Mouse', layout, finalize=True, keep_on_top=True)
    # windows.bind da letra M
    window.bind('<m>', '-CLICK-')

    # loop de eventos
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == '-CANCEL-':
            break

        if event == '-CLICK-':
            # pega as coordenadas do mouse
            x, y = position()
            window['-X-'].update(x, disabled=False)
            window['-Y-'].update(y, disabled=False)

            window['-X-'].update(x, disabled=True)
            window['-Y-'].update(y, disabled=True)

            # pega a cor do pixel
            cor = pixel(x, y)
            window['-PIXEL-'].update(button_color=rgb_para_hexdecimal(cor), disabled=False)
            window['-PIXEL-'].update(button_color=rgb_para_hexdecimal(cor), disabled=True)

        # caso o botão de salvar seja clicado
        if event == '-SAVE-':
            # caso os campos estejam vazios
            if values['-X-'] == '' or values['-Y-'] == '':
                continue
            else:
                window.close()
                return values['-X-'], values['-Y-'], pixel(int(values['-X-']), int(values['-Y-']))

    # fecha a janela
    window.close()