import imaplib
import email
import os

import config

def read(archivo, termino, carpeta=None):
    # crear conexion
    imap = imaplib.IMAP4_SSL(config.smtp)
    imap.login(config.user, config.password)

    status, mensajes = imap.select("INBOX")

    # cantidad total de correos
    mensajes = int(mensajes[0])
    file = open('email_leidos.txt','r')
    leidos = int(file.readline())
    file.close()
    N = mensajes - leidos

    for i in range(mensajes, mensajes - N, -1) :
        # Obtener el mensaje no leidos
        try:
            res, mensaje = imap.fetch(str(i), "(RFC822)")
        except:
            break
        for respuesta in mensaje:
            if isinstance(respuesta, tuple):
                # Obtener el contenido
                mensaje = email.message_from_bytes(respuesta[1])

                if mensaje.is_multipart():
                    # Recorrer las partes del correo
                    for part in mensaje.walk():
                        # Extraer el contenido
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))

                        if "attachment" in content_disposition:
                            # download attachment
                            nombre_archivo = part.get_filename()

                            # crear una carpeta para el mensaje
                            if carpeta != None:
                                if not os.path.isdir(carpeta):
                                    os.mkdir(carpeta)
                            else:
                                if not os.path.isdir(archivo):
                                    os.mkdir(archivo)
                            
                            if nombre_archivo:
                                print(nombre_archivo.split('.')[1])
                                if archivo == nombre_archivo[:len(archivo)] and termino == nombre_archivo.split('.')[1]:
                                    ruta_archivo = os.path.join(archivo, nombre_archivo)
                                    open(ruta_archivo, "wb").write(part.get_payload(decode=True))

        # Actuañizamos mensajes leidos
        file = open('email_leidos.txt','w')
        file.write(str(mensajes))
        file.close()

    imap.close()
    imap.logout()

