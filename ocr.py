import glob
from PIL import Image
from pytesseract import *
import json
import re

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

images = glob.glob("./Cropped/*.jpg")
repaletizaje = []
count = 0
while len(images) > count:
    img = Image.open(images[count])
    datos = str(pytesseract.image_to_string(img, lang='eng',  config='--psm 6'))
    datos = datos.split('\n')
    datos = [i for i in datos if i != '']
    datos = datos[2:]

    img_1 = Image.open(images[count+1])
    datos_1 = str(pytesseract.image_to_string(img_1, lang='eng',  config='--psm 6'))
    datos_1 = datos_1.split('\n')
    datos_1 = [i for i in datos_1 if i != '']
    datos_1 = datos_1[2:]

    i = 0
    e = 0
    pallets_originales = []
    pallet_nuevo = ''
    while len(datos) > i:   
        respuesta = re.findall(r'[0-9]{8,12}', datos[i])
        if respuesta != []:
            if pallets_originales != []:
                repaletizaje.append({'pallet_nuevo': pallet_nuevo, 'pallets_originales': pallets_originales})
                pallets_originales = []
            pallet_nuevo = respuesta[0]
        else:
            respuesta_1 = re.findall(r'[0-9]{8,12}', datos_1[e])
            pallets_originales.append(respuesta_1[0])
            e += 1
        i += 1
    repaletizaje.append({'pallet_nuevo': pallet_nuevo, 'pallets_originales': pallets_originales})
    count += 2

print(repaletizaje)
    
   
with open('Repalitizados.json', 'w') as fp:
    json.dump(repaletizaje, fp)
 
#with open('repalitizados.json', 'r') as fp:
#    datos = json.load(fp)
#print(datos)

