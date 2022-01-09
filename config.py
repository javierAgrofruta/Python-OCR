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

#user = util.decodificar(os.environ.get('PYTHON_EMAIL'))
password = decodificar(os.environ.get('PYTHON_PASS'))
#poppler_path = os.environ.get('PYTHON_POPPLER')
#tesseract_cmd = os.environ.get('PYTHON_TESSERACT')
smtp = 'smtp.office365.com'

user = os.environ.get('PYTHON_EMAIL')
email_to = 'j.ibarra@agrofruta.cl' 
poppler_path = r'C:\Users\javie\Desktop\poppler-0.68.0\bin'
tesseract_cmd =  r'C:\Program Files\Tesseract-OCR\tesseract.exe'