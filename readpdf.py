from pdf2image import convert_from_path
import glob
import os



# Obtiene lista ordenada de elementos por tiempod de creacion
files_path = os.path.join('Repaletizados', '*.pdf')
files = sorted( glob.iglob(files_path), key=os.path.getctime, reverse=True) 

pages = convert_from_path(files[0], 500, poppler_path=r'C:\Users\javie\Desktop\poppler-0.68.0\bin') 

image_counter = 1

for page in pages: 
    filename = "Image/page_"+str(image_counter)+".jpg"
    page.save(filename, 'JPEG') 
    image_counter += 1

