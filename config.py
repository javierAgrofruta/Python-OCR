import crypto64 as crypt
import os

user = os.environ.get('PYTHON_EMAIL')
password = crypt.decodificar(os.environ.get('PYTHON_PASS'))
smtp = 'smtp.office365.com'