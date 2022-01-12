from pdf2image import convert_from_path
from PIL import Image
from pytesseract import *
import json
import re
import cv2
import config
#import base64
import glob
import os

def file_delete(folder, extencion):
    images = glob.glob(folder+extencion)
    for img in images:
        os.remove(img)

def folder_create(folder):
    if not os.path.isdir(folder):
        os.mkdir(folder)

def convert_PDF_to_JPEG(folder):
    # Obtiene lista ordenada de elementos por tiempod de creacion
    files_path = os.path.join(folder, '*.pdf')
    files = sorted( glob.iglob(files_path), key=os.path.getctime, reverse=True) 

    pages = convert_from_path(files[0], 500, poppler_path=config.poppler_path) 

    image_counter = 1

    for page in pages: 
        folder_create("Image")
        filename =  os.path.join("Image","page_"+str(image_counter)+".jpg")
        page.save(filename, 'JPEG') 
        image_counter += 1

def cortes(img, x, y, w, h, image_counter):
    crop_img = img[y:y+h, x:x+w]
    filename = "./Cropped/crop"+str(image_counter)+".jpg"
    cv2.imwrite(filename,crop_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def recortar(folder):
    folder_create("Cropped")
    image_counter = 1
    images = glob.glob(folder)

    for image in images:
        img=cv2.imread(image,1)

        cortes(img, 70, 870, 500, 4228, image_counter)
        image_counter += 1
        cortes(img, 3000, 820, 400, 4228, image_counter)
        image_counter += 1

def OCR():
    pytesseract.tesseract_cmd = config.tesseract_cmd

    images = sorted(glob.glob("./Cropped/*.jpg"), key=os.path.getctime, reverse=False)
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
                if e < len(datos_1):
                    respuesta_1 = re.findall(r'[0-9]{8,12}', datos_1[e])
                    pallets_originales.append(respuesta_1[0])
                    e += 1
                else:               # ERROR de lectura
                    return False
            i += 1
        repaletizaje.append({'pallet_nuevo': pallet_nuevo, 'pallets_originales': pallets_originales})
        count += 2

    
    repaletizaje = {"Repaletizajes": repaletizaje}
    #print(repaletizaje)
    
    with open('Repalitizados.json', 'w') as fp:
        json.dump(repaletizaje, fp)

    return True




