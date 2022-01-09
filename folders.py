import glob
import os

def delete(folder, extencion):
    images = glob.glob(folder+extencion)
    for img in images:
        os.remove(img)

def create(folder):
    pass

#images = glob.glob("./Cropped/*.jpg")
#for img in images:
#    os.remove(img)
#
#images = glob.glob("./Image/*.jpg")
#for img in images:
#    os.remove(img)