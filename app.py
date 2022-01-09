import util
import Email
import config

util.file_delete("./Cropped/","*.jpg")
util.file_delete("./Image/","*.jpg")

email_leido = Email.read('Repaletizados', 'pdf')

if email_leido:
    util.convert_PDF_to_JPEG('Repaletizados')

    util.recortar("./Image/*.jpg")

    util.OCR()

    Email.send("Repaletizados","Archivo de repaletizados", config.email_to, "Repalitizados.json")