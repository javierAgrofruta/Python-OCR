import util
import Email
import config

util.file_delete("./Cropped/","*.jpg")
util.file_delete("./Image/","*.jpg")

#email_leido, mensajes = Email.read('Repaletizados', 'pdf')

email_leido, mensajes = True, 344

if email_leido:
    util.convert_PDF_to_JPEG('Repaletizados')

    util.recortar("./Image/*.jpg")

    if util.OCR():
        Email.send("Repaletizados","Archivo de repaletizados", config.email_recipients, "Repalitizados.json")

        # Actualizamos mensajes leidos
        file = open('datos.dat','w')
        file.write(str(mensajes))
        file.close()
    else:
        Email.send("Error Integracion Rio Blanco", "Error al leer archivo con OCR", config.email_error)

else:
    file = open('datos.dat','w')
    file.write(str(mensajes))
    file.close()