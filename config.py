import base64
import os

def codificar(mensaje):
    mensaje_bytes = mensaje.encode('ascii')
    mensaje_base64 = base64.b64encode(mensaje_bytes)
    mensaje_codificado = mensaje_base64.decode('ascii')
    return mensaje_codificado

def decodificar(mensaje_codificado):
    mensaje_bytes = mensaje_codificado.encode('ascii')
    mensaje_base64 = base64.b64decode(mensaje_bytes)
    mensaje = mensaje_base64.decode('ascii')
    return mensaje




# --------------------------- CON ENVIRON  ---------------------------------
recipients = os.environ.get('RECIPIENTS')
recipients = recipients.split('/')
email_recipients = ", ".join(recipients)

alert = os.environ.get('ALERT_EMAIL')
alert = alert.split('/')
alert_email = ", ".join(alert)

user = os.environ.get('USER_EMAIL')
password = decodificar(os.environ.get('USER_PASS'))

poppler_path = r'C:\Users\javie\Desktop\poppler-0.68.0\bin'
tesseract_cmd =  r'C:\Program Files\Tesseract-OCR\tesseract.exe'