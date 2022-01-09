import glob
import cv2
  
image_counter = 1

def cortes(img, x, y, w, h, image_counter):
        crop_img = img[y:y+h, x:x+w]
        filename = "./Cropped/crop"+str(image_counter)+".jpg"
        #cv2.imshow('windo',crop_img)
        cv2.imwrite(filename,crop_img)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()

images = glob.glob("./Image/*.jpg")

for image in images:
        img=cv2.imread(image,1)

        cortes(img, 70, 820, 500, 4228, image_counter)
        image_counter += 1
        cortes(img, 2900, 820, 400, 4228, image_counter)
        image_counter += 1


