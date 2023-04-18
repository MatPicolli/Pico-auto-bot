from pyautogui import pixel
import keyboard


def inicia_acoes():
    import handle_file as hf

    while True:
        for item in hf.lista_dropdown:
            if item.ativo:
                if pixel(int(item.x), int(item.y)) != item.cor:
                    keyboard.press(item.tecla.lower())

        # caso aperte a tecla END
        if keyboard.is_pressed('end'):
            break
