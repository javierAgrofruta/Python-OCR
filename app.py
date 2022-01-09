import LeerEmail
import folders
import readpdf
import cropping
import ocr
import Email

folders.delete("./Cropped/","*.jpg")
folders.delete("./Image/","*.jpg")

LeerEmail.read('Repaletizados', 'pdf')

Email.send("Repaletizados","Probando archivo adjunto","j.ibarra@agrofruta.cl", "Repalitizados.json")