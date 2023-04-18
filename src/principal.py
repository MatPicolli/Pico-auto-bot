import PySimpleGUI as sg
import handle_area as ha
import acoes


class Item:
    def __init__(self, name='TESTE', x=0, y=0, cor=(0, 0, 0), ativo=False, tecla=''):
        self.name = name
        self.x = x
        self.y = y
        self.cor = cor
        self.ativo = ativo
        self.tecla = tecla


def janela_principal():
    import handle_file as hf

    # tema da janela
    sg.theme('DarkAmber')

    teclas = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',
              '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
              'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
              'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
              'Z', 'X', 'C', 'V', 'B', 'N', 'M']

    # layout da janela
    layout = [
        [sg.Button('Adicionar área', key='-ADD_AREA-')],
        # uma lista dropdown onde voce não pode escrever, apenas selecionar
        [sg.DropDown(values=[], size=(18, 6), key='-DROPDOWN-'), sg.Button('Carregar', key='-DROPDOWN_CHECK-')],
        [sg.Text('X:', size=(2, 1)), sg.Input(key='-X-', size=(10, 1), disabled=True, text_color='black')],
        [sg.Text('Y:', size=(2, 1)), sg.Input(key='-Y-', size=(10, 1), disabled=True, text_color='black')],
        [sg.Text('Pixel:', size=(4, 1)), sg.Button(key='-PIXEL-', size=(2, 1), disabled=True)],
        [sg.Checkbox('Ativo', default=False, key='-ATIVO-'),
         sg.Text('Key:', size=(3, 1)), sg.DropDown(teclas, size=(8, 1), key='-TECLA-'),
         sg.Button('Confirmar', key='-TECLA_CHECK-')],
    ]

    # cria a janela
    window = sg.Window('Principal', layout, finalize=True, size=(275, 190))
    # windows.bind da tecla home
    window.bind('<Home>', '-HOME-')

    # loop de eventos
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        # caso o botão de adicionar área seja clicado
        if event == '-ADD_AREA-':
            # chama a função de adicionar área
            item = Item()
            item.x, item.y, item.cor = ha.adicionar_area()
            # adiciona a lista de listbox
            hf.lista_dropdown.append(item)
            # atualiza a lista_dropdown mostrando apenas o item.name
            window['-DROPDOWN-'].update(values=hf.lista_dropdown)

        # caso tenha um item selecionado no dropdown e o botão check seja apertado
        try:
            if event == '-DROPDOWN_CHECK-':
                # pega o item selecionado
                item = window['-DROPDOWN-'].get()
                # atualiza o item selecionado
                window['-X-'].update(item.x, disabled=False)
                window['-Y-'].update(item.y, disabled=False)
                window['-X-'].update(item.x, disabled=True)
                window['-Y-'].update(item.y, disabled=True)
                window['-PIXEL-'].update(button_color=ha.rgb_para_hexdecimal(item.cor), disabled=False)
                window['-PIXEL-'].update(button_color=ha.rgb_para_hexdecimal(item.cor), disabled=True)
                window['-ATIVO-'].update(item.ativo)
                if item.tecla != '':
                    window['-TECLA-'].update(item.tecla)
        except AttributeError:
            continue

        try:
            if event == '-HOME-':
                sg.popup('Iniciando...')
                # minimizar a janela
                window.minimize()
                acoes.inicia_acoes()
                sg.popup('Encerrando...')

        except AttributeError:
            continue

        try:
            # caso tenha um item selecionado no dropdown e o botão tecla_check seja clicado
            if event == '-TECLA_CHECK-':
                # pega o item selecionado
                item = window['-DROPDOWN-'].get()
                # atualiza o item selecionado
                item.tecla = window['-TECLA-'].get()
                print('X:', item.x)
                print('Y:', item.y)
                print('COR:', item.cor)
                print('TECLA:', item.tecla)
                item.ativo = window['-ATIVO-'].get()
                print('ATIVO:', item.ativo)

        except IndexError:
            continue

    # fecha a janela
    window.close()
