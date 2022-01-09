from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib

import imaplib
import email
import os
import shelve

import util
import config


def send(subject, message, to, filename=None):
        
    mime_message = MIMEText(message, "plain")
    mime_message["From"] = 'Agrofruta <'+config.user+'>'
    mime_message["To"] = to
    mime_message["Subject"] = subject

    if filename != None:
        mime_message = MIMEMultipart()
        mime_message["From"] = 'Agrofruta <'+config.user+'>'
        mime_message["To"] = to
        mime_message["Subject"] = subject

        fp=open(filename,'rb')
        att = MIMEApplication(fp.read(),_subtype="json")
        fp.close()
        att.add_header('Content-Disposition','attachment',filename=filename)
        mime_message.attach(att)

    else:
        mime_message = MIMEText(message, "plain")
        mime_message["From"] = 'Agrofruta <'+config.user+'>'
        mime_message["To"] = to
        mime_message["Subject"] = subject
    
    try:
        server = smtplib.SMTP(config.smtp, 587)
        server.starttls()
        server.login(config.user, config.password)

        server.sendmail(config.user, to,  mime_message.as_string())
    except:
        print('error al enviar email')
        return False
    finally:
        server.quit()
    return True


def read(archivo, termino, carpeta=None):
    email_leido = False
    # crear conexion
    imap = imaplib.IMAP4_SSL(config.smtp)
    imap.login(config.user, config.password)

    status, mensajes = imap.select("INBOX")

    # cantidad total de correos
    mensajes = int(mensajes[0])
    
    try:
        file = open('datos.dat','r')
        leidos = int(file.readline())
        file.close()
    except:
        file = open('datos.dat','w')
        number = 308
        file.write(str(number))
        leidos = number
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
                                util.folder_create(carpeta)
                            else:
                                util.folder_create(archivo)
                                carpeta = archivo
                            
                            if nombre_archivo:
                                if archivo == nombre_archivo[:len(archivo)] and termino == nombre_archivo.split('.')[1]:
                                    ruta_archivo = os.path.join(carpeta, nombre_archivo)
                                    open(ruta_archivo, "wb").write(part.get_payload(decode=True))
                                    email_leido = True 

        # Actualizamos mensajes leidos
        file = open('datos.dat','w')
        file.write(str(mensajes))
        file.close()

    imap.close()
    imap.logout()
    return email_leido
#email.send('test de prueba 1', 'mesaje enviado desde python mediante smtplib', 'jaibarra1@miuandes.cl')

#read('Repaletizados', 'pdf')