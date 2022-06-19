import cv2
import numpy as np
import imutils
import os #Para guardar o almacenar datos

Datos =  'n'  # P es el nombre de la carpeta que vamos a crear 
if not os.path.exists(Datos): # Si la carpeta existe no se va a crear 
    print('Carpeta creada: ', Datos)
    os.makedirs(Datos) # Para crear la carpeta 

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) #iniciar la camara

count = 0 #Decalaramos una variable (count) y la igualamos a 0

while True:
    ret, frame = cap.read()
    if ret == False: break #Esta condicion es para que no genere ningun conflicto cuando guardemos la imagen en nuestra computadora
   
    k = cv2.waitKey(1)
    if k == ord('s'): #cuando precionemos la tecla S tomara foto de la imagen 
        cv2.imwrite(Datos + '/objeto_{}.jpg'.format(count), frame) #Guarda la imagen tomada
        print('Imagen almacenada: '+ 'objeto_{}.jpg'.format(count))
        count = count +   1 

    if k == 27: # Esc de nuestra computadora
        break

    cv2.imshow('frame',frame)

cap.release()
cv2.destroyAllWindows()
